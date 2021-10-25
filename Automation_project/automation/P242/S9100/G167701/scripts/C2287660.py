'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287660'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels

class C2287660_TestClass(AS_BaseTestCase):
    def test_C2287660(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Options 
                    Select Output Viewer Settings
                    Select Chrome for Browser Setup
                    Click OK'''
            
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
              
        as_utilobj.select_element_appstudio_options(list_item="Output Viewer Settings",radio_button="1146")
        time.sleep(2)
            
        as_utilobj.select_element_appstudio_options(list_item="Chrome")
        time.sleep(2)
                        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
          
        '''Step 02: In Environments Tree, set Filter to Library Files
                    Navigate to CC - AppStudio->AS Report Caster
                    Double click on SimpleLibraryReportLIB
                    Close the Chrome browser'''
         
        as_panel_obj.environment_panel_file_filter(filter="Library Files")
        time.sleep(1)
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        tree_path="Domains->CC - AppStudio->AS Report Caster"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(15)
          
        as_utilobj.click_element_using_ui(tree_item="SimpleLibraryReportLIB")
        time.sleep(15)
          
        as_utilobj.verify_google_browser("WebFOCUS Report","Step 02: Verified SimpleLibraryReportLIB opens the Chrome",browser_close=True)
        time.sleep(20)
        
        '''Step 03: Click on AS menu->Options 
                    Select Output Viewer Settings
                    Select Firefox for Browser Setup
                    Click OK'''
         
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="Output Viewer Settings",radio_button="1146")
        time.sleep(2)
          
        as_utilobj.select_element_appstudio_options(list_item="Firefox")
        time.sleep(2)
                      
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        '''Step 04: Double click on SimpleLibraryReportLIB
                    Close the Firefox browser'''
         
        as_utilobj.click_element_using_ui(tree_item="SimpleLibraryReportLIB")
        time.sleep(25)
         
        as_utilobj.Verify_Browser_Content("MozillaWindowClass","Step 04: Verified SimpleLibraryReportLIB opens the Firefox",verify_browser=True,browser_close=True)
        time.sleep(15)

        '''Step 05: Click on AS menu->Options 
                    Select Output Viewer Settings
                    Select Internet Explorer for Browser Setup
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
           
        as_utilobj.select_element_appstudio_options(list_item="Output Viewer Settings",radio_button="1146")
        time.sleep(2)
         
        as_utilobj.select_element_appstudio_options(list_item="Internet Explorer")
        time.sleep(2)
                     
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 06: Double click on SimpleLibraryReportLIB
                    Close the Internet Explorer browser'''
        
        as_utilobj.click_element_using_ui(tree_item="SimpleLibraryReportLIB")
        time.sleep(25)
         
        as_utilobj.Verify_Browser_Content("IEFrame","Step 06: Verified SimpleLibraryReportLIB opens the Internet Explorer",verify_browser=True,browser_close=True)
        time.sleep(10)
        
        as_panel_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 