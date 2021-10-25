'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287744'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators

class C2287744_TestClass(AS_BaseTestCase):
    def test_C2287744(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        wait=[1,2,3,4,5] 
        
        '''Testcase verification'''
        
        verify_app_studio_option_dialogue="App Studio Options"
        verify_environment_options="step2_C2287744.png"
        verify_msg_1="Step 01: Verify App Studio options been invoked"
        verify_msg_2="Step 02: Verify Environment section displayed"
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Options'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(wait[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_app_studio_option_dialogue,verify_msg_1)
        time.sleep(wait[2])
        
        '''Step 02: Click Environmemts
                    Click Cancel'''
        
        as_utilobj.select_element_appstudio_options(list_item=locators.environments_button)
        time.sleep(wait[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_environment_options,verify_msg_2)
        time.sleep(wait[1])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait[2])
        
if __name__=='__main__' :
    unittest.main()