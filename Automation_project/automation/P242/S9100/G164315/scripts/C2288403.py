'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288403'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2288403_TestClass(AS_BaseTestCase):
    def test_C2288403(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click on File/Properties panel and pinned
                    Right click on AS-2260 and select Duplicate.
           Step 02: Select the first AS-2260 in the Environments Tree
                    Double click the first AS-2260 in the Environments Tree'''
        
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
        
        as_utilobj.Verify_Element("Duplicate","Step 01: Verified duplicate folder created above the same folder.",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("Duplicate","Step 02: verified File/Folder properties displayed in the name AS-2260. AS-2260 File invoked in report canvas",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        '''Step 03: Select the second AS-2260 in the Environments Tree
                    Double click the second AS-2260 in the Environments Tree'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("Duplicate","Step 03: verified File/Folder properties displayed in the name AS-2260_1. AS-2260_1 File invoked in report canvas",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        '''Step 04: Close AS-2260 tab
                    Close AS-2260 tab
                    Right click the first AS-2260 in the Environments Tree and select Delete
                    Click Yes to the App Studio prompt for deletion
                    Unpinned File/Properties panel'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("Delete","Step 04: verified delete prompt displays for AS-2260_1.",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()        