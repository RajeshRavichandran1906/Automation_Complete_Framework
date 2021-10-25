'''
Created on MAY 18, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205167
TestCase Name = verify a chart shows correct filtered output once filter applied from context menu - Area Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup, ia_resultarea
from common.lib import utillity

class C2205167_TestClass(BaseTestCase):

    def test_C2205167(self):
        
        Test_Case_ID="C2205167"
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series 0', expire_time=20)
        
        """
            Step 02: On the Format tab, in the Output Types group, click active report/Active Flash/Active PDF.
        """           
        ribbonobj.change_output_format_type('active_report')
        utillobj.synchronize_with_visble_text("#HomeFormatType", 'ActiveReport', expire_time=5)
        
        """
            From the Format tab, select Area Chart.
        """
        ribbonobj.select_ribbon_item('Format', 'Area')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1>svg path[class*='marea']", 5, expire_time=15)
        
        """
           Step 03: Select data from the left pane (Dimensions and Measures) Category - Columns, Product - Horizontal Axis, Unit Sales - Vertical Axis
        """  
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='colHeader-label!']", 'Category', expire_time=8)
        
        metadataobj.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Product', expire_time=8)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=8)
        
        """
            Verify preview
        """
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 03.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.a(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.b: Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.c: Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!marea!r0!c0!", "bar_blue1", "Step 03.d: Verify  bar color")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, "Step 03.e: Verify number of Area",custom_css=".chartPanel .scrollCharts path[class*='riser']")
        
        """
            Step 04 : Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 g.chartPanel g text[class='yaxis-title']", 'UnitSales', expire_time=8)
        
        """
            Verify run window
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 04.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.a(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.b: Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 04.c: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0","riser!s0!g0!marea!r0!c0!", "bar_blue", "Step 04.d: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 04.e(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.e(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.e(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.e(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, "Step 04.e(v): Verify number of Area")
        
        """
            Step 05 : over over on Latte area. Verify context menu displays:
            Category: Coffee
            Product: Latte
            Unit Sales: 878,063
            Filter Chart
            Exclude from Chart
        """ 
        expected_tooltip_list=['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip("marker!s0!g6!mmarker!r0!c0!", verify_tooltip_list=expected_tooltip_list, msg='Step 05: Verify bar value')
    
        """
            Step 06:Left click and drag a box around Croissant and Scone in the FOOD Category.
            Filter icon is also displayed in the active tool bar.
        """
        circle_1=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g4!mmarker!r0!c1!']")
        source_offset=utillobj.enable_marker_using_javascript(circle_1, coordinate_type='middle')
        circle_2=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g8!mmarker!r0!c1!']")
        target_offset=utillobj.enable_marker_using_javascript(circle_2, coordinate_type='middle')
        utillobj.drag_drop_on_screen(sx_offset=source_offset['x']-15, sy_offset=source_offset['y']-20 ,tx_offset=target_offset['x']+20, ty_offset=target_offset['y']+20)
        utillobj.synchronize_with_number_of_element("[id^='ibi'][class='tdgchart-tooltip'][style*='visible']", 1, expire_time=2)
        
        """
            Step 07 : Click Filter Chart option.
        """
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m7!']", '700K', expire_time=8)
        
        """
            Verify output
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.a(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 07.a(ii): Verify -xAxis Title")
        expected_xval_list=['Croissant', 'Scone']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K','600K', '700K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.b :Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 07.c: Verify number of Area")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Food'], "Step 07.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!r0!c0!", "bar_blue", "Step 07.e: Verify  bar color")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 07.f(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.f(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.f(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.f(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 07.d(v): Filter Button Visible')
        
        """
            Step 08 : Click Remove Filter option.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m5!']", '1,000K', expire_time=8)
        
        """
            Verify original chart appears in the output. 
            Make sure filter icon is not present.
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 08.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.a(v): Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 08.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 08.b(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.c: Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 08.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!r0!c1!", "bar_blue", "Step 08.e: Verify  bar color")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, "Step 08.f:  Verify number of line")
        
        """ 
            Step 09 : Hover over on Biscotti area. Verify context menu displays:
            Category: Food
            Product: Biscotti
            Unit Sales: 421,377
            Filter Chart
            Exclude from Chart
            Step 10 : Click Exclude from Chart option.
        """
        expected_tooltip_list=['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip("marker!s0!g0!mmarker!r0!c1!", select_tooltip='Exclude from Chart', verify_tooltip_list=expected_tooltip_list, msg='Step 05: Verify bar value')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_f [class*='xaxisOrdinal-labels']", 9, expire_time=8)
        
        """
            Verify FOOD category is excluded from the chart and filter icon appears on the Active tool bar.
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 10.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.a(v): Filter Button Visible')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 10.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 10.b(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.c: Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 10.d: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!r0!c0!", "bar_blue", "Step 10.e: Verify  bar color")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 12, "Step 10.f: Verify number of Area")
        
        """
            Step 11 : Click remove filter icon from the active tool bar.
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_f [class*='xaxisOrdinal-labels']", 10, expire_time=8)
        
        """
            Verify original chart appears with 4 points in the GIFTS category and 'Remove filter' is no longer present
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 11.a(i): Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.a(ii): Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.a(iii): Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.a(iv): Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.a(v): Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.b(i): Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.b(ii): Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.c: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, "Step 11.d: Verify number of Area")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11.e: Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!marea!r0!c0!", "bar_blue", "Step 11.f: Verify  bar color")
        utillobj.switch_to_default_content(pause=3)
        
        """
            Take screenshot and save file
        """
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
      
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)

if __name__ == '__main__':
    unittest.main()
    