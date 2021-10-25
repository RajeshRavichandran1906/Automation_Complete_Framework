'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287550'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as auto

class C2287550_TestClass(AS_BaseTestCase):
    def test_C2287550(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        domains="Domains"
        select_data_source_dialog="Select Data Source"
        
        '''Test Case Verifications'''
        
        verify_master_file_folder="step3_C2287550.png"
        verify_msg_1="Step 01: Verify new folder created as - "
        verify_msg_2="Step 03: Verify data source dialog displayed"
        verify_msg_3="Step 04: Verify master file selection list is displayed"
        verify_msg_4="Step 05: Verify created folder has been deleted for reason of next run"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on Domains and select New Folder
                    Type AS2515 and hit Enter
                    Right click on AS2515 and select New-> Folder
                    Type 1, hit Enter'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(domains)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=domains,click=component_locators.new_folder_under_webapp)
        time.sleep(1)
        
        auto.SendKeys('AS2515{Enter}')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="AS2515",click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(1)
        
        auto.SendKeys('1{Enter}')
        time.sleep(1)
        
        '''Step 02: Right click on 1 and select New-> Folder
                    Type 2, hit Enter
                    Right click on 2 and select New-> Folder
                    Type 3, hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="1",click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(1)
        
        auto.SendKeys('2{Enter}')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="2",click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(1)
        
        auto.SendKeys('3{Enter}')
        time.sleep(1)
        
        new_tree_folders=['AS2515','1','2','3']
        for folders in new_tree_folders:
            as_utilobj.verify_element_using_ui(verify_msg_1 + folders,tree_item=folders,available=True)
        
        '''Step 03: Right-click folder 3 and choose New | Report'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="3",click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens(select_data_source_dialog,verify_msg_2)
        time.sleep(1)
        
        '''Step 04: Double-click sub-folder 2
                    Click Cancel
                    Right click on AS2515 and select Delete
                    Click Yes in App Studio prompt message'''
        
        as_utilobj.verify_picture_using_sikuli(verify_master_file_folder, verify_msg_3)
        time.sleep(1)
        
        as_utilobj.select_tree_view_pane_item("2")
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
             
        as_utilobj.select_component_by_right_click(right_click_folder="AS2515",click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item="AS2515",unavailable=True)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 