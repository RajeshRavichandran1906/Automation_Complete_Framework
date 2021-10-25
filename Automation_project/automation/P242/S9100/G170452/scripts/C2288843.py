'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288843'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2288843_TestClass(AS_BaseTestCase):
    def test_C2288843(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_dataservers="Data Servers->EDASERVE->Applications"
        select_baseapp="baseapp"
    
        '''Testcase verification'''
        
        verify_webfocus_admin="step3_C2288843.png"
        verify_msg_1="Step 01: Verify WebFOCUS administration been disabled"
        verify_msg_2="Step 02: Verify WebFOCUS administration been enabled"
        verify_msg_3="Step 03: Verify WebFOCUS Administration Console dropdown is displayed and '7' administartion option been found - Domains"
        verify_msg_4="Step 04: Verify WebFOCUS Administration Console dropdown is displayed and '7' administartion option been found - Dataservers"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, select Configured Environments'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_1,split_button_item=locators.wf_admin_splitbutton,disabled=True)
        time.sleep(1)
         
        '''Step 02: In Environments Tree, select a configured environment'''
         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_2,split_button_item=locators.wf_admin_splitbutton,enabled=True)
        time.sleep(1)
         
        '''Step 03: Click on the drop down arrow next to WebFOCUS Administration'''
         
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli(verify_webfocus_admin,verify_msg_3)
        time.sleep(2)
         
        '''Step 04: Navigate to Data Servers->EDASERVE->Applications
                    Expand Applications and select baseapp
                    Click on the drop down arrow next to WebFOCUS Administration
                    Collapse Data Servers'''
        
        as_utilobj.select_tree_view_pane_item(expand_dataservers) 
        time.sleep(1)
        
        as_utilobj.select_file(tree_item=select_baseapp)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_webfocus_admin,verify_msg_4)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button=locators.wf_admin_splitbutton)
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
            
if __name__=='__main__' :
    unittest.main()     