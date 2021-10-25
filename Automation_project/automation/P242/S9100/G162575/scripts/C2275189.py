'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275189'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys
import uiautomation as automation

class C2275189_TestClass(AS_BaseTestCase):
    def test_C2275189(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button(move_x=1150,move_y=45)
        time.sleep(1)
        
        '''Step 01: Press Alt key, press F (for Application Menu)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
                
        as_utilobj.verify_picture_using_sikuli("step1_C2275189.png","Step 01: VerifY Each option in the AS Application Menu has a hotkey assigned..")
        time.sleep(1)
        
        keys.press('esc')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 