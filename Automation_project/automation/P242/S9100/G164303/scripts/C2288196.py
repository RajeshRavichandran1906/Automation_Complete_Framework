'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288196'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import keyboard as keys_1

class C2288196_TestClass(AS_BaseTestCase):
    def test_C2288196(self):
        
        '''Required CarParm, CarTwoParms, Chart1 files to be in S9100 folder under domains'''
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
         
        '''Step 01: In Environments Tree, Domains, right click on AS Framework->New->Folder
                    Type Delete and hit Enter
                    Select SimpleReportForChart hold down shift key and select userdoc1'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")
        time.sleep(1)
           
        keys_1.write("Delete")
        keys.hotkey("enter")
        time.sleep(2)
   
        as_utilobj.select_multiple_files("CarParm",['CarTwoParms','Chart1'])
        time.sleep(1)
                      
        '''Step 02: Right click within Environments Tree panel and select Copy
                    Navigate to Delete folder,right click and select Paste
                    Expand Delete folder'''
              
        keys.click(button='right')
        as_utilobj.click_element_using_ui(menu_item=True,name="Copy")  
          
        tree_path="Delete"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(right_click_folder="Delete",click="Paste")
        time.sleep(2)
          
        '''Step 03: Right click on CarParm and select Delete
                    Check "Don't show this message again", then click Yes.'''
          
        as_utilobj.click_element_using_ui(tree_item="Delete")
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_item="CarParm",click="Delete")
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(check_box=True,id="1681")
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
        
        '''Step 04: Right click on CarTwoParms and select Delete'''
               
        as_utilobj.select_component_by_right_click(right_click_folder="Delete",click="Delete")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Closes("Yes","Step 04: Verified file is deleted from the tree without a message")
        
        '''Step 05: Click AS Main menu -> Options 
                    Click on Reset All Messages Boxes
                    Click OK'''

        as_utilobj.select_application_menu_options(options=True)
        time.sleep(2)
                   
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Message Boxes")
        time.sleep(2)

        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 06: Right click on Delete and select Delete
                    Click Yes'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")
        time.sleep(1)
           
        keys_1.write("Delete")
        keys.hotkey("enter")
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="Delete",click="Delete")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 06: Verified message boxes are resetted")
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)      
     
if __name__=='__main__' :
    unittest.main()       