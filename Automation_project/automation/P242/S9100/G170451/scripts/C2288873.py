'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288873'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288873_TestClass(AS_BaseTestCase):
    def test_C2288873(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_folder="Domains->S9100"
        key_pattern_1=['down','enter']
        type_file_name="$$Rep"
        wait_time=[1,2,3,4,5] 
        
        '''Testcase verification'''
        
        verify_error_message_prompt="$$rep\nFile not found.\nPlease verify the correct file name was given."
        verify_msg_1="Step 01: Verify error message prompt is displayed for wrong file name"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu and select Open
                    Type $$rep for File name
                    Click OK'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[3])
                     
        as_utilobj.select_tree_view_pane_item(select_folder) 
        time.sleep(wait_time[3])
        
        as_utilobj.select_application_menu_options(send_keys=key_pattern_1)
        time.sleep(wait_time[1])

        as_utilobj.select_any_dialog(button=component_locators.ok_button,rename_file=type_file_name)
        time.sleep(wait_time[1])
        
        as_utilobj.verify_element_using_ui(verify_msg_1,text_item=verify_error_message_prompt)
        time.sleep(wait_time[1])
        
        '''Step 02: Click OK on the App Studio message
                    Click Cancel in the Open File dialog'''
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(wait_time[1])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[1])
        
if __name__=='__main__' :
    unittest.main()