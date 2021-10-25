'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287702'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import uiautomation as automation

class C2287702_TestClass(AS_BaseTestCase):
    def test_C2287702(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        press_down=['down']
        select_security_center=['down','down','down']
    
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify sign out options is enabled under the webfocus environment" 
        verify_msg_2="Step 02: Verify right click menu disabled under domains"
        
        '''Test Script'''
        
        '''Step 01: Under WebFOCUS Administration, select Security Center from the drop down list'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                                 
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton,send_keys=select_security_center)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=tree_path,send_keys=press_down)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,menu_item=locators.sign_out,unavailable=True)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=locators.domains,send_keys=press_down)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,menu_item=component_locators.refresh_descendants,unavailable=True)
        time.sleep(2)
        
        '''Step 02: Close Security Center tab'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main() 