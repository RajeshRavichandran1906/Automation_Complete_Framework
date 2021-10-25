'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275196'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275196_TestClass(AS_BaseTestCase):
    def test_C2275196(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Open existing report. Press Alt key, press F (for app menu), press A (for Save As)'''   
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100->Report1"            
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="Refresh Descendants")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("Save As","Step 01: Verify Save as Dialogue Opens")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()