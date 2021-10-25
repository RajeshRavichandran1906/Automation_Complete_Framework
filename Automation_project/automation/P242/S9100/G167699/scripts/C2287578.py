'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287578'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators
from common.locators import as_components_ui_locators
import uiautomation as auto

class C2287578_TestClass(AS_BaseTestCase):
    def test_C2287578(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        domains="Domains"
        
        '''Test Case Verifications'''
        
        verify_new_folder="AS.2500"
        verify_folder_name_title="step2_C2287578.png"
        verify_msg_1="Step 01: Verify new Domain folder created with Period"
        verify_msg_2="Step 02: Verify new Domain folder Title Contains a Period"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree panel, View Options ->"View by Title"
                    Right-click Domains and select New Folder
                    Type AS.2500, hit Enter'''
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_option_menu_item)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_items_by_title)
        time.sleep(2)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(domains)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=domains,click=component_locators.new_folder_under_webapp)
        time.sleep(1)
        
        auto.SendKeys('AS.2500{Enter}')
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=verify_new_folder,available=True)
        time.sleep(1)
        
        '''Step 02: Click File/Folder Properties panel'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=verify_new_folder,click=component_locators.properties_button)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_folder_name_title,verify_msg_2)
        time.sleep(2)
        
        '''Created folder deleted for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=verify_new_folder,click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 