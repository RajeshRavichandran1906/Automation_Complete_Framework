'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287528'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import keyboard as keys
import uiautomation as automation

class C2287528_TestClass(AS_BaseTestCase):
    def test_C2287528(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path="Data Servers->EDASERVE->Applications"
        select_ibisamp="ibisamp"
        write_my_comment="my comment"
        edit_control_box="1516"
        format_htm="htm"
        select_save=['down','down']
        select_save_as=['down','down','down']
        
        '''Testcase verification'''

        verify_warning_message="Extension change not permitted."
        verify_msg_1="Step 01: Verify warning message is displayed"
        verify_msg_2="Step 02: Verify warning message is displayed"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, Navigate Data Servers ->EDASERVE->Applications and expand
                    Right click on ibisamp and select New->"Procedure via Text Editor"
                    Add following line in text editor:
                    <!-- my comment -->'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(folder_path)
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=select_ibisamp,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.procedure_via_text_editor)
        time.sleep(2)
          
        as_utilobj.select_home_button(move_x=870,move_y=750)
        time.sleep(1)
          
        keys.write(write_my_comment)
        time.sleep(1)
          
        as_utilobj.select_component_by_right_click(right_click_folder=select_ibisamp,click=component_locators.refresh_descendants)
        time.sleep(2)
          
        '''Step 02: Click on AS menu
                    Click Save 
                    For File name, type myfile.htm
                    Click OK
                    Click OK in App Studio message prompt'''
        
        as_utilobj.select_application_menu_options(send_keys=select_save)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_control_box)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_RIGHT,waitTime=1)
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKeys(format_htm)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,text_item=verify_warning_message)
        time.sleep(1)

        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
        
        '''Step 03: Click Cancel in Save As dialog 
                    Click on AS menu
                    Click Save As
                    For File name, type myfile.htm
                    Click OK'''
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder=select_ibisamp,click=component_locators.refresh_descendants)
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(send_keys=select_save_as)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_control_box)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_RIGHT,waitTime=1)
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKey(automation.Keys.VK_BACK,waitTime=1) 
        automation.SendKeys(format_htm)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,text_item=verify_warning_message)
        time.sleep(1)

        '''Step 04: Click OK in App Studio message prompt
                    Click Cancel in Save As dialog 
                    Close Edit Procedure1.fex* tab
                    Click No in App Studio save message prompt
                    Collapse Data Servers'''
               
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
    
if __name__=='__main__' :
    unittest.main()  