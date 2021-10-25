'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275209'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275209_TestClass(AS_BaseTestCase):
    def test_C2275209(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 1: Double click a file to open, modify the file (add column to report, measure to chart, component to html, comment to procedure, etc.)'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100->Report1"            
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - Report1","Step 01: Verify report invoked successfully")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tree_item="DEALER_COST")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Report1*","Step 02: Verify File name on File tab has asterisk (*) denoting file was modified and not yet saved.")
        time.sleep(1)
                
        '''Step 2: Press Alt key, press 2 (for Save)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
       
        automation.SendKey(automation.Keys.VK_2, waitTime=3)
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - Report1","Step 03: Verify Asterisk (*) at end of file name disappears.")
        time.sleep(1)   
        
        '''Step 3: Close report.File closes without a prompt to save'''
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
        
if __name__=='__main__' :
    unittest.main()     