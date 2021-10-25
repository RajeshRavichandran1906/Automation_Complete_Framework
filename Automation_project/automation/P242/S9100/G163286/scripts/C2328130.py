'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328130'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328130_TestClass(AS_BaseTestCase):
    def test_C2328130(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_tree="Domains->S9100"
        select_0724RObj="0724RObj"
        select_161337="161337.fex"
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_dialog="Open File"
        verify_msg_1="Step 01: Verify open dialog is enabled and works when text editor is opens"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Navigate to Domains->CC - AppStudio->AS Framework 
                    Right click on 0724RObj.fex and select Open in Text Editor
                    Click the Open icon in the QAT
                    Select 161337.fex in the Open File dialog
                    Click OK'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(sleep[2])
                    
        as_utilobj.select_tree_view_pane_item(expand_tree) 
        time.sleep(sleep[3])
         
        as_utilobj.select_component_by_right_click(right_click_item=select_0724RObj,click=component_locators.open_in_text_editor)
        time.sleep(sleep[3])
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.open_button)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_1)
        
        as_utilobj.select_file(list_item=select_161337)
        time.sleep(sleep[1])
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(sleep[1])
        
        '''Step 02: Close 161337 tab
                    Close Edit 0724RObj.fex tab'''                   
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()  