'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288358'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility
import pyautogui as keys

class C2288358_TestClass(AS_BaseTestCase):
    def test_C2288358(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWSubfolder and select Rename
                    Append 1 to name, hit Enter
                    Right click FWSubfolder1 and click Properties'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Rename")
        time.sleep(2)

        keys.press(['right','1'])
        time.sleep(1)
        
        keys.press("enter")
        time.sleep(1)
    
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder1",click="Properties")
        time.sleep(2)
        
        as_utilobj.Verify_Element("FWSubFolder1","Step 01: The properties panel opens on the right side of the AS window (default location, can be changed by user) displaying the sub folder's properties.",available=True)
        time.sleep(2)
        
        '''Step 02: Right click FWSubfolder1 and select Rename
                    Remove 1 to name, hit Enter'''

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder1",click="Rename")
        time.sleep(1)

        keys.press(['right','backspace'])
        time.sleep(2)
        
        keys.press("enter")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()