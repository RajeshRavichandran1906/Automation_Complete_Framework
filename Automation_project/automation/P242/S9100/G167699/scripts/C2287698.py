'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287698'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2287698_TestClass(AS_BaseTestCase):
    def test_C2287698(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Domains->Public"
    
        '''Test Case Verifications'''
        
        verify_msg_1="Step 01: Verify canvas 'Rules on this Resource - Repository' opens without any script error"
        verify_msg_2="Step 02: Verify Rules on this Resource - Public canvas opens without any script error"
        verify_msg_3="Step 03: Verify Focus returns to AS desktop"
                
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right-click Domains context and select Security | Rules on this Resource...'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="Domains",click=component_locators.security,click_sub_menu=component_locators.rules_on_this_resource)
        time.sleep(15)
        
        as_utilobj.verify_active_tool("App Studio - Rules on this Resource - Repository",verify_msg_1)
        time.sleep(2)
        
        '''Step 02: Click X on Rules on this Resource - repository tab to close it'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
        
        '''Step 03: Right-click Public domain and select Security | Rules on this Resource...'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="Public",click=component_locators.security,click_sub_menu=component_locators.rules_on_this_resource)
        time.sleep(15)
        
        as_utilobj.verify_active_tool("App Studio - Rules on this Resource - Public",verify_msg_2)
        time.sleep(2)
        
        '''Step 04: Click the Close button at the bottom of the Rules canvas'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(5)
        
        as_utilobj.verify_active_tool("App Studio",verify_msg_3)
        time.sleep(2)
          
if __name__=='__main__' :
    unittest.main() 