'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288810'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import pyautogui as keys

class C2288810_TestClass(AS_BaseTestCase):
    def test_C2288810(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        files=["160526009.fex","BarChart.htm","TextFile.txt"]
        down_key='down'
        key_pattern_1=['down','enter']
        key_pattern_2=['down','down','down','down','down','down','down','down','down','down','enter']
        wait_time=[1,2,3,4,5,6,7,8,9] 
        
        '''Testcase verification'''
        
        verify_fex_file="step1_C2288810.png"
        verify_html_file="step2_C2288810.png"
        verify_txt_file="step3_C2288810.png"
        verify_msg_1="Step 01: Verify Inspect the file information displayed at the bottom left of the window for .fex file"
        verify_msg_2="Step 02: Verify Inspect the file information displayed at the bottom left of the window for .html file"
        verify_msg_3="Step 03: Verify Inspect the file information displayed at the bottom left of the window for .txt file"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu and click on Open
                    Select 161337.fex in the detail pane.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[3])
                  
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(wait_time[3])
        
        as_utilobj.select_application_menu_options(send_keys=down_key)
        time.sleep(wait_time[1])
        
        as_utilobj.select_file(list_item=files[0])
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_fex_file,verify_msg_1)
        time.sleep(wait_time[1])
        
        '''Step 02: Click on the drop arrow next to Procedure Files and select HtmlPage Files (*.htm)'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
        
        keys.press(key_pattern_1)
        time.sleep(wait_time[0])
        
        as_utilobj.select_file(list_item=files[1])
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_html_file,verify_msg_2)
        time.sleep(wait_time[0])
        
        '''Step 03: Click on the drop arrow next to Procedure Files and select Text Document (*.txt)
                    Click Cancel'''
        
        as_utilobj.click_element_using_ui(combo_box=component_locators.file_format_dropdown_id)
        time.sleep(wait_time[1])
        
        keys.press(key_pattern_2)
        time.sleep(wait_time[0])
        
        as_utilobj.select_file(list_item=files[2])
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_txt_file,verify_msg_3)
        time.sleep(wait_time[0])
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[0])
        
if __name__=='__main__' :
    unittest.main()