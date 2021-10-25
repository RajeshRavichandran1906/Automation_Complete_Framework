'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288714'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288714_TestClass(AS_BaseTestCase):
    def test_C2288714(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        mainpage_locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        paste_file_in_crime="crime"
        select_aliceblue="aliceblue.css"
        expand_base_app="Web Applications->baseapp"
        go_down=['down']
        
        '''Testcase verification'''
        
        verify_right_click_on_css_file=['Open','Edit in Windows Associated Tool','Print','New','Duplicate','Copy','Rename','Delete','Properties']
        verify_right_click_on_css_file_open_state=['Print','New','Duplicate','Copy','Properties']
        verify_sub_menu_new=['HTML Page','JavaScript File','Cascading Style Sheet','Folder']
        verify_msg_1="Step 01: Verify css file right click contextual menu contains : "
        verify_msg_2="Step 02: Verify aliceblue file has been pasted"
        verify_msg_3="Step 03: Verify open state css file right click contextual menu contains : "
        verify_msg_4="Step 04: Verify contextual menu 'new' sub menu contains : "
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Web Applications->baseapp
                    Right click on aliceblue.css
                    Select Copy'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
                    
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,send_keys=go_down) 
        time.sleep(2) 
         
        for items in verify_right_click_on_css_file:
            as_utilobj.verify_element_using_ui(verify_msg_1 + items,menu_item_enabled=items,enabled=True)
             
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
            
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,click=component_locators.copy) 
        time.sleep(3) 
         
        '''Step 02: Right click on CRIME and select Paste
                    In Environments Tree, set Filter to Other Files'''
          
        as_utilobj.select_component_by_right_click(right_click_folder=paste_file_in_crime,click=component_locators.paste) 
        time.sleep(3) 
           
        as_utilobj.select_component_by_right_click(right_click_folder=paste_file_in_crime,click=component_locators.refresh_descendants) 
        time.sleep(3) 
         
        as_panel_obj.environment_panel_file_filter(filter=mainpage_locators.other_files)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(tree_item=paste_file_in_crime)
        time.sleep(2)
         
        as_utilobj.select_file(tree_item=select_aliceblue)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=select_aliceblue,available=True)
        time.sleep(2)
         
        '''Step 03: Double click on aliceblue.css
                    Right click on aliceblue.css
                    Close aliceblue.css tab'''
         
        as_utilobj.click_element_using_ui(tree_item=select_aliceblue)
        time.sleep(6)
         
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,send_keys=go_down) 
        time.sleep(2) 
    
        for items in verify_right_click_on_css_file_open_state:
            as_utilobj.verify_element_using_ui(verify_msg_3 + items,menu_item_enabled=items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 04: Right click on aliceblue.css and hover New'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,click=component_locators.right_click_menu_new) 
        time.sleep(2) 
        
        for items in verify_sub_menu_new:
            as_utilobj.verify_element_using_ui(verify_msg_4 + items,menu_item_enabled=items,enabled=True)
        
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        as_panel_obj.environment_panel_file_filter(filter=mainpage_locators.all_files_filter)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()