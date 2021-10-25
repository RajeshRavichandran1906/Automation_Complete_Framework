'''
Created on MAY 22, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205169
TestCase Name = Verify a chart shows correct filtered output once filter via lasso applied - Bar Chart
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity


class C2205169_TestClass(BaseTestCase):

    def test_C2205169(self):
        
        Test_Case_ID="C2205169"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created  
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)

        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        time.sleep(4)  
        """
            Step 02: On the Format tab, in the Output Types group, click active report/Active PDF
        """   
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 03: Select data from the left pane (Dimensions and Measures) 
            Category - Columns,
            Product - Horizontal Axis,
            Unit Sales - Vertical Axis.
        """  
     
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        parent_css="#TableChart_1 g.chartPanel g text[class='colHeader-label!']"
        resobj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product', 1, 0, 'Add To Query', 'Horizontal Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        resobj.wait_for_property(parent_css, 1, string_value='Product', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        resobj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        time.sleep(4)
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 03.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.b: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 03.c: Verify the total number of risers displayed on preview')
        time.sleep(1)
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.d: Verify row header and value")
        time.sleep(2)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 03.e: Verify  bar color")
        """
            Step 04:Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 04.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.b: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 04.c: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 04.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 04.e: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 04.f(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.f(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.f(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
            Step 05:Left click and drag a box around the Capuccino and Espresso bars.
            Step 06:Click Filter Chart option.
        """ 
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'start')
#         time.sleep(5)
#         elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g1!mbar!r0!c0!']")
#         source_elem=utillobj.get_object_screen_coordinate(elem1, 'middle', move=True)   
#         elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='riser!s0!g5!mbar!r0!c0!']")
#         target_elem=utillobj.get_object_screen_coordinate(elem2, 'middle', move=True)  
        time.sleep(3)
#         utillobj.drag_drop_on_screen(sx_offset=source_elem['x'],sy_offset=source_elem['y'],tx_offset=target_elem['x'],ty_offset=target_elem['y'])
        resobj.create_lasso("MAINTABLE_wbody0", "rect", "riser!s0!g1!mbar!r0!c0!",target_tag="rect",target_riser="riser!s0!g5!mbar!r0!c0!")
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        resobj.wait_for_property(parent_css, 2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 06.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 06.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 06.b: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 06.c: Verify the total number of risers displayed on preview')
        time.sleep(5)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee'], "Step 06.d: Verify row header and value")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 06.e: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 06.f(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.f(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.f(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 06:f(v) Filter Button Visible')
        """
            Step 07:Click on Capuccino bar.
        """
        expected_tooltip_list=['Category:Coffee', 'Product:Capuccino', 'Unit Sales:189217', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", expected_tooltip_list, "Step 07: Verify bar value")
        time.sleep(3)
        
        """
            Step 08:Click Remove Filter option.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        resobj.wait_for_property(parent_css, 10)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 08.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.a(v) Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 08.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 08.b(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.c: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 08.d: Verify the total number of risers displayed on preview')
        
        """
            Step 09:Left click and drag a box around the Espresso, Latte, Biscotti and Croissant bars. 
            This will span two different Categories.
            Step 10:Click Exclude from Chart option.
        """
        time.sleep(6)   
        resobj.create_lasso("MAINTABLE_wbody0", 'rect', 'riser!s0!g5!mbar!r0!c0!', target_tag='rect', target_riser='riser!s0!g4!mbar!r0!c1!')
        time.sleep(3)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(2)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        resobj.wait_for_property(parent_css, 6)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 10.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 11:a(v) Filter Button Visible')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 10.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 10.b(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.c: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 6, 'Step 10.d: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 10:e Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!r0!c1!", "bar_blue", "Step 10.f: Verify  bar color")
        
        """
            Step 11 :Click Remove Filter option.
            
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g.risers>g>rect[class^='riser']"
        resobj.wait_for_property(parent_css, 10)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 11.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.a(v) Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.b(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.b(iii): Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 11.c: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 11.e: Verify  bar color")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()