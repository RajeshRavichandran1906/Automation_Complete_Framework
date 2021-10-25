'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2308283'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
from common.pages import as_panels

class C2308283_TestClass(AS_BaseTestCase):
    def test_C2308283(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panel_obj=as_panels.AS_Panels(driver)
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Open
                    Navigate to a Configured Environment, expand Data Servers->EDASERVE->Applications
                    Click ibisamp->cargraph.fex
                    Hit "z"
                    Click Cancel'''
    
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                          
        tree_path="Data Servers->EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(send_keys=['down'])
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(list_item="cargraph.fex")
        
        keys.press('z')
        
        as_utilobj.Verify_Element("zcomp.fex","Step 01: Verify navigate using key strokes works fine under Data Server",available=True)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
         
        '''Step 02: In Environments Tree, set Filter by Procedures files
                    Navigate to Domains->CC - AppStudio->AS Files
                    Click on AS menu and click Open and highlight the first file 
                    Hit "a" key
                    Click Cancel'''
        
        as_panel_obj.environment_panel_file_filter(filter="Procedure Files")
        time.sleep(1)
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
         
        as_utilobj.select_application_menu_options(send_keys=['down'])
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(list_item="CarParm.fex")
        time.sleep(1)
        
        keys.press("A")
        time.sleep(1)
        
        as_utilobj.Verify_Element("ActiveChart.fex","Step 02: Verify navigate using key strokes works fine under Domains",available=True)
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel") 
        time.sleep(1)
        
        '''Step 03: Check the Environments Detail
                    In Environment Detail, navigate to Data Servers->EDASERVE->Applications
                    Click ibisamp, highlight the first file 
                    Hold the Shift key down and hit "m"
                    UnCheck the Environments Detail'''
        
        as_utilobj.Verify_Element("App Studio","Step 03: Verify navigate using key strokes works fine under environment Detail",available=True)
        time.sleep(1)
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
          
if __name__=='__main__' :
    unittest.main()     