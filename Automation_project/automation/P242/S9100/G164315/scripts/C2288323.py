'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288323'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2288323_TestClass(AS_BaseTestCase):
    def test_C2288323(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
            
        '''Step 01: In Environments Tree, Domains, right click on Public folder and select Security>Effective Policy...'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Security",click_sub_menu="Effective Policy...")
        time.sleep(1)
         
        as_utilobj.verify_active_tool("App Studio - Effective Policy - S9100","Step 01: Verified Effective Policy window opens displaying list of Privileges with the associated list of Effective Policy.")
        time.sleep(2)
        
        '''Step 02: Close Effective Policy - Public tab by clicking on X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(1) 
        
        as_utilobj.verify_active_tool('App Studio',"Step 02: Verified Effective Policy window closes")
        time.sleep(2)
        
        '''Step 03: In Environments Tree, Domains, right click on Public folder and select Security>Owner...'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Security",click_sub_menu="Owner...")
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio - Set Owner - S9100","Step 03: Verified Set Owner window opens")
        time.sleep(2)
  
        '''Step 04: Close Set Owner - Public tab by clicking on X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)       
        
        as_utilobj.verify_active_tool("App Studio","Step 04: Set Owner Window closes")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()