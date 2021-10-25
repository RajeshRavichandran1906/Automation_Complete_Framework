'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287598'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287598_TestClass(AS_BaseTestCase):
    def test_C2287598(self): 
        
        '''Need to check check box for projects'''
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
         
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Options 
                    Select Environments
                    Click Cancel'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="Environments")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 01: Verified - Content changed to Domains in Options|Environments section",check_box="Show Domains area")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)

if __name__=='__main__' :
    unittest.main()  