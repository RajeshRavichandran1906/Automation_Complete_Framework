'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288374'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2288388_TestClass(AS_BaseTestCase):
    def test_C2288388(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click on File/Folder Properties panel and pinned
                    Right click on AS-2260 and select Duplicate.
           Step 02: Click on the first AS-2260 in the Environments Tree
           Step 03: Click on the second AS-2260 in the Environments Tree'''
        
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
        
        as_utilobj.Verify_Element("Duplicate","Step 01: file/Folder properties of AS-2260 been displayed in the name AS-2260",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Element("Duplicate","Step 02: Duplicated and file/Folder properties of AS-2260 been displayed in the name AS-2260_1",available=True)
        time.sleep(1)
        
        keys.hotkey('escape')
        time.sleep(1)
        
        '''Step 04: Double click on the first AS-2260 in the Environments Tree
                    Close AS-2260 tab'''
        
        tree_path="AS-2260"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260","Step 03: AS-2260 fex been invoked in Report canvas")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 05: Right click on the first AS-2260 and select Run
                    Close the WebFOCUS Report tab
                    Right on the first AS-2260 and select Delete
                    Click Yes to App Studio Prompt'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Run")
        time.sleep(1)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 04: AS-2260 Report containing following",item_list=['COUNTRY','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY'],browser_close=True)
        time.sleep(3)
        
        '''Step 06: Double click on the second AS-2260 in the Environments Tree
                    Close AS-2260 tab
                    Unpinned File/Folder Properties panel'''
        
        tree_path="AS-2260"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260","Step 05: AS-2260 fex been invoked in Report canvas")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  