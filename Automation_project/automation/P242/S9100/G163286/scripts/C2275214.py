'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/22875214'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import keyboard as keyboard_keys
import uiautomation as automation_keys

class C2275214_TestClass(AS_BaseTestCase):
    def test_C2275214(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_initial_repository="Domains"
        folder_under_domain="S9100"
        type_words="WORDS"
        undo_text='{Ctrl}(Z)'
        redo_text='{Ctrl}(Y)'
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_image_1="step1_C2275214.png"
        verify_image_2="step2_C2275214.png"
        verify_msg_1="Step 01: Verify WORDS as typed in text document"
        verify_msg_2="Step 02: Verify the text 'WORDS' is removed"
        verify_msg_3="Step 03: Verify the text 'WORDS' is added back"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains->CC - AppStudio 
                    Right click on AS Framework and select New > Text Documentl
                    Type 'WORDS"'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(select_initial_repository) 
        time.sleep(sleep[3])
         
        as_utilobj.select_component_by_right_click(right_click_folder=folder_under_domain,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_text_document)
        time.sleep(sleep[2])
          
        keyboard_keys.write(type_words)
        time.sleep(sleep[2])
          
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1)
        time.sleep(2)
          
        '''Step 02: Press Ctrl+Z'''
          
        automation_keys.SendKeys((undo_text),interval=0.25,waitTime=1)
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_2)
        time.sleep(2)
          
        '''Step 03: Press Ctrl+Y'''
         
        automation_keys.SendKeys((redo_text),interval=0.25,waitTime=1)
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_3)
        time.sleep(2)
        
        '''Step 04: Close Edit Text1.txt* tab
                    Click No to App Studio saving prompt'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()     