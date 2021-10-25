'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288379'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
from common.pages import as_panels

class C2288379_TestClass(AS_BaseTestCase):
    def test_C2288379(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panels_obj=as_panels.AS_Panels(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Set Filter to Other Files
                    In Domains, CC - AppStudio->AS Framework
                    Right click on TextFile'''
        
        as_panels_obj.environment_panel_file_filter(filter="Other Files")
        time.sleep(1)

        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="TextFile",send_keys=['down'])
        time.sleep(2)
        
        item_list=['Open in Text Editor','Edit in Windows Associated Tool','Hide','Security','New','Duplicate','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: "+ items + " element avaliable in right click options of text file",available=True)
            
        keys.press('esc')
        time.sleep(5)
            
        '''Step 02: Double click on TextFile to open 
                    Right click on TextFile
                    Close Edit TextFile tab '''  
            
        tree_path="TextFile"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3) 

        as_utilobj.select_component_by_right_click(right_click_item="TextFile",send_keys=['down'])
        time.sleep(1)
        
        item_list=['Hide','Security','New','Duplicate','Copy','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: "+ items + " element avaliable in right click options of text file in opened state",available=True)
            
        keys.press('esc')
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_panels_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
            
if __name__=='__main__' :
    unittest.main()