'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288187'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288187_TestClass(AS_BaseTestCase):
    def test_C2288187(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, navigate to CC - AppStudio and expand
                    Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
            
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(1)
            
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(1)
            
        '''Step 02: Double click on COUNTRY
                    Double click on SALES'''
           
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        time.sleep(1)
           
        as_utilobj.verify_picture_using_sikuli("step2_C2288187.png","Step 02: Verified Sort Down highlighted")
           
        as_utilobj.click_element_using_ui(tree_item="SALES")
        time.sleep(1)
           
        as_utilobj.verify_picture_using_sikuli("step3_C2288187.png","Step 03: Verified Aggregate is highlighted")
          
        '''Step 03l: Click AS Main menu -> Options 
                    Un-check "Set new lcolumn type based on metadata/surrounding fields" 
                    Click OK'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(5)
          
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(2)
                     
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="204")
        time.sleep(2)
             
        as_utilobj.select_any_dialog("OK")
          
        '''Step 04: Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(2)
          
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(2)
          
        '''Step 05: Double click on COUNTRY
                    Double click on SALES'''
          
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli("step5_C2288187.png","Step 05: Verified Detail highlighted")
          
        as_utilobj.click_element_using_ui(tree_item="SALES")
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli("step6_C2288187.png","Step 06: Verified Detail is highlighted")
               
        '''Step 06: Click AS Main -> Options 
                    Check "Set new column type based on metadata/surrounding fields" 
                    Click OK
                    Select Report3 tab
                    Double click CAR'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(12)
         
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(3)
                    
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="204")
        time.sleep(2)
            
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(tree_item="CAR")
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 07: Verified message prompt displayed to select sort\Details")
        time.sleep(1)
        
        '''Step 07: Click Cancel
                    Close Report3 tab
                    Click No for App Studio prompt message
                    Close Report4 tab
                    Click No for App Studio prompt message'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(12)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 