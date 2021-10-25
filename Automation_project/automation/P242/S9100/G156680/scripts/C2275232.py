'''@author: Adithyaa 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275232'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import uiautomation as automation

class C2275232_TestClass(AS_BaseTestCase):
    def test_C2275232(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Navigate to CC - AppStudio->AS Files. Filter by Procedures Files. Double click on any procedure. Press Alt key, press H (for Home ribbon), press PV (for Procedure View)'''
 
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                              
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        tree_path="Domains->S9100->Report1"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Report1","Step 01: Verify Report been invoked")
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('p','v')
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 02: Verified - Report Invoked successfully and Procedure view tab is showing on the left side of AS window",check_box="Procedure View")
        time.sleep(1)
        
        '''Step 02: Press Alt key, press H (for Home ribbon), press PV (for Procedure View)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey('p','v')
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 03.Verified - Procedure view tab is now showing on the left side of AS window and procedure view in home ribbon is checked",check_box="Procedure View")
        time.sleep(1) 
        
        '''Step 03: Close Report tab and the procedure tab'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()    