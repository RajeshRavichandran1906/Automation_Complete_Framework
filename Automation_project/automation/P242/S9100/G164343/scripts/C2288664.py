'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288664'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288664_TestClass(AS_BaseTestCase):
    def test_C2288664(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase verification'''
        
        verify_app_studio_help_window="App Studio Help"
        verify_msg_1="Step 01: Verify Help opens to 'How to Add a WebFOCUS Environment'"
        verify_msg_2="Step 02: Verify Help opens on same page 'How to Add a WebFOCUS Environment'"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Home tab, click Environments 
                    Click Help in Environments List window
                    Close App Studio Help window'''
                 
        as_utilobj.click_element_using_ui(button_item=True,name=locators.environments_button)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.help_button)
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,window_control_item=verify_app_studio_help_window,window_close=True)
        time.sleep(1)
        
        '''Step 02: Press F1 
                    Close App Studio Help window'''
        
        automation.SendKey(automation.Keys.VK_F1, waitTime=3)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,window_control_item=verify_app_studio_help_window,window_close=True)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()     