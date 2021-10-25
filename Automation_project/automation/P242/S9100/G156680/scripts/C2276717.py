'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2276717'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import uiautomation as automation

class C2276717_TestClass(AS_BaseTestCase):
    def test_C2276717(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: If Help Wizard is checked on the ribbon bar, un-check it and Press Alt key, press H (for Home ribbon), press HW'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('H','W')
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 01: Verified - Help Wizard panel displays on the right and Help Wizard check-box in Home ribbon is checked",check_box="Help Wizard")
        time.sleep(1)
    
        '''Step 02: Press Alt key, press H (for Home ribbon), press HW'''
                
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('H','W')
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 02: Verified - Help Wizard panel no longer displays on the right and Help Wizard check-box in Home ribbon is unchecked",check_box="Help Wizard")
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()      