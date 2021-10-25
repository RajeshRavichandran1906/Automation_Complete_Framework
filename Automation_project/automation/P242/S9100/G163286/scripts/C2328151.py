'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328151'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import keyboard as keys

class C2328151_TestClass(AS_BaseTestCase):
    def test_C2328151(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_domain="Domains"
        root_folder="S9100"
        write_two_words="TWO WORDS"
        
        '''Testcase verification'''
        
        verify_msg_1="Step 1.1: Verify Undo icons on the Quick Access Tool bar are disabled"
        verify_msg_2="Step 1.2: Verify Redo icons on the Quick Access Tool bar are disabled"
        verify_msg_3="Step 02: Verify Undo icons on the Quick Access Tool bar are enabled"
        verify_msg_4="Step 3.1: Verify Undo icons on the Quick Access Tool bar are enabled"
        verify_msg_5="Step 3.2: Verify Redo icons on the Quick Access Tool bar are enabled"
        verify_msg_6="Step 4.1: Verify All the text was removed from the canvas. Undo is disabled"
        verify_msg_7="Step 4.2: Verify Redo is enabled in QAT"
        verify_msg_8="Step 5.1: Verify word TWO is added back. Undo is enabled"
        verify_msg_9="Step 5.2: Verify Redo is enabled in QAT"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right on AS Framework and select New > Text Document'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_tree_view_pane_item(expand_domain) 
        time.sleep(5)
               
        as_utilobj.select_component_by_right_click(right_click_folder=root_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_text_document)
        time.sleep(6)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,button_item=locators.undo_button,disabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_2,button_item=locators.redo_button,disabled=True)
        time.sleep(1)
        
        '''Step 02: Line 1, type 'TWO WORDS' in the Text Editor canvas.'''
        
        keys.write(write_two_words)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,button_item=locators.undo_button,enabled=True)
        time.sleep(1)
        
        '''Step 03: Click the Undo icon in the QAT once.'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.undo_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,button_item=locators.undo_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,button_item=locators.redo_button,enabled=True)
        time.sleep(1)
        
        '''Step 04: Click the Undo icon in the QAT twice'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.undo_button)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.undo_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_6,button_item=locators.undo_button,disabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_7,button_item=locators.redo_button,enabled=True)
        time.sleep(1)
        
        '''Step 05: Use the Redo icon in the QAT'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.redo_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_8,button_item=locators.undo_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_9,button_item=locators.redo_button,enabled=True)
        time.sleep(1)
        
        '''Step 06: Close Edit Text1.txt* tab
                    Click No to App Studio saving prompt'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main()  