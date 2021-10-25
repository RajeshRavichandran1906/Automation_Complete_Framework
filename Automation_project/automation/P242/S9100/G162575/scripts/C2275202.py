'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275202'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275202_TestClass(AS_BaseTestCase):
    def test_C2275202(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Press Alt key, press F (for app menu), press T for Options.'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_T, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio Options","Step 01: Verify App Studio Options windows opens to the General tab.")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  