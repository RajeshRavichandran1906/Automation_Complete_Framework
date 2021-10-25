'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288707'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288707_TestClass(AS_BaseTestCase):
    def test_C2288707(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_crime1="crime1.js"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        
        '''Testcase verification'''
        
        verify_javascript_file="App Studio - crime1.js"
        verify_javascript_file_in_notepad="crime1.js - Notepad"
        verify_msg_1="Step 01: Verify javascript files opens in text editor of AS canvas"
        verify_msg_2="Step 02: Verify javascript file invokes in notepad"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Detail, Web Applications->baseapp
                    Right click on crime1.js and select Open 
                    Close crime1.js tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
                   
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1,click=component_locators.open_button) 
        time.sleep(5)
        
        as_utilobj.verify_active_tool(verify_javascript_file,verify_msg_1)
        time.sleep(3)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 02: Right click on crime1.js and select Edit in Windows Associated Tool
                    Close crime1.js - WordPad window'''
        
        as_utilobj.select_file(tree_item=baseapp)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1,click=component_locators.associted_window_tool) 
        time.sleep(5)
        
        as_utilobj.verify_notepad_content(verify_javascript_file_in_notepad,verify_msg_2)
        time.sleep(3)
    
if __name__=='__main__' :
    unittest.main()