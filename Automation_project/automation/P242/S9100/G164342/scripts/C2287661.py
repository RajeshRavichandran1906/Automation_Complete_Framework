'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287661'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2287661_TestClass(AS_BaseTestCase):
    def test_C2287661(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        local_machine="Local Machine"
    
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify button control is not available in Environments dialog" 
        
        '''Test Script'''
        
        '''Step 01: Click Environments under Home tab
                    Click Add
                    Click Cancel
                    Click Cancel in Environments List dialog'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.environments_button)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.add_environment)
        time.sleep(3)
        
        as_utilobj.Verify_Element(local_machine,verify_msg_1,unavailable=True)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main() 