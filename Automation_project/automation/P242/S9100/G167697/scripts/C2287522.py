'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287522'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import pyautogui as keys
from common.lib import as_utility

class C2287522_TestClass(AS_BaseTestCase):
    def test_C2287522(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
                        
        '''Step 02: Create a new Text Document in any domain application (folder) on a remote wf environment'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(3)   
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Text Document")
        time.sleep(2)
          
        as_utilobj.verify_active_tool("App Studio - Edit Text1.txt","Step 01: Verify new text docucment invoked")
        time.sleep(2)   
               
        '''Step 03: Make a minor change in the text editor'''
          
        as_utilobj.select_home_button(move_x=800,move_y=250)
        time.sleep(1)   
               
        keys.typewrite('TWO WORDS')
        time.sleep(1)
                         
        '''Step 04: Choose Save As from AS menu and save the file in default filename'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(5)   
          
        as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
        time.sleep(1)   
               
        as_utilobj.click_element_using_ui(edit_element=True,id="1516",write="C2287522")
        time.sleep(1)   
                       
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)   
          
        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        '''Step 05: Verify that the file attributes are updated in the environment detail panel'''
        
        as_utilobj.select_tree_view_pane_item("S9100")
        time.sleep(2)     
             
        as_utilobj.select_file(list_item="C2287522.txt")
        time.sleep(3)   
         
        as_utilobj.verify_element_using_ui("Step 05: Verify that the file attributes are updated in the environment detail panel",list_item_exist="C2287522.txt",available=True) 
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="C2287522.txt",click="Delete")
        time.sleep(1)   
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)   
     
        print("Created file deleted for reason of next run")
        time.sleep(1)   
       
if __name__=='__main__' :
    unittest.main()