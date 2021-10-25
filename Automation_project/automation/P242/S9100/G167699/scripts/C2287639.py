'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287639'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2287639_TestClass(AS_BaseTestCase):
    def test_C2287639(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder="Web Applications"
        
        '''Test Case Verifications'''
        
        verify_folder_name="step2_C2287639.png"
        verify_sub_folder_name="step4_C2287639.png"
        verify_msg_1="Step 01: Verify new folder created with underscores"
        verify_msg_2="Step 02: Verify new folder display with underscores as as2998_project in property panel"
        verify_msg_3="Step 03: Verify new sub-folder created with underscores"
        verify_msg_4="Step 4.1: Verify new sub folder name is modified with underscores"
        verify_msg_5="Step 4.2: Verify new sub folder name is modified in property panel with underscores"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, navigate to Web Applications 
                    Right-click Web Applications and select New Folder
                    Type AS 2998 Project an hit Enter'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3) 
                
        as_utilobj.select_tree_view_pane_item(base_folder)
        time.sleep(3)
           
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.new_folder_under_webapp)
        time.sleep(5)
           
        automation.SendKeys("as 2998 project{Enter}")
        time.sleep(3)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item="as_2998_project",available=True)
        time.sleep(1)
         
        '''Step 02: Click File/Folder Properties'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="as_2998_project",click=component_locators.properties_button)
        time.sleep(2)
          
        as_utilobj.verify_picture_using_sikuli(verify_folder_name,verify_msg_2)
        time.sleep(1)
         
        '''Step 03: Right-click aS_2998_project and select New | Folder
                    Type "Sub Folder of AS 2998" and hit Enter'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="as_2998_project",click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(2)
          
        automation.SendKeys("sub folder of as 2998{Enter}")
        time.sleep(3)
          
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item="sub_folder_of_as_2998",available=True)
        time.sleep(1)
         
        '''Step 04: Click File/Folder Properties, Name property
                    Highlight value and type AS 2998 sub folder'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="sub_folder_of_as_2998",click=component_locators.properties_button)
        time.sleep(2)
         
        automation.PaneControl(AutomationId="1548").DoubleClick(ratioX=204,ratioY=44)
        time.sleep(1)
         
        automation.PaneControl(AutomationId="1548").DoubleClick(ratioX=204,ratioY=44)
        time.sleep(1)
         
        automation.SendKeys("AS 2998 sub folder{Enter}")
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item="AS_2998_sub_folder",available=True)
        time.sleep(1)
         
        as_utilobj.select_component_by_right_click(right_click_folder="AS_2998_sub_folder",click=component_locators.properties_button)
        time.sleep(2)
         
        as_utilobj.verify_picture_using_sikuli(verify_sub_folder_name,verify_msg_5)
        time.sleep(1)
         
        '''Step 05: In Environments Tree, right click on aS_2998_project and select Delete
                    Click Yes in App Studio confirm delete message
                    Collapse Web Applications'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="as_2998_project",click=component_locators.delete)
        time.sleep(2)
         
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(5)
         
        as_utilobj.click_element_using_ui(tree_item=base_folder)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 