'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288883'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels

class C2288883_TestClass(AS_BaseTestCase):
    def test_C2288883(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panelobj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to All Files
                    Right click on CALLME1.mnt and select Copy
                    Navigate to Data Servers->EDASERVE->Applications
                    Right click on baseapp and select Paste'''
         
        as_panelobj.environment_panel_file_filter(filter="All Files")
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="CALLME1",click="Copy")
        time.sleep(1)
         
        tree_path="Data Servers->EDASERVE->Applications"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
         
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="Paste")
        time.sleep(2)
        
        '''Step 02: Expand baseapp
                    Right click on callme1.mnt and select Properties
                    Collapse Data Servers'''
        
        tree_path="baseapp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
                
        as_utilobj.select_component_by_right_click(right_click_item="callme1.mnt",click="Properties")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step6_C2288883.png","Step 02: Verified the Maintain files under Content showing Data Server section in the properties panel")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item='callme1.mnt',click='Delete')
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()     