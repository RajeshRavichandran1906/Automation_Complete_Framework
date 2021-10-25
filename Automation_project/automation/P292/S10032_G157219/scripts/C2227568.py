'''

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227568
TestCase Name = Verify create a report then drilldown to a report
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227568_TestClass(BaseTestCase):

    def test_C2227568(self):
        
        Test_Case_ID = "C2227568"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: Launch IA Report mode with EMPLOYEE file:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/EMPLOYEE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/EMPLOYEE','P292/S10032_ia_1', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)        
           
        """
        Step02: Double click "LAST_NAME", "CURR_SAL".    
        """
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['LAST_NAME','CURR_SAL']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)        
         
        """
        Step03: Drag DEPARTMENT into the Filter pane
        """
        metaobj.datatree_field_click('DEPARTMENT', 1, 1,'Filter')
        time.sleep(2)
         
        """
        Step04: Select Type: Parameter > Click OK > OK
        """
        ia_ribbonobj.create_parameter_filter_condition('simple', ['AREA'],filter_dialog_close=True)
        time.sleep(2)
         
        """
        Step05: Click "Save" > save as "Report002" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID+"_Report002")
        time.sleep(2)
         
        """
        Step06: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step07: Launch IA Report mode with employee:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/employee&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/EMPLOYEE','P292/S10032_ia_1', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step08: Double click "EMP_ID", "LAST_NAME", "CURR_SAL"
        """
        metaobj.datatree_field_click('EMP_ID', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['EMP_ID','LAST_NAME','CURR_SAL']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 08: Verify Column titles ")
        time.sleep(2) 
         
        """
        Step09: Verify the following report is displayed.
        """
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, 'C2227566_Ds01.xlsx', 'Step09: Verify report data set on preview')
        
        """
        Step10: Select "CURR_SAL"
        """
        time.sleep(2)
        metaobj.querytree_field_click("CURR_SAL", 1, 0)
        time.sleep(2)        
         
        """
        Step11: Click "Drill down" from Field Tab Ribbon
        """
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        
        """
        Step12: On "Drill Down" dialog, Verify "Report" is enabled by default
        """
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
        
        """
        Step13: Click "Browse" > Select "Report002" > Open
        """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name='C2227568_Report002')
        
        """
        Step14: Click the "&" Sign in Parameters.
        Step15: Click on the Name (dropdown) and select "DEPARTMENT"
        Step16: Click "Type" dropdown and select "Constant"
        Step17: Enter "Value" = "MIS"
        Step18: Click "OK"
        """
        browser_type=utillobj.parseinitfile('browser')
        if browser_type == 'Chrome':
            ia_ribbonobj.create_drilldown_report("report",set_ampersand='add')
            time.sleep(1)
            elem=driver.find_element_by_css_selector("#drillDownParmPopup #paramValueName")
            action1 = ActionChains(driver)
            action1.move_to_element_with_offset(elem, 25, 8).click().perform()
            del action1
            time.sleep(1)
        ia_ribbonobj.create_drilldown_report("report",set_ampersand='add',name_select='DEPARTMENT', type_select='Constant', value_input="MIS", popup_close='ok')

        """
        Step19: Verify the 3 buttons are enabled (after a parameter has been entered)
        Step20: Verify the inputed text (DEPARTMENT, MIS) are displayed in the textbox area
        Step21: Click "OK" to dismiss "Drill Down" window
        """
        ia_ribbonobj.create_drilldown_report("report", verify_enabled_parameter_icons = ['add','edit','remove'], verify_input_text=['DEPARTMENT','MIS'], click_ok='yes')
        
        
        """
        Step22: Verify hyperlinks are created for "CURR_SAL" on "Live Preview"
        """
        ia_resultobj.verify_autolink("TableChart_1","$11,000.00",12,"Step22: Verify Report preview with hyperlinks")
        time.sleep(3)
         
        """
        Step23: Click "Run".
        Step24: Verify the following report is displayed
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        '''frame=self.driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=frame.location['x']
        y_fr=frame.location['y'] 
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))'''
        time.sleep(5)
        utillobj.switch_to_frame(pause=1)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227567_run_Ds01.xlsx" , 'Step 24: Verify report data set on run window')
         
        """
        Step25: Verify that clicking on a hyperlink displays the "Report002" in a new window
        """        
        time.sleep(2)
        #ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='C2227568_Report002', msg='Step25:Verify Drilldown tooltip',x_offset=x_fr,y_offset=y_fr-17,browser_height=80)
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='C2227568_Report002', msg='Step25:Verify Drilldown tooltip')
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(10)  
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227568_run_Ds01.xlsx" , 'Step25: Verify drilldown "Report002" data set')

        """
        Step26: Close the new window
        """ 
        time.sleep(3)       
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(3)
        
        """
        Step27: Click "IA" > "Save"
        Step28: Enter Title = "C2227568"
        Step29: Click "Save"
        """
        utillobj.switch_to_default_content()
        #self.driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step30: Run saved fex:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2227568.fex
        """
        suite_name=utillobj.parseinitfile('suite_id')
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', suite_name, 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "table[summary='Summary']")
        resultobj._validate_page(elem1) 
        
        """
        Step31: Verify the following report is displayed
        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227567_run_Ds01.xlsx" , 'Step31: Verify report data set on run window')        
        

if __name__ == '__main__':
    unittest.main()
    