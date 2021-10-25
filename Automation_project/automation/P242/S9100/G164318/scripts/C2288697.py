'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288697'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288697_TestClass(AS_BaseTestCase):
    def test_C2288697(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_baseapp="Web Applications->baseapp"
        select_ivp_html="ivp.html"
        
        '''Testcase verification'''
        
        verify_html_tool="App Studio - Edit ivp.html"
        verify_file_invoked_in_windows_tool="ivp.html - Notepad"
        verify_msg_1="Step 01: Verify ivp html file invoked successfully"
        verify_msg_2="Step 02: Verify ivp.html invoked successfully in notepad"
                
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Treel->Web Applications->baseapp
                    Right click on ivp.html and select Open
                    Close Edit ivp.html tab'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(expand_baseapp) 
        time.sleep(3)
                        
        as_utilobj.click_element_using_ui(tree_item=select_ivp_html)
        time.sleep(5)
          
        as_utilobj.verify_active_tool(verify_html_tool,verify_msg_1)
        time.sleep(2)
          
        as_utilobj.close_canvas_item()
        time.sleep(3)
 
        '''Step 02: Right click on ivp.html and select Edit in Windows Associated Tool
                    Close Edit ivp.html tab
                    Close ivp.html WordPad window'''
         
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,click=component_locators.associted_window_tool)
        time.sleep(1)
        
        as_utilobj.verify_notepad_content(verify_file_invoked_in_windows_tool,verify_msg_2)
        time.sleep(2)
      
if __name__=='__main__' :
    unittest.main()