'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288412'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288412_TestClass(AS_BaseTestCase):
    def test_C2288412(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on NewPage and select Open.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="1 Column",click="Open")
        time.sleep(8)
        
        as_utilobj.verify_active_tool("App Studio - Page Designer","Step 01: Verified Page Designer opens inside App Studio. Home ribbon is minimized and QAT is disabled except for AS Menu, New and Open.")
        time.sleep(2)
        
        '''Step 02: Select Close from AS menu.'''
    
        as_utilobj.close_canvas_item()
        time.sleep(5)
        
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified Page Designer closes.")
        time.sleep(2)
        
        '''Step 03: Double click on NewPage'''
        
        tree_path="1 Column"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - Page Designer","Step 03: Verified Page Designer opens inside App Studio on double-click. Home ribbon is minimized and QAT is disabled except for AS Menu, New and Open.")
        time.sleep(2)
        
        '''Step 04: Close Page Designer tab'''
        
        as_utilobj.close_canvas_item()
        time.sleep(5)
        
if __name__=='__main__' :
    unittest.main()  