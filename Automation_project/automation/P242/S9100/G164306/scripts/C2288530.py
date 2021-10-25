'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288530'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288530_TestClass(AS_BaseTestCase):
    def test_C2288530(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click AS menu->Options
                    Click Document 
                    Preview settings, select Simulated Data radio button
                    Click OK'''
          
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
              
        as_utilobj.select_element_appstudio_options(list_item="Document",radio_button="23152")
        time.sleep(2)
      
        as_utilobj.select_any_dialog("OK")
          
        '''Step 02: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
          
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(5) 
        
        '''Step 03: Click on Report and draw on canvas 
                    Right click within report container and select New report
                    Navigate to ibisamp and double on car.mas
                    Double click on COUNTRY, CAR, RETAIL_COST
                    Close Document2_report1'''
        
        as_utilobj.drag_drop_component("Insert","Report",source_x=410,source_y=265,target_x=890,target_y=665)
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(click="New report")
        time.sleep(4)
        
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")   
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")      
        
        as_utilobj.click_element_using_ui(tree_item="CAR")      
          
        as_utilobj.click_element_using_ui(tree_item="RETAIL_COST")      
        
        as_utilobj.select_home_button(move_x=518,move_y=114)
        time.sleep(3)      
        
        '''Step 04: Click Yes for App Studio prompt save message'''
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step4_C2288530.png","Step 04: Verified simulated data been displayed in document canvas")
        
        '''Step 05: Close Document2 tab
                    Click No for App Studio prompt save message
                    Click AS menu->Options
                    Click "Reset All Options to Default"
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        '''Step 06: Click Document
                    Click OK'''
        
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
         
if __name__=='__main__' :
    unittest.main()            