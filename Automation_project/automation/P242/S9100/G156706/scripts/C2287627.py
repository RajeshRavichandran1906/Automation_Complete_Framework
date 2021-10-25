'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287627'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287627_TestClass(AS_BaseTestCase):
    def test_C2287627(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        select_data_server_repository="Data Servers"
        car_master_file="car.mas"
        folders=["S9100","ibisamp","baseapp"]
        sleep=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_msg_1="Step 01: Verify the Finish button is disabled"
        verify_msg_2="Step 02: Verify the Finish button is enabled"
        verify_msg_3="Step 03: Verify the Finish button is disabled"
        verify_msg_4="Step 04: Verify the Finish button is enabled"
        verify_msg_5="Step 05: Verify the Finish button is enabled"
        verify_msg_6="Step 06: Verify the Finish button is disabled"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New | Report
                    Click ibisamp folder'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(sleep[4])
                
        as_utilobj.select_component_by_right_click(right_click_folder=folders[0],click=component_locators.right_click_menu_new,click_sub_menu=component_locators.new_report)
        time.sleep(sleep[2])
         
        as_utilobj.select_file(tree_item=folders[1])
        time.sleep(sleep[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_1,button_item=component_locators.finish_button,disabled=True)
        time.sleep(sleep[0]) 
         
        '''Step 02: Click car.mas'''
          
        as_utilobj.select_file(list_item=car_master_file)
        time.sleep(sleep[0])

        as_utilobj.verify_element_using_ui(verify_msg_2,button_item=component_locators.finish_button,enabled=True)
        time.sleep(sleep[0]) 
        
        '''Step 03: Click ibinccen folder'''
          
        as_utilobj.select_file(tree_item=folders[2])
        time.sleep(sleep[0])
        
        as_utilobj.verify_element_using_ui(verify_msg_3,button_item=component_locators.finish_button,disabled=True)
        time.sleep(sleep[0]) 
          
        '''Step 04: Navigate to Data Servers, expand EDASERVE
                    Click ibisamp folder
                    Click car.mas'''
         
        as_utilobj.click_element_using_ui(tree_item=select_data_server_repository)
        time.sleep(sleep[0])
         
        as_utilobj.select_file(tree_item=folders[1])
        time.sleep(sleep[0])
         
        as_utilobj.select_file(list_item=car_master_file)
        time.sleep(sleep[0])
         
        as_utilobj.verify_element_using_ui(verify_msg_4,button_item=component_locators.finish_button,enabled=True)
        time.sleep(sleep[0]) 
         
        '''Step 05: Click baseapp folder
                    Click car.mas
                    Collapse EDASERVE'''
         
        as_utilobj.select_file(tree_item=folders[2])
        time.sleep(sleep[0])
         
        as_utilobj.select_file(list_item=car_master_file)
        time.sleep(sleep[0])
         
        as_utilobj.verify_element_using_ui(verify_msg_5,button_item=component_locators.finish_button,enabled=True)
        time.sleep(sleep[0]) 
         
        '''Step 06: Click AS Framework folder 
                    Click Cancel'''
         
        as_utilobj.select_file(tree_item=folders[1])
        time.sleep(sleep[0])
         
        as_utilobj.verify_element_using_ui(verify_msg_6,button_item=component_locators.finish_button,disabled=True)
        time.sleep(sleep[0]) 
         
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[0])
          
if __name__=='__main__' :
    unittest.main() 