'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287542'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators
import keyboard as keys

class C2287542_TestClass(AS_BaseTestCase):
    def test_C2287542(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Domains->S9100"
        base_folder="S9100"
        
        '''Test Case Verifications'''
        
        verify_name_title_1="step2_C2287542.png"
        verify_name_title_2="step3_C2287542.png"
        verify_msg_1="Step 01: Verify name and title in property panel"
        verify_msg_2="Step 02: Verify name and title in property panel"
        verify_msg_3="Step 03: Verify files displays in Name format"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on AS Framework and select New->Text Document
                    Type TABLE
                    Close Edit Text1.txt tab
                    Click Yes in App Studio saving prompt message
                    Type AS-2485a for File name and click OK'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
          
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_text_document)
        time.sleep(5)
              
        as_utilobj.select_home_button(move_x=650,move_y=650)
        time.sleep(1)
          
        keys.write("TABLE")
                   
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
      
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file="AS-2485a")
        time.sleep(1)
          
        '''Step 02: In Environments Tree, select AS-2485a
                    Click File/Folder Properties panel'''
          
        as_utilobj.select_component_by_right_click(right_click_item="AS-2485a",click=component_locators.properties_environment)
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli(verify_name_title_1,verify_msg_1)
        time.sleep(2)
         
        '''Step 03: In Environments Tree, right click on AS Framework and select New->WebFOCUS StyleStyleheet
                    Type Style
                    Close Edit StyleSheet1.sty tab
                    Click Yes in App Studio saving prompt message
                    Type AS-2485b for File name and click OK'''
         
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_wf_stylesheet)
        time.sleep(5)
             
        as_utilobj.select_home_button(move_x=650,move_y=650)
        time.sleep(1)
         
        keys.write("Style")
                   
        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
         
        as_utilobj.select_any_dialog(component_locators.ok_button,rename_file="AS-2485b")
        time.sleep(3)
         
        '''Step 04: In Environments Tree panel, click Other Files
                    Select AS-2485a
                    Click File/Folder Properties panel'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=locators.other_files)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="AS-2485b",click=component_locators.properties_environment)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_name_title_2,verify_msg_2)
        time.sleep(2)
        
        '''Step 05: In Environments Tree panel->View Options, click to "View Items by Name"
                    Expand CCAppStudio->ASFramework
                    In Environments Tree panel->View Options, click to "View Items by Title"'''
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_option_menu_item)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_items_by_name)
        time.sleep(1)
        
        as_utilobj.select_tree_view_pane_item(base_folder)
        time.sleep(1)
        
        verify_files=['AS-2485a.txt','AS-2485b.sty']
        
        for files in verify_files:
            as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=files,available=True)
            time.sleep(1)
            
        as_utilobj.click_element_using_ui(button_item=True,name=locators.all_files_filter)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_option_menu_item)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(menu_item=True,name=locators.view_items_by_title)
        time.sleep(1)
        
        '''Created files deleted for reason nxt run'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2485a",click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2485b",click=component_locators.delete)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
              
if __name__=='__main__' :
    unittest.main()     