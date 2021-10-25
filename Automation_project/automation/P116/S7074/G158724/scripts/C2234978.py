'''
Created on June 9, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234978
TestCase Name = Verify chart filter functionality in Vertical Absolute Area in others tab (under Format menu).
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea, ia_ribbon
from common.lib import utillity
from common.lib.utillity import UtillityMethods


class C2234978_TestClass(BaseTestCase):

    def test_C2234978(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID="C2234978"
        
        
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES and 
                    From Home tab Select Active Report as Output file format.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(9)
        
        """ Step 2: Select Format > Other
                    Select Vertical Absolute Area
                    Click OK.
        """
        ribbonobj.select_ribbon_item("Format", "Other")       
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('area', 'area', 1, ok_btn_click=True)
        time.sleep(1)
        
        
        """ Step 3: Add fields as follows:
                    Region under Columns,
                    Dollar Sales and Unit Sales under Vertical Axis
                    Product ID under Horizontal Axis
        """
        metadataobj.datatree_field_click('Region', 1, 1, 'Add To Query', 'Columns')
        parent_css="#TableChart_1 g.chartPanel text[class^='colHeader-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='Region', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Product ID', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='ProductID', with_regular_exprestion=True)
        result_obj.verify_xaxis_title("TableChart_1", 'Product ID', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_visualization_row_column_header_labels('TableChart_1', 'columns', 'Region', ['Midwest', 'Northeast', 'Southeast', 'West'], 'Step 3.2: ')
        expected_xval_list=['C141', 'C141', 'C144', 'C141', 'C144', 'C141', 'C144']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.4 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea!r0!c1!', 'bar_green', 'Step 3.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 8, 'Step 3.6: Verify Number of riser', custom_css="path[class^='riser']")
        
        
        """ Step 4: Click Run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product ID', "Step 4.1: Verify X-Axis Title")
        expected_xval_list=['C...', 'C...', 'F1...', 'F1...', 'F1...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F1...', 'F1...', 'F1...', 'G...',
                            'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F1...', 'F1...', 'F1...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...',
                            'F1...', 'F1...', 'F1...', 'G...', 'G...', 'G...', 'G...']
        expected_xval_list_cr=['C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M']
        br1 = UtillityMethods.parseinitfile(self,'browser')
        if br1=="Chrome" or br1=="IE":
            result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list_cr, expected_yval_list, 'Step 4.2: Verify XY Label')
        else:
            result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 4.2: Verify XY Label')
            
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 8, 'Step 4.3: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!marea!r0!c0!', 'pale_green', 'Step 4.4: Verify Color')
        css="#MAINTABLE_wbody0 .chartPanel"
        move=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(move, 'start')
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g1!mmarker!r0!c0!']")
        utillobj.click_on_screen(parent_obj,'middle', javascript_marker_enable=True, mouse_duration=2.5)
        time.sleep(3)
        expected_tooltip_list=['Region:Midwest', 'Product ID:C142', 'Dollar Sales:2883566', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'marker!s0!g3!mmarker!r0!c0', expected_tooltip_list, 'Step 4.5: verify the default tooltip values', default_move=True, mouse_duration=2.5)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales BY Region, Product ID', 'Step 4.6: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 4.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 4.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 4.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()