'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288384'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui
from common.pages import as_panels

class C2288384_TestClass(AS_BaseTestCase):
    def test_C2288384(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panels_obj=as_panels.AS_Panels(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filters to Procedure Files
                    Right click on AS-2260'''
                
        as_panels_obj.environment_panel_file_filter(filter="Procedure Files")
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down'])
        time.sleep(2)
         
        item_list=['Open','Open in Text Editor','Edit in Windows Associated Tool','Run','Run Deferred','Schedule','Print','Security','New','Duplicate','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: "+ items + " element avaliable in right click options of fex file before publishing",available=True)
        time.sleep(2)
             
        pyautogui.press('esc')
        time.sleep(1)
         
        '''Step 02: Right click on AS Framework and select Publish
                    Right click on AS-2260'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
                 
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down'])
        time.sleep(1)
         
        item_list=['Open','Open in Text Editor','Edit in Windows Associated Tool','Run','Run Deferred','Schedule','Print','Hide','Security','New','Duplicate','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: "+ items + " element avaliable in right click options of fex file after publishing",available=True)
        time.sleep(2)
             
        pyautogui.press('esc')
        time.sleep(1)
         
        '''Step 03: Double click on AS-2260
                    Close AS-2260 tab'''
         
        tree_path="AS-2260"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
         
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",send_keys=['down'])
        time.sleep(2)
         
        item_list=['Schedule','Print','Security','New','Duplicate','Copy','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 03: "+ items + " element avaliable in right click options of fex file in opened state",available=True)
             
        pyautogui.press('esc')
        time.sleep(1)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        '''Step 04: Right click on AS-2260 and hover New'''
                
        as_utilobj.select_component_by_right_click(right_click_item="AS-2260",click="New")
        time.sleep(2)
        
        item_list=['Procedure','Procedure via Text Editor','Report','SQL Report','Chart','SQL Chart','HTML/Document','Visualization','Alert','Reporting Object','URL','Collaborative Portal','Portal Page','JavaScript File','Cascading Style Sheet','WebFOCUS StyleSheet','Text Document','Schedule','Distribution List','Library Access List','Folder','Blog']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 04: "+ items + " element avaliable on right clicking 'New'",available=True)
        time.sleep(2)

        pyautogui.press(['esc','esc'])
        time.sleep(1)
        
        '''Again revert back folder to unpublish state'''

        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
        
        as_panels_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()