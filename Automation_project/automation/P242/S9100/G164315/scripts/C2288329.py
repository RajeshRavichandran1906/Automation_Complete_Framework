'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288329'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2288329_TestClass(AS_BaseTestCase):
    def test_C2288329(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, right click on Public folder under and select ReportCaster Explorer.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",send_keys=["down"],click="ReportCaster Explorer")
        time.sleep(3)
         
        as_utilobj.verify_active_tool("App Studio - ReportCaster Explorer","Step 01: Verified ReportCaster web tool explorer opens inside App Studio canvas to the current location.")
        time.sleep(3)
        
        '''Step 02: Close the ReportCaster Explorer tab by clicking on X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(1) 
        
        as_utilobj.verify_active_tool("App Studio", "Step 02: Verified Explorer window closes.")
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()