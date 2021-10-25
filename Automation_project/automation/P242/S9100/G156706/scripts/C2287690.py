'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287690'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators,as_uiautomation_mainpage_locators

class C2287690_TestClass(AS_BaseTestCase):
    def test_C2287690(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_initial_repository="Data Servers->EDASERVE->Applications->ibisamp"
        select_data_server_repository="ibisamp->cargraph.fex"
        master_files=["carinst.fex","carinst2.fex","carmgn.fex"]
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_carinst2_window="App Studio - carinst2.fex"
        verify_image_1="step1_C2287690.png"
        verify_image_2="step2_C2287690.png"
        verify_image_3="step3_C2287690.png"
        verify_image_4="step4_C2287690.png"
        verify_msg_1="Step 01: Verify Procedure Name value include correct path"
        verify_msg_2="Step 02: Verify Focus remains in Report Wizard Opening an existing procedure dialog. Procedure Name value include correct path"
        verify_msg_3="Step 03: Verify Procedure Name value include correct path"
        verify_msg_4="Step 04: Verify Procedure Name value include correct path"
        verify_msg_5="Step 05: Verify carinst.fex tab opens and Report tab opens under carinst.fex tab"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Under Home ribbon, click Report
                    Click Open Existing
                    Under EDASERVE->ibisamp, double click on cargraph.fex'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                  
        as_utilobj.select_tree_view_pane_item(select_initial_repository) 
        time.sleep(sleep[4])
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.report_button)
        time.sleep(sleep[2])
        
        as_utilobj.click_element_using_ui(button_item=True,name=component_locators.open_existing_File)
        time.sleep(sleep[2])
        
        as_utilobj.select_tree_view_pane_item(select_data_server_repository)
        time.sleep(sleep[2])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1)
        time.sleep(sleep[2])
        
        '''Step 02: Double click on carinst.fex
                    Double click on carinst2.fex
                    Double click on carmgn.fex'''
        
        as_utilobj.select_file(tree_item=master_files[0])
        time.sleep(sleep[2]) 
        
        as_utilobj.verify_picture_using_sikuli(verify_image_2,verify_msg_2)
        time.sleep(sleep[2])
        
        as_utilobj.select_file(tree_item=master_files[1])
        time.sleep(sleep[2])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_3,verify_msg_3)
        time.sleep(sleep[2])
        
        as_utilobj.select_file(tree_item=master_files[2])
        time.sleep(sleep[2])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_4,verify_msg_4)
        time.sleep(sleep[2])
        
        '''Step 03: Click on carinst2.fex 
                    Click Finish
                    Close carinst2.fex tab
                    Click No in App Studio prompt saving message'''
        
        as_utilobj.select_file(tree_item=master_files[1])
        time.sleep(sleep[2])
        
        as_utilobj.select_any_dialog(component_locators.finish_button)
        time.sleep(sleep[8])
        
        as_utilobj.verify_active_tool(verify_carinst2_window,verify_msg_5)
        time.sleep(sleep[1])
        
        as_utilobj.close_canvas_item()
        time.sleep(sleep[3])
        
        as_utilobj.select_any_dialog(component_locators.no_button)
        time.sleep(sleep[1])
          
if __name__=='__main__' :
    unittest.main() 