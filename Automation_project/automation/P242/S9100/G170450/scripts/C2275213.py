'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275213'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import keyboard as keys

class C2275213_TestClass(AS_BaseTestCase):
    def test_C2275213(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(self.driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: Right click a folder under Content and select New > Text Document. Type 'TWO WORDS'. Press Alt key, press 5 (for undo)'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"            
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Text Document")
        time.sleep(2)

        keys.write('TWO WORDS')
        time.sleep(2)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_5, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Element("WORDS","Step 01: Verified - Undo done, The text 'WORDS' is removed",unavailable=True)
        time.sleep(3)
        
        '''Step 02: Press Alt key, press 6 (for redo)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_6, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Element("TWO WORDS","Step 02: Verified - Redo done, the text 'WORDS' is added",unavailable=True)
        time.sleep(3)

        '''Step 03: Close text editor, say No to save prompt'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
               
if __name__=='__main__' :
    unittest.main()