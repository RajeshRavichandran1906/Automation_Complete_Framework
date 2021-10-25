'''@author: Adithyaa

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275229'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275229_TestClass(AS_BaseTestCase):
    def test_C2275229(self):
    
        '''Create instance of object '''
        
        driver=self.driver 
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        """Step 01.If File/Folder Properties is checked on the ribbon bar, uncheck it."""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("F","P")
        time.sleep(1) 
        
        as_utilobj.verify_element_using_ui("Step 01: VFPerify File/Folder Properties panel must close",check_box="File/Folder Properties")
        time.sleep(2)
            
        """Step 02.Press Alt key, press H (for Home ribbon), press FP (for File/Folder Properties)"""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("F","P")
        time.sleep(1) 
        
        as_utilobj.verify_element_using_ui("Step 02: Verified - File/Folder Properties checkbox in Home ribbon is checked..",check_box="File/Folder Properties")
        time.sleep(2)
        
        """Step 03.Press Alt key, press H (for Home ribbon), press FP (for File/Folder Properties)."""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("F","P")
        time.sleep(1) 
        
        as_utilobj.verify_element_using_ui("Step 03: Verified - File/Folder Properties panel or tab disappears and checkbox in Home ribbon is Unchecked..",check_box="File/Folder Properties")
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("F","P")
        time.sleep(1) 
        
if __name__=='__main__' :
    unittest.main() 