'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287528'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as auto
import pyautogui as keys

class C2287538_TestClass(AS_BaseTestCase):
    def test_C2287538(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Domains->S9100"
        base_folder="S9100"
        
        '''Test Case Verifications'''
        
        verify_pasted_comment="step3_C2287538.png"
        verify_msg_1="Step 01: Verify there must be new Comment component inserted after the top level folder"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, right click on AS Framework and select New->Procedure
                    Right-click the parent folder in Procedure View panel
                    Select New... | Set'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(5)
            
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                  
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,click=component_locators.comments_new,click_sub_menu=component_locators.new_set)  
        time.sleep(3) 
            
        '''Step 02: Double-click ACCBLN in Available Settings list
                    Close the Set and Comment tabs
                    Click Procedure View panel 
                    Right-click Comment component and choose Copy'''
            
        auto.PaneControl(Name="Set").DoubleClick(ratioX=420,ratioY=340)
        time.sleep(2)
           
        auto.TabControl(AutomationId="1018").Click(ratioX=115,ratioY=13)
        time.sleep(2)
 
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(1)

        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
    
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.comment) 
        time.sleep(1) 
        keys.press(['down','down','down','enter'])
        time.sleep(3) 
        
        '''Step 03: Right-click the top folder in Procedure View panel and choose Paste
                    Close Procedure1 tab
                    Click No in App Studio saving prompt message'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder)  
        time.sleep(1) 
        keys.press(['down','down','enter'])
        time.sleep(3) 
        
        as_utilobj.verify_picture_using_sikuli(verify_pasted_comment,verify_msg_1)
        time.sleep(2)
        
        as_utilobj.select_home_button(move_x=700,move_y=700)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()     