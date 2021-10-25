'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288289'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288289_TestClass(AS_BaseTestCase):
    def test_C2288289(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click Domains and select Impact Analysis'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder='Domains',click="Impact Analysis")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source", "Step 01: Verified that 'Select a Data Source' dialog opens")
        time.sleep(1)
        
        '''Step 02: Click Cancel'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Closes("Select Data Source","Step 02: Verified that 'Select a Data Source' dialog closed")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()