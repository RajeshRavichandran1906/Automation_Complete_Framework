'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224435'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import pyautogui as keys
import uiautomation as automation

class C2224435_TestClass(AS_BaseTestCase):
    def test_C2224435(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        new_folder="New Folder1"
        press_enter="enter"
        wait_time=[1,2,3,4,5,6] 
        
        '''Testcase verification'''

        verify_images=["step3_C2224435.png","step4_C2224435.png"]
        verify_msg_1="Step 01: Verify New folder1 is created with default name 'New Folder1' in edit mode."
        verify_msg_2="Step 02: Verify 'New Folder1' label exits edit mode."
        verify_msg_3="Step 03: Verify New Folder is created under 'New Folder1' with default name 'New Folder1' in edit mode."
        verify_msg_4="Step 04: Verify label of Subfolder 'New Folder1' exits edit mode."
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click Domain and select New Folder.'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_component_by_right_click(right_click_folder=locators.domains,click=component_locators.new_folder_under_webapp)
        time.sleep(wait_time[3])
    
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=new_folder,available=True)
        time.sleep(1)
        
        '''Step 02: Click outside label of New Folder1'''
        
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=3)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=new_folder,available=True)
        time.sleep(1)
        
        '''Step 03: Right Click 'New Folder1' and select New->Folder.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=new_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_picture_using_sikuli(verify_images[0],verify_msg_3)
        time.sleep(wait_time[0])
         
        '''Step 04: Label of subfolder 'New Folder1' exits edit mode.'''
        
        keys.hotkey(press_enter)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_picture_using_sikuli(verify_images[1],verify_msg_4)
        time.sleep(wait_time[0])
        
        '''Step 05: Right click the parent folder, New Folder1 under Domains and select Delete.
                    Click Yes in App Studio prompt message'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=new_folder,click=component_locators.delete)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()     