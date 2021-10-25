'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287737'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators

class C2287737_TestClass(AS_BaseTestCase):
    def test_C2287737(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        select_folder="S9100"
        sleep=[1,2,3,4,5,6,7,8,9] 
        offset_values=[447,293,875,669]
        
        '''Testcase verification'''
        
        verify_file_type_dropdown="step2_C2287737.png"
        verify_msg_1="Step 01: Verify image formats are displayed in dropdown"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New->HTML/Document, click Next, click Finish canvas
                    Click on Image and draw a place holder on canvas'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                     
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
          
        as_utilobj.select_component_by_right_click(right_click_folder=select_folder,click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_html_document)
        time.sleep(sleep[0])
          
        as_utilobj.select_any_dialog(component_locators.next_button)
        time.sleep(sleep[0])
          
        as_utilobj.select_any_dialog(component_locators.finish_button)
        time.sleep(sleep[0])
        
        as_utilobj.drag_drop_component(locators.components_tab,locators.image_button,source_x=offset_values[0],source_y=offset_values[1],target_x=offset_values[2],target_y=offset_values[3])
        time.sleep(sleep[0])
        
        '''Step 02: From the Open File dialog window, click on drop down
                    Click Cancel'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_type_dropdown)
        time.sleep(sleep[0])
        
        as_utilobj.verify_picture_using_sikuli(verify_file_type_dropdown,verify_msg_1)
        time.sleep(sleep[2])
        
        '''Step 03: Close HtmlPage1 tab
                    Click No for App Studio saving prompt'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_type_dropdown)
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[2])
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(sleep[0])
        
if __name__=='__main__' :
    unittest.main()