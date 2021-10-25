'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2304543'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2304543_TestClass(AS_BaseTestCase):
    def test_C2304543(self):
        
        '''Creating Object Instance'''
        
        driver = self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: Check the box for Status Bar on Home ribbon in View section'''
        
        as_utilobj.click_element_using_ui(check_box=True,name="Status Bar")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 01: Status bar appears at the bottom of App Studio. Currently not in use and shows only panel1 and panel2. See project 159697",pane_item="59393")
        time.sleep(3) 
              
        '''Step 02 : Un-check box for Status Bar on Home ribbon in View section'''
            
        as_utilobj.click_element_using_ui(check_box=True,name="Status Bar")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 02: Verified - Status bar disappears",check_box="Status Bar")
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main() 