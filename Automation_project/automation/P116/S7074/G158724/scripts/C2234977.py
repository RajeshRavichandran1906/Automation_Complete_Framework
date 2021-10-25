'''
Created on JUL 31, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2234977
TestCase Name = Verify chart filter functionality in Vertical Absolute Line in others tab (under Format menu).
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2234977_TestClass(BaseTestCase):

    def test_C2234977(self):
        
        """
            TESTCASE VARIABLES
        """     
        Test_Case_ID="C2234977"
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : Create a new chart in IA using the GGSALES file.Select Active Report as Output file format. From the Format/Other menu, select Lines.Select Vertical Absolute Line.Click OK..
        """    
        utillobj.infoassist_api_login('Chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s0!']", 'Series0', 20)
        
        ribbonobj.change_output_format_type('active_report', location='Home')
        utillobj.synchronize_with_visble_text("#HomeFormatType>div", 'ActiveReport', 6)
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbonobj.select_other_chart_type('line', 'vertical_absolute_line', 1, ok_btn_click=True)
        utillobj.synchronize_with_number_of_element("#pfjTableChart_1 svg path[class*='mline']", 5, 10)
        time.sleep(2)
        
        """
            Step 02 : Add fields as follows: Region under Rows, Unit Sales and Dollar Sales under Vertical Axis, Product ID under Horizontal Axis
        """
        metadataobj.datatree_field_click('Region', 1, 0, 'Add To Query', 'Rows')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='rowHeader-label!']", 'Region', 10)
        
        metadataobj.datatree_field_click('Unit Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='yaxis-title']", 'UnitSales', 10)
        
        metadataobj.datatree_field_click('Dollar Sales', 1, 0, 'Add To Query', 'Vertical Axis')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s1!']", 'DollarSales', 10)
         
        metadataobj.datatree_field_click('Product ID', 1, 0, 'Add To Query', 'Horizontal Axis')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'ProductID', 10)
        
        """
            Step 03 : See corresponding data is displayed in the Live Preview pane.
        """ 
        resobj.verify_xaxis_title("TableChart_1", "Product ID", "Step 03.1 : Verify -xAxis Title")
        resobj.verify_visualization_row_column_header_labels('TableChart_1', 'Rows', 'Region', ['Midwest','Northeast','Southeast','West'], "Step 03.2 :")
        expected_xval_list=['C141','C144']
        expected_yval_list=['0','0.3M','0.6M','0.9M','1.2M','1.5M','0','0.3M','0.6M','0.9M','1.2M','1.5M','0','0.3M','0.6M','0.9M','1.2M','1.5M','0','0.3M','0.6M','0.9M','1.2M','1.5M']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, "Step 03.3 :")
        legend=['Unit Sales','Dollar Sales']
        resobj.verify_riser_legends('TableChart_1', legend, "Step 03.4 : ")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!r2!c0!", "bar_blue1", "Step 03.5 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 8, "Step 03.6: Verify number of line",custom_css=".chartPanel .scrollCharts path[class*='riser']")
        
        """
            Step 04 : Run the report    
        """ 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'ProductID', 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product ID", "Step 04.1: Verify -xAxis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Region', ['Midwest','Northeast','Southeast','West'], "Step 04.2 : ")
        expected_xval_list=['C141','C142','C144','F101','F102','F103','G100','G104','G110','G121']
        expected_yval_list=['0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M','0','0.5M','1M','1.5M','2M','2.5M','3M','3.5M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, "Step 04.3 : ")
        legend=['Unit Sales','Dollar Sales']
        resobj.verify_riser_legends('MAINTABLE_wbody0', legend, "Step 04.4 : ")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0!", "bar_blue", "Step 04.5 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, "Step 04.6 : Verify number of line",custom_css=".chartPanel .scrollCharts path[class*='riser']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 04.7 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.8 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!r1!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=4.5)
        expected_tooltip_list=['Region:Northeast', 'Product ID:C141', 'Dollar Sales:850107', 'Filter Chart', 'Exclude from Chart']
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g0!mmarker!r1!c0", expected_tooltip_list, "Step 04.11 : Verify bar value", default_move=True)
        
        """
            Step 05 : Select F101, F102 and F103 points for Unit Sales and Dollar Sales for Northeast region
        """
        elem1=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g3!mmarker!r1!c0!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g5!mmarker!r1!c0!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-20,sy_offset=source_elem['y']+20,tx_offset=target_elem['x']+20,ty_offset=target_elem['y']-20)
        utillobj.synchronize_with_number_of_element("[id^='ibi$tt$'][style*='visible']", 1, 2)
        
        """
            Step 06 : Verify that chart filter context menu appears on the screen with these options : 6 points, Filter Chart, Exclude from Chart
        """
        resobj.select_or_verify_lasso_filter(verify=['6 points','Filter Chart','Exclude from Chart'],msg='Step 06: Expect to see the left-click options appear', select='Filter Chart')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m5!']", '2M', 5)
        
        """
            Step  07 : Click Filter chart and verify F101, F102 and F103 Product IDs are displayed.
        """
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='yaxis-labels!m5!']", '2M', 5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product ID", "Step 07.1 : Verify -xAxis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Region', ['Northeast'], "Step 07.2 : ")
        expected_xval_list=['F101','F102','F103']
        expected_yval_list=['0','0.4M','0.8M','1.2M','1.6M','2M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, "Step 07.3 : ")
        legend=['Unit Sales','Dollar Sales']
        resobj.verify_riser_legends('MAINTABLE_wbody0', legend, "Step 07.4 : ")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0", "bar_blue", "Step 07.5 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, "Step 07.6: Verify number of line",custom_css="path[class*='riser']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 07.7 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.8 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 07.11 : Filter Button Visible')
        
        """
            Step 08 : Hover over F101 Dollar Sales point and verify this context menu appears: Region: Northeast, Product ID: F101, Dollar Sales: 907,171, Filter Chart Exclude from Chart, Remove Filter
        """
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=4.5)
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        expected_tooltip_list=['Region:Northeast', 'Product ID:F101', 'Dollar Sales:907171', 'Filter Chart', 'Exclude from Chart','Remove Filter'] #As per ACT-1247 jira added "Undo Filter" in tooltip verification value
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g0!mmarker!r0!c0", expected_tooltip_list, "Step 08: Verify bar value",default_move=True)      
        
        """
            Step 09 : Click Exclude from chart
        """
        
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0", "marker!s1!g0!mmarker!r0!c0", 'Exclude from Chart',default_move=True)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-labels!g0!mgroupLabel!']", 'F102', 5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product ID", "Step 09.1 : Verify -xAxis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Region', ['Northeast'], "Step 09.2 : ")
        expected_xval_list=['F102','F103']
        expected_yval_list=['0','0.4M','0.8M','1.2M','1.6M','2M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, "Step 09.3 : ")
        legend=['Unit Sales','Dollar Sales']
        resobj.verify_riser_legends('MAINTABLE_wbody0', legend, "Step 09.4")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!r0!c0", "bar_blue", "Step 09.5 : Verify  bar color",attribute_type='stroke')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, "Step 09.6 : Verify number of line",custom_css="path[class*='riser']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 09.7 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.8 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.11 : Filter Button Visible')
        
        """
            Step 10 : Hover over F102 Dollar Sales point and verify this context menu appears: Region: Northeast, Product ID: F102, Dollar Sales: 1802005, Filter Chart, Exclude from Chart, Remove Filter
        """
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=4.5)
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        expected_tooltip_list=['Region:Northeast', 'Product ID:F102', 'Dollar Sales:1802005', 'Filter Chart', 'Exclude from Chart', 'Undo Filter', 'Remove Filter'] #As per ACT-1247 jira added "Undo Filter" in tooltip verification value
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g0!mmarker!r0!c0", expected_tooltip_list, "Step 10 : Verify bar value", default_move=True)
        
        """
            Step 11 : Click Exclude from chart
        """
        resobj.select_default_tooltip_menu("MAINTABLE_wbody0","marker!s1!g0!mmarker!r0!c0", 'Exclude from Chart',default_move=True)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-labels!g0!mgroupLabel!']", 'F103', 8)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "Product ID", "Step 11.1 : Verify -xAxis Title")
        resobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody0', 'Rows', 'Region', ['Northeast'], "Step 11.2")
        expected_xval_list=['F103']
        expected_yval_list=['0','0.4M','0.8M','1.2M','1.6M','2M']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, "Step 11.3 : ")
        legend=['Unit Sales','Dollar Sales']
        resobj.verify_riser_legends('MAINTABLE_wbody0', legend, "Step 11.4 : ")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, "Step 11.5 : Verify number of line",custom_css="path[class*='riser']")
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 11.6 : Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.7 : Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.9 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 11.10 : Filter Button Visible')       
        
        """
            Step 12 : Hover over F103 Dollar Sales point and verify this context menu appears: Region: Northeast, Product ID: F102, Dollar Sales: 1670818, Remove Filter
        """
        parent_obj = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        utillobj.synchronize_with_number_of_element("#tdgchart-tooltip[style*='visible']", 1, 2)
        expected_tooltip_list=['Region:Northeast', 'Product ID:F103', 'Dollar Sales:1670818', 'Undo Filter', 'Remove Filter']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "marker!s1!g0!mmarker!r0!c0!", expected_tooltip_list, "Step 12 : Verify bar value",default_move=True)
        utillobj.switch_to_default_content(pause=3)
        
        ele=self.driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
     
if __name__ == '__main__':
    unittest.main()
