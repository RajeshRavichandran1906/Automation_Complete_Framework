'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287515'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2287515_TestClass(AS_BaseTestCase):
    def test_C2287515(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path="Domains->S9100"
        base_folder="S9100"
        write_as_2313="AS-2313{Enter}"
        new_folder="AS-2313"
        
        '''Testcase verification'''

        verify_msg_1="Step 01: Verify default location must be Domains->S9100->AS-2313"
        verify_msg_2="Step 02: Verify default location must be Domains->S9100->AS-2313"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree. right click on AS Framework and select New Folder
                    Type AS-2313 and hit Enter
                    Right click on AS-2313 and select New Report
                    Click Cancel'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(folder_path)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_folder)
        time.sleep(2)
        
        automation.SendKeys(write_as_2313)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=new_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=new_folder,available=True)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
        '''Step 02: Right click on AS-2313 and select New Report
                    Click Cancel'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=new_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=new_folder,available=True)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder=new_folder,click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()