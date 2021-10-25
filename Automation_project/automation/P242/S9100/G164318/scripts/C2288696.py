'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288696'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation
from common.pages import as_panels

class C2288696_TestClass(AS_BaseTestCase):
    def test_C2288696(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_baseapp="Web Applications->baseapp"
        web_applications="Web Applications"
        baseapp="baseapp"
        ibisamp="ibisamp"
        move_to_new_menu="right"
        
        '''Testcase verification'''
        
        verify_ivp_html_file="ivp.html"
        verify_new_components_on_right_click=['HTML Page','JavaScript File','Cascading Style Sheet','Folder']
        verify_msg_1="Step 01: Verify Contextual menu includes: "
        verify_msg_2="Step 02: Verify pasted file is updated in the appropriate folder - "
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree->WEb Applications->baseapp
                    Right click ivp.html and hover over New'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(expand_baseapp) 
        time.sleep(3)
                        
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.right_click_menu_new,send_keys=move_to_new_menu)
        time.sleep(2)
          
        for items in verify_new_components_on_right_click:
            as_utilobj.verify_element_using_ui(verify_msg_1 + items,menu_item_enabled=items,enabled=True)
                
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
         
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
         
        '''Step 02: Right click ivp.html and select Copy
                    Right click on ibisamp and select Paste
                    In Environments Tree, set Filter to HTML Files'''
         
        as_utilobj.select_component_by_right_click(right_click_item=verify_ivp_html_file,click=component_locators.copy)
        time.sleep(4)
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(web_applications) 
        time.sleep(3)
          
        as_utilobj.select_component_by_right_click(right_click_folder=ibisamp,click=component_locators.paste)
        time.sleep(2)
        
        as_utilobj.select_tree_view_pane_item(ibisamp)
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=verify_ivp_html_file)
        time.sleep(1)
        
        as_panel_obj.environment_panel_file_filter(filter=locators.html_files)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2 + verify_ivp_html_file,tree_item=verify_ivp_html_file,available=True)
        time.sleep(3)
        
        as_panel_obj.environment_panel_file_filter(filter=locators.all_files_filter)
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main()