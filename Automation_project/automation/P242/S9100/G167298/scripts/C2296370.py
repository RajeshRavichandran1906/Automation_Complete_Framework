'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2296369'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2296370_TestClass(AS_BaseTestCase):
    def test_C2296370(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
          
        as_utilobj.select_home_button()
        
        '''Step 01: Click Environments icon in the Home Ribbon'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="Environments")
        time.sleep(1) 
        
        as_utilobj.Verify_Current_Dialog_Opens("Environments List","Step 01: Verify Configured Environment list is been opened")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()        