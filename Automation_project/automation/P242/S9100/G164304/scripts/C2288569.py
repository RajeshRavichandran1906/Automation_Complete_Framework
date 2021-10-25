'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288569'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import uiautomation as automation

class C2288569_TestClass(AS_BaseTestCase):
    def test_C2288569(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains"
        select_folders=["ibisamp","S9100"]
        files=["table2.ftp","car.mas"]
        browse_button_id="20827"
        edit_element_id=["1148","20826"]
        file_name="table2.ftp" 
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_image_1="step3_C2288569.png"
        verify_image_2="step4_C2288569.png"
        verify_msg_2="Step 03: Verify page number content in Report Canvas"
        verify_msg_3="Step 04: Verify syntax: Page No < "
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS Menu->Options, click on Reporting
                    Click on pushbutton Browse for Default Report Template'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(sleep[0])
                      
        as_utilobj.select_element_appstudio_options(list_item=component_locators.reporting_category)
        time.sleep(sleep[0])
        
        as_utilobj.click_element_using_ui(button_item=True,id=browse_button_id)
        time.sleep(sleep[0])
        
        '''Step 02: In Open dialog box, select table2.ftp file-> Open'''
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_element_id[0],write=file_name)
        time.sleep(sleep[0])
    
        automation.SendKey(automation.Keys.VK_RETURN, waitTime=2)
        time.sleep(sleep[0])
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_element_id[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(sleep[0])
        
        '''Step 03: Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[0])
                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
                
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[1],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(sleep[0])
              
        as_utilobj.select_file_in_dialogs(component_locators.finish_button,tree_path=select_folders[0],select_file=files[1])
        time.sleep(sleep[5])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_2)
        time.sleep(sleep[0])
        
        '''Step 04: In Object Inspector, click on Source tab'''
    
        as_utilobj.click_element_using_ui(tab_item=locators.source_view)
        time.sleep(sleep[2])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_3)
        time.sleep(sleep[1])
        
        '''Step 05: Close Report4 tab 
                    Click on AS Menu->Options
                    Click on "Reset All Options to Default"
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[3])
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(sleep[0])
                    
        as_utilobj.select_element_appstudio_options(list_item=component_locators.general_category,button=component_locators.reset_button)
        time.sleep(sleep[0]) 
                
        as_utilobj.select_any_dialog(locators.ok_button)
        time.sleep(sleep[0])  
        
if __name__=='__main__' :
    unittest.main()