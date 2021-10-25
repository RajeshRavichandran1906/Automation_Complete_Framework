'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224430'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2224430_TestClass(AS_BaseTestCase):
    def test_C2224430(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        key_pattern_2=['down','down','down','down']
        wait_time=[1,2,3,4]
        
        '''Testcase verification'''
        
        verify_dialog="Reset Layout"
        verify_msg_1="Step 01: Verify Reset Layout window pops up with options Yes and No (the default) and an OK button."
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        time.sleep(wait_time[0])
        
        '''Step 01: Click the Help icon to expand the Help menu and select Reset Layout.'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_page_button,x=0.85,y=0.35,send_keys=key_pattern_2)
        time.sleep(wait_time[2])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_1)
        time.sleep(wait_time[0])
        
        '''Step 02: Click Cancel.'''
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()