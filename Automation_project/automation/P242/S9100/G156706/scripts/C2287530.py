'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287530'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287530_TestClass(AS_BaseTestCase):
    def test_C2287530(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        text_file="TextFile"
        select_file="as2437"
        folder="S9100"
        select_save_as=['down','down','down']
        write_as2437_htm="as2437.htm" 
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_error_message="Extension change not permitted."
        verify_text_tool="App Studio - Edit as2437"
        verify_as2437_file_created="as2437"
        verify_msg_1="Step 01: Verify extension change permitted dialog been displayed"
        verify_msg_2="Step 02: Verify the Text Editor tab will be updated to show Edit 'as2437'"
        verify_msg_3="Step 03: Verify The Environments Tree will contain a new file 'as2437'"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, AS Framework folder, right click on 161337 and select Open In Text Editor
                    Click AS Menu and select Save As
                    Type as2437.htm
                    Click OK'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                  
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
               
        as_utilobj.select_component_by_right_click(right_click_item=text_file,click=component_locators.open_in_text_editor)
        time.sleep(sleep[1])
        
        as_utilobj.select_component_by_right_click(right_click_folder=folder,click=component_locators.refresh_descendants)
        time.sleep(sleep[0])
        
        as_utilobj.select_application_menu_options(send_keys=select_save_as)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(button=component_locators.ok_button,rename_file=write_as2437_htm)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Element(verify_error_message,verify_msg_1,available=True)
        time.sleep(sleep[0])
    
        '''Step 02: Click OK in App Studio message prompt
                    Click OK in the Save As dialog to accept the default name
                    Close Edit as2437 tab'''
        
        as_utilobj.select_any_dialog(button=component_locators.ok_button)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(button=component_locators.ok_button)
        time.sleep(sleep[0])
        
        as_utilobj.verify_active_tool(verify_text_tool,verify_msg_2)
        time.sleep(sleep[0])
         
        as_utilobj.close_canvas_item()
        time.sleep(sleep[2])
        
        as_utilobj.select_file(tree_item=select_file)
        time.sleep(sleep[0])
        
        as_utilobj.Verify_Element(verify_as2437_file_created,verify_msg_3,available=True)
        time.sleep(sleep[0])
        
        as_utilobj.select_component_by_right_click(right_click_item=select_file,click=component_locators.delete)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.yes_button)
        time.sleep(sleep[0])
        
if __name__=='__main__' :
    unittest.main()   