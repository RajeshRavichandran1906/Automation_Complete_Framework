'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288819'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2288819_TestClass(AS_BaseTestCase):
    def test_C2288819(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_folder="Domains->S9100"
        data_server_path="Data Servers->EDASERVE - EDASERVE->Applications->baseapp"
        select_file="160526009"
        refresh_folder="S9100"
        edit_box_id="1516" 
        press_c="c" 
        key_pattern_2=['down','down','down']
        wait_time=[1,2,3,4,5,6,7,8,9] 
        delete_key="delete"
        report_1="report1"
        filename_with_special_charectors="report1.."
        file_name_extension_modify="report1.is"
        
        '''Testcase verification'''
        
        verify_image_1="step1_C2288819.png"
        verify_element="List Item"
        verify_warning_message_1="report1 already exists.\nDo you want to overwrite it?"
        verify_warning_message_2="The name contains one or more invalid characters.\nFiles in this folder may not contain spaces, or more than one period character."
        verify_extension_warning_message="Extension change not permitted."
        verify_msg_1="Step 01: Verify A list of files starting with same letters appears below the file name input box"
        verify_msg_2="Step 02: Verify the drop down box closes hiding the search results"
        verify_msg_3="Step 03: Verify the drop down box opens and displays the last results of the last search and search term display in the File name field"
        verify_msg_4="Step 04: Verify Warning pops up 'report1 already exists. Do you want to overwrite it?'"
        verify_msg_5="Step 05: Verify Error displays 'The name contains one or more invalid characters'"
        verify_msg_6="Step 06: Verify Extension warning message displayed"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, CC - AppStudio->AS Framework
                    Right click on 161337 and select Open
                    Click on AS menu and select Save As
                    Delete the original File name in the Save As dialog and type r'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[3])
                     
        as_utilobj.select_tree_view_pane_item(select_folder) 
        time.sleep(wait_time[3])
           
        as_utilobj.select_component_by_right_click(right_click_item=select_file,click=component_locators.open_button)
        time.sleep(wait_time[6])
          
        as_utilobj.select_component_by_right_click(right_click_item=refresh_folder,click=component_locators.refresh_descendants)
        time.sleep(wait_time[5])
         
        as_utilobj.select_application_menu_options(send_keys=key_pattern_2)
        time.sleep(wait_time[2])
         
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_box_id,write=press_c) 
        time.sleep(wait_time[1])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1)
        time.sleep(wait_time[2])
         
        '''Step 02: Click the down arrow for the File name'''
         
        automation.EditControl(AutomationId=edit_box_id).Click(ratioX=390, ratioY=10)
        time.sleep(wait_time[1]) 
         
        as_utilobj.Verify_Element(verify_element,verify_msg_2,unavailable=True)
        time.sleep(wait_time[1])
         
        '''Step 03: Delete r in the File name and click the down arrow'''
         
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_box_id,send_key=delete_key) 
        time.sleep(wait_time[1])
         
        automation.EditControl(AutomationId=edit_box_id).Click(ratioX=390, ratioY=10)
        time.sleep(wait_time[1])
         
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_3)
        time.sleep(wait_time[2])
         
        '''Step 04 & 05: While search results box is open, delete the r character in File name field
                        Type report1 for File name click OK 
                        Click NO'''
         
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=report_1)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_element_using_ui(verify_msg_4,text_item=verify_warning_message_1)
        time.sleep(wait_time[2])
         
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(wait_time[1])
         
        '''Step 05: Type report1.. for File name click OK 
                    Click OK on App Studio message'''
         
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=filename_with_special_charectors)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_element_using_ui(verify_msg_5,text_item=verify_warning_message_2)
        time.sleep(wait_time[2])
         
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(wait_time[1])
         
        '''Step 06: In the Save As dialog, navigate to Dataservers->EDASERVE->Applications
                    Select baseapp
                    Type report1.is for File nane
                    Click OK'''
         
        as_utilobj.select_tree_view_pane_item(data_server_path)
        time.sleep(wait_time[3])
         
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=file_name_extension_modify)
        time.sleep(wait_time[2])
         
        as_utilobj.verify_element_using_ui(verify_msg_6,text_item=verify_extension_warning_message)
        time.sleep(wait_time[2])
          
        '''Step 07: Click OK on App Studio message
                    Click Cancel
                    Close 161337 tab'''
         
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(wait_time[1])
         
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[1])
        
        as_utilobj.close_canvas_item()
        time.sleep(wait_time[3])

if __name__=='__main__' :
    unittest.main()     