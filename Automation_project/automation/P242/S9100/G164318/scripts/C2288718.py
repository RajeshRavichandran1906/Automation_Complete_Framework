'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288718'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288718_TestClass(AS_BaseTestCase):
    def test_C2288718(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_aliceblue="aliceblue.css"
        select_duplicated_file="aliceblue_1.css"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        
        '''Testcase verification'''
        
        verify_css_file="App Studio - aliceblue.css"
        verify_duplicated_css_file="App Studio - aliceblue_1.css"
        verify_msg_1="Step 01: Verify file is duplicated in name of aliceblue_1.css"
        verify_msg_2="Step 02: Verify css file invoked"
        verify_msg_3="Step 03: Verify css file property panel displays name correctly"
        verify_msg_4="Step 04: Verify duplicated css file invoked"
        verify_msg_5="Step 05: Verify css duplicated file property panel displays name correctly"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Web Applications->baseapp
                    Right click on aliceblue.css and select Duplicate'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.refresh_descendants) 
        time.sleep(6) 
                    
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,click=component_locators.duplicate_file) 
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=select_duplicated_file)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=select_duplicated_file,available=True)
        time.sleep(2)
         
        '''Step 02: Double click on aliceblue.css'''
         
        as_utilobj.click_element_using_ui(tree_item=select_aliceblue)
        time.sleep(3)
         
        as_utilobj.verify_active_tool(verify_css_file,verify_msg_2)
        time.sleep(3)
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 03: Click on File/Folder Properties
                    Close aliceblue.css tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_aliceblue,click=component_locators.properties_button)
        time.sleep(1)
        
        as_utilobj.select_file(tree_item=select_aliceblue)
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=select_aliceblue,available=True)
        time.sleep(2)
        
        '''Step 04: Double click on aliceblue_1.css'''
        
        as_utilobj.click_element_using_ui(tree_item=select_duplicated_file)
        time.sleep(3)
        
        as_utilobj.verify_active_tool(verify_duplicated_css_file,verify_msg_4)
        time.sleep(3)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 05: Click on File/Folder Properties
                    Close aliceblue_1.css tab'''

        as_utilobj.select_component_by_right_click(right_click_item=select_duplicated_file,click=component_locators.properties_button)
        time.sleep(1)
        
        as_utilobj.select_file(tree_item=select_duplicated_file)
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,tree_item=select_duplicated_file,available=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()