'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328157'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328157_TestClass(AS_BaseTestCase):
    def test_C2328157(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        open_report="Domains->S9100->Report1"
        select_car_field=[687,207]
        
        '''Testcase verification'''
        
        verify_car_field="CAR"
        verify_car_field_removed="CARR"
        verify_msg_1="Step 1.1: Verify Cut in the QAT are disabled"
        verify_msg_2="Step 1.2: Verify Copy in the QAT are disabled"
        verify_msg_3="Step 1.3: Verify Paste in the QAT are disabled"
        verify_msg_4="Step 2.1: Verify Cut in QAT are now enabled"
        verify_msg_5="Step 2.2: Verify copy in QAT are now enabled"
        verify_msg_6="Step 2.3: Verify paste is disabled"
        verify_msg_7="Step 3.1: Verify Cut in the QAT are enabled"
        verify_msg_8="Step 3.2: Verify Copy in the QAT are enabled"
        verify_msg_9="Step 3.3: Verify Paste in the QAT are enabled"
        verify_msg_10="Step 04: Verify the column is pasted"
        verify_msg_11="Step 05: Verify the pasted column is removed"
        
        '''Test script'''
        
        as_utilobj.select_home_button()
         
        '''Step 01: Close all files and review the cut, copy and paste icons in the QAT.'''
         
        as_utilobj.verify_element_using_ui(verify_msg_1,button_item=locators.cut_button,disabled=True)
        time.sleep(1)
          
        as_utilobj.verify_element_using_ui(verify_msg_2,button_item=locators.copy_button,disabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_3,button_item=locators.paste_button,disabled=True)
        time.sleep(1)
         
        '''Step 02: Double click on Report2
                    Select CAR column'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
              
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_tree_view_pane_item(open_report) 
        time.sleep(5)
        
        as_utilobj.select_home_button(move_x=select_car_field[0],move_y=select_car_field[1])
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_4,button_item=locators.cut_button,enabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_5,button_item=locators.copy_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_6,button_item=locators.paste_button,disabled=True)
        time.sleep(1)
        
        '''Step 03: Click the Copy icon in the QAT'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.copy_button)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_7,button_item=locators.cut_button,enabled=True)
        time.sleep(1)
         
        as_utilobj.verify_element_using_ui(verify_msg_8,button_item=locators.copy_button,enabled=True)
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui(verify_msg_9,button_item=locators.paste_button,enabled=True)
        time.sleep(1)
        
        '''Step 04: Click the Paste icon in the QAT bar'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.paste_button)
        time.sleep(2)
        
        as_utilobj.Verify_Element(verify_car_field,verify_msg_10,available=True)
        time.sleep(1)
        
        '''Step 05: While last column still selected, click the Cut icon in the QAT bar'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.cut_button)
        time.sleep(2)
        
        as_utilobj.Verify_Element(verify_car_field_removed,verify_msg_11,unavailable=True)
        time.sleep(1)
        
        '''Step 06: Close Report2 tab
                    Click No in App Studio prompt saving message'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()   