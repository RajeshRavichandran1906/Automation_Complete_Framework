'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288283'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288283_TestClass(AS_BaseTestCase):
    def test_C2288283(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS menu->Options
                    Click HTML Page
                    In Grid Settings, uncheck Snap to Grid
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="HTML Page",check_box="15007")
        time.sleep(2)
                    
        as_utilobj.select_any_dialog("OK")
        
        '''Step 02: Right click AS Framework->New->HTML/Document
                    Click Next
                    Click Finish
                    Close HtmlPage1 tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
             
        as_wizard_obj.Html_Document_Wizard("Home","html_document","HTML Page")  
        time.sleep(15)
         
        as_utilobj.verify_picture_using_sikuli("step2_C2288283.png","Step 02: Verified that html page invoked in grid settings assigned")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        '''Step 03: Click on AS menu->Options
                    Click Reset All Options to Default
                    Click HTML Page 
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(button="OK")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()  