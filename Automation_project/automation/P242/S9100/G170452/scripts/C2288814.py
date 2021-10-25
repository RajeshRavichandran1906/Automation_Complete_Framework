'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288814'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288814_TestClass(AS_BaseTestCase):
    def test_C2288814(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_folder="Domains->S9100"
        select_161337="161337"
        base_folder="S9100"
        select_seats="SEATS"
        select_sales="SALES"
        select_save=["down","down"]
        
        '''Testcase verification'''
        
        verify_dialog="Save As"
        verify_save_as_warning_message="Do you want to save the changes to file 161337?"
        verify_msg_1="Step 02: Verify file closes without the save as prompt"
        verify_msg_2="Step 03: Verify file closes without the save as prompt"
        verify_msg_3="Step 04: Verify file closes with save as warning prompt"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, CC - AppStudio->AS Framework
                    Right click on 161337 and select Open
                    Double click on SEATS
                    Click the AS logo
                    Click Save'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                      
        as_utilobj.select_tree_view_pane_item(expand_base_folder) 
        time.sleep(3)
                   
        as_utilobj.select_component_by_right_click(right_click_item=select_161337,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.open_button)
        time.sleep(3)
          
        as_utilobj.click_element_using_ui(tree_item=select_seats)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(3)
          
        as_utilobj.select_application_menu_options(send_keys=select_save)
        time.sleep(2)
      
        '''Step 02: Close 161337 tab
                    Right click on 161337 and select Open'''
          
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
        as_utilobj.Verify_Current_Dialog_Closes(verify_dialog, verify_msg_1)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_item=select_161337,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.open_button)
        time.sleep(3)
          
        '''Step 03: Double click SALES
                    Click the AS logol
                    Click Save
                    Close 161337 tab'''
          
        as_utilobj.click_element_using_ui(tree_item=select_sales)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(3)
          
        as_utilobj.select_application_menu_options(send_keys=select_save)
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        as_utilobj.Verify_Current_Dialog_Closes(verify_dialog,verify_msg_2)
        time.sleep(2)
         
        '''Step 04: Right click on 161337 and select Open'''
         
        as_utilobj.select_component_by_right_click(right_click_item=select_161337,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.open_button)
        time.sleep(3)
        
        '''Step 05: Right click on SALES and select Delete
                    Right click on SEATS and select Delete'''
        
        as_utilobj.select_home_button(move_x=830,move_y=286)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(click=component_locators.delete)
        time.sleep(3)
        
        as_utilobj.select_home_button(move_x=830,move_y=286)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(click=component_locators.delete)
        time.sleep(2)

        '''Step 06: Close 161337 tab
                    Click Yes in App Studio saving prompt'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,text_item=verify_save_as_warning_message)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
    
if __name__=='__main__' :
    unittest.main()