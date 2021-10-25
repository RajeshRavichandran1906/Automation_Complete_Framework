'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287831'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import keyboard as keys
from common.lib import as_utility

class C2287831_TestClass(AS_BaseTestCase):
    def test_C2287831(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on Configured Environments'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="Configured Environments",send_keys=['down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element('Add...',"Step 01: Verified - Contextual menu includes one option 'Add'",available=True)
            
        keys.press('enter')
        time.sleep(3)
        
        '''Step 02: Select Add from contextual menu of Configured Environments.'''
        
        as_utilobj.Verify_Current_Dialog_Opens("WebFOCUS Environment Properties","Step 02: Verified - Environment configuration dialog opens")
        
        '''Step 03: Click Cancel to close (configuring environment is tested in another test plan)'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)

        as_utilobj.Verify_Current_Dialog_Closes("WebFOCUS Environment Properties","Step 03: Verified - Environment configuration dialog Closes")
        
if __name__=='__main__' :
    unittest.main()