'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288010'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels

class C2288010_TestClass(AS_BaseTestCase):
    def test_C2288010(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to ReportCaster Files
                    Right click on 123 and select Copy
                    Right click on Public Folder and select Paste'''
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                                                                    
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
              
        as_utilobj.select_component_by_right_click(right_click_item="123",click="Copy")
        time.sleep(2)
               
        as_utilobj.select_component_by_right_click(right_click_folder="Public",click="Paste")
        time.sleep(2)
    
        '''Step 02: Expand Public Folder'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->Public"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="123",click="Properties")
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 02: Verified that a schedule can be copied and pasted in the environment",tree_item="123",available=True)
        time.sleep(2)
                
        as_utilobj.select_component_by_right_click(right_click_item="123",click="Delete")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 