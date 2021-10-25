'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275231'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275231_TestClass(AS_BaseTestCase):
    def test_C2275231(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Press Alt key, press H (for Home ribbon), press SB (for Status Bar)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('s','b')
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 01: Verified - Status bar appears at the bottom of the App Studio window and checkbox for Status Bar in Home ribbon is checked",pane_item="59393")
        time.sleep(1)

        '''Step 02: Press Alt key, press H (for Home ribbon), press SB (for Status Bar)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('s','b')
        time.sleep(1)

        as_utilobj.verify_element_using_ui("Step 02: Verified - Status Bar no longer visible and the checkbox for Context Bar is unchecked",check_box="Status Bar")
        time.sleep(5) 
        
if __name__=='__main__' :
    unittest.main()     