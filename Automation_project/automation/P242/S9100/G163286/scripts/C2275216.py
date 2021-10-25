'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/22875216'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation_keys

class C2275216_TestClass(AS_BaseTestCase):
    def test_C2275216(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_initial_repository="Domains->S9100"
        file_161337="161337"
        copy_text='{Ctrl}(C)'
        paste_text='{Ctrl}(V)'
        cut_text='{Ctrl}(X)'
        offset_values=[272,228]
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_text_file="App Studio - Edit 161337"
        verify_image_1="step2_C2275216.png"
        verify_image_2="step3_C2275216.png"
        verify_msg_1="Step 01: Verify 161337 fex file invoked in text editor"
        verify_msg_2="Step 02: Verify copied text been pasted in line 7"
        verify_msg_3="Step 03: Verify pasted line been cut"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: AS Framework folder, right click on 161337 and select Open in Text Editor'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(select_initial_repository) 
        time.sleep(sleep[3])
         
        as_utilobj.select_component_by_right_click(right_click_item=file_161337,click=component_locators.open_in_text_editor)
        time.sleep(sleep[2])
        
        as_utilobj.verify_active_tool(verify_text_file,verify_msg_1)
        time.sleep(sleep[1])
        
        '''Step 02: Press Ctrl+C
                    Place the cursor on line 7 and press Ctrl+V'''
        
        automation_keys.SendKeys((copy_text),interval=0.25,waitTime=1)
        time.sleep(1)
    
        as_utilobj.select_home_button(move_x=offset_values[0],move_y=offset_values[1])
        time.sleep(1)
        
        automation_keys.SendKeys((paste_text),interval=0.25,waitTime=1)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_2)
        time.sleep(2)
        
        '''Step 03: Highlight Line 7 and press Ctrl+X
                    Close Edit 161337* tab
                    Click No to App Studio saving prompt'''
        
        as_utilobj.select_home_button(move_x=offset_values[0],move_y=offset_values[1])
        time.sleep(1)
        
        automation_keys.SendKeys((cut_text),interval=0.25,waitTime=1)
        time.sleep(1)
        
        automation_keys.SendKey(automation_keys.Keys.VK_ENTER,waitTime=2)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_3)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()   