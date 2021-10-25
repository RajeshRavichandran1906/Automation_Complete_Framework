'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288709'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288709_TestClass(AS_BaseTestCase):
    def test_C2288709(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_crime1="crime1.js"
        select_duplicated_file="crime1_1.js"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify file is duplicated in name of crime1_1.js"
        verify_msg_2="Step 02: Verify java script file name displayed in propety panel"
        verify_msg_3="Step 03: Verify duplicated java script file name displayed in propety panel"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Detail, Web Applications->baseapp
                    Right click on crime1.js and select Duplicate'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.refresh_descendants) 
        time.sleep(6) 
                    
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1,click=component_locators.duplicate_file) 
        time.sleep(3)
        
        as_utilobj.select_file(tree_item=select_duplicated_file)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=select_duplicated_file,available=True)
        time.sleep(2)
         
        '''Step 02: Right click on crime1.js and select Properties'''
         
        as_utilobj.select_component_by_right_click(right_click_item=select_crime1,click=component_locators.properties_button) 
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=select_crime1,available=True)
        time.sleep(2)

        '''Step 03: Right click on crime1_1.js and select Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_item=select_duplicated_file,click=component_locators.properties_button) 
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=select_duplicated_file,available=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()