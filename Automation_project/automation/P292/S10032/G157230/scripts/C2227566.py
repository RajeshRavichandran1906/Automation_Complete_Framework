'''

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227566
TestCase Name = Verify create a report then drilldown to a report
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling,\
    ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227566_TestClass(BaseTestCase):

    def test_C2227566(self):
        
        Test_Case_ID = "C2227566"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: Launch IA Report mode with EMPLOYEE file:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/EMPLOYEE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/employee','P292/S10032_ia_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)  
          
        """
        Step02: Double click "EMP_ID", "LAST_NAME", "CURR_SAL".    
        """
        metaobj.datatree_field_click("EMP_ID", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('LAST_NAME', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CURR_SAL', 2, 1)
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['EMP_ID','LAST_NAME','CURR_SAL']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)        
         
        """
        Step03: Verify the following report is displayed.
        """
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, 'C2227566_Ds01.xlsx', 'Step 03: Verify report data set on preview')        
         
        """
        Step04: Click "IA" > "Save" > "Report001" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID+"_Report001")
        time.sleep(2)
         
        """
        Step05: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step06: Launch IA Report mode with CAR file:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_ia_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)  

        """
        Step07: Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY','CAR','DEALER_COST','RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 07: Verify Column titles ")
        time.sleep(2)              
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 4, 'C2227566_Ds02.xlsx', 'Step 07: Verify report data set on preview') 
        
        """
        Step08: Select "DEALER_COST".
        """
        metaobj.querytree_field_click("DEALER_COST", 1, 0)
        time.sleep(2)        
         
        """
        Step09: Click "Links" > "Drill down" from "Field" tab.
        """
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        
        """
        Step10: On "Drill Down" window, Verify "Report" is enabled by default
        """
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
        
        """
        Step11: Click "Browse" > Select "Report001" > Open.
        Step12: Verify the "Report" textfield is populated.
        """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name='C2227566_Report001')
        
        """
        Step13: Verify all the icons are enabled.
        Step14: Click "OK".
        """
        ia_ribbonobj.create_drilldown_report("report", verify_enabled_left_pane_icons=['create','duplicate','rename','remove','options'], click_ok='yes')

        """
        Step15: Verify hyperlinks are created for "DEALER_COST" on "Live Preview".
        """
        ia_resultobj.verify_autolink("TableChart_1","18,621",10,"Step15: Verify Report preview with hyperlinks")
        time.sleep(3)
        
        """
        Step16: Click "Run".
        Step17: Verify the report is displayed.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        '''frame=self.driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=frame.location['x']
        y_fr=frame.location['y'] 
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))'''
        time.sleep(5)
        utillobj.switch_to_frame(pause=1)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227566_run_Ds01.xlsx" , 'Step 17: Verify report data set on run window')
        
        """
        Step18: Click any hyperlink and verify that drilldown to "Report001" is working properly.
        """
        time.sleep(2)
        #ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='C2227566_Report001', msg='Step18:Verify Drilldown tooltip',x_offset=x_fr,y_offset=y_fr-17,browser_height=80)
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='C2227566_Report001', msg='Step18:Verify Drilldown tooltip')
        time.sleep(8)
        utillobj.switch_to_default_content()
        utillobj.switch_to_window(1)
        time.sleep(10)  
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227566_run_Ds02.xlsx" , 'Step 18: Verify drilldown "Report001" data set')

        """
        Step19: Close the New window
        """ 
        time.sleep(3)       
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(3)
        
        """
        Step20: Click "IA" > "Save" > C2227566 > Click Save
        """
        self.driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
    