'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287650'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import uiautomation as automation

class C2287650_TestClass(AS_BaseTestCase):
    def test_C2287650(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        description_for_environment="10000"
        type_special_charectors='!@#$%^&*<>:"\/'
        null_value=''
    
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify that none of the characters in the list can be added to the host description" 
        
        '''Test Script'''
        
        '''Step 01: Click Environments under Home tab
                    Click Add
                    In Environments List dialog, select you current environment 
                    Click Properties'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.environments_button)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.add_environment)
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(edit_element=True,id=description_for_environment)
        time.sleep(2)
        
        automation.SendKeys(type_special_charectors)
        time.sleep(1)
        
        as_utilobj.verify_accesible_current_value(null_value,verify_msg_1,edit_control=description_for_environment)
        time.sleep(2)
        
        '''Step 02: Click Cancel in WebFOCUS Environment Properties dialog 
                    Click Cancel Environments List dialog'''
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main() 