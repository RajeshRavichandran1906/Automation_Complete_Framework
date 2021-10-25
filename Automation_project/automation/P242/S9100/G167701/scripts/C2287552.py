'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287552'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui

class C2287552_TestClass(AS_BaseTestCase):
    def test_C2287552(self): 
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
          
        '''Step 01: In Environments Tree, navigate to Data Servers->EDASERVE->Applications->ibisamp
                    Double click on carinst2.fex
                    Right click on COUNTRY, click Delete
                    Click AS menu->Exit
                    Hit Cancel at "save changes" prompt'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
                                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        tree_path="Data Servers->EDASERVE->Applications->ibisamp->carinst2.fex"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(8)
          
        as_utilobj.select_home_button(move_x=590,move_y=296) 
        time.sleep(1)
         
        as_utilobj.select_component_by_right_click(click="Delete") 
        time.sleep(1)
           
        as_utilobj.select_application_menu_options(send_keys=['up'])
        time.sleep(1)
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - carinst2.fex*","Step 01: Verified - AS and the Report tool remains open")
        time.sleep(1)
           
        '''Step 02: Close carinst2.fex; click No to save changes prompt
                    In Environments Tree, Domains->Public folder
                    Right-click on Public->New | Procedure
                    On Line 2, Type -* '''
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
         
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
         
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Procedure")
        time.sleep(3)
         
        as_utilobj.select_home_button(move_x=940,move_y=570)
        time.sleep(2)
           
        pyautogui.typewrite("-* '''")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(1)
        
        '''Step 03: Click AS menu->Exit
                    Click Cancel at "save changes" prompt
                    Close the Text Editor tool; do not save changes'''
        
        as_utilobj.select_application_menu_options(send_keys=['up','enter'])
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Procedure1*","Step 02: Verified - AS and the text editor tool remains open")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(1)
             
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
              
if __name__=='__main__' :
    unittest.main()  