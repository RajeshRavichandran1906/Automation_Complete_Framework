'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287664'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_panels
from common.lib import as_utility
import uiautomation as automation

class C2287664_TestClass(AS_BaseTestCase):
    def test_C2287664(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panel_obj=as_panels.AS_Panels(driver)
          
        as_utilobj.select_home_button()
         
        '''Step 01: In Environments Tree, filter by Other Files
                    Right-click Domains>CC - AppStudio._AS Files->callcenter.css and select Open
                    Click Home on the ribbon bar
                    Click the down arrow on Windows then click New Window'''
         
        as_panel_obj.environment_panel_file_filter(filter="Other Files")
        time.sleep(1)
               
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Domains->S9100->callcenter"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio - callcenter","Step 01: Verify app studio does not crash after .CSS file opened")
        time.sleep(3)
         
        as_utilobj.select_home_button()
        time.sleep(1)
 
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
         
        as_utilobj.select_home_button()
        time.sleep(1)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_W, waitTime=2)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_N, waitTime=2)
        time.sleep(5)
         
        '''Step 02a: Right-click mapview.js and select Open
                    Click Home on the ribbon bar
                    Click the down arrow on Windows then click New Window'''
         
        as_utilobj.click_element_using_ui(tree_item="mapview")
        time.sleep(5)
        
        as_utilobj.verify_active_tool("App Studio - mapview","Step 02: Verify app studio does not crash after .JS file opened")
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(3)
         
        as_utilobj.select_home_button()
        time.sleep(1)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_W, waitTime=2)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_N, waitTime=2)
        time.sleep(4)
        
        '''Step 03: Close mapview.js:2 by clicking the X 
                    Close mapviewset.js by clicking the X
                    Close callcenter.css:2 by clicking the X 
                    Close callcenter.css by clicking the X'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(4)
              
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(4)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)

if __name__=='__main__' :
    unittest.main() 