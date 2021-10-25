'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224441'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators

class C2224441_TestClass(AS_BaseTestCase):
    def test_C2224441(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
         
        '''Test-case property variables'''
        
        webfocus_env_path="webfocus_environment"
        press_keys=['down','down']
        wait_time=[1,2,3,4,5,6] 
        
        '''Test-case verification'''

        verify_msg_1="Step 01: Verify Web-site opens in IE browser (If system default browser is IE)"
        
        '''Test-script'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click the down arrow next to the Help icon on top right corner of AS window.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[2])
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_page_button,x=0.85,y=0.35,send_keys=press_keys)
        time.sleep(wait_time[5])
        
        as_utilobj.Verify_Browser_Content(locators.ie_browser_classname,verify_msg_1,verify_browser=True,browser_close=True)
        time.sleep(wait_time[2])
        
if __name__=='__main__' :
    unittest.main()  