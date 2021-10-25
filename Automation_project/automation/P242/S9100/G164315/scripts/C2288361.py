'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288361'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility

class C2288361_TestClass(AS_BaseTestCase):
    def test_C2288361(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWSubfolder and select Delete. 
                    Click Yes
                    Right click FWfolder and select Delete. 
                    Click Yes'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)

        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Delete")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 01: Message pops up asking if you are sure. Sub folder is deleted from the tree.")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Closes("FWFolder", "Step 02: Message pops up asking if you are sure .Folder is deleted from the tree.")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()