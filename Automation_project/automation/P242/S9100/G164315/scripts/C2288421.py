'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288421'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels
import keyboard as keys 

class C2288421_TestClass(AS_BaseTestCase):
    def test_C2288418(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panels_obj=as_panels.AS_Panels(driver)
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework-> New > JavaScript File.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="JavaScript File")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - JavaScriptFile1.js","Step 01: Verified that new java stylesheet been created")
        time.sleep(1)
        
        '''Step 02: Place cursor at end of Line 1, hit Enter
                    Type the following java script into the editor:
                    <script>
                    document.getElementById("demo").innerHTML = "Hello Dolly.";
                    </script>'''
        
        as_utilobj.select_home_button(move_x=900,move_y=410)
        time.sleep(1)
        
        keys.press('enter')
        time.sleep(1)
        
        keys.write('<script>')
        time.sleep(1)
        
        keys.press('enter')
        time.sleep(1)
        
        keys.write('document.getElementById("demo").innerHTML = "Hello Dolly.";')
        time.sleep(1)
        
        keys.press('enter')
        time.sleep(1)
        
        keys.write('</script>')
        time.sleep(3)
        
        '''Step 03: Click X on tab to close file > Yes to save prompt 
                    Click OK to save with default name.'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 03: Verified that java script been entered into javascript file")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 04: Set Filter All Files'''
        
        as_panels_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
    
        as_utilobj.select_component_by_right_click(right_click_item="JavaScriptFile1",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Note: Created new javascript file deleted for reason of next run")
        
if __name__=='__main__' :
    unittest.main()  