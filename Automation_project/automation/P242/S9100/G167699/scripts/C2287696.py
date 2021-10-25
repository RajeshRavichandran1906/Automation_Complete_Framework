'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287696'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as auto

class C2287696_TestClass(AS_BaseTestCase):
    def test_C2287696(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Data Servers->EDASERVE->Applications->baseapp"
        base_folder="baseapp"
        
        '''Test Case Verifications'''
        
        verify_msg_1="Step 02: Verify newly created text file 'a.txt' is added in tree"
        verify_msg_2="Step 03: Verify newly created style sheet file 'b.sty' is added in tree"
        verify_msg_3="Step 04: Verify newly created fex 'c.fex' is added in tree"
        verify_msg_4="Step 05: Verify newly created text file 'a.txt' deleted from tree"
        verify_msg_5="Step 06: Verify newly created style sheet file 'b.sty' deleted from tree"
        verify_msg_6="Step 07: Verify newly created fex 'c.fex' deleted from tree"
                
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, navigate to Data Servers->EDASERVE-Applications and expand
                    Right click on baseapp and select New->Text Document
                    Type TABLE
                    Close Edit Text1.txt tab
                    Click Yes in App Studio saving message prompt'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
            
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_text_document)
        time.sleep(5)
         
        as_utilobj.select_home_button(move_x=600,move_y=600)
        time.sleep(1)
         
        auto.SendKeys("TABLE")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        '''Step 02: Type a for File name and click OK
                    Expand baseapp'''
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file="a")
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=base_folder)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item="a.txt",available=True)
        time.sleep(2)
        
        '''Step 03: Right click on baseapp and select New->WebFOCUS Stylesheet
                    Type Style
                    Close Edit StyleSheet1.sty tab
                    Click Yes in App Studio saving message prompt
                    Type b for File name and click OK'''
           
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_wf_stylesheet)
        time.sleep(5)
         
        as_utilobj.select_home_button(move_x=600,move_y=600)
        time.sleep(1)
         
        auto.SendKeys("Style")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file="b")
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=base_folder)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item="b.sty",available=True)
        time.sleep(2)
        
        '''Step 04: Right click on baseapp and select New->Procedure with Text Editor
                    Type Text Editor
                    Close Procedure1.fex tab
                    Click Yes in App Studio saving message prompt
                    Type c for File name and click OK'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.procedure_via_text_editor)
        time.sleep(5)
         
        as_utilobj.select_home_button(move_x=600,move_y=600)
        time.sleep(1)
         
        auto.SendKeys("Text Editor")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file="c")
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=base_folder)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item="c.fex",available=True)
        time.sleep(2)
        
        '''Step 05: In Environments Tree, Data Servers->EDASERVE-Applications->baseapp
                    Right click on a.txt and select Delete
                    Click Yes in App Studio delete message'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="a.txt",click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item="a.txt",unavailable=True)
        time.sleep(2)
        
        '''Step 06: Right click on b.sty and select Delete
                    Click Yes in App Studio delete message'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="b.sty",click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,tree_item="b.sty",unavailable=True)
        time.sleep(2)
        
        '''Step 07: Right click on c.fex and select Delete
                    Click Yes in App Studio delete message
                    In Environments Tree, collapse Data Servers'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="c.fex",click=component_locators.delete)
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_6,tree_item="c.fex",unavailable=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()        