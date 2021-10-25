'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287725'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2287725_TestClass(AS_BaseTestCase):
    def test_C2287725(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: From Environments Detail panel, right-click a domain folder and select New | Folder'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="New Folder")
        time.sleep(1)
        
        keys.write("C2287725")
        keys.press("enter")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="C2287725",click="Properties")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 01: Verify that Environment Detail panel has focus and that the newly added folder is selected.",tree_item="C2287725",available=True) 
        time.sleep(2)
        
        '''Step 02: Delete the created folder'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="C2287725",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Step 02: Created folder been verified and deleted for reason of next run")
        
if __name__=='__main__' :
    unittest.main()   