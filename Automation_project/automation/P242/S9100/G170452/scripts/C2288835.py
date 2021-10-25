'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288824'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288833_TestClass(AS_BaseTestCase):
    def test_C2288833(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_select_161337="Domains->S9100->161337"
        select_161337="161337"
        base_folder="S9100"
        select_seats="SEATS"
        select_close=['down','down','down','down','down','down','down']
        
        '''Testcase verification'''
        
        verify_161337="App Studio - 161337"
        verify_161337_closes="App Studio"
        verify_save_warning_prompt="Do you want to save the changes to file 161337?"
        verify_msg_1="Step 01: Verify 161337 is invoked"
        verify_msg_2="Step 02: Verify Procedure canvas closes"
        verify_msg_3="Step 04: Verify save as prompt is displayed on closing the edited document"
        
        '''Testscript'''
        
        as_utilobj.select_home_button() 
        
        '''Step 01: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on 161337
                    Click the AS and select Close'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_tree_view_pane_item(expand_select_161337) 
        time.sleep(8)
         
        as_utilobj.verify_active_tool(verify_161337,verify_msg_1)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(2)
         
        '''Step 02: Click the AS and select Close'''
         
        as_utilobj.select_application_menu_options(send_keys=select_close)
        time.sleep(2)
         
        as_utilobj.verify_active_tool(verify_161337_closes,verify_msg_2)
        time.sleep(2)
         
        '''Step 03: Double click on 161337 
                    Double click SEATS'''
         
        as_utilobj.select_tree_view_pane_item(select_161337) 
        time.sleep(8)
         
        as_utilobj.click_element_using_ui(tree_item=select_seats)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(2)
        
        '''Step 04: Click the AS and select Close
                    Click Cancel in the App Studio saving prompt'''
        
        as_utilobj.select_application_menu_options(send_keys=select_close)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,text_item=verify_save_warning_prompt)
        time.sleep(2)
        
        '''Step 05: Click No in the App Studio saving prompt'''
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(2)
        
        '''Step 06: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Double click on 161337
                    Close 161337 tab'''
        
        as_utilobj.select_tree_view_pane_item(select_161337) 
        time.sleep(8)
    
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()