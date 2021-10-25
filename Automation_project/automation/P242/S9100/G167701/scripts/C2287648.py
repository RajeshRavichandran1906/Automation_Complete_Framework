'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287648'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287648_TestClass(AS_BaseTestCase):
    def test_C2287648(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Select a Configured Environments
                    Click on AS menu->Options 
                    Select Output Viewer Settings, select Chrome for Browser Setup
                    In Navigation Options, select "Run in new window/tab" radio button
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="Output Viewer Settings",radio_button="1146")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(list_item="Chrome")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 02: In Environments Tree, select Domains>Public
                    Click WebFOCUS Administration drop down arrow
                    Select WebFOCUS Administration Console
                    Close the Administration Console tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->Public"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 02: Verified the WebFOCUS Administration Console opens in an IE browser and is positioned at the Welcome page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 03: Click WebFOCUS Administration drop down arrowl
                    Select Reporting Server Console (If the reporting server is running with security on, enter valid credentials)
                    Close the WebFOCUS..... tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 03: Verified the Reporting Server Console opens in IE at the Applications tab",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 04: Click WebFOCUS Administration drop down arrow
                    Select BI Portal
                    Close WebFOCUS Home tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 04: Verified the WebFOCUS BI Portal opens in an IE browser and is positioned at the welcome page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 05: Click WebFOCUS Administration drop down arrow
                    Select Deferred Status
                    Close the Deferred Report Status tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 05: Verified the Deferred Report Status window opens in IE",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 06: Click WebFOCUS Administration drop down arrow
                    Select ReportCaster Console
                    Close the Report Caster Status tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 06: Verified Report Caster Status opens in IE at Server Status page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 07: Click WebFOCUS Administration drop down arrow
                    Select Session Viewer
                    Close the admin..... tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 07: Verified IE opens at admin Session Viewer",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 08: In Environments, Domains, right-click on Public and select Upload Data
                    Close WebFOCUS...Server tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
              
        as_utilobj.select_component_by_right_click(right_click_folder="Public",click="Upload Data")
        time.sleep(1)  
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 08: Verified IE opens at Upload page",verify_browser=True,browser_close=True)
        time.sleep(4) 
        
        '''Step 09: Click on AS menu->Options 
                    Select Output Viewer Settings, select Firefox for Browser Setup
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="Output Viewer Settings",radio_button="1146")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(list_item="Firefox")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 10: Click WebFOCUS Administration drop down arrow
                    Select WebFOCUS Administration Console
                    Close the Administration Console tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 09: Verified the WebFOCUS Administration Console opens in an IE browser and is positioned at the Welcome page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 11: Click WebFOCUS Administration drop down arrow
                    Select Reporting Server Console (If the reporting server is running with security on, enter valid credentials)
                    Close the WebFOCUS..... tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 10: Verified the Reporting Server Console opens in IE at the Applications tab",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 12: Click WebFOCUS Administration drop down arrow
                    Select BI Portal
                    Close WebFOCUS Home tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 12: Verified the WebFOCUS BI Portal opens in an IE browser and is positioned at the welcome page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 13: Click WebFOCUS Administration drop down arrow
                    Select Deferred Status
                    Close the Deferred Report Status tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 13: Verified the Deferred Report Status window opens in IE",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 14: Click WebFOCUS Administration drop down arrow
                    Select ReportCaster Console
                    Close the Report Caster Status tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 14: Verified Report Caster Status opens in IE at Server Status page",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 15: Click WebFOCUS Administration drop down arrow
                    Select Session Viewer
                    Close the admin..... tab'''
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=['down','down','down','down','down','down','down','enter'])
        time.sleep(2)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 15: Verified IE opens at admin Session Viewer",verify_browser=True,browser_close=True)
        time.sleep(4)
        
        '''Step 16: In Environments, Domains, right-click on Public and select Upload Data
                    Close WebFOCUS...Server tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
              
        as_utilobj.select_component_by_right_click(right_click_folder="Public",click="Upload Data")
        time.sleep(1)  
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 16: Verified IE opens at Upload page",verify_browser=True,browser_close=True)
        time.sleep(4) 
        
        '''Step 17: Click on AS menu->Options 
                    Click "Reset All Options to Default"
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()         