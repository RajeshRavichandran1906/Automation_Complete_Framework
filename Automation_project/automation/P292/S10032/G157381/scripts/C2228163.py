'''
Created on Dec 20, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228163
TestCase Name = Verify slicers (82xx)
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C2228163_TestClass(BaseTestCase):

    def test_C2228163(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2228163'
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        chart = Chart(self.driver)
        
        """
        TESTCASE CSS
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        
        
        """
        Step 01: Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        chart.wait_for_visible_text(chart_css, "Group 0")
         
        """
        Step 02: Double click on "LAST_NAME", "SALARY"..
        """
        chart.double_click_on_datetree_item("LAST_NAME", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "LAST_NAME")

        chart.double_click_on_datetree_item("SALARY", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "SALARY")
        
        """
        Step 03: Click on the "Slicers" tab.
        """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(4)
        
        """
        Step 04: Drag "LAST_NAME" from Data pane into "Group 1" in Slicer tab.
        """
        ia_ribbobj.drag_drop_fields_to_slicer('LAST_NAME', 1, 1)
        
        parent_css= "#SlicersCluster_1_Control1Slicer_0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """
        Step 05: Click the "LAST_NAME" (dropdown).
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'LAST_NAME')
        
        parent_css= "[id^='QbSlicerValuesDialog'] #filterValuesOkBtn img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        """
        Step 06: Multi-select "CROSS", "IRVING", "JONES", and "MCCOY".
        """
        combo_item_list = ['CROSS', 'IRVING', 'JONES', 'MCCOY']
        ia_ribbobj.select_slicer_values_from_single_list(combo_item_list)
        
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
        utillobj.synchronize_with_number_of_element(parent_css, 4, 30)
       
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step09:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step09:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        
        """
        Step 10: Click "Run".
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
         
        """
        Step 11: Verify the same chart displayed in "Live Preview" is displayed at runtime.
        """
        
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 30)
       
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step11:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        
        """
        Step 12: Click Save in the toolbar > Save as "C2228163" > Click Save
        Step 13: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnOK", "Save")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(5)
           
        """
        Step 14:Step 14: Run saved fex from bip using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228163.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_chart_1','mrid','mrpass')
        time.sleep(15)
        
        """
        Step 15:Verify the chart is run in a new window.
        """
        parent_css="#jschart_HOLD_0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 45)
       
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step17:a(ii) Verify X-Axis Title")
        expected_xval_list=['BANNING', 'BLACKWOOD', 'CROSS', 'GREENSPAN', 'IRVING', 'JONES', 'MCCOY', 'MCKNIGHT', 'ROMANS', 'SMITH', 'STEVENS']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step17:a(ii):Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 11, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 17.c: Verify first bar color")
        
        #ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 16:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 17:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228163.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_chart_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)   

        """
        Step 18:Verify IA is launched preserving the chart in "Live Preview".
        """
       
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 65)
        
        xaxis_value="LAST_NAME"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step20:a(i) Verify X-Axis Title")
        yaxis_value="SALARY"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step20:a(ii) Verify X-Axis Title")
        expected_xval_list=['CROSS', 'IRVING', 'JONES', 'MCCOY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step20.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 20.c: Verify first bar color")
        
        """
        Step 19:Select "Slicers" tab.
        Step 20: Verify the "LAST_NAME" slicer is still available.
        """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(5)
        expected_list= ['Group 1', 'LAST_NAME', 'Multiple']
        ia_ribbobj.verify_slicer_group(1, expected_list, "Step 20: Verify the 'LAST_NAME' slicer is still available.")
        
        """
        Step 21:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp Click "IA" > "Exit".
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()