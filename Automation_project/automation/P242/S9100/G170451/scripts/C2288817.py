'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288817'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288817_TestClass(AS_BaseTestCase):
    def test_C2288817(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test case property variables'''
        
        environment_path="webfocus_environment"
        select_file="Domains->S9100->160526009"
        base_folder="S9100"
        files=["API","ASNewBlog","110045RIA","mapview"]
        key_path_to_save_as=['down','down','down']
        key_pattern_1=['down','down']
        wait_time=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] 
        files_to_be_deleted=["Portal1 Resources","Portal1"]
        
        '''Test case verifications'''
        
        verify_save_as_dialog="Save As"
        verify_only_procedure_file_displayed="Procedure Files"
        verify_only_text_file_format="Text Files"
        verify_save_as_options_for_blog_file="step5_C2288817.png"
        verify_portal_page="step5_C2288817.png"
        verify_html_files="Html files"
        verify_javascript_files="JavaScript Files"
        verify_library_access_file="step5_C2288817.png"
        verify_msg_1="Step 01: Verify Save As dialog opens, the current location is highlighted, the original FEX file is highlighted in the details pane, file name is populated with current file name, file type is procedure"
        verify_msg_2="Step 02: Verify only Procedure Files available in drop down menu"
        verify_msg_3="Step 03: Verify Save As dialog opens, the current location is highlighted, the original TEXT file is highlighted in the details pane"
        verify_msg_4="Step 04: Verify only text File available in drop down menu"
        verify_msg_5="Step 05: Verify Save As option been disabled under application menu"
        verify_msg_6="Step 06: Verify Save As dialog opens, the current location is highlighted, the original HTML file is highlighted in the details pane"
        verify_msg_7="Step 07: Verify only HTML File available in drop down menu"
        verify_msg_8="Step 08: Verify Save As option been disabled under application menu"
        verify_msg_9="Step 09: Verify Save As dialog opens, the current location is highlighted, the original Javescript file is highlighted in the details pane"
        verify_msg_10="Step 10: Verify only Java script file available in drop down menu"
        verify_msg_11="Step 11: Verify Save As option been disabled under application menu"
        
        '''Test script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains->CC - App Studio->AS Framework
                    Double click on 161337 
                    Click AS Menu->Save As'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[3])
                    
        as_utilobj.select_tree_view_pane_item(select_file) 
        time.sleep(wait_time[6])
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click_sub_menu=component_locators.refresh_descendants)
        time.sleep(wait_time[4])
         
        as_utilobj.select_application_menu_options(send_keys=key_path_to_save_as)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_save_as_dialog,verify_msg_1)
        time.sleep(wait_time[2])
         
        '''Step 02: Click the down arrow for Procedures Files
                    Click Cancel
                    Close 161337 tab'''
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.Verify_Element(verify_only_procedure_file_displayed,verify_msg_2,available=True)
        time.sleep(wait_time[2])
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[2])
         
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])
         
        '''Step 03: Double click on API
                    Click AS Menu->Save As'''
         
        as_utilobj.select_tree_view_pane_item(files[0]) 
        time.sleep(wait_time[6])
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(wait_time[4])
         
        as_utilobj.select_application_menu_options(send_keys=key_path_to_save_as)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_save_as_dialog,verify_msg_3)
        time.sleep(wait_time[1])
         
        '''Step 04: Click the down arrow for Procedures Files
                    Click Cancel
                    Close 161337 tab'''
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.Verify_Element(verify_only_text_file_format,verify_msg_4,available=True)
        time.sleep(wait_time[1])
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[2])
         
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])
         
        '''Step 05: Double click on ASNewBlog
                    Click AS Menu 
                    Click Close'''
         
        as_utilobj.select_tree_view_pane_item(files[1])
        time.sleep(wait_time[10])
         
        as_utilobj.select_application_menu_options(send_keys=key_pattern_1)
        time.sleep(wait_time[1])
         
        as_utilobj.verify_picture_using_sikuli(verify_save_as_options_for_blog_file,verify_msg_5)
        time.sleep(wait_time[1])
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(wait_time[4])
         
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[6])
         
        '''Step 06: Double click on DisneyBallDog
                    Click AS Menu->Save As'''
         
        as_utilobj.select_tree_view_pane_item(files[2])
        time.sleep(wait_time[10])
         
        as_utilobj.select_application_menu_options(send_keys=key_path_to_save_as)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Current_Dialog_Opens(verify_save_as_dialog,verify_msg_6)
        time.sleep(wait_time[2])
         
        '''Step 07: Click the down arrow for Html files
                    Click Cancel 
                    Close DisneyBallDog tab''' 
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.Verify_Element(verify_html_files,verify_msg_7,available=True)
        time.sleep(wait_time[1])
         
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
         
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[2])
         
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])
         
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(wait_time[1])
        
        '''Step 08: Double click on ExistedPortal
                    Click AS Menu 
                    Click Close'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_collaborative_portal)
        time.sleep(wait_time[2])    
         
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(wait_time[12])               
         
        as_utilobj.click_element_using_ui(text_click=component_locators.cancel_button)
        time.sleep(wait_time[3])
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(wait_time[4])
         
        as_utilobj.select_application_menu_options(send_keys=key_path_to_save_as)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_picture_using_sikuli(verify_portal_page,verify_msg_8)
        time.sleep(wait_time[1])
         
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])
         
        '''Step 09: Double click on JavaScriptFile1
                    Click AS Menu->Save As'''
        
        as_utilobj.select_tree_view_pane_item(files[3])
        time.sleep(wait_time[5])

        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(wait_time[4])
                
        as_utilobj.select_application_menu_options(send_keys=key_path_to_save_as)
        time.sleep(wait_time[2])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_save_as_dialog,verify_msg_9)
        time.sleep(wait_time[2])
        
        '''Step 10: Click the down arrow for JavaScript Files
                    Click Cancel 
                    Close JavaScriptFile1 tab'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
        
        as_utilobj.Verify_Element(verify_javascript_files,verify_msg_10,available=True)
        time.sleep(wait_time[1])
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[2])
        
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])
        
        '''Step 11: Double click on LibraryAccessList
                    Click AS Menu 
                    Click Close'''
        
        as_utilobj.select_application_menu_options(send_keys=key_pattern_1)
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_library_access_file,verify_msg_11)
        time.sleep(wait_time[1]) 
        
        '''Delete the created portal page for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=files_to_be_deleted[0],click=component_locators.delete)
        time.sleep(wait_time[1])
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(wait_time[1])
        
        as_utilobj.select_component_by_right_click(right_click_item=files_to_be_deleted[1],click=component_locators.delete)
        time.sleep(wait_time[1])
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(wait_time[1])
        
if __name__=='__main__' :
    unittest.main() 