'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328138'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328138_TestClass(AS_BaseTestCase):
    def test_C2328138(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        open_carinst_file="Data Servers->EDASERVE->Applications->ibisamp->carinst.fex"
        enable_message_viewer_on=['down','down']
        enable_message_viewer_off=['down']
        refresh_folder="S9100"
        ie_browser_classname="IEFrame"
        run_drop_down=[30,10]
        
        '''Testcase verification'''
        
        verify_browser_text=["0 NUMBER OF RECORDS IN TABLE=       18  LINES=     18","0 HOLDING HTML FILE ON PC DISK ..."]
        verify_webfocus_report="WebFOCUS Report"
        verify_msg_1="Step 01: Verify Report is executed and displays in browser/viewer."
        verify_msg_2="Step 02: Messages - "
        verify_msg_3="Step 03: Verify messages are not displayed after message viewer OFF"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
         
        '''Step 01: In Environments Tree, ibisamp applications, double click on carinst.fex
                    Click on drop down icon next to the run icon and select Message Viewer ON
                    Click Run
                    Close WebFOCUS Report tab'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
             
        as_utilobj.select_tree_view_pane_item(open_carinst_file) 
        time.sleep(8)
          
        as_utilobj.select_component_by_right_click(right_click_folder=refresh_folder,click=component_locators.refresh_descendants)
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.run_splitbutton,x=run_drop_down[0],y=run_drop_down[1],send_keys=enable_message_viewer_on)
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(5)
          
        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_1,verify_pane=verify_webfocus_report)
        time.sleep(1)
          
        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_2,item_list=verify_browser_text,browser_close=True)
        time.sleep(1)
          
        '''Step 02: Click on drop down icon next to the run icon and select Message Viewer OFF
                    Click Run
                    Close WebFOCUS Report tab
                    Close carinst.fex tab
                    Collapse Data Servers'''
          
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.run_splitbutton,x=run_drop_down[0],y=run_drop_down[1],send_keys=enable_message_viewer_off)
        time.sleep(2)
         
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(5)
         
        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_3,verify_pane=verify_webfocus_report,browser_close=True)
        time.sleep(5)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
    
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main() 