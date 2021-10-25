'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328140'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328140_TestClass(AS_BaseTestCase):
    def test_C2328140(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        open_fex_file="Domains->S9100->AS-2260"
        enable_display_dialogue_manager_commands=['down','down','down','down']
        enable_message_viewer_off=['down']
        refresh_folder="S9100"
        ie_browser_classname="IEFrame"
        run_drop_down=[30,10]
        
        '''Testcase verification'''
        
        verify_browser_text=["-*Section Created in CString CConnectionContext::PrependAppPaths starts","-*Section Created in CString CConnectionContext::PrependAppPaths ends"]
        verify_webfocus_report="WebFOCUS Report"
        verify_msg_1="Step 01: Verify Results display in browser/viewer"
        verify_msg_2="Step 02: Verify FOCUS commands executed along with Display Dialogue Manager commands - "
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
         
        '''Step 01: In Environments Tree, navigate to Domains
                    Expand CC - App Studio->AS Framework
                    Double click on AS-2260
                    Click on drop down icon next to the run icon and select Display Dialogue Manager commands
                    Click Run''' 
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
             
        as_utilobj.select_tree_view_pane_item(open_fex_file) 
        time.sleep(8)
        
        as_utilobj.select_component_by_right_click(right_click_folder=refresh_folder,click=component_locators.refresh_descendants)
        time.sleep(2)

        as_utilobj.click_element_using_ui(split_button_with_offset=locators.run_splitbutton,x=run_drop_down[0],y=run_drop_down[1],send_keys=enable_display_dialogue_manager_commands)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(8)

        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_1,verify_pane=verify_webfocus_report)
        time.sleep(1)
          
        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_2,item_list=verify_browser_text,browser_close=True)
        time.sleep(1)
        
        '''Step 02: Close WebFOCUS Report tab
                    Close AS-2260 tab'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.run_splitbutton,x=run_drop_down[0],y=run_drop_down[1],send_keys=enable_message_viewer_off)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
            
if __name__=='__main__' :
    unittest.main() 