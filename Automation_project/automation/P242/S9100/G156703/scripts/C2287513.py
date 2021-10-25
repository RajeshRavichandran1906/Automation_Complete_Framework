'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287513'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import pyautogui as keys
from common.lib import as_utility
from common.pages import as_wizard

class C2287513_TestClass(AS_BaseTestCase):
    def test_C2287513(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj= as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
         
        '''Step 01: Click on AS menu->Options 
                    Click HTML Page
                    Set Record limit for reports to 1
                    Click OK'''
               
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
                         
        as_utilobj.select_element_appstudio_options(list_item="Document",edit_element="23137",write="1")
        time.sleep(2)
                 
        as_utilobj.select_any_dialog("OK")
                   
        '''Step 02: Domains, select Public folder, click on HTML /Document, click Next, click Finish
                    Click on Report component and draw on canvas
                    Right click within report component->New report
                    Click Cancel at Open File window'''
                
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                 
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
          
        as_wizard_obj.Html_Document_Wizard("Home","html_document","HTML Page")  
        time.sleep(2)
             
        '''Click on Report component and draw on canvas'''
                    
        as_utilobj.drag_drop_component("Components","Report",source_x=346,source_y=211,target_x=813,target_y=577)
        time.sleep(1)
       
        as_utilobj.select_component_by_right_click(send_keys=['down','enter'])
        time.sleep(2)
           
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(3)
                              
        '''Step 03: Click Yes at message prompt to use the text editor and type the following in the text editor:
                    TABLE FILE WF_RETAIL
                    PRINT COGS_LOCAL
                    END 
                    Close HtmlPage1_report1'''
           
        as_utilobj.select_any_dialog("Yes") 
           
        keys.typewrite("TABLE FILE WF_RETAIL", interval=0.25)
        time.sleep(2)
        keys.press("enter")
        time.sleep(1)
        keys.typewrite("PRINT COGS_LOCAL", interval=0.25)
        time.sleep(2)
        keys.press("enter")
        time.sleep(1)
        keys.typewrite("END", interval=0.25)
        time.sleep(2)
            
        keys.hotkey("ctrl","s")
        time.sleep(10)
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(7)
          
        as_utilobj.close_canvas_item()
        time.sleep(6)
        
        as_utilobj.verify_picture_using_sikuli("step3_C2287513.png","Step 03: Verify that HTML Page preview respect record limit set in AS Options:HTML Page")
        time.sleep(1)
        
        '''Step 04: Close Htmlpag1 without saving
                    Click on AS menu->Options
                    Click "Reset All Options to Default" 
                    Click HTML Page
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)

        as_utilobj.select_any_dialog("No")   
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(options=True)
        
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(button="OK")
        time.sleep(2)
        
        print("Step 04: Verified - Resetted All Options to Default in HTML page") 
        time.sleep(2) 
        
if __name__=='__main__' :
    unittest.main() 