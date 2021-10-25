'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224429'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
from common.locators import as_uiautomation_mainpage_locators

class C2224429_TestClass(AS_BaseTestCase):
    def test_C2224429(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        key_pattern=["down"]
        wait_time=[1,2,3,4,5,6,7,8,9]
        
        '''Testcase verification'''
        
        verify_help_dialog="App Studio Help"
        verify_msg_1="Step 01: Help file from local server opens in AS viewer"
        verify_msg_2="Step 02: Help file from local server opens in AS viewer for dropdown 'Help Topics'"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        '''Step 01: Click on the question mark at the far top right corner.
                    Close the WebFOCUS App Studio Online Help window'''
         
        as_utilobj.click_element_using_ui(split_button=locators.help_page_button)
        time.sleep(wait_time[0])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_help_dialog,verify_msg_1)
        time.sleep(wait_time[1])
          
        automation.WindowControl(ClassName=locators.dialog_class_name).Close(waitTime=1)
        time.sleep(wait_time[0])
         
        '''Step 02: Click the down arrow next to the question mark at top right and select Help Topics.
                    Close the WebFOCUS App Studio Online Help window'''
         
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_page_button,x=0.85,y=0.35,send_keys=key_pattern)
        time.sleep(wait_time[6])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_help_dialog,verify_msg_2)
        time.sleep(wait_time[1])
          
        automation.WindowControl(ClassName=locators.dialog_class_name).Close(waitTime=1)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()