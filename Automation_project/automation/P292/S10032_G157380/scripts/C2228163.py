'''
Created on Dec 20, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228163
TestCase Name = Verify slicers (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228163_TestClass(BaseTestCase):

    def test_C2228163(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228163'
        Test_Case_saveas_ID ="IA-CHART-VAL-018"
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        time.sleep(5)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
         
        """
        Step 02: Double click on "LAST_NAME", "SALARY"..
        """
        time.sleep(3)
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 11)
         
        metaobj.datatree_field_click('SALARY', 2, 1)
        time.sleep(4)
        parent_css= "#TableChart_1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 03: Click on the "Slicers" tab.
        """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(4)
        
        """
        Step 04: Drag "LAST_NAME" from Data pane into "Group 1" in Slicer tab.
        """
        ia_ribbobj.drag_drop_fields_to_slicer('LAST_NAME', 1, 1)
        time.sleep(4)
        parent_css= "#SlicersCluster_1_Control1Slicer_0"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 05: Click the "LAST_NAME" (dropdown).
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'LAST_NAME')
        time.sleep(4)
        parent_css= "[id^='QbSlicerValuesDialog'] #filterValuesOkBtn img"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 06: Multi-select "CROSS", "IRVING", "JONES", and "MCCOY".
        """
        combo_item_list = ['CROSS', 'IRVING', 'JONES', 'MCCOY']
        ia_ribbobj.select_slicer_values_from_single_list(combo_item_list)
        time.sleep(2)
        
        """
        Step 07: Click "OK".
        """
        ia_ribbobj.close_slicer_dialog('ok')
        
        """
        Step 08: Click "Update Preview" in the "Options" group.
        """
        ribbonobj.select_ribbon_item('Slicers', 'update_preview')
        time.sleep(3)
        
        """
        Step 09: Verify the chart in Live Preview displays the selected values.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step09:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step09:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
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
        Step 11: Verify the same chart displayed in "Live Preview" is displayed at runtime.
        """
        time.sleep(6)
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step11:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['LAST_NAME:CROSS', 'SALARY:$52,837.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 11.d: Verify bar value")
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 12: Click "IA" > "Save".
        Step 13: Enter Title = "IA-CHART-VAL-018".
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
        Step 16: Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_saveas_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(10) 
        
        """
        Step 17: Verify the chart is run in a new window.
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step17:a(ii) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step17:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 11, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 17.c: Verify first bar color")
        time.sleep(5)
        bar=['LAST_NAME:BANNING', 'SALARY:$29,700.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar", bar,"Step 17.d: Verify bar value")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 18: Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 19: Locate the saved fex > Right Mouse click > "Edit With..." > InfoAssist+.
        """
        utillobj.infoassist_api_edit(Test_Case_saveas_ID, 'idis', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 20: Verify IA is launched preserving the chart in "Live Preview".
        """
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(elem)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step20:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step20:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 20.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step 21: Select "Slicers" tab.
        Step 22: Verify the "LAST_NAME" slicer is still available.
        """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(4)
        expected_list= ['Group 1', 'LAST_NAME', 'Multiple']
        ia_ribbobj.verify_slicer_group(1, expected_list, "Step 22: Verify the 'LAST_NAME' slicer is still available.")
        
        """
        Step 23: Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()