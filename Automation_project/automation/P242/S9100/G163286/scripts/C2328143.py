'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328143'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2328143_TestClass(AS_BaseTestCase):
    def test_C2328143(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Test case property variables'''
        
        environment_path="webfocus_environment"
        open_fex_file="Domains->S9100->AS-2260"
        ie_browser_classname="IEFrame"
        chrome_title="WebFOCUS Report - Google Chrome"
        firefox_title="MozillaWindowClass"
        
        '''Test case verification'''
        
        verify_browser_text=["COUNTRY","ENGLAND","FRANCE","ITALY","W GERMANY"]
        verify_browser_report="step2_C2328143.png"
        verify_msg_1="Step 01: Verify Report display in IE Browser"
        verify_msg_2="Step 02: Verify Report display in Chrome Browser"
        verify_msg_3="Step 03: Verify Report displayed in Firefox browser"
        
        '''Test script'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, AS Framework sub folder
                    Double click on AS-2260
                    Click on Run icon
                    Close WebFOCUS Report output browser tab'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item=component_locators.output_viewer_settings)
        time.sleep(2)
         
        as_utilobj.click_element_using_ui(list_item=component_locators.internet_explorer)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
              
        as_utilobj.select_tree_view_pane_item(open_fex_file) 
        time.sleep(5)
         
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(8)
          
        as_utilobj.Verify_Browser_Content(ie_browser_classname,verify_msg_1,item_list=verify_browser_text,browser_close=True)
        time.sleep(2)
          
        '''Step 02: Click AS menu->Options0
                    Click Output Viewer Settings
                    Select Chrome in Browser Setup list
                    Click OK
                    Click on Run icon'''
         
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item=component_locators.output_viewer_settings)
        time.sleep(2)
          
        as_utilobj.click_element_using_ui(list_item=component_locators.chrome)
        time.sleep(1)
          
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
         
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(8)
         
        as_utilobj.verify_google_browser(chrome_title,verify_msg_2,verify_image=verify_browser_report,browser_close=True)
        time.sleep(2)
         
        '''Step 03: Close WebFOCUS Report output browser tab 
                    Click AS menu->Options
                    Click Output Viewer Settings
                    Select Fire fox in Browser Setup list
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item=component_locators.output_viewer_settings)
        time.sleep(2)
         
        as_utilobj.click_element_using_ui(list_item=component_locators.firefox)
        time.sleep(1)
        
        as_utilobj.select_any_dialog(component_locators.ok_button)
        time.sleep(2)
        
        '''Step 04: Click on Run icon'''
        
        as_utilobj.click_element_using_ui(split_button=locators.run_splitbutton)
        time.sleep(10)
        
        as_utilobj.Verify_Browser_Content(firefox_title,verify_msg_3,verify_browser=True,browser_close=True)
        time.sleep(6)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
        
        as_utilobj.select_element_appstudio_options(list_item=component_locators.general_category,button=component_locators.reset_button)
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  