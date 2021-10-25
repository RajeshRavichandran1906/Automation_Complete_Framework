'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288720'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation

class C2288720_TestClass(AS_BaseTestCase):
    def test_C2288720(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_duplicated_file="aliceblue_1.css"
        rename_file_as_1aliceblue="1aliceblue{Enter}"
        expand_base_app="Web Applications->baseapp"
        
        '''Testcase verification'''
        
        verify_renamed_file="1aliceblue.css"
        verify_msg_1="Step 01: Verify existing file renamed as 1aliceblue.css"
        verify_msg_2="Step 02: Verify filename displayed in property panel and list_item are similar"
        verify_msg_3="Step 03: Verify file is deleted"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Web Applications->baseapp
                    Right click on aliceblue_1.css and select Rename
                    Type 1aliceblue 
                    Hit Enter'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                      
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        as_utilobj.select_tree_view_pane_item(expand_base_app)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item=select_duplicated_file,click=component_locators.rename_file) 
        time.sleep(2)
 
        automation.SendKeys((rename_file_as_1aliceblue))
        time.sleep(2)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=verify_renamed_file,available=True)
        time.sleep(2)
        
        '''Step 02: Right click on 1aliceblue.css and select Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_item=verify_renamed_file,click=component_locators.properties_button) 
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=verify_renamed_file,available=True)
        time.sleep(2)
        
        '''Step 03: Right click on 1aliceblue.css and select Delete
                    Click Yes in App Studio prompt message
                    Un-Check Environments Detail in View group'''
        
        as_utilobj.select_component_by_right_click(right_click_item=verify_renamed_file,click=component_locators.delete) 
        time.sleep(2)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=verify_renamed_file,unavailable=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()