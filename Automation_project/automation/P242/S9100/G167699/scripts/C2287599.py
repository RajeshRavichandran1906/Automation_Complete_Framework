'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287599'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287599_TestClass(AS_BaseTestCase):
    def test_C2287599(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Domains->S9100"
        base_folder="S10141"
        
        '''Test Case Verifications'''
        
        verify_new_procedure="App Studio - Procedure1"
        verify_msg_1="Step 1.1: Verify new procedure is invoked"
        verify_msg_2="Step 2.1: Verify DM If tab is opened"
        verify_msg_3="Step 2.2: Verify DM If tab is closed"
        verify_msg_4="Step 3.1: Verify DM Goto tab is opened"
        verify_msg_5="Step 3.2: Verify DM Goto tab is closed"
        verify_msg_6="Step 4.1: Verify DM Label tab is opened"
        verify_msg_7="Step 4.2: Verify DM Label tab is closed"
        verify_msg_8="Step 5.1: Verify DM Repeat tab is opened"
        verify_msg_9="Step 5.2: Verify DM Repeat tab is closed"
        verify_msg_10="Step 6.1: Verify Dialogue Mngr tab is opened"
        verify_msg_11="Step 6.2: Verify Dialogue Mngr tab is closed"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on AS Framework and select New->Procedure
                    Pin the Procedure View panel
                    Close the Comment component editor tab'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
           
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_procedure)
        time.sleep(5)
          
        as_utilobj.verify_active_tool(verify_new_procedure,verify_msg_1)
        time.sleep(1)
               
        as_utilobj.click_element_using_ui(tab_control="1018",x=110,y=10)
        time.sleep(2)
         
        '''Step 02: Right-click top-level folder in Procedure View panel and select New>Dialogue Mngr>DM If
                    Click X on the DM If editor tab to close it'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(1)
         
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                   
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,send_keys=['down','right'],click=component_locators.new_dialogue_manager,click_sub_menu=component_locators.new_dm_if)  
        time.sleep(3) 
         
        as_utilobj.verify_element_using_ui(verify_msg_2,pane_control="DM If",available=True)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tab_control="1018",x=110,y=10)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_3,pane_control="DM If",unavailable=True)
        time.sleep(1)
         
        '''Step 03: Right-click top-level folder in Procedure View panel & select New>Dialogue Mngr>DM Goto
                    Click X on the DM Goto editor tab to close it'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                   
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,send_keys=['down','right'],click=component_locators.new_dialogue_manager,click_sub_menu=component_locators.new_dm_goto)  
        time.sleep(3) 
         
        as_utilobj.verify_element_using_ui(verify_msg_4,pane_control="DM Goto",available=True)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tab_control="1018",x=110,y=10)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_5,pane_control="DM Goto",unavailable=True)
        time.sleep(1)
         
        '''Step 04: Right-click top-level folder in Procedure View panel & select New>Dialogue Mngr>DM Label
                    Click X on the DM Label editor tab to close it'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                   
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,send_keys=['down','right'],click=component_locators.new_dialogue_manager,click_sub_menu=component_locators.new_dm_label)  
        time.sleep(3) 
         
        as_utilobj.verify_element_using_ui(verify_msg_6,pane_control="DM Label",available=True)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tab_control="1018",x=110,y=10)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_7,pane_control="DM Label",unavailable=True)
        time.sleep(1)
         
        '''Step 05: Right-click top-level folder in Procedure View panel & select New>Dialogue Mngr>DM Repeat
                    Click X on the DM Repeat editor tab to close it'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                   
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,send_keys=['down','right'],click=component_locators.new_dialogue_manager,click_sub_menu=component_locators.new_dm_repeat)  
        time.sleep(3) 
         
        as_utilobj.verify_element_using_ui(verify_msg_8,pane_control="DM Repeat",available=True)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tab_control="1018",x=110,y=10)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_9,pane_control="DM Repeat",unavailable=True)
        time.sleep(1)
        
        '''Step 06: Right-click top-level folder in Procedure View panel & select New>Dialogue Mngr>Dialog Mngr
                    Click X on the Dialogue Mngr to close it
                    UnPin the Procedure View panel
                    Close Procedure1 tab'''
        
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                  
        as_utilobj.select_component_by_right_click(right_click_folder=component_locators.parent_folder,send_keys=['down','right'],click=component_locators.new_dialogue_manager,click_sub_menu=component_locators.new_dialogue_manager)  
        time.sleep(3) 
        
        as_utilobj.verify_element_using_ui(verify_msg_10,pane_item="59648")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tab_control="1018",x=122,y=10)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_11,pane_control="Dialogue Mngr",unavailable=True)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main() 