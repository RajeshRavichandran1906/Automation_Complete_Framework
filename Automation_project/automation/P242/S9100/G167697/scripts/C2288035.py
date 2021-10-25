'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288035'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_panels
from common.lib import as_utility

class C2288035_TestClass(AS_BaseTestCase):
    def test_C2288035(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01:  Set Filter to Show Only Procedure Files
                    Navigate to S9100
                    Right click on adminsharedFEX an select Copy'''
           
        as_panel_obj.environment_panel_file_filter(filter="Procedure Files")
        time.sleep(1)
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2) 
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="ActiveChart",click="Copy")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio","Step 01: Verify file been copied and App Studio should not crashed")
        time.sleep(2)
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 