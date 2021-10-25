'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288296'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288296_TestClass(AS_BaseTestCase):
    def test_C2288296(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click Domains and select ReportCaster Explorer.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder='Domains',click='ReportCaster Explorer')
        
        as_utilobj.verify_active_tool("App Studio - ReportCaster Explorer","Step 01: Verified ReportCaster Explorer window opens inside App Studio canvas")
        
        '''Step 02: Close ReportCaster Explorer window by clicking the X on the tab.'''
            
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
        
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified ReportCaster Explorer closes.")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 