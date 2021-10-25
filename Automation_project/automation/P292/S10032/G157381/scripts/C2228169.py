'''
Created on Dec 29, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228169
TestCase Name = Verify Legend Position and Legend orientation (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase

class C2228169_TestClass(BaseTestCase):

    def test_C2228169(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228169'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
        Step 02: Double click "HIRE_DATE", "SALARY", "CURR_SAL".
        """
        
        metaobj.datatree_field_click('HIRE_DATE', 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 15)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 15)
         
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 15)
        
        legend_right_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_right_height:',legend_right_height)
        
        """
        Step 03: Click on "Format" tab.
        Step 04: Expand "Labels" group.
        Step 05: Click "Legend" dropdown.
        Step 06: Select "More Legend Options...".
        """
        
        ribbonobj.select_ribbon_item('Format', 'labels')
        ribbonobj.select_ribbon_item('Format', 'legend', opt='More Legend Options...')
        time.sleep(5)
        
        """
        Step 07: Click "Legend Position" dropdown > "Top".
        Step 08: Click "OK".
        """
        parent_css="[id^='QbDialog'] [class*='active'] #legendSplitPane"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 25)
        
        utillobj.verify_object_visible(parent_css, True, "Step 07: Verify the Format Legend window is displayed.")
        position_dropdown = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='legendPositionComboBox_MOONBEAM'] div[class^='bi-button button']")
        
#         combo_elem=self.driver.find_element_by_css_selector("#legendPositionComboBox_MOONBEAM")
        utillobj.select_any_combobox_item(position_dropdown, 'Top')

        ok_btn_css = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='legendOkBtn']")
        utillobj.default_click(ok_btn_css)
        time.sleep(2)
        
        """
        Step 09: Verify the chart legend options are applied in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 15)
        
        xaxis_value="HIRE_DATE"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step09:a(i) Verify X-Axis Title")
        expected_xval_list=['80/06/02', '81/07/01', '81/11/02', '82/01/04', '82/02/02', '82/04/01', '82/05/01', '82/07/01', '82/08/01']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step09:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 9, 'Step09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step09.c: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step09.d: Verify first bar color")
        legend=['SALARY', 'CURR_SAL']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step09:e Verify Y-Axis Title")
        
        legend_top_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_top_height:',legend_top_height)
        height_status = legend_right_height>legend_top_height
        print(height_status)
        utillobj.asequal(height_status, True, "Step 09: Verify the chart legend moved to top in Live Preview") 
        
        """
        Step 10: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
         
        """
        Step 11: Verify the chart displayed is the same as in "Live Preview".
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 15)
        
        xaxis_value="HIRE_DATE"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        expected_xval_list=['80/06/02', '81/07/01', '81/11/02', '82/01/04', '82/02/02', '82/04/01', '82/05/01', '82/07/01', '82/08/01']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step11:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 9, 'Step11.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'CURR_SAL']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step11:c Verify Y-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 11.g: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 11.h: Verify first bar color")
        legend_top_height1=driver.find_element_by_css_selector("#jschart_HOLD_0 .legend-clip").get_attribute('height')
        print('legend_top_height1:',legend_top_height1)
        height_status1 = legend_right_height>legend_top_height1
        print(height_status1)
        utillobj.asequal(height_status1, True, "Step 11(i): Verify the chart legend moved to top in Run window") 
        utillobj.switch_to_default_content(pause=2)
        
        """
        Step 12: Click "IA" > "Save".
        Step 13: Click Save in the toolbar > Save as "C2228169" > Click Save, click save
        Step 14: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 15:Run saved fex from bip using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228169.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_chart_1','mrid','mrpass')
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 65)
        
        """
        Step 16: Verify the chart is the same as when run from IA.
        """
        xaxis_value="HIRE_DATE"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        expected_xval_list=['80/06/02', '81/07/01', '81/11/02', '82/01/04', '82/02/02', '82/04/01', '82/05/01', '82/07/01', '82/08/01']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step17:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 2, 9, 'Step17.b: Verify the total number of risers displayed on preview')
        legend=['SALARY', 'CURR_SAL']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step17:c Verify Y-Axis Title")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 17.g: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar", "bar_green", "Step 17.h: Verify first bar color")
        
        legend_top_height2=driver.find_element_by_css_selector("#jschart_HOLD_0 .legend-clip").get_attribute('height')
        print('legend_top_height2:',legend_top_height2)
        height_status2 = legend_right_height>legend_top_height2
        print(height_status2)
        utillobj.asequal(height_status2, True, "Step 17(i): Verify the chart legend moved to top in Run window") 
        
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 17: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 18: Restore the fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228169.fex
        Step 19: Verify IA is launched and the correct chart is displayed.
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 18, 65)
        
        xaxis_value="HIRE_DATE"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step20:a(i) Verify X-Axis Title")
        expected_xval_list=['80/06/02', '81/07/01', '81/11/02', '82/01/04', '82/02/02', '82/04/01', '82/05/01', '82/07/01', '82/08/01']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K', '80K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step20:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 2, 9, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step20.c: Verify first bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar", "bar_green", "Step20.d: Verify first bar color")
        legend=['SALARY', 'CURR_SAL']
        resultobj.verify_riser_legends("TableChart_1", legend, "Step20:e Verify Y-Axis Title")
        
        legend_top_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_top_height:',legend_top_height)
        height_status = legend_right_height>legend_top_height
        print(height_status)
        utillobj.asequal(height_status, True, "Step 20(i): Verify the chart legend moved to top in Live Preview")
        
        """
        Step 20:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()