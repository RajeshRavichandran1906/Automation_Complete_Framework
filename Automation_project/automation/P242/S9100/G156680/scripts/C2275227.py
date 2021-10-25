'''@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275227'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275227_TestClass(AS_BaseTestCase):
    def test_C2275227(self):
    
        '''Create instance of object '''
        
        driver=self.driver 
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        """Step 1.Press Alt key, press H (for Home), press CC (for Command Console)"""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("C","C")
        time.sleep(1)
        
        as_utilobj.Verify_Element("Command Console","Step 01: Verify command console invokes",available=True)
        time.sleep(1)
        
        """Step 2.Click the X to close"""
        
        as_utilobj.close_canvas_item()
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio","Step 02: Verify command console closes.")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()