'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2326979'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2326979_TestClass(AS_BaseTestCase):
    def test_C2326979(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        base_folder_path="Data Servers->EDASERVE->Applications->ibisamp"
        carinst2="carinst2.fex"
        
        '''Test Case Verifications'''
        
        verify_msg_1="Step 02: Verify carinst2.fex files is pasted in se folder"
        verify_msg_2="Step 03: Verify the file is removed from the tree, the tree is refreshed and there is no trace of the previously pasted carinst2.fex"
        verify_msg_3="Step 04: Verify carinst2.fex file is added in se folder"
        verify_msg_4="Step 05: Verify carinst2.fex file is removed in se folder"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree panel, expand Data Servers->EDASERVE->Applications->ibisamp 
                    Right click on carinst2.fex and select Copy'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(base_folder_path)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_item=carinst2,click=component_locators.copy)
        time.sleep(3)
        
        '''Step 02: Right-click on EDASERVE->Applications->ibisamp >se and select Paste
                    Expand se folder'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="se",click=component_locators.paste)
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item("se")
        time.sleep(2)
                    
        as_utilobj.verify_element_using_ui(verify_msg_1,tree_item="se",available=True)
        time.sleep(2)
        
        '''Step 03: Right-click on EDASERVE->Applications->ibisamp >se>carinst2.fex and select Delete
                    Click Yes for the App Studio prompt to delete'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item("Data Servers->EDASERVE->Applications->ibisamp->se")
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_item=carinst2,click=component_locators.delete)
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_2,tree_item="carinst2.fex",available=True)
        time.sleep(2)
        
        '''Step 04: Right-click on EDASERVE->Applications->ibisamp >se and select Paste'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="se",click=component_locators.properties_button)
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,tree_item="se",available=True)
        time.sleep(2)
        
        '''Step 05: Right-click on EDASERVE->Applications->ibisamp >se>carinst2.fex and select Delete
                    Click Yes for the App Studio prompt to delete'''
        
        as_utilobj.select_component_by_right_click(right_click_item=carinst2,click=component_locators.delete)
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,tree_item="carinst2.fex",available=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()   