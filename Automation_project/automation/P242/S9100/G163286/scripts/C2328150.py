'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328150'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328150_TestClass(AS_BaseTestCase):
    def test_C2328150(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        open_fex_file="Domains->S9100->AS-2260"
        select_car="CAR"
        
        '''Testcase verification'''
        
        verify_msg_1="Step 1.1: Verify Undo icons on the Quick Access Tool bar are disabled"
        verify_msg_2="Step 1.2: Verify Redo icons on the Quick Access Tool bar are disabled"
        verify_msg_3="Step 2.1: Verify Undo icons on the Quick Access Tool bar are enabled"
        verify_msg_4="Step 2.2: Verify Redo icons on the Quick Access Tool bar are disabled"
        verify_msg_5="Step 3.1: Verify field added above to report is removed and Redo button is now enabled"
        verify_msg_6="Step 3.2: Verify Undo button is now disabled"
        verify_msg_7="Step 4.1: Verify field removed in last step is added back to the report. Undo button is enabled"
        verify_msg_8="Step 4.2: Verify Redo is disabled."
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Close all files. Review the Undo/Redo icon on the QAT.'''
         
        as_utilobj.verify_element_using_ui(verify_msg_1,button_item=locators.undo_button,disabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_2,button_item=locators.redo_button,disabled=True)
        time.sleep(1)
         
        '''Step 02: Under As Framework subfolder, double click on AS-2260
                    Double click on CAR'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
               
        as_utilobj.select_tree_view_pane_item(open_fex_file) 
        time.sleep(5)
         
        as_utilobj.click_element_using_ui(tree_item=select_car)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_3,button_item=locators.undo_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,button_item=locators.redo_button,disabled=True)
        time.sleep(1)
        
        '''Step 03: Click the Undo icon in the Quick Access Tool bar.'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.undo_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_5,button_item=locators.undo_button,disabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_6,button_item=locators.redo_button,enabled=True)
        time.sleep(1)
        
        '''Step 04: Click the Redo icon in the Quick Access Tool bar.'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.redo_button)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui(verify_msg_7,button_item=locators.undo_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_8,button_item=locators.redo_button,disabled=True)
        time.sleep(1)
        
        '''Step 05: Close AS-2260* tab
                    Click No to App Studio saving prompt message'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(2)
    
if __name__=='__main__' :
    unittest.main()  