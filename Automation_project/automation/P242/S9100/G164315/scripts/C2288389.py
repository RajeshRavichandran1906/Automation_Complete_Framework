'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288389'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility

class C2288389_TestClass(AS_BaseTestCase):
    def test_C2288389(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS-2260 and select Open
                    Close AS-2260 tab '''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Open")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260","Step 01: Verified AS-2260 file invoked in report canvas")
        time.sleep(1)
         
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 02: Right click on AS-2260 and select Open in Text Editor
                    Close Edit AS-2260 tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Open in Text Editor")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Edit AS-2260","Step 02: Verified AS-2260 file invoked in text editor canvas")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 03: Right click on ActiveChart and select Open
                    Close ActiveChart tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="ActiveChart",click="Open")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - ActiveChart","Step 03: Verified Active chart invoked in canvas area of App Studio")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 04: Right click on ActiveChart and select Open in Text Editor
                    Close Edit ActiveChart tab'''
        
        
        as_utilobj.select_component_by_right_click(right_click_item="ActiveChart",click="Open in Text Editor")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Edit ActiveChart","Step 04: Verified Active chart invoked in text editor canvas of App Studio")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  