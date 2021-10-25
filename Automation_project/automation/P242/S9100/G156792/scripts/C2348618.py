'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348618'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_panels
from common.lib import as_utility
import pyautogui as keys

class C2348618_TestClass(AS_BaseTestCase):
    def test_C2348618(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panel_obj=as_panels.AS_Panels(driver)
    
        as_utilobj.select_home_button()
         
        '''Step 1: In Environments Tree, set Filter to Procedures Files
                    Navigate to CC - AppStudio->AS Files 
                    Select Autodrill and click File Folder Properties'''
         
        as_panel_obj.environment_panel_file_filter(filter="Procedure Files")
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                 
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="Autodrill",click="Properties")
        time.sleep(1)
         
        '''Step 2: Right click on Autodrill'''
         
        as_utilobj.select_home_button()
           
        as_utilobj.select_component_by_right_click(right_click_item="Autodrill",send_keys='down')
        time.sleep(1)
         
        item_list=['Run','Run Deferred']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: Verified "+ items + " element avaliable for Autodrill",available=True)
            if items=='Run Deferred':
                break
             
        keys.press('esc')
        time.sleep(2)
         
        '''Step 03: Expand AS Framework
                    Right click on BIPAutodrill and select Properties'''
            
        as_utilobj.select_component_by_right_click(right_click_item="Autodrill",click="Properties")
        time.sleep(1)
        
        '''Step 04: Right click on BIPAutodrill'''
        
        as_utilobj.select_home_button()
          
        as_utilobj.select_component_by_right_click(right_click_item="BIPAutodrill",send_keys='down')
        time.sleep(1)
        
        item_list=['Run','Run Deferred']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 04: Verified "+ items + " element avaliable for BIP Autodrill",available=True)
            if items=='Run Deferred':
                break
            
        keys.press('esc')

        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)

if __name__=='__main__' :
    unittest.main() 