'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328135'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation_keys

class C2328135_TestClass(AS_BaseTestCase):
    def test_C2328135(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        open_161337_file="Domains->S9100->161337"
        click_161337_file="161337"
        refresh_folder="S9100"
        ctrl_s=('{Ctrl}(S)')
        select_seats=[850,305]
        click_seats="SEATS"
        
        '''Testcase verification'''
        
        verify_astreicks_added_to_file_name="App Studio - 161337*"
        verify_astreicks_removed_from_file_name="App Studio - 161337"
        verify_dialog="do you want to save the changes to file?"
        verify_modification_has_been_saved="step4_C2328135.png"
        verify_msg_1="Step 01: Verify astreicks_added_to_file_name to indicate file was modified and not yet saved"
        verify_msg_2="Step 02: Verify Asterisk (*) at end of file name disappears after save."
        verify_msg_3="Step 03: Verify File closes without save prompt."
        verify_msg_4="Step 04: Verify modification has been saved"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
         
        '''Step 01: Under AS Framework, double click on 161337 
                    Double click on SEATS'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                    
        as_utilobj.select_tree_view_pane_item(open_161337_file) 
        time.sleep(4)
         
        as_utilobj.click_element_using_ui(tree_item=click_seats)
        time.sleep(2)
         
        as_utilobj.verify_active_tool(verify_astreicks_added_to_file_name,verify_msg_1)
        time.sleep(2)
         
        '''Step 02: Press Ctrl+S'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=refresh_folder,click=component_locators.refresh_descendants)
        time.sleep(2)
         
        automation_keys.SendKeys((ctrl_s),interval=0.25,waitTime=1)
        time.sleep(2)
 
        as_utilobj.verify_active_tool(verify_astreicks_removed_from_file_name,verify_msg_2)
        time.sleep(2)
         
        '''Step 03: Click AS menu and select Close'''
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        as_utilobj.Verify_Current_Dialog_Closes(verify_dialog,verify_msg_3)
        time.sleep(1)
         
        '''Step 04: Double click on 161337'''
         
        as_utilobj.select_tree_view_pane_item(click_161337_file) 
        time.sleep(4)
         
        as_utilobj.verify_picture_using_sikuli(verify_modification_has_been_saved,verify_msg_4)
        time.sleep(1)
         
        '''Step 05: Select SEATS column and click Delete in ribbon
                    Close 161337 tab
                    Click Yes to App Studio saving prompt'''
        
        as_utilobj.select_home_button(move_x=select_seats[0],move_y=select_seats[1])
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()