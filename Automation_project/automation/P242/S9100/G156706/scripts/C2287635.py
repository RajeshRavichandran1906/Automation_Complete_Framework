'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287635'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
from common.pages import as_ribbon

class C2287635_TestClass(AS_BaseTestCase):
    def test_C2287635(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_ribbon_obj=as_ribbon.AS_Ribbon(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        folders=["S9100","Comment"]
        procedure_view_panel=[-52,170]
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_dialog="Select Data Source"
        verify_msg_1="Step 01: Verify the Select Data Source dialog opens for Report"
        verify_msg_2="Step 02: Verify the Select Data Source dialog opens for Chart"
        verify_msg_3="Step 03: Verify the Select Data Source dialog opens for Define in procedure view"
        verify_msg_4="Step 04: Verify the Select Data Source dialog opens for Join in procedure view"
        verify_msg_5="Step 05: Verify the Select Data Source dialog opens for Report"
        verify_msg_6="Step 06: Verify the Select Data Source dialog opens for Chart"
        verify_msg_7="Step 07: Verify the Select Data Source dialog opens for Define in procedure view"
        verify_msg_8="Step 08: Verify the Select Data Source dialog opens for Join in procedure view"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework folder and select New->Report
                    Click Cancel'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                  
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
               
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_1)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        '''Step 02: Right click on AS Framework folder and select New | Chart
                    Click Cancel'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_chart)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_2)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        '''Step 03: Right click on AS Framework folder and select New | Procedure
                    Click Procedure View panel
                    Right-click top-level folder and select New... | Define
                    Click Cancel'''       
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(sleep[2])
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_define)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_3)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        '''Step 04: Click Procedure View panel
                    Right-click top-level folder and select New... | Join
                    Click Cancel 
                    Close Procedure1 tab'''
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_join)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_4)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[1])
        
        '''Step 05: Under Home ribbon, check Environments Detail
                    Expand Domains->CC-AppStudio
                    Right click on AS Framework folder and select New->Report
                    Click Cancel'''
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.environmentstree_checkbox)
        time.sleep(sleep[0])
        
        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.environmentsdetail_checkbox)
        time.sleep(sleep[0])
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                  
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
               
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_5)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        '''Step 06: Right click on AS Framework folder and select New | Chart
                    Click Cancel'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_chart)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_6)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        '''Step 07: Right click on AS Framework folder and select New | Procedure
                    Click Procedure View panel
                    Right-click top-level folder and select New... | Define
                    Click Cancel'''
                    
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(sleep[2])
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_define)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_7)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])   
        
        '''Step 08: Click Procedure View panel
                    Right-click top-level folder and select New... | Join
                    Click Cancel 
                    Close Procedure1 tab
                    Under Home ribbon, uncheck Environments Detail'''    
        
        as_utilobj.select_home_button(move_x=procedure_view_panel[0],move_y=procedure_view_panel[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[1],click=component_locators.comments_new,click_sub_menu=component_locators.new_join)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_8)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0]) 
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[0]) 
        
        as_ribbon_obj.verify_click_checkbox(msg=None,uncheck=locators.environmentsdetail_checkbox)
        time.sleep(sleep[0])
        
        as_ribbon_obj.verify_click_checkbox(msg=None,click=locators.environmentstree_checkbox)
        time.sleep(sleep[0])
        
if __name__=='__main__' :
    unittest.main()   