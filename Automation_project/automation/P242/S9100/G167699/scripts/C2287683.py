'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287683'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2287683_TestClass(AS_BaseTestCase):
    def test_C2287683(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Test Case Property Variables'''
        
        webfocus_env_path="webfocus_environment"
        
        '''Test Case Verifications'''
        
        verify_domain_icon="step1_C2287683.png"
        verify_msg_1="Step 01: Verify the icon beside Domains under tree"
        verify_msg_2="Step 02: Verify the icon beside Domains under details"
        
        '''Test Script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.verify_picture_using_sikuli(verify_domain_icon,verify_msg_1)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(check_box=True,name=locators.environmentstree_checkbox)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(check_box=True,name=locators.environmentsdetail_checkbox)
        time.sleep(3)
        
        '''Step 02: Check Environments Detail in View group
                    Un-Check Environments Detail in View group'''
        
        as_utilobj.verify_picture_using_sikuli(verify_domain_icon,verify_msg_2)
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(check_box=True,name=locators.environmentsdetail_checkbox)
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(check_box=True,name=locators.environmentstree_checkbox)
        time.sleep(1)
           
if __name__=='__main__' :
    unittest.main() 