'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287551'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as auto

class C2287551_TestClass(AS_BaseTestCase):
    def test_C2287551(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder="Domains"
        
        '''Test Case Verifications'''
        
        verify_folder_name_panel="step2_C2287551.png"
        verify_msg_1="Step 01: Verify name and title in property panel for folder"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on Domains and select New Folder
                    Type AS2553_ and hit Enter'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        as_utilobj.select_tree_view_pane_item(base_folder)
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click="New Folder")
        time.sleep(2)
        
        auto.SendKeys('AS2553_{Enter}',waitTime=2)
        
        '''Step 02: Click File/Folder Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="AS2553_",click=component_locators.properties_environment)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_folder_name_panel,verify_msg_1)
        time.sleep(1)
        
        '''Created folder deleted for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="AS2553_",click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 