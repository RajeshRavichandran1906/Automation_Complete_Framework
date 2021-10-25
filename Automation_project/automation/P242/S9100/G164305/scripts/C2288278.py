'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288278'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288278_TestClass(AS_BaseTestCase):
    def test_C2288278(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Options
                    Click HTML Page
                    In Grid Settings, set Width to 0, set Height to 0
                    Click OK
                    Click on AS menu->Options->HTML Page'''
          
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="HTML Page",edit_element="15002",write="1")
        time.sleep(2)
          
        as_utilobj.select_element_appstudio_options(edit_element="15004",write="1")
        time.sleep(2)
          
        as_utilobj.select_any_dialog("OK")
         
        '''Step 02: Navigate to CC - AppStudio->AS Framework
                    Right click AS Framework->New->HTML/Document
                    Click Next
                    Click Finish'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
             
        as_wizard_obj.Html_Document_Wizard("Home","html_document","HTML Page")  
        time.sleep(10)
         
        as_utilobj.verify_picture_using_sikuli("step2_C2288278.png","Step 02: Verified that html page invoked in grid settings assigned")
        time.sleep(1)
        
        '''Step 03: Close HtmlPage1 tab
                    Click on AS menu->Options
                    Click Reset All Options to Default
                    Click HTML Page
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
          
if __name__=='__main__' :
    unittest.main()  