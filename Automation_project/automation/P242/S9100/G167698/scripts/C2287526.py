'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287526'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2287526_TestClass(AS_BaseTestCase):
    def test_C2287526(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
         
        '''Step 01: Right click on AS Framework->New->Text Document
                    Add a few lines of text
                    Close Edit Text1.txt tab
                    Click Yes to App Studio save prompt
                    Type C2287526 and click OK'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
                                              
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                          
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
           
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Text Document")
        time.sleep(2)
            
        as_utilobj.select_home_button(move_x=900,move_y=417)
            
        keys.typewrite("Testing purpose")
            
        as_utilobj.close_canvas_item()
        time.sleep(2)
            
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1) 
            
        as_utilobj.select_any_dialog("OK",rename_file="C2287526")
        time.sleep(3)
           
        '''Step 02: In Environments Tree, set filter to Other Files 
                    Right click on C2287526 and select 'Open file in Text Editor'
                    Add a word on Line 1
                    Close Edit C2287526 tab
                    Click Yes to App Studio save prompt'''
          
        as_utilobj.select_component_by_right_click(right_click_item="C2287526",click="Open in Text Editor")
        time.sleep(2)
           
        as_utilobj.select_home_button(move_x=900,move_y=417)
        keys.typewrite("Testing purpose")
        time.sleep(1)
           
        as_utilobj.close_canvas_item()
        time.sleep(3)
           
        as_utilobj.select_any_dialog("Yes")
        time.sleep(3) 
           
        as_utilobj.Verify_Current_Dialog_Closes("Save As","Step 02: Verified File been saved and no further SAVE AS dialog appeared") 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="C2287526",click="Delete")
        time.sleep(1) 
         
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2) 
            
if __name__=='__main__' :
    unittest.main() 