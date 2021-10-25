'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288284'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288284_TestClass(AS_BaseTestCase):
    def test_C2288284(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS Menu and click Options, click OK
                    Click HTML Page
                    Under 'Form Type' select 'None' 
                    Click OK'''
          
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="HTML Page",radio_button="23512")
        time.sleep(2)
                       
        as_utilobj.select_any_dialog("OK")
         
        '''Step 02: Right click AS Framework->New->HTML/Document
                    Click Next
                    Click Finish
                    Click on Report and draw a report container on canvas
                    Right click within the report container and select "Import existing report"'''
                       
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
           
        '''Step 03: Click on Report and draw a report container on canvas
                    right click within the report container and select "Import existing report"
                    Navigate to CC - AppStudio-AS Files and double click on CarParm.fex'''
           
        as_utilobj.drag_drop_component("Components","Report",source_x=346,source_y=211,target_x=813,target_y=577)
        time.sleep(2)
           
        as_utilobj.select_component_by_right_click(click="Import existing report")
        time.sleep(2)
        
        as_utilobj.select_file_in_dialogs("OK",select_file="CarParm.fex")
        time.sleep(3)
           
        as_utilobj.Verify_Current_Dialog_Opens("New Parameters","Step 03: Verified that new parameters window opened for carparm.fex")
        time.sleep(4)
           
        '''Step 04: Click OK'''
           
        as_utilobj.select_any_dialog("OK")
        time.sleep(2)
           
        as_utilobj.verify_picture_using_sikuli("step4_C2288284.png","Step 04: Verified that carparm.fex been invoked in html canvas")
        time.sleep(1)
          
        '''Step 05: Click Run
                    Close HtmlPage output tab
                    Close HtmlPage1 tab 
                    Click No to App Studio saving prompt'''
         
        as_utilobj.click_element_using_ui(split_button="Run",send_keys=".")
        time.sleep(8)
        
        as_utilobj.Verify_Browser_Content("IEFrame","Step 5.1: Verified browser invoked",verify_browser=True)
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(button_item=True,id="Submit")
        time.sleep(2)
         
        as_utilobj.verify_picture_using_sikuli("step5_C2288284.png","Step 5.2: Verified that report displays in browser with one form")
        time.sleep(2)
         
        as_utilobj.Verify_Browser_Content("IEFrame","skip this message",browser_close=True)
        time.sleep(3)
         
        as_utilobj.close_canvas_item()
        time.sleep(1)
         
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
         
        '''Step 06: Click on AS menu->Options
                    Click Reset All Options to Default
                    Click HTML Page 
                    Click OK'''
 
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
          
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
         
        as_utilobj.select_any_dialog("OK")
        time.sleep(2)
    
if __name__=='__main__' :
    unittest.main()                