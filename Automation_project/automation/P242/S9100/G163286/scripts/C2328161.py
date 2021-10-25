'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328161'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2328161_TestClass(AS_BaseTestCase):
    def test_C2328161(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()

        '''Testcase verification'''
        
        verify_quick_access_toolbar="step1_C2328161.png"
        verify_msg_1="Step 01: Verify drop down with customization options displays"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Click on the down arrow at the right end of the Quick Access Tool bar'''
        
        as_utilobj.click_element_using_ui(split_button=locators.customize_splitbutton)
        time.sleep(3)
        
        as_utilobj.verify_picture_using_sikuli(verify_quick_access_toolbar,verify_msg_1)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button=locators.customize_splitbutton)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()