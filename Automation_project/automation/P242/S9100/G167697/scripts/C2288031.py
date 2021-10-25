'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288031'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_ribbon
from common.lib import as_utility

class C2288031_TestClass(AS_BaseTestCase):
    def test_C2288031(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver) 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In View group, check Environments Tree
                    Collapse all environments in Environments Tree
                    Collapse all environments in Environments Detail
                    Uncheck Environments Tree'''
                                    
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Detail")
        time.sleep(1)
         
        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Tree")
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
        
        '''Step 02: Uncheck Environments Detail
                    Check Environments Detail'''
        
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Tree")
        time.sleep(1)
        
        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Detail")
        time.sleep(1)

        as_utilobj.verify_element_using_ui("Step 01: Verify Environments Detail panel opens along the left border of AS window, the pin is pointing down and the items in the tree pane are collapsed",check_box="Environments Detail")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()      