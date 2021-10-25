'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288188'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288188_TestClass(AS_BaseTestCase):
    def test_C2288188(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, navigate to CC - AppStudio 
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
         
        '''Step 02: Double click on COUNTRY'''
         
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli("step2_C2288188.png","Step 02: Verified field ribbon is activated")
        time.sleep(1)
         
        '''Step 03: Click AS Main menu -> Options 
                    Uncheck "Activate Field ribbon tab when selecting a field on the report canvas"
                    Click OK 
                    Click on empty space on Report Canvas'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
         
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(2)
                    
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="205")
        time.sleep(2)
            
        as_utilobj.select_any_dialog("OK")
 
        as_utilobj.select_home_button(move_x=1100,move_y=320)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli("step3_C2288188.png","Step 03: Verified layout ribbon is activated")
        time.sleep(1)
         
        '''Step 04: Select COUNTRY column in canvas.'''
         
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli("step4_C2288188.png","Step 04: Verified layout ribbon is still activated")
        time.sleep(1)
         
        '''Step 05: Click AS Main menu -> Options 
                    Check "Activate Field ribbon tab when selecting a field on the report canvas"
                    Click OK
                    Click on COUNTRY column on Report Canvas'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(5)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
                   
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="205")
        time.sleep(2)

        as_utilobj.select_any_dialog("OK")
        
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")

        '''Step 06: Close Report3 tab
                    Click No for App Studio prompt message'''
        
        as_utilobj.close_canvas_item()
        time.sleep(1)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()   