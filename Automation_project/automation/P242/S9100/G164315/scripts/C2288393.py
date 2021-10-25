'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288393'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288393_TestClass(AS_BaseTestCase):
    def test_C2288393(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS-2260 and select Schedule->Email
                    Close AS-2260 - Schedule (Basic) tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Schedule",click_sub_menu="Email...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260- Schedule (Basic)","Step 01: Verified Schedule Email tab been invoked in App studio canvas")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 02: Right click on AS-2260 and select Schedule->FTP
                    Close AS-2260 - Schedule (Basic) tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Schedule",click_sub_menu="FTP...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260- Schedule (Basic)","Step 02: Verified Schedule FTP tab been invoked in App studio canvas")
        time.sleep(3)
            
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 03: Right click on AS-2260 and select Schedule->Printer
                    Close AS-2260 - Schedule (Basic) tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Schedule",click_sub_menu="Printer...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260- Schedule (Basic)","Step 03: Verified Schedule Printer tab been invoked in App studio canvas")
        time.sleep(3)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 04: Right click on AS-2260 and select Schedule->Report Library
                    Close AS-2260 - Schedule (Basic) tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Schedule",click_sub_menu="Report Library...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260- Schedule (Basic)","Step 04: Verified Schedule Report Library tab been invoked in App studio canvas")
        time.sleep(3)
            
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 05: Right click on AS-2260 and select Schedule->Managed Reporting
                    Close AS-2260 - Schedule (Basic) tab'''
        
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="Schedule",click_sub_menu="Managed Reporting...")
        time.sleep(15)
        
        as_utilobj.verify_active_tool("App Studio - AS-2260- Schedule (Basic)","Step 05: Verified Schedule Managed Reporting tab been invoked in App studio canvas")
        time.sleep(3)
            
        as_utilobj.close_canvas_item()
        time.sleep(3)
                
if __name__=='__main__' :
    unittest.main()