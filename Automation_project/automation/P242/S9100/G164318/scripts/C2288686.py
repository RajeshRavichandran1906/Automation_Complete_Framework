'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288686'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288686_TestClass(AS_BaseTestCase):
    def test_C2288686(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        baseapp="baseapp"
        move_to_new_menu="right"
        press_down=['down']
        
        '''Testcase verification'''

        verify_new_components_on_right_click=['Rename','Delete','New','Properties','Refresh Descendants']
        verify_new_components_on_new_sub_menu=['HTML Page','JavaScript File','Cascading Style Sheet','Folder']
        verify_msg_1="Step 01: Verify contextual menu includes : "
        verify_msg_2="Step 02: Verify Contextual sub-menu new includes: "
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Web Applications
                    Right click on baseapp'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(locators.web_application) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,send_keys=press_down)
        time.sleep(2)
        
        for items in verify_new_components_on_right_click:
            as_utilobj.verify_element_using_ui(verify_msg_1 + items,menu_item_enabled=items,enabled=True)
               
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
        
        '''Step 02: Hover on New'''
                       
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.right_click_menu_new,send_keys=move_to_new_menu)
        time.sleep(2)
         
        for items in verify_new_components_on_new_sub_menu:
            as_utilobj.verify_element_using_ui(verify_msg_2 + items,menu_item_enabled=items,enabled=True)
               
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main()