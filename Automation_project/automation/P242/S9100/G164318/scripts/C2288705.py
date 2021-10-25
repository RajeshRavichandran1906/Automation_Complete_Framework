'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288705'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2288705_TestClass(AS_BaseTestCase):
    def test_C22888705(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        base_file_repository="Domains->S9100"
        select_crime1="crime1"
        select_crime1_under_web_path="crime1.js"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        down=['down']
        
        '''Testcase verification'''
        
        verify_right_click_on_javascript_file=['Open','Edit in Windows Associated Tool','Print','New','Duplicate','Copy','Rename','Delete','Properties']
        verify_right_click_on_javascript_file_open_state=['Print','New','Duplicate','Copy','Properties']
        verify_new_components_on_right_click=['HTML Page','JavaScript File','Cascading Style Sheet','Folder']
        verify_java_script_tool="App Studio - crime1.js"
        verify_msg_1="Step 01: Verify file crime1 files is pasted into baseapp"
        verify_msg_2="Step 02: Verify contextual menu displays : "
        verify_msg_3="Step 03: Verify crime1 file is invoked"
        verify_msg_4="Step 04: Verify contextual menu items in file open state"
        verify_msg_5="Step 05: Verify contextual menu 'new' sub menu contains : "
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree navigate to Domains-> CC- AppStudio->AS Framework folder
                    Right click on crime1 and select Copy
                    Collapse Domains
                    Navigate to Web Applications, right click on baseapp and select Paste'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        as_utilobj.select_tree_view_pane_item(base_file_repository)
        time.sleep(2)
                       
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1,click=component_locators.copy) 
        time.sleep(2) 
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)  
          
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.paste) 
        time.sleep(2) 
          
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.refresh_descendants) 
        time.sleep(2) 
        
        as_utilobj.select_file(tree_item=select_crime1_under_web_path)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=select_crime1_under_web_path,available=True)
        time.sleep(2)
        
        '''Step 02: Set Filter to Other Files
                    Right click on crime1.js'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1_under_web_path,send_keys=down) 
        time.sleep(2) 
        
        for sub_menu_items in verify_right_click_on_javascript_file:
            as_utilobj.verify_element_using_ui(verify_msg_2 + sub_menu_items,menu_item_enabled=sub_menu_items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        '''Step 03: Double click on crime1.js'''
        
        as_utilobj.click_element_using_ui(tree_item=select_crime1_under_web_path)
        time.sleep(3)
        
        as_utilobj.verify_active_tool(verify_java_script_tool,verify_msg_3)
        time.sleep(3)
        
        '''Step 04: Right click on crime1.js
                    Close crime1.js tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1_under_web_path,send_keys=down) 
        time.sleep(2) 
        
        for items in verify_right_click_on_javascript_file_open_state:
            as_utilobj.verify_element_using_ui(verify_msg_4 + items,menu_item_enabled=items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(5)
        
        '''Step 05: Right click on crime1.js and hover New'''
        
        as_utilobj.select_file(tree_item=baseapp)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1_under_web_path,click=component_locators.right_click_menu_new,send_keys=down) 
        time.sleep(2) 
        
        for sub_menu_items in verify_new_components_on_right_click:
            as_utilobj.verify_element_using_ui(verify_msg_5 + sub_menu_items,menu_item_enabled=sub_menu_items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=2)
        time.sleep(2)
    
if __name__=='__main__' :
    unittest.main()