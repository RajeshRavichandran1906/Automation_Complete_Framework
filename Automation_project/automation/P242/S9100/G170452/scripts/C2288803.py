'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288803'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288803_TestClass(AS_BaseTestCase):
    def test_C22888803(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        configured_environments="Configured Environments"
        select_domains="Domains"
        select_framework_folder="S9100"
        open_0724RObj_file="0724RObj"
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_application_menu_dropdown="step1_C2288803.png"
        verify_application_menu_dropdown_enabled="step5_C2288803.png"
        verify_msg_1="Step 01: Verify Open is enabled on selecting configured environments"
        verify_msg_2="Step 02: Verify Open is enabled on selecting webfocus environments"
        verify_msg_3="Step 03: Verify Open is enabled on selecting domains"
        verify_msg_4="Step 04: Verify Open is enabled on selecting folders"
        verify_msg_5="Step 05: Verify Open is enabled on invoking fex file"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, select Configured Environments
                    Click the AS logo '''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        as_utilobj.select_tree_view_pane_item(configured_environments) 
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_application_menu_dropdown,verify_msg_1)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 02: Select a Configured Environments in the tree
                    Click the AS logo'''
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)

        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_application_menu_dropdown,verify_msg_2)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 03: In Environments Tree, select Domains
                    Click the AS logo'''
                    
        as_utilobj.select_tree_view_pane_item(select_domains) 
        time.sleep(sleep[3])            
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_application_menu_dropdown,verify_msg_3)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 04: In Environments Tree, Domains->CC - AppStudio
                    Select AS Framework folder
                    Click the AS logo'''
        
        as_utilobj.select_tree_view_pane_item(select_framework_folder) 
        time.sleep(sleep[3])  
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_application_menu_dropdown,verify_msg_4)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        '''Step 05: Right click on 0724RObj and select Open in Text Editor
                    Click the AS logo
                    Close Edit 0724RObj.fex tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item=open_0724RObj_file,click=component_locators.open_in_text_editor)
        time.sleep(6)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_application_menu_dropdown_enabled,verify_msg_5)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(open_application_menu=True)
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
        
if __name__=='__main__' :
    unittest.main() 