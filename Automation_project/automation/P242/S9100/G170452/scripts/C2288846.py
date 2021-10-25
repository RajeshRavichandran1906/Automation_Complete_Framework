'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288669'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators
import uiautomation as automation

class C2288669_TestClass(AS_BaseTestCase):
    def test_C2288669(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        select_blue_style=['down','down']
        select_default_style=['down']
        
        '''Testcase verification'''
        
        verify_style_dropdown="step1_C2288846.png" 
        verify_blue_style="step2_C2288846.png"
        verify_msg_1="Step 01: Verify A list of Office styles displays"
        verify_msg_2="Step 02: Verify vlue style selected"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click the drop down arrow next to Style located at top right.'''
        
        as_utilobj.click_element_using_ui(split_button=locators.style_splitbutton)   
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_style_dropdown,verify_msg_1)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(split_button=locators.style_splitbutton)   
        time.sleep(1)
        
        '''Step 02: Select Office 2007 (Blue Style)
                    Click the drop down arrow next to Style'''
        
        as_utilobj.click_element_using_ui(split_button=locators.style_splitbutton,send_keys=select_blue_style)   
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_RETURN,waitTime=1)
        time.sleep(2) 

        as_utilobj.verify_picture_using_sikuli(verify_blue_style,verify_msg_2)
        time.sleep(1)
        
        '''Step 03: Select Default
                    Click the drop down arrow next to Style'''
        
        as_utilobj.click_element_using_ui(split_button=locators.style_splitbutton,send_keys=select_default_style)   
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_RETURN,waitTime=1)
        time.sleep(2) 
        
if __name__=='__main__' :
    unittest.main()     