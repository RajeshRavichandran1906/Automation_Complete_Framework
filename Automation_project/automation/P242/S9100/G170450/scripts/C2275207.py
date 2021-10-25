'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275207'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275207_TestClass(AS_BaseTestCase):
    def test_C2275207(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Select your folder under Content. Press Alt key. Press 1 (for Open)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_1, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 01: Verify - Open file dialog opens. Default location is your folder under Content")
        time.sleep(2)
        
        '''Step 02: Click cancel'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()