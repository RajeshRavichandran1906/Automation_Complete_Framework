'''
Created on May 17, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234935
TestCase Name = Verify that a default Bar Chart can be changed to an Area Graph via the Series option.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea, active_miscelaneous
from common.lib import utillity



class C2234935_TestClass(BaseTestCase):

    def test_C2234935(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        Test_Case_ID="C2234935"
        
        
        """ Step 1: Right click on folder created in IA. 
                    Select New > Chart. 
                    Select Reporting server as GGSALES.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        
        """ Step 2: On the Format tab, in the Output Types group, click Active report. 
                    Click on Category and Unit Sales.
        """
        ribbonobj.change_output_format_type('active_report')
        time.sleep(1)
        parent_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        result_obj.wait_for_property(parent_css, 1, string_value='ActiveReport', with_regular_exprestion=True)
        time.sleep(1)
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        
        """ Step 3: Expect to see the following Preview Pane.
        """        
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 3.2: Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 1, 'Step 3.4: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 3.5: Verify Color')
        
        
        
        """ Step 4: Right click in the Bar on the Preview pane.
                    For the Series Type, select AREA.
                    Expect to see the following Series Type menu in the Preview Pane.
        """
        parent_css="#TableChart_1 .chartPanel g rect[class='riser!s0!g0!mbar!']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        elem=driver.find_element_by_css_selector(parent_css)
        utillobj.click_on_screen(elem, coordinate_type='start', click_type=1, x_offset=100, y_offset=50, pause=7)
        utillobj.select_or_verify_bipop_menu('Series Type')
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Area')
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 4.2: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 4.3: Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4.4: ')
        
        
        """ Step 5: Now click Run.
                    Expect to see the Area Chart displayed.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(1)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_0', 4, 'Step 5: Expect to see the Series Selection set to Line.')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5.1: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0 ', 'riser!s0!g0!marea', 'lochmara', 'Step 5.2: Verify Color')
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 5.3: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 5.4: Verify Y-Axis Title")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales BY Category', 'Step 5.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 5.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()