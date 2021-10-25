'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287597'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287597_TestClass(AS_BaseTestCase):
    def test_C2287597(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        folders=["S9100","Comment"]
        procedure_view_panel=[-52,170]
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_data_source_dialog="Select Data Source"
        verify_open_file_dialog="Open File"
        verify_msg_1="Step 01: Verify control is returned to Procedure View panel, with no additional message boxes for Match"
        verify_msg_2="Step 02: Verify control is returned to Procedure View panel, with no additional message boxes for Chart"
        verify_msg_3="Step 03: Verify control is returned to Procedure View panel, with no additional message boxes for Execute"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New->Procedure
                    Click on Procedure View panel, right-click top-level folder and select New|Match
                    Click Cancel at Open File dialog'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                     
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(sleep[2])
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_match)
        time.sleep(sleep[0])

        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Closes(verify_data_source_dialog,verify_msg_1)
        time.sleep(sleep[0])
        
        '''Step 02: Click on Procedure View panel, right-click top-level folder and select New|Chart
                    Click Cancel at Open File dialog'''
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_chart)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Closes(verify_data_source_dialog,verify_msg_2)
        time.sleep(sleep[0])
        
        '''Step 03: Click on Procedure View panel, right-click top-level folder and select New|Execute
                    Click Cancel at Open File dialog 
                    Close Procedure1 tab'''
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_execute)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Closes(verify_open_file_dialog,verify_msg_3)
        time.sleep(sleep[0])
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[0]) 
              
if __name__=='__main__' :
    unittest.main()