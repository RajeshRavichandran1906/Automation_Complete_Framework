'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224442'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2224442_TestClass(AS_BaseTestCase):
    def test_C2224442(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test-case property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path_1="Domains->P292_S10032_G156803"
        folder_path_2="Data Servers->EDASERVE->Applications->baseapp"
        folders=["FrameWork","baseapp"]
        wait_time=[1,2,3,4,5,6] 
        
        '''Test-case verification'''
        
        verify_dialog="Select Data Source"
        verify_msg_1="Step 01: Verify Open File dialog should be replaced as 'Select a Data source' for selecting Master files under Domain."
        verify_msg_2="Step 02: Verify Open File dialog should be replaced as 'Select a Data source' for selecting Master files under DataServer"
        
        '''Test-script'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree->Domains->P292_S10032_G156803
                    Right click Framework and select New->Report'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
              
        as_utilobj.select_tree_view_pane_item(folder_path_1) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(wait_time[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_1)
        time.sleep(wait_time[0])
        
        '''Step 02: Click Cancel
                    Expand Data Servers->EDASERVE->Applications'
                    Right click baseapp and select New->Report''' 
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
              
        as_utilobj.select_tree_view_pane_item(folder_path_2) 
        time.sleep(wait_time[2])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(wait_time[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_2)
        time.sleep(wait_time[0])
        
        '''Step 03: Click Cancel'''
        
        as_utilobj.select_any_dialog(locators.cancel_button)
        time.sleep(wait_time[0])
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
        
if __name__=='__main__' :
    unittest.main() 