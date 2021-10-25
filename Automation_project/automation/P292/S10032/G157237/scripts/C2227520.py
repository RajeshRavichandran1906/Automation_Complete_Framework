'''
Created on Dec 4, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227520
TestCase Name = Verify a Reporting Object with Report and Chart
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity, core_utility, global_variables
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_reporting_object, ia_run

class C2227520_TestClass(BaseTestCase):

    def test_C2227520(self):
        
        Test_Case_ID = "C2227520"
        
        driver = self.driver
        iarunobj = ia_run.IA_Run(self.driver)
        g_var = global_variables.Global_variables()
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
          
        """
        Step 01 : Launch Reporting Object with car:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=ibisamp/car
        """
        utillobj.infoassist_api_login('reportingobject','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        reporting_applicaton_button_css="#applicationButton img"
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
         
        """    
        Step 02: Double click "Report".
        """
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report", click_type = 2)
        core_utilobj.switch_to_new_window()
         
        """    
        Step 03: Double click "CAR", "SALES".
        """
        meta_datatree_css="[id^=QbMetaDataTree]"
        utillobj.synchronize_until_element_is_visible(meta_datatree_css, resultobj.chart_long_timesleep)
         
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'CAR',  resultobj.chart_long_timesleep) 
         
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'SALES',  resultobj.chart_long_timesleep)
         
        """    
        Step 04: Click "IA" > "Save".
        Step 05: Verify "Message" prompt is displayed.
        Step 06: Click "OK".
        """
        ribbonobj.select_tool_menu_item('save')
        utillobj.synchronize_until_element_is_visible("div[id^='BiDialog'] img[src*='infomark']", resultobj.chart_long_timesleep)
        prompt=driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        utillobj.asequal(prompt,True,"Step 05: Verify 'Message' prompt is displayed.")
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(3)
         
        """    
        Step 07: Click "IA" > Exit
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
         
        """    
        Step 08: Double click "Chart".
        """
        wfreportobj.select_ro_tree_item("Chart")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Chart", click_type = 2)
        core_utilobj.switch_to_new_window()
         
        """    
        Step 09: Double click "CAR", "SALES".
        """
        utillobj.synchronize_until_element_is_visible(meta_datatree_css, resultobj.chart_long_timesleep)
        
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#TableChart_2 rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, resultobj.chart_long_timesleep)
         
        metaobj.datatree_field_click("SALES", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2 text[class='yaxis-title']", 'SALES', resultobj.chart_long_timesleep)
         
        xaxis_value="CAR"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 09:a(i) Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step09.b:Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 10, 'Step09.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue", "Step09.d: Verify first bar color")
         
        """    
        Step 10: Click "IA" > "Save".
        Step 11: Verify "Message" prompt is displayed.
        Step 12: Click "OK".
        """
        ribbonobj.select_tool_menu_item('save')
        utillobj.synchronize_until_element_is_visible("div[id^='BiDialog'] img[src*='infomark']", resultobj.chart_long_timesleep)
        prompt=driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        utillobj.asequal(prompt,True,"Step 11: Verify 'Message' prompt is displayed.")
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(3)
         
        """    
        Step 13: Click "IA" > Exit
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        core_utilobj.switch_to_previous_window(window_close=False)
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
        
        """    
        Step 14: Click "Run" in "Reporting Object" window.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
        
        """    
        Step 15: Verify the following is displayed.
        """
        submit_button_css="html table > tbody > tr input[type='submit']"
        utillobj.synchronize_until_element_is_visible(submit_button_css, resultobj.chart_long_timesleep)
        
        css = "html table > tbody > tr input[value='table']"
        utillobj.verify_object_visible(css, True, 'Step 15.a: Verify the run report is displayed.')
        
        css = "html table > tbody > tr input[value='graph']"
        utillobj.verify_object_visible(css, True, 'Step 15.b: Verify the run report is displayed.')
        
        """    
        Step 16: Click "Submit".
        """
        wfreportobj.select_run_option(run_option_input_value='table', submit_type='Submit')
        
        """    
        Step 17: Verify the report is displayed.
        """
        utillobj.synchronize_with_visble_text("table[summary='Summary']", 'CAR', resultobj.chart_long_timesleep)
#         iarunobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+'_Ds01.xlsx' )
        iarunobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+'_Ds01.xlsx', 'Step 17: Verify the report is displayed')
        
        """    
        Step 18: Dismiss the output window.
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
        
        """    
        Step 19: Click "Run" in "Reporting Object" window.
        """
        if g_var.browser_name.lower() == 'firefox':
            run_btn=driver.find_element_by_css_selector("#runButton img")
            core_utilobj.python_move_to_element(run_btn, element_location='top_left')
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
        
        """    
        Step 20: Enable "Run Graph" radio button.
        """
        utillobj.synchronize_until_element_is_visible(submit_button_css, resultobj.chart_long_timesleep)
        wfreportobj.select_run_option(run_option_input_value='graph', submit_type='Submit')
        
        """    
        Step 21: Verify the chart is displayed.
        """
        parent_css="#jschart_HOLD_0"
        utillobj.synchronize_until_element_is_visible(parent_css, resultobj.chart_long_timesleep)
        xaxis_value="CAR"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 21:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 21:a(i) Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step21.b:Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step21.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step21.d: Verify first bar color")
        
        """    
        Step 22: Dismiss the output window.
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
        
        """    
        Step 23: Click "RO" > "Save As"
        Step 24: Enter Title = "C2227520".
        Step 25: Click "Save".
        """
        wfreportobj.select_ro_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 26: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 27: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227520.fex&tool=reportingobject
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'reportingobject', 'S10032_infoassist_4',mrid='mrid',mrpass='mrpass')
        
        """
        Step 28: Verify successful restore
        """
        utillobj.synchronize_until_element_is_visible(reporting_applicaton_button_css, resultobj.chart_long_timesleep)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreportobj.verify_ro_tree_item(ro_tool_name,"Step 28: Verify successful restore")
        
        """
        Step 29: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()