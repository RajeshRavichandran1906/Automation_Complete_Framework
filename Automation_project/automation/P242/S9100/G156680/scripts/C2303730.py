'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2303730'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2303730_TestClass(AS_BaseTestCase):
    def test_C2303730(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Launch App Studio, press Alt +H'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2303730.png","Step 01: Verified Hot Keys are displays for each objects in the Home Tab")
        time.sleep(2)
        
        keys.press(['esc','esc'])
        time.sleep(1)

if __name__=='__main__' :
    unittest.main()         