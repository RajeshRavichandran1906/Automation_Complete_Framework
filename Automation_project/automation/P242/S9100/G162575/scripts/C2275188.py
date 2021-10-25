'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275188'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys
import uiautomation as automation

class C2275188_TestClass(AS_BaseTestCase):
    def test_C2275188(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Close all files. Press Alt key.'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2275188.png","Step 01: Verified Hot hotkeys display: F = app menu, 1-09 = QAT, H = Home ribbon, W = WebFOCUS Administration, S = Style, E = Help menu.")
        time.sleep(5)
        
        keys.press('esc')
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main() 