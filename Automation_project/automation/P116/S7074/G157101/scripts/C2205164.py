'''
Created on MAY 15, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205164
TestCase Name = Verify a chart shows correct filtered output once filter applied from context menu - Bar Chart
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup
from common.lib import utillity

class C2205164_TestClass(BaseTestCase):

    def test_C2205164(self):
        
        Test_Case_ID="C2205164"
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
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)  
        """
            Step 02: On the Format tab, in the Output Types group, click active report/Active Flash/Active PDF
        """   
        ribbonobj.change_output_format_type('active_report', location='Home')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        """
            Step 03: Select data from the left pane (Dimensions and Measures) Category - Columns,Product - Horizontal Axis,Unit Sales - Vertical Axis.    
    
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
        """
            Step 04:See corresponding data is displayed in the Live Preview pane.
        """ 
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 04.a(i): Verify -yAxis Title")
        time.sleep(1)
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 04.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 04.b: Verify XY labels")
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 04.c: Verify the total number of risers displayed on preview')
        time.sleep(1)
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 04.d: Verify row header and value")
        time.sleep(2)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 04.e: Verify  bar color")
        """
            Step 05:Run the report    
    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 05.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 05.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 05.b: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 05.c: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 05.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 05.e: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 05.f(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.f(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.f(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        """
            Step 06:Hover over on Latte bar. Verify context menu displays:
        """ 
        time.sleep(2)
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", expected_tooltip_list, "Step 06: Verify bar value")
        parent_element_obj=self.driver.find_element_by_id('MAINTABLE_wbody0')
        utillobj.click_on_screen(parent_element_obj, 'top_middle')
        
        """
            Step 07:Click Filter Chart option.
            Verify based on "Latte' product selection, that bar is displayed as filtered value. 
            Filter icon is also displayed in the active tool bar.
        """ 
        time.sleep(5)
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","riser!s0!g6!mbar!r0!c0!", 'Filter Chart')
        time.sleep(3)
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 07.a(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=["Latte"]
        expected_yval_list=['0', '0.2M', '0.4M', '0.6M', '0.8M', '1M', '1.2M']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.b: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 1, 'Step 07:c(i) Verify the total number of risers displayed on preview')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 07.c(ii): Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 07.d(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.d(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.d(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.d(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 07:d(v) Filter Button Visible')
        """
            Step 08:Click on Latte bar. Verify context menu displays:
            Category: Coffee
            Product: Latte
            Unit Sales: 878,063
            Remove Filter
        """
        expectedtooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", 'riser!s0!g0!mbar!r0!c0!', expectedtooltip_list, "Step 08: Verify bar value")
        time.sleep(3)
        """
            Step 09:Click Remove Filter option.
            Verify original chart appears in the output. 
            Make sure filter icon is not present.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 09.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 09.a(v) Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 09.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 09.b(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 09.b(iii): Verify XY labels")
        time.sleep(2)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 09.c: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 09.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", "bar_blue", "Step 09.e: Verify  bar color")
        """
            Step 10:Hover over on Biscotti bar. Verify context menu displays
            Category: Food
            Product: Biscotti
            Unit Sales: 421,377
            Filter Chart
            Exclude from Chart
        """
        time.sleep(2)
        expectedtooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart'] 
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c1!", expectedtooltip_list, "Step 10: Verify bar value")
        time.sleep(5)
        """
            Step 11: Click Exclude from Chart option.
            Verify FOOD category is excluded from the chart and filter icon appears on the Active tool bar.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c1!", 'Exclude from Chart')
        time.sleep(3)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 11.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 11:a(v) Filter Button Visible')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.b(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.c: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 9, 'Step 11.d: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11:e Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!r0!c0!", "bar_blue", "Step 11.f: Verify  bar color")
        """
            Step 12:Click remove filter icon from the active tool bar.
            Verify original chart appears with FOOD category and 'Remove filter' is not present.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 12.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 12.a(v): Filter Button Removed')
        yaxis_value ="Unit Sales"
        resobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 12.b(i): Verify -yAxis Title")
        time.sleep(3)
        xaxis_value ="Product"
        resobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 12.b(ii): Verify -xAxis Title")
        time.sleep(2)
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 12.c: Verify XY labels")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 10, 'Step 12:d: Verify the total number of risers displayed on preview')
        time.sleep(2)
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 12.e: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!r0!c0!", "bar_blue", "Step 12.f: Verify  bar color")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
