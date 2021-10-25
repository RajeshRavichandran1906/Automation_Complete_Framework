'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288636'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2288636_TestClass(AS_BaseTestCase):
    def test_C2288636(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, CC - AppStudio->AS Framework
                    Right click on AS Framework and select Security->Rules'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
        
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu="Rules...")
        time.sleep(20)
        
        as_utilobj.verify_active_tool("App Studio - Security Rules - S9100","Step 01: Security Rules invoked for the folder S9100")
        time.sleep(3)
        
        '''Step 02: Double click on Domains
                    Close Security Rules - ASFramework tab'''
        
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - Security Rules - S9100","Step 02: Verified One Security Center window is open at any point in time for folder.")
        time.sleep(5)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(5)
        
        '''Step 03: In Environments Tree, expand CC - AppStudio->AS Framework
                    Right click on AS-2260 and select Security->Rules'''
                 
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item='AS-2260',click="Security",click_sub_menu="Rules...")
        time.sleep(20)
        
        as_utilobj.verify_active_tool("App Studio - Security Rules - AS-2260","Step 03: Security Rules invoked for the folder AS-2260")
        time.sleep(3)
        
        '''Step 04: Double click on Domains
                    Close Security Rules - AS-2260 tab'''
        
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
        
        as_utilobj.verify_active_tool("App Studio - Security Rules - AS-2260","Step 04: Verified One Security Center window is open at any point in time for file.")
        time.sleep(3)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(5)

if __name__=='__main__' :
    unittest.main()     