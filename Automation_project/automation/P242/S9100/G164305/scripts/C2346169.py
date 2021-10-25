'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346169'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2346169_TestClass(AS_BaseTestCase):
    def test_C2346169(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: AS Menu->Options->HTML Page->Form Settings'''

        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="HTML Page",button="Form Settings")
        time.sleep(2)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2346169.png","Step 01: Verified form settings contains following '5,10,10,4' values")
        time.sleep(2)

        '''Step 02: Click Cancel
                    Click Cancel'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 