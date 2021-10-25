'''
Created on MAY 17, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2205166
TestCase Name = Verify a chart shows correct filtered output once filter applied from context menu - Line Chart
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,active_chart_rollup, ia_resultarea
from common.lib import utillity

class C2205166_TestClass(BaseTestCase):

    def test_C2205166(self):
        
        Test_Case_ID="C2205166"
        
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
            Step 01 : Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', 20)
        
        """
            Step 02: On the Format tab, in the Output Types group, click active report/Active Flash/Active PDF, From the Format tab, select Line Chart.
        """   
        ribbonobj.change_output_format_type('active_report', location='Home')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div", 'ActiveReport', 6)
        
        ribbonobj.select_ribbon_item('Format', 'Line')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 svg path[class*='mline']", 5, 10)
        time.sleep(2)
        
        """
            Step 03  : Select data from the left pane (Dimensions and Measures) Category - Columns,Product - Horizontal Axis,Unit Sales - Vertical Axis.    
        """  
        metadataobj.datatree_field_click('Category', 1, 0, 'Add To Query', 'Columns')
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='colHeader-label!']", 'Category', 8)
        
        metadataobj.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']", 'Product', 8)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_visble_text("#TableChart_1 g.chartPanel g text[class='yaxis-title']", 'UnitSales', 8)
        
        """
            Verify Preview
        """
        resobj.verify_yaxis_title("TableChart_1", "Unit Sales", "Step 03.1 : Verify -yAxis Title")
        resobj.verify_xaxis_title("TableChart_1", "Product", "Step 03.2 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step 03.3 : Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Category', ['Coffee'], "Step 03.4 : Verify row header and value")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!r0!c0!", "bar_blue1", "Step 03.5 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, "Step 03.6 : Verify number of line",custom_css=".chartPanel .scrollCharts path[class*='riser']")
        
        """
            Step 04 : Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-title']", 'UnitSales', 20)
        
        """
            Verify run window output
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 04.1 : Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 04.2 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 04.3 : Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 04.4 : Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 04.5 : Verify  bar color",attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 04.6 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.7 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 04.10 : Verify number of line",custom_css="path[class^='riser']")
         
        """
            Step 05 : Hover over on Espresso point in the middle of the Coffee Line chart. Verify context menu displays:
            Category: Coffee
            Product: Espresso
            Unit Sales: 308,986
            Filter Chart
            Exclude from Chart
        """
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g5!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=4.5)
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        expected_tooltip_list=['Category:Coffee', 'Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", None, expected_tooltip_list, "Step 05.1 :  Verify context menu displays", default_move=True)
        
        """
            Step 06 : Left-click and drag a box that covers Capuccino and Espresso.   
        """
        elem1=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g1!mmarker!r0!c0!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g5!mmarker!r0!c0!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-15,sy_offset=source_elem['y']+25,tx_offset=target_elem['x']+20,ty_offset=target_elem['y']-20)
        
        """
            Step 07 : Click Filter Chart option.
        """ 
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m7!']", '350K', 10)
        
        """
            Verify output 
        """
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 07.1 : Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 07.2 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K','300K', '350K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 07.3 : Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, "Step 07.4 : Verify number of line",custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 07.5 : Verify  bar color", attribute_type='stroke')
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 07.6 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.6 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.7 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 07.9 : Filter Button Visible')
         
        """
            Step 08 : Click Remove Filter option
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m5!']", '1,000K', 10)
        
        """
            Verify original chart appears in the output. Make sure filter icon is not present.
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 08.1 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.2 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.3 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.4 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.5 : Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 08.6 : Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 08.7 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 08.9 : Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 08.10 : Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 08.11 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, "Step 08.12 : Verify number of line", custom_css="path[class^='riser']")
         
        """ 
            Step 09:Hover over the Coffee Grinder point on the Gifts chart. Verify context menu displays:
            Category: Gifts, Product: Coffee Grinder, Unit Sales: 186,534, Filter Chart, Exclude from Chart
        """
        expected_tooltip_list=['Category:Gifts', 'Product:Coffee Grinder', 'Unit Sales:186534', 'Filter Chart', 'Exclude from Chart']
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g2!mmarker!r0!c2!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s0!g2!mmarker!r0!c2!", expected_tooltip_list, "Step 09: Verify bar value", default_move=True)
         
        """
            Step 10: Click Exclude from Chart option.
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","marker!s0!g2!mmarker!r0!c2!", 'Exclude from Chart', default_move=True)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_f g[class='markers'] circle", 9, 5)
        
        """
            Verify FOOD category is excluded from the chart and filter icon appears on the Active tool bar.
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 10.1 :Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.2 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.3 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.4 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.5 : Filter Button Visible')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 10.6 : Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 10.7 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 10.8 : Verify XY labels")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0_f', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 10:d Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 10.9 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 12, "Step 10.10 : Verify number of line")
        
        """ 
            Step 11: Click remove filter icon from the active tool bar. 
        """
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0_f g[class='markers'] circle", 10, 5)
        
        """
            Verify original chart appears with 4 points in the GIFTS category and 'Remove filter' is no longer present.
        """
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category, Product', 'Step 11.1 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.2 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.3 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.4 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.5 : Filter Button Removed')
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "Unit Sales", "Step 11.6 : Verify -yAxis Title")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product", "Step 11.7 : Verify -xAxis Title")
        expected_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 11.8 : Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, "Step 11.9 : Verify number of line")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'columns', 'Category', ['Coffee','Food', 'Gifts'], "Step 11.10 : Verify row header and value")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 11.11 : Verify  bar color",attribute_type='stroke')
       
        utillobj.switch_to_default_content(pause=3)
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()