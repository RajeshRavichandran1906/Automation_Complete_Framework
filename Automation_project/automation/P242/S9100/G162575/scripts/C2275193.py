'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275193'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2275193_TestClass(AS_BaseTestCase):
    def test_C2275193(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)

        '''Step 01: Select a folder under Content. Press Ctrl+O'''   
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2) 
        
        keys.hotkey('ctrl','o')
        time.sleep(3)

        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 01: Verified - Open File dialog displays, current folder is highlighted in the left pane")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1) 
        
if __name__=='__main__' :
    unittest.main() 