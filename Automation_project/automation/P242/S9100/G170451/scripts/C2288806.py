'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288806'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators
import uiautomation as automation

class C2288806_TestClass(AS_BaseTestCase):
    def test_C2288806(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_repository="Domains->S9100"
        edit_box_id="1516" 
        press_c="c" 
        wait_time=[1,2,3,4,5,6,7,8,9] 
        delete_key="delete"
        
        '''Testcase verification'''
        
        verify_image_1="step1_C2288806.png"
        verify_element="list_dropdown"
        verify_msg_1="Step 01: Verify list of files starting with same charectors ('wf') displays the below input box"
        verify_msg_2="Step 02: Verify the drop down box closes hiding the search results"
        verify_msg_3="Step 03: Verify the drop down box opens and displays the last results for your last search ('wf')"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, expand CC- AppStudio and select AS Framework
                    On Quick Access Tool bar, click on Open
                    In File name, type w'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(wait_time[2])
                  
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(wait_time[3])
                  
        as_utilobj.select_tree_view_pane_item(select_repository) 
        time.sleep(wait_time[3])
        
        as_utilobj.click_element_using_ui(button_item=True,name=locators.open_button)
        time.sleep(wait_time[1])
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_box_id,write=press_c) 
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_1)
        time.sleep(wait_time[1])
        
        '''Step 02: Click the down arrow for the File name field'''
        
        automation.EditControl(AutomationId=edit_box_id).Click(ratioX=394, ratioY=10)
        time.sleep(wait_time[1]) 
        
        as_utilobj.Verify_Element(verify_element,verify_msg_2,unavailable=True)
        time.sleep(wait_time[1])
        
        '''Step 03: Delete wf from File name input box and click the down arrow'''
        
        as_utilobj.click_element_using_ui(edit_element=True,id=edit_box_id,send_key=delete_key) 
        time.sleep(wait_time[1])
        
        automation.EditControl(AutomationId=edit_box_id).Click(ratioX=394, ratioY=10)
        time.sleep(wait_time[1])
        
        as_utilobj.verify_picture_using_sikuli(verify_image_1,verify_msg_3)
        time.sleep(wait_time[1])
        
        '''Step 04: While search results box is open, delete the pr characters in File name field 
                    Click Cancel'''
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(wait_time[1])    
        
if __name__=='__main__' :
    unittest.main()      