'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288684'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288684_TestClass(AS_BaseTestCase):
    def test_C2288684(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        down_key=['down']
        C2288684='c2288684{Enter}'
        
        '''Testcase verification'''
        
        verify_renamed_folder="c2288684" 
        verify_web_application_right_click_items=["New Folder","Refresh Descendants"]
        verify_new_folder="newapp"
        verify_msg_1="Step 01: Verify Contextual menu includes: "
        verify_msg_2="Step 02: Verify new folder been created under web application"
        verify_msg_3="Step 03: Verify new folder been renamed"
        verify_msg_4="Step 04: Verify folder name updated in property panel also"
        verify_msg_5="Step 05: Verify created and renamed folder is been deleted"
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on Web Applications.'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=locators.web_application,send_keys=down_key)
        time.sleep(2)
         
        for items in verify_web_application_right_click_items:
            as_utilobj.verify_element_using_ui(verify_msg_1 + items,menu_item_enabled=items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        
        '''Step 02: Select New Folder
                    Hit Enter'''
        
        as_utilobj.select_component_by_right_click(click=verify_web_application_right_click_items[0])
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=verify_new_folder,available=True)
        time.sleep(2)
        
        '''Step 03: Right click on newapp and select Rename
                    Type c2288684
                    Hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=verify_new_folder,click=component_locators.rename_file)
        time.sleep(2)  
         
        automation.SendKeys(C2288684,waitTime=2)
         
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=verify_renamed_folder,available=True)
        time.sleep(2)
        
        '''Step 04: Right on c2288684 and select Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=verify_renamed_folder,click=component_locators.properties_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item=verify_renamed_folder,available=True)
        time.sleep(2)
        
        '''Step 05: Right on c2288684 and select Delete
                    Click Yes in App Studio delete prompt message'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=verify_renamed_folder,click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,tree_item=verify_renamed_folder,unavailable=True)
        time.sleep(2)
           
if __name__=='__main__' :
    unittest.main()