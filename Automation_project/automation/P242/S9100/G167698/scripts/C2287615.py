'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287615'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287615_TestClass(AS_BaseTestCase):
    def test_C2287615(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New->Report
                    Click on ibisamp->car.mas
                    Click Finish'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(2) 
        
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(2)
        
        '''Step 02: Click Source tab at the bottom of the Report Canvas'''
        
        as_utilobj.click_element_using_ui(tab_item="Source")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step2_C2287615.png","Step 02: Verified that Ribbon bar switched to Text Editor")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
              
if __name__=='__main__' :
    unittest.main()     