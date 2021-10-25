'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287614'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2287614_TestClass(AS_BaseTestCase):
    def test_C2287614(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: In Environments Tree, select a defined WebFOCUS environment
                    Expand Data Servers
                    On QAT, click WebFOCUS Administration'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        tree_path="Data Servers"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=["down","down"])
        time.sleep(2)
        
        as_utilobj.Verify_Element("Reporting Server Console","Step 01: Verified Reporting Server Console is enabled")
        time.sleep(1)
        
        keys.hotkey("esc")
        time.sleep(1)
        
        '''Step 02: Expand EDASERVE->Applications>ibisamp
                    On QAT, click WebFOCUS Administration'''
        
        tree_path="EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(8)
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=["down","down"])
        time.sleep(1)
        
        as_utilobj.Verify_Element("Reporting Server Console","Step 02: Verified Reporting Server Console is enabled")
        time.sleep(1)
        
        keys.hotkey("esc")
        
if __name__=='__main__' :
    unittest.main()      