'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667286'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C6667286_TestClass(AS_BaseTestCase):
    def test_C6667286(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains"
        select_folders=["ibisamp","S9100"]
        files=["car.mas"]
        click_items=["Reporting","Report","COUNTRY","CAR","Source","Design","No"]
        radio_button_id=["199"]
        dialog_buttons=["OK","OK"]  
        key_pattern_1=['down','down','right'] 
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify that Qualified field name selected by default for Authoring mode:"
        verify_msg_2="Step 03: Verify syntax in report canvas matches Qualified fieldname settings"
        verify_image_1="step3_C6667286.png"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS Menu->Options, click on Reporting
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(sleep[0])
             
        as_utilobj.select_element_appstudio_options(list_item=click_items[0])
        time.sleep(sleep[0]) 
        
        as_utilobj.verify_element_using_ui(verify_msg_1,radio_button_id=radio_button_id[0])
        
        as_utilobj.select_any_dialog(dialog_buttons[0])
        time.sleep(sleep[0])
        
        '''Step 02: Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish
                    Double click on COUNTRY 
                    Double click on CAR'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[0])
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
          
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
          
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[1],send_keys=key_pattern_1,click=click_items[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_file_in_dialogs(dialog_buttons[1],tree_path=select_folders[0],select_file=files[0])
        time.sleep(sleep[2])
        
        as_utilobj.click_element_using_ui(tree_item=click_items[2])
        
        as_utilobj.click_element_using_ui(tree_item=click_items[3])
        
        '''Step 03: In Object Inspector click on Source tab'''
        
        as_utilobj.click_element_using_ui(tab_item=click_items[4])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_2)
        
        '''Step 04: Click on Design tab
                    Close Report4 tab
                    Click No in App Studio prompt for saving'''
        
        as_utilobj.click_element_using_ui(tab_item=click_items[5])
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog(click_items[6])
        
if __name__=='__main__' :
    unittest.main()    