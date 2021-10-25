'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667306'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import pyautogui as keys
from common.lib import as_utility
import keyboard as keys_1

class C6667306_TestClass(AS_BaseTestCase):
    def test_C6667306(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
         
        '''Step 01: Domains, right click on ContextMenu folder ->New-> Report
                    Double click on ibisamp 
                    Click car.mas, click Ok'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                               
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(2)
             
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(4)
           
        '''Step 02: Click Source at the bottom of the Report canvas'''
          
        as_utilobj.click_element_using_ui(tab_item="Source")
        time.sleep(1)
           
        '''Step 03: Change line 2 from ON TABLE SET PAGE-NUM NOLEAD to TABLE SET PAGE-NUM NOLEAD
                    Click Save on the QAT'''
           
        as_utilobj.select_home_button(move_x=297,move_y=174)
        time.sleep(1)
        keys.hotkey("delete")
        keys.hotkey("enter")
          
        as_utilobj.select_home_button(move_x=297,move_y=174)
        time.sleep(1)
         
        keys_1.write("TABLE SET PAGE-NUM NOLEAD")
        time.sleep(1)
         
        keys.hotkey("enter")
        time.sleep(1)
          
        as_utilobj.click_element_using_ui(button_item=True,name="Save")
        time.sleep(1)
          
        as_utilobj.Verify_Current_Dialog_Opens("Save As","Step 03: Verified Save As window is shown")
      
        '''Step 04: Click OK in the Save As dialog (to accept the default name and location)'''
           
        as_utilobj.select_any_dialog("OK")
          
        as_utilobj.Verify_Current_Dialog_Opens("Error parsing report request","Step 03: Verified Save As window is shown")
        time.sleep(1)
           
        '''Step 05: Click OK at Error parsing report request window'''
          
        as_utilobj.select_any_dialog("OK")
  
        '''Step 06: Click X on the Report tab & Click OK at Error parsing report request window'''
          
        as_utilobj.close_canvas_item()
        time.sleep(1)
          
        as_utilobj.Verify_Current_Dialog_Opens("Error parsing report request","Step 06: Verified Error parsing report request been displayed while clicking close on 'Report'")
        time.sleep(1)
           
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        '''Step 07: Click X on the Report1 tab & Click OK at Error parsing report request window'''
          
        as_utilobj.close_canvas_item()
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens("Error parsing report request","Step 07: Verified Error parsing report request been displayed while clicking close on 'Report1'")
        time.sleep(1)
           
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
                   
        '''Step 08: Click AS menu-> Close. Click OK at Error parsing report request window'''
          
        as_utilobj.close_canvas_item()
        time.sleep(1)
          
        as_utilobj.Verify_Current_Dialog_Opens("Error parsing report request","Step 07: Verified Error parsing report request been displayed while clicking close on 'Report1'")
        time.sleep(1)
           
        as_utilobj.select_any_dialog("OK")
          
        '''Step 09: Change line 2 from TABLE SET PAGE-NUM NOLEAD to ON TABLE SET PAGE-NUM NOLEAD. Click X on the Report1 tab'''
         
        as_utilobj.select_home_button(move_x=297,move_y=174)
        time.sleep(1)
        keys.hotkey("delete")
        keys.hotkey("enter")
         
        as_utilobj.select_home_button(move_x=297,move_y=174)
        time.sleep(1)
        
        keys_1.write("ON TABLE SET PAGE-NUM NOLEAD")
        
        keys.hotkey("enter")
        time.sleep(1)
 
        as_utilobj.close_canvas_item()
        time.sleep(2)
                 
        '''Step 10: Click No at "Do you want to save the changes to file Report1?" prompt'''
        
        as_utilobj.select_any_dialog("No")
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()