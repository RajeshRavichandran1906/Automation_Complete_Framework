'''

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227567
TestCase Name = Verify create a report then drilldown to a report
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227567_TestClass(BaseTestCase):

    def test_C2227567(self):
        
        Test_Case_ID = "C2227567"
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
        Step04: Select "CURR_SAL" in "Query" pane.
        """
        time.sleep(2)
        metaobj.querytree_field_click("CURR_SAL", 1, 0)
        time.sleep(2)        
         
        """
        Step05: Click "Links" > "Drill down" from "Field" tab.
        """
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        
        """
        Step06: Verify the following window is displayed.
        """
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
        
        """
        Step07: On "Drill Down" window, Enable "Webpage" radio button
        Step08: Set "URL" = http://www.yahoo.com.
        Step09: Set "Description" = "Yahoo Drilldown".
        Step10: Tab out of the textfield
        Step11: Verify "Yahoo Drilldown" is showing on the left frame.
        Step12: Click "OK".
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.yahoo.com", set_description='Yahoo Drilldown')
        ia_ribbonobj.create_drilldown_report ("webpage", verify_left_pane=['1','Yahoo Drilldown'], click_ok='yes',msg="Step11: Verify Yahoo Drilldown is showing on the left frame")
        
        """
        Step13: Verify hyperlinks are created in "Live Preview"..
        """
        ia_resultobj.verify_autolink("TableChart_1","$11,000.00",12,"Step13: Verify Report preview with hyperlinks")
        time.sleep(3)
        
        """
        Step14: Click "Run".
        Step15: Verify the report is displayed.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        '''frame=self.driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=frame.location['x']
        y_fr=frame.location['y'] 
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))'''
        utillobj.switch_to_frame(pause=1)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227567_run_Ds01.xlsx" , 'Step 15: Verify report data set on run window')
        
        """
        Step16: Hover over the hyperlinks and verify that "Description" is displayed.
        Step17: Click on any hyperlink.
        """
        time.sleep(2)
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='Yahoo Drilldown', msg='Step16:Verify Drilldown tooltip')
        #ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='Yahoo Drilldown', msg='Step16:Verify Drilldown tooltip',x_offset=x_fr,y_offset=y_fr-17,browser_height=80)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(10)  
        
        """
        Step18: Verify it displays a new window going to www.yahoo.com site.
        """
        drill=("Yahoo" in driver.title)
        utillobj.asequal(True, drill, "Step 35a: Verify Yahoo page is displayed")
        time.sleep(3)       
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        time.sleep(3)
        
        """
        Step19: Click "IA" > "Save" > C2227567 > Click Save
        """
        utillobj.switch_to_default_content(pause=2)
        #self.driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
    