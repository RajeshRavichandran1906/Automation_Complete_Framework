'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288827'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288827_TestClass(AS_BaseTestCase):
    def test_C2288827(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_folder="Domains->S9100"
        select_runtest="RunTest"
        select_message_viewer_off=['down','down','down','down','down','right']
        browser_classname="IEFrame"
        add_value_france="FRANCE"
        filter_control="COUNTRY"
        click_run="Run with filter values"
        
        '''Testcase verification'''
        
        verify_browser_runtime_text=["Filter Values","COUNTRY"]
        verify_message_viewer_text=["FRANCE","PEUGEOT","504 4 DOOR"]
        verify_msg_1="Step 02: Verify browser invokes with the "
        verify_msg_2="Step 03: Verify no messages displayed through message viewer when it is in off state"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click the AS logo
                    Mouse over Run and select Display command lines'''
                      
        as_utilobj.select_application_menu_options(send_keys=select_message_viewer_off)
        time.sleep(2)
            
        '''Step 02: In Environments Tree, Domains->CC- AppStudio->AS Framework                
                    Right click on RunTest and select Run'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
            
        as_utilobj.select_tree_view_pane_item(expand_base_folder) 
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_item=select_runtest,click=component_locators.run_button)
        time.sleep(9)
           
        as_utilobj.Verify_Browser_Content(browser_classname,verify_msg_1,item_list=verify_browser_runtime_text)
        time.sleep(1)
        
        '''Step 03: Enter FRANCE for COUNTRY and click the Run button 
                    Close the WebFOCUS Report tab output'''
        
        as_utilobj.click_element_using_ui(edit_element=True,name=filter_control,write=add_value_france)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(hyperlink_control=click_run)
        time.sleep(6)
        
        as_utilobj.Verify_Browser_Content(browser_classname,verify_msg_2,item_list=verify_message_viewer_text,browser_close=True)
        time.sleep(3) 
        
        '''Step 04: Close the WebFOCUS Report tab output
                    Close Edit RunTest tab
                    Click the AS logo
                    Mouse over Run and select Message Viewer OFF'''

        as_utilobj.select_application_menu_options(send_keys=select_message_viewer_off)
        time.sleep(2)
    
if __name__=='__main__' :
    unittest.main()