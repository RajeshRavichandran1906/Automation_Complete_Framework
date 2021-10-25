'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275230'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275230_TestClass(AS_BaseTestCase):
    def test_C2275230(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Press Alt key, press H (for Home ribbon), press CB (for Context Bar)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('c','b')
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui("Step 01: Context Bar appears under the ribbon and checkbox for Context Bar is checked.",pane_item="221")
        time.sleep(1)
        
        '''Step 02: Press Alt key, press H (for Home ribbon), press CB (for Context Bar)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('c','b')
        time.sleep(3)
        
        as_utilobj.verify_element_using_ui("Step 02: Context Bar no longer visible and the checkbox for Context Bar is unchecked.",check_box="Context Bar")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()        