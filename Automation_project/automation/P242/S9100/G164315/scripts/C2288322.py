'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288322'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2288322_TestClass(AS_BaseTestCase):
    def test_C2288322(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
            
        '''Step 01: In Environments Tree, Domains, right click on Public and select Security>Rules...'''
     
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Security",click_sub_menu="Rules...")
        time.sleep(3)
         
        as_utilobj.verify_active_tool("App Studio - Security Rules - S9100","Step 01: Verified WebFOCUS Security window opens displaying Groups and Users and the rules for each")
        time.sleep(2)
         
        '''Step 02: Close Security Rules - Public by clicking X'''
         
        as_utilobj.close_canvas_item()
        time.sleep(1)      
 
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified Rules Window closes")
        
        '''Step 03: In Environments Tree, Domains, right click on Public and select Security>Rules on this Resource...'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Security",click_sub_menu="Rules on this Resource...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - Rules on this Resource - S9100","Step 03: Verified WebFOCUS Security window opens displaying Groups and Users and the rules for each")
        time.sleep(2)

        '''Step 04: Close Rules on this Resource - Public by clicking X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(1)   
        
        as_utilobj.verify_active_tool("App Studio","Step 04: Rules on this resource Window closes")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()