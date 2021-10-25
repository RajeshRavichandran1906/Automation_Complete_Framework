'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328133'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import keyboard as keys

class C2328133_TestClass(AS_BaseTestCase):
    def test_C2328133(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_domains="Domains"
        folders=["S9100","ibisamp"]
        files=["car.mas"]
        select_country="COUNTRY"
        type_table="TABLE"
        newreport="newreport" 
        newproc="newproc"
        newhtml="newhtml"
        drag_button=[485,226]
        drop_button=[754,280]
        
        '''Testcase verification'''
        
        verify_report_tool="App Studio - Report2*"
        verify_dialog="Save As"
        verify_close_all_documents_warning_prompt="All documents have been saved. Close all documents?"
        verify_msg_1="Step 01: Verify File name on file tab has asterisk (*) indicating the file was modified and not yet saved."
        verify_msg_2="Step 02: Verify save as window invokes for Report"
        verify_msg_3="Step 03: Verify save as window invokes for Procedure"
        verify_msg_4="Step 04: Verify save as window invokes for HTML"
        verify_msg_5="Step 05: Verify close all documents warning prompt been displayed"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on AS Framework and select New | Report
                    Select ibisamp->car.mas
                    Click Finish
                    Double click on COUNTRY'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                   
        as_utilobj.select_tree_view_pane_item(expand_domains) 
        time.sleep(2)
                
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(2)
        
        as_utilobj.select_file_in_dialogs(component_locators.finish_button,tree_path=folders[1],select_file=files[0])
        time.sleep(8)
        
        as_utilobj.click_element_using_ui(tree_item=select_country)
        time.sleep(2)
        
        as_utilobj.verify_active_tool(verify_report_tool,verify_msg_1)
        time.sleep(2)
        
        '''Step 02: Right click on AS Framework and select New | Procedure
                    Type TABLE on line 2 
                    Right click on AS Framework and select New | HTML/Document
                    Click Next, click Finish
                    Click on Button and draw on canvas'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(4)
        
        keys.write(type_table)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_html_document)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.next_button)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.finish_button)
        time.sleep(8)
        
        as_utilobj.drag_drop_component(locators.components_tab,locators.button_item,source_x=drag_button[0],source_y=drag_button[1],target_x=drop_button[0],target_y=drop_button[1])
        time.sleep(2)
        
        '''Step 03: Click on Save All icon
                    Type new for File name in Save As window
                    Click OK'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.saveall_button)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_2)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=newreport)
        time.sleep(5)
        
        '''Step 04: Type newproc for File name in Save As window
                    Click OK
                    Type newhtml for File name in Save As window'''
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_3)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=newproc)
        time.sleep(5)
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_4)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file=newhtml)
        time.sleep(5)
        
        '''Step 05: Click OK
                    Click Yes in App Studio message window'''
        
        as_utilobj.verify_element_using_ui(verify_msg_5,text_item=verify_close_all_documents_warning_prompt)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        '''Delete the created files'''
        
        as_utilobj.select_multiple_files(newhtml,[newproc,newreport],click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()