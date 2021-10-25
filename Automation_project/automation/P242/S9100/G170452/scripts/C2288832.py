'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288832'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288832_TestClass(AS_BaseTestCase):
    def test_C2288832(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_folder="Domains->S9100"
        select_161337="161337"
        base_folder="S9100"
        select_print_preview=['down','down','down','down','down','down','right','down']
        
        '''Testcase verification'''
        
        verify_print_preview_document="step1_C2288832.png"
        verify_msg_1="Step 01: Verify print preview document is displayed in App studio canvas"
        
        '''Testscript'''
        
        as_utilobj.select_home_button() 
        
        '''Step 01: In Environments Tree, Domains->CC - AppStudio->AS Framework
                    Right click on 161337 and select Open in Text Editor
                    Click the AS 
                    Hover on PRINT and select the second option: Print Preview'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                      
        as_utilobj.select_tree_view_pane_item(expand_base_folder) 
        time.sleep(3)
                   
        as_utilobj.select_component_by_right_click(right_click_item=select_161337,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.open_in_text_editor)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.refresh_descendants)
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(send_keys=select_print_preview)
        time.sleep(2)
        
        as_utilobj.verify_picture_using_sikuli(verify_print_preview_document,verify_msg_1)
        time.sleep(2)
        
        '''Step 02: Click Close in Preview section
                    Close Edit 161337 tab'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()