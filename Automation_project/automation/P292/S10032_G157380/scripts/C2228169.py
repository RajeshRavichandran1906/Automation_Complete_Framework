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
from selenium.webdriver.common.by import By

class C2228169_TestClass(BaseTestCase):

    def test_C2228169(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228169'
        Test_Case_saveas_ID ="C125117"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "HIRE_DATE", "SALARY", "CURR_SAL".
        """
        time.sleep(3)
        metaobj.datatree_field_click('HIRE_DATE', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 9)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
         
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18)
        
        legend_right_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_right_height:',legend_right_height)
        
        """
        Step 03: Click on "Format" tab.
        Step 04: Expand "Labels" group.
        Step 05: Click "Legend" dropdown.
        Step 06: Select "More Legend Options...".
        """
        ribbonobj.select_ribbon_item('Format', 'Legend_Dropdown', opt='More Legend Options...')
        time.sleep(5)
        
        """
        Step 07: Click "Legend Position" dropdown > "Top".
        Step 08: Click "OK".
        """
        parent_css="[id^='QbDialog'] [class*='active'] #legendSplitPane"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)
        utillobj.verify_object_visible(parent_css, True, "Step 07: Verify the Format Legend window is displayed.")
        position_dropdown = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='legendPositionComboBox_MOONBEAM'] div[class^='bi-button button']")
        utillobj.click_on_screen(position_dropdown, 'middle')
        utillobj.click_on_screen(position_dropdown, 'middle',  click_type=0)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Top', custom_css="div[id*='BiComboBoxItem']")
        time.sleep(3)
        ok_btn_css = driver.find_element_by_css_selector("[id^='QbDialog'] [class*='active'] [id='legendOkBtn']")
        utillobj.click_on_screen(ok_btn_css, 'middle')
        utillobj.click_on_screen(ok_btn_css, 'middle',  click_type=0)
        
        """
        Step 09: Verify the chart legend options are applied in "Live Preview".
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18)
        time.sleep(5)
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
        time.sleep(5)
        legend_top_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_top_height:',legend_top_height)
        height_status = legend_right_height>legend_top_height
        print(height_status)
        utillobj.asequal(height_status, True, "Step 09: Verify the chart legend moved to top in Live Preview") 
        time.sleep(5)
        
        """
        Step 10: Click "Run".
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 11: Verify the chart displayed is the same as in "Run window".
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18)
        time.sleep(5)
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
        time.sleep(5)
        bar= ['HIRE_DATE:80/06/02', 'SALARY:$21,000.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 11.i: Verify bar value")
        time.sleep(3)
        legend_top_height1=driver.find_element_by_css_selector("#jschart_HOLD_0 .legend-clip").get_attribute('height')
        print('legend_top_height1:',legend_top_height1)
        height_status1 = legend_right_height>legend_top_height1
        print(height_status1)
        utillobj.asequal(height_status1, True, "Step 11(i): Verify the chart legend moved to top in Run window") 
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 12: Click "IA" > "Save".
        Step 13: Enter Title = "C125117".
        Step 14: Click "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_saveas_ID)
        time.sleep(10)
        
        """
        Step 15: Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 16: Locate saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 17: Verify the chart is the same as when run from IA.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18)
        time.sleep(5)
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
        time.sleep(5)
        bar=['HIRE_DATE:80/06/02', 'SALARY:$21,000.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 17.i: Verify bar value")
        time.sleep(3)
        legend_top_height2=driver.find_element_by_css_selector("#jschart_HOLD_0 .legend-clip").get_attribute('height')
        print('legend_top_height2:',legend_top_height2)
        height_status2 = legend_right_height>legend_top_height2
        print(height_status2)
        utillobj.asequal(height_status2, True, "Step 17(i): Verify the chart legend moved to top in Run window") 
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 18: Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 19: Right click the saved fex > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 20: Verify IA is launched and the correct chart is displayed.
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 18)
        time.sleep(5)
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
        time.sleep(5)
        legend_top_height=driver.find_element_by_css_selector("#TableChart_1 .legend-clip").get_attribute('height')
        print('legend_top_height:',legend_top_height)
        height_status = legend_right_height>legend_top_height
        print(height_status)
        utillobj.asequal(height_status, True, "Step 20(i): Verify the chart legend moved to top in Live Preview") 
        
        """
        Step 21: Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()