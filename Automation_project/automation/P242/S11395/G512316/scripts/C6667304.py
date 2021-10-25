'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667304'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C6667304_TestClass(AS_BaseTestCase):
    def test_C6667304(self):
        
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
         
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(1)
        
        '''Step 02: Double click on COUNTRY'''
        
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        
        '''Step 03: Click on the canvas where there is no column'''
        
        as_utilobj.select_home_button(move_x=1100,move_y=320)
        
        '''Step 04: Click AS Main menu -> Options 
                    Un-check the option "Activate Layout ribbon tab when no selection is made on the report canvas"
                    Click OK 
                    Double click CAR'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(10)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(2)
                   
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="206")
        time.sleep(2)

        as_utilobj.select_any_dialog("OK")
        
        as_utilobj.click_element_using_ui(tree_item="CAR")
        
        '''Step 05: Click on the canvas where there are no columns'''
        
        as_utilobj.select_home_button(move_x=1100,move_y=320)
        time.sleep(2)
        
        as_utilobj.verify_element_using_ui("Step 05: Verified that Report tab is activated instead of layout tab",tab_item_status="Home",active=True)
        time.sleep(2)
        
        '''Step 06: Click AS Main menu -> Options 
                    Check the option "Activate Layout ribbon tab when no selection is made on the report canvas"
                    Click OK
                    Select CAR column'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(2)
                   
        as_utilobj.select_element_appstudio_options(list_item="General",check_box="206")
        time.sleep(2)

        as_utilobj.select_any_dialog("OK")
        
        as_utilobj.click_element_using_ui(tree_item="CAR")
        
        as_utilobj.verify_element_using_ui("Step 06: Verified that Field tab is activated",tab_item_status="Field",active=True)
        time.sleep(2)
        
        '''Step 07: Click on the canvas where there are no columns'''
        
        as_utilobj.select_home_button(move_x=1100,move_y=320)
        
        as_utilobj.verify_element_using_ui("Step 07: Verified that layout tab is activated",tab_item_status="Layout",active=True)
        time.sleep(2)
        
        '''Step 08: Close Report3 tab
                    Click No for App Studio prompt message'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  