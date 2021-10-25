'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287621'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui

class C2287621_TestClass(AS_BaseTestCase):
    def test_C2287621(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In a Configured Environments, right-click on Domains'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        '''Step 02: Click Security'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='Domains',click="Security")
        
        as_utilobj.Verify_Current_Dialog_Closes("Owner","Step 01: Verified that Owner... is NOT in the Security menu")
        time.sleep(2)
        
        pyautogui.press(['esc','esc'])
        
if __name__=='__main__' :
    unittest.main()  