'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288532'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_wizard

class C2288532_TestClass(AS_BaseTestCase):
    def test_C2288532(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj=as_wizard.AS_Wizard_Windows(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click AS menu->Options
                    Click Document
                    Preview settings, uncheck Reports and Charts Preview
                    Click OK'''
            
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
                  
        as_utilobj.select_element_appstudio_options(list_item="Document",check_box="23026")
        time.sleep(2)
          
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
            
        '''Step 02: In Environments Tree, right click on AS Framework->New->HTML/Document
                    Select Document (PDF, Excel...) File Type
                    Click Next, click Finish
                    Click on Report and draw on canvas, click on canvas
                    Click on Chart and draw on canvas'''
            
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
           
        as_utilobj.drag_drop_component("Insert","Report",source_x=440,source_y=252,target_x=950,target_y=520)
        time.sleep(2)
            
        as_utilobj.select_home_button(move_x=970,move_y=370)
        time.sleep(3)
            
        as_utilobj.drag_drop_component("Insert","Chart",source_x=440,source_y=623,target_x=950,target_y=935)
        time.sleep(2)
            
        as_utilobj.select_home_button()
        time.sleep(1)
            
        as_utilobj.verify_picture_using_sikuli("step2_C2288532","Step 02: Verified report and chart component added to document canvas")
        time.sleep(1)
           
        '''Step 03: Right click within report container and select "Reference existing procedure"
                    Double click on SimpleReportForChart.fex
                    Right click within chart container and select "New chart"
                    Navigate to ibisamp
                    Double click on car.mas'''
          
        as_utilobj.select_home_button(move_x=600,move_y=347)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(click="Reference existing procedure")
        time.sleep(2)

        as_utilobj.select_file(list_item="SimpleReportForChart.fex")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(2)
         
        as_utilobj.select_home_button(move_x=600,move_y=740)
        time.sleep(2)
          
        as_utilobj.select_component_by_right_click(click="New chart")
        time.sleep(2)
        
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")  
        time.sleep(15)
         
        '''Step 04: Double click on COUNTRY, RETAIL_COST
                    Click on HOME tab and select Active Report from Drop down
                    Close Document2_chart1 tab 
                    Click Yes to AppStudio prompt message'''
        
        as_utilobj.click_element_using_ui(text_double_click="COUNTRY")  
        time.sleep(3)    
        
        as_utilobj.click_element_using_ui(text_double_click="RETAIL_COST") 
        time.sleep(2) 
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step4_C2288532.png","Step 04: Verified that chart and report does not display preview")
        time.sleep(3)
         
        '''Step 05: Close Document2 tab
                    Click AS menu->Options
                    Click Reset All Options to Default
                    Click OK'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
        
        as_utilobj.select_element_appstudio_options(list_item="General",button="Reset All Options to Default")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(2)
                   
if __name__=='__main__' :
    unittest.main()   