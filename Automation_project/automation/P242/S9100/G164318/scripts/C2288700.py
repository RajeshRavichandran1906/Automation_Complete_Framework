'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288700'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2288700_TestClass(AS_BaseTestCase):
    def test_C2288700(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_app="Web Applications->baseapp"
        baseapp="baseapp"
        select_ivp_html="ivp.html"
        duplicated_html_file="ivp_1.html"
        
        '''Testcase verification'''

        verify_msg_1="Step 02: Verify file name displayed as ivp.html"
        verify_msg_2="Step 03: Verify file name displayed as ivp_1.html"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree->Web Applications->baseapp
                    Right click on ivp.html and select Duplicate.'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(expand_base_app) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder=baseapp,click=component_locators.refresh_descendants)
        time.sleep(4)
                         
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,click=component_locators.duplicate_file)
        time.sleep(2)
         
        '''Step 02: Right click on ivp.html and select Properties'''
         
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,click=component_locators.file_property)
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=select_ivp_html,available=True)
        time.sleep(1)
         
        '''Step 03: Right click on ivp_1.html and select Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_item=duplicated_html_file,click=component_locators.file_property)
        time.sleep(2) 
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=duplicated_html_file,available=True)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()