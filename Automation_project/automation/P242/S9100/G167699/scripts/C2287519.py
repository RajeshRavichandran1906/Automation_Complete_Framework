'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287519'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators

class C2287519_TestClass(AS_BaseTestCase):
    def test_C2287519(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        component_locators=as_components_ui_locators.ASComponentsLocators()
    
        '''Testcase property variables'''
        
        webfocus_env_path="webfocus_environment"
        folder_path="Domains->S9100"
        base_folder="S9100"
        car_master_file_path="Data Servers->EDASERVE - EDASERVE->Applications->ibisamp"
        
        '''Testcase verification'''
        
        verify_search_path_impact_analyse_result="step1_C2287519.png"
        verify_msg_1="Step 01: Verify Impact Analysis' Search Path List is 1 column"
        
        '''Testscript'''
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click on AS Framework and select Impact Analysis
                    Select Data Servers->EDASERVE->Applications->ibisamp
                    Double click on car.mas 
                    Close Impact Analysis tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,webfocus_env_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_tree_view_pane_item(folder_path)
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder=base_folder,click=component_locators.impact_analysis)                                         
        time.sleep(2)
        
        as_utilobj.select_file_in_dialogs(component_locators.ok_button,tree_path=car_master_file_path,select_file="car.mas")
        time.sleep(5)
        
        as_utilobj.verify_picture_using_sikuli(verify_search_path_impact_analyse_result,verify_msg_1)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
             
if __name__=='__main__' :
    unittest.main()