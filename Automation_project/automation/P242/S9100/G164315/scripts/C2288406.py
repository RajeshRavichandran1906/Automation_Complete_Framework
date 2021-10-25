'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288406'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2288406_TestClass(AS_BaseTestCase):
    def test_C2288406(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on ActiveChart and select Properties.
           Step 02: Under Environments Tree, View Options
                    Check View items by Name
                    In Environments Tree, Domains
                    Expand ASFramework'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("AS-2260","Step 02: Verified file/folder properties displays title & name for AS-2260 in check view by title",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 03: Right click on ActiveChart and select Properties 
           Step 04: Under Environments Tree, View Options
                    Check View items by Title
                    Expand AS Framework'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("AS-2260","Step 04: Verified file/folder properties displays title & name for AS-2260 in check view by name",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()        