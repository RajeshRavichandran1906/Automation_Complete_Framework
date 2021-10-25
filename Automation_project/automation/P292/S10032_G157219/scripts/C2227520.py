'''
Created on Dec 4, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227520
TestCase Name = Verify a Reporting Object with Report and Chart
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_reporting_object, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2227520_TestClass(BaseTestCase):

    def test_C2227520(self):
        
        Test_Case_ID = "C2227520"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfreportobj = wf_reporting_object.Wf_Reporting_Object(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01 : Launch Reporting Object with car:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=reportingobject&master=ibisamp/car
        """
        utillobj.infoassist_api_login('reportingobject','ibisamp/CAR','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(6)
         
        """    
        Step 02: Double click "Report".
        """
        wfreportobj.select_ro_tree_item("Report")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Report", click_type = 2)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
         
        """    
        Step 03: Double click "CAR", "SALES".
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
         
        metaobj.datatree_field_click("CAR", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 11, expire_time=10) 
        time.sleep(3)    
         
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#TableChart_1  div[class^='x']", 22, expire_time=10) 
        time.sleep(3)
         
        """    
        Step 04: Click "IA" > "Save".
        Step 05: Verify "Message" prompt is displayed.
        Step 06: Click "OK".
        """
        ribbonobj.select_tool_menu_item('save')
        time.sleep(5)
        prompt=driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        utillobj.asequal(prompt,True,"Step 05: Verify 'Message' prompt is displayed.")
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(3)
         
        """    
        Step 07: Click "IA" > Exit
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
         
        """    
        Step 08: Double click "Chart".
        """
        wfreportobj.select_ro_tree_item("Chart")
        time.sleep(2)
        wfreportobj.select_ro_tree_item("Chart", click_type = 2)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
         
        """    
        Step 09: Double click "CAR", "SALES".
        """
        parent_css="[id^=QbMetaDataTree]"
        resultobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(2)
         
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#TableChart_2 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 10, expire_time=15)   
         
        metaobj.datatree_field_click("SALES", 2, 1)
        resultobj.wait_for_property("#TableChart_2 text[class='yaxis-title']", 1, expire_time=10, string_value='SALES')
         
        time.sleep(5)
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
        time.sleep(5)
        prompt=driver.find_element_by_css_selector("div[id^='BiDialog'] img[src*='infomark']").is_displayed()
        utillobj.asequal(prompt,True,"Step 11: Verify 'Message' prompt is displayed.")
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(3)
         
        """    
        Step 13: Click "IA" > Exit
        """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    
        Step 14: Click "Run" in "Reporting Object" window.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        
        """    
        Step 15: Verify the following is displayed.
        """
        parent_css="html table > tbody > tr input[type='submit']"
        resultobj.wait_for_property(parent_css, 1)
        
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
        time.sleep(3)
#         iarunobj.create_table_data_set("table[summary='Summary']", Test_Case_ID+'_Ds01.xlsx' )
        iarunobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+'_Ds01.xlsx', 'Step 17: Verify the report is displayed')
        
        """    
        Step 18: Dismiss the output window.
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    
        Step 19: Click "Run" in "Reporting Object" window.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        
        """    
        Step 20: Enable "Run Graph" radio button.
        """
        parent_css="html table > tbody > tr input[type='submit']"
        resultobj.wait_for_property(parent_css, 1)
        wfreportobj.select_run_option(run_option_input_value='graph', submit_type='Submit')
        
        """    
        Step 21: Verify the chart is displayed.
        """
        time.sleep(5)
        parent_css="#jschart_HOLD_0"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="CAR"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 09:a(i) Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step09.b:Verify XY labels")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step09.c: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step09.d: Verify first bar color")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 26.4: Verify tooltiptip values")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0")
        utillobj.take_screenshot(ele,'C2227520_Actual_step21', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    
        Step 22: Dismiss the output window.
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    
        Step 23: Click "RO" > "Save As"
        Step 24: Enter Title = "C2227520".
        Step 25: Click "Save".
        """
        time.sleep(2)
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
        time.sleep(10)
        
        """
        Step 28: Verify successful restore
        """
        parent_css="#applicationButton img[src*='reporting_objects']"
        resultobj.wait_for_property(parent_css, 1)
        ro_tool_name=['Reporting Object', 'Preprocessing Other', 'Joins', 'Defines', 'Filters', 'Where Statements', 'Report', 'Chart', 'Postprocessing Other']
        wfreportobj.verify_ro_tree_item(ro_tool_name,"Step 28: Verify successful restore")
        
        """
        Step 29: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()