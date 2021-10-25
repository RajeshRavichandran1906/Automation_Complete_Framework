'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287517'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2287517_TestClass(AS_BaseTestCase):
    def test_C2287517(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        message_box="Extension change not permitted."
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Configured Environments->Web Applications 
                    Right click on baseapp->New->HTML Page
                    Type the following code:
                    <!DOCTYPE HTML>
                    <HTML>
                    </HTML>'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                  
        tree_path="Web Applications->baseapp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="HTML Page")
        time.sleep(6)
 
        keys.typewrite("<!DOCTYPE HTML>")
        time.sleep(1)
        keys.press("enter")
        time.sleep(1)
        keys.typewrite("<HTML>")
        time.sleep(1)
        keys.press("enter")
        keys.typewrite("</HTML>")
        time.sleep(1)
        
        '''Step 02: Close HtmlPage1.htm
                    Click Yes to save file prompt
                    Type C2287517.fex for File name
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK",rename_file="C2287517.fex")
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 02: Verified - Extension change not permitted dialog box is displayed for .fex",text_item=message_box)
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)

        '''Step 03: Click OK from Message box.
                    Type C2287517.prt for File name
                    Click OK'''
        
        as_utilobj.select_home_button()
        
        as_utilobj.select_any_dialog("OK",rename_file="C2287517.prt")
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 03: Verified - Extension change not permitted dialog box is displayed for .prt",text_item=message_box)
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)

        '''Step 04: Click OK from Message box
                    Type as2349.mnt for File name
                    Click OK'''
        
        as_utilobj.select_home_button()
        
        as_utilobj.select_any_dialog("OK",rename_file="C2287517.mnt")
        time.sleep(2)

        as_utilobj.verify_element_using_ui("Step 04: Verified - Extension change not permitted dialog box is displayed for .mnt",text_item=message_box)
        time.sleep(1)

        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        '''Step 05: Click OK from Message box
                    Close HtmlPage1.htm
                    Click No to save file prompt'''
        
        as_utilobj.select_any_dialog("Cancel")
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)

if __name__=='__main__' :
    unittest.main()        