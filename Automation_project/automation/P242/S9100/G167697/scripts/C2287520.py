'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287520'''

from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
import time,unittest
import keyboard as keys
from common.pages import as_ribbon

class C2287520_TestClass(AS_BaseTestCase):
    def test_C2287520(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_ribbon_obj=as_ribbon.AS_Ribbon(driver)

        as_utilobj.select_home_button() 

        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Detail")
        time.sleep(1)
          
#         as_utilobj.drag_drop(source_x=201,source_y=245,target_x=325,target_y=245)
#         time.sleep(4)
         
        '''Step 1: Right-click S9100 folder & choose New->Text Document'''
                          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                   
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Text Document")
        time.sleep(4)
                      
        as_utilobj.verify_active_tool("App Studio - Edit Text1.txt","Step 01: Verify text document been opened") 
        time.sleep(1)   
               
        '''Step 2: Make a minor/small change in the text editor'''
        
        as_utilobj.select_home_button(move_x=800,move_y=250)
        time.sleep(2)
               
        keys.write('WebFocus') 
        time.sleep(1)   
         
        '''Step 5: Click X on the text editor's tab'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        '''Step 6: Choose Yes to save file'''
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)   
        
        '''Step 7: Enter AS-2362.B & Enter AS-2362.TXT'''
        
        as_utilobj.click_element_using_ui(edit_element=True,id="1516",write="AS2362.B")
        time.sleep(4)   
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)   
        
        as_utilobj.verify_element_using_ui("Step 06: Verify text document extension not permitted",text_item="Extension change not permitted.")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)   
        
        as_utilobj.click_element_using_ui(edit_element=True,id="1516",write="AS2362")
        time.sleep(4)   
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)  
        
        as_utilobj.select_tree_view_pane_item("S9100")
        time.sleep(2)
 
        as_utilobj.verify_element_using_ui("Step 07: Verify text editor closes and file is saved successfully",list_item_exist="AS2362.txt",available=True)
        time.sleep(3)   
        
        '''Delete the created file for reason of next run'''
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="AS2362.txt",click="Delete")
        time.sleep(1)   
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 