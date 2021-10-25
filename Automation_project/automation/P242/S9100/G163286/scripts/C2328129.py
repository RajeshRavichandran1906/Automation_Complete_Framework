'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328129'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328129_TestClass(AS_BaseTestCase):
    def test_C2328129(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        expand_tree_till_ibisamp="Data Servers->EDASERVE->Applications->ibisamp"
        select_cargraph="cargraph.fex"
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_dialog="Open File"
        verify_image_1="step2_C2328129.png"
        verify_msg_1="Step 01: Verify Open file dialog opens with ibisamp as default location, Procedure Files as default type"
        verify_msg_2="Step 02: Verify Drop down for file types shows"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Under Data Servers>EDASERV>Applications-ibisamp
                    Select cargraph.fex and click the Open icon in the QAT'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(expand_tree_till_ibisamp) 
        time.sleep(sleep[3])
        
        as_utilobj.select_file(tree_item=select_cargraph)
        time.sleep(sleep[1])
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.open_button)
        time.sleep(sleep[1])
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_dialog,verify_msg_1)
        time.sleep(sleep[1])
        
        '''Step 02: Click on drop down next to Procedure Files
                    Click on drop down next to Procedure Files again
                    Click Cancel in Open File dialog
                    Collapse Data Servers'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(sleep[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_2)
        time.sleep(sleep[1])
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(sleep[1])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(sleep[1])
        
if __name__=='__main__' :
    unittest.main()  