'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667285'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C6667285_TestClass(AS_BaseTestCase):
    def test_C6667285(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        '''Variables declared'''
        
        environment_path="webfocus_environment"
        select_repository="Domains"
        select_folders=["ibisamp","S9100"]
        files=["car.mas"]
        click_items=["Reporting","Report"]
        check_box_id=["20901"]
        dialog_buttons=["OK","OK"]  
        key_pattern_1=['down','down','right'] 
        sleep=[1,2,3,4,5,6,7,8,9] 
        verify_msg_1="Step 02: Verify that field tree in not expanded in Object inspector"
        verify_elements=["COUNTRY"]
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS Menu->Options, click on Reporting
                    Uncheck Expand field tree
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(sleep[0])
             
        as_utilobj.select_element_appstudio_options(list_item=click_items[0],check_box=check_box_id[0])
        time.sleep(sleep[0])
            
        as_utilobj.select_any_dialog(dialog_buttons[0])
        time.sleep(sleep[0])
        
        '''Step 02: Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[0])
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
          
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[1])
          
        as_utilobj.select_component_by_right_click(right_click_folder=select_folders[1],send_keys=key_pattern_1,click=click_items[1])
        time.sleep(sleep[0])
        
        as_utilobj.select_file_in_dialogs(dialog_buttons[1],tree_path=select_folders[0],select_file=files[0])
        time.sleep(sleep[2])
        
        as_utilobj.Verify_Element(verify_elements[0],verify_msg_1,unavailable=True)
        
        '''Step 03: Close Report4 tab
                    Click on AS Menu->Options, click on Reporting
                    Check Expand field tree
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(sleep[0])
             
        as_utilobj.select_element_appstudio_options(list_item=click_items[0],check_box=check_box_id[0])
        time.sleep(sleep[0])
            
        as_utilobj.select_any_dialog(dialog_buttons[0])
        time.sleep(sleep[0])
          
if __name__=='__main__' :
    unittest.main()  