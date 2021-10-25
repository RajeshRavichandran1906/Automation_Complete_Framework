'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288702'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import keyboard as keys
import uiautomation as automation

class C2288702_TestClass(AS_BaseTestCase):
    def test_C2288702(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_base_app="Web Applications->baseapp"
        select_ivp_html="ivp_1.html"
        rename_as_C2288702="c2288702"
        rename_as_new="new"
        
        '''Testcase verification'''
        
        verify_renamed_file_1="c2288702.html"
        verify_renamed_file_2="new.html"
        verify_msg_1="Step 02: Verify file is renamed as c2288702"
        verify_msg_2="Step 03: Verify file is renamed as c2288702 in property panel"
        verify_msg_3="Step 04: Verify file is renamed as new from c2288702"
         
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Detail->Web Applications->baseapp
                    Right click on ivp_1.html and select Rename'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(expand_base_app) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_item=select_ivp_html,click=component_locators.rename_file)
        time.sleep(4)
                       
        '''Step 02: Type c2288702
                    Hit Enter'''        
        
        keys.write(rename_as_C2288702)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=2)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item=verify_renamed_file_1,available=True)
        time.sleep(1)
        
        '''Step 03: Right click on c2288702.html and select Properties'''
        
        as_utilobj.select_component_by_right_click(right_click_item=verify_renamed_file_1,click=component_locators.properties_button)
        time.sleep(2) 
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item=verify_renamed_file_1,available=True)
        time.sleep(1)
        
        '''Step 04: Click c2288702.html
                    Type new
                    Hit Enter'''
        
        as_utilobj.select_component_by_right_click(right_click_item=verify_renamed_file_1,click=component_locators.rename_file)
        time.sleep(4)
        
        keys.write(rename_as_new)
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_ENTER, waitTime=2)
        time.sleep(2)
    
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item=verify_renamed_file_2,available=True)
        time.sleep(1)    
        
        '''Step 05: Right click on new.html and select Delete
                    Click Yes in App Studio prompt message'''
        
        as_utilobj.select_component_by_right_click(right_click_item=verify_renamed_file_2,click=component_locators.delete)
        time.sleep(4)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()