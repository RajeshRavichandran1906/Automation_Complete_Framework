'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288695'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2288695_TestClass(AS_BaseTestCase):
    def test_C2288695(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_app="Web Applications->baseapp"
        select_ivp_html="ivp.html"
        move_to_menu="down"
        
        '''Testcase verification'''
        
        right_click_on_html_file=['Open','Edit in Windows Associated Tool','Print','New','Duplicate','Copy','Rename','Delete','Properties']
        right_click_on_html_file_open_state=['Print','New','Duplicate','Copy','Properties']
        verify_html_tool="App Studio - Edit ivp.html"
        verify_msg_1="Step 01: Verify Contextual menu includes: "
        verify_msg_2="Step 02: Verify ivp html file been invoked"
        verify_msg_3="Step 03: Verify Contextual menu includes: "
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to HTML files
                    Web Applications->baseapp
                    Right click on ivp.html'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item(expand_base_app) 
        time.sleep(3)
                       
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,send_keys=move_to_menu)
        time.sleep(2)
         
        for items in right_click_on_html_file:
            as_utilobj.verify_element_using_ui(verify_msg_1 + items,menu_item_enabled=items,enabled=True)
               
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
        
        '''Step 02: Double click on ivp.html'''
        
        as_utilobj.click_element_using_ui(tree_item=select_ivp_html)
        time.sleep(5)
        
        as_utilobj.verify_active_tool(verify_html_tool,verify_msg_2)
        time.sleep(2)
        
        '''Step 03: Right click on ivp.html 
                    Close Edit ivp.html tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,send_keys=move_to_menu)
        time.sleep(2)
        
        for items in right_click_on_html_file_open_state:
            as_utilobj.verify_element_using_ui(verify_msg_3 + items,menu_item_enabled=items,enabled=True)
            
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
         
if __name__=='__main__' :
    unittest.main()