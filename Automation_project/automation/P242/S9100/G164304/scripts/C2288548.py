'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288548'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288548_TestClass(AS_BaseTestCase):
    def test_C2288548(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on AS Menu->Options, click on Reporting
                    Uncheck "Display the field name"
                    Check "Display field titles"
                    Click OK'''
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="Reporting",check_box="20790")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(check_box="20791")
        time.sleep(2)
                      
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
        '''Step 02: Right click on AS Framework->New->Report
                    Select ibisamp->car.mas
                    Click Finish'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(3)
                             
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",send_keys=['down','down','right'],click="Report")
        time.sleep(1)
         
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(1)
        
        '''Step 03: Right click on Object inspector-> select Show Field List 
                    Hover the CAR field'''
        
        as_utilobj.select_home_button(move_x=400,move_y=829)
        
        as_utilobj.select_component_by_right_click(click="Show Field List")
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(text_click="(COUNTRY)")
        
        as_utilobj.Verify_Element("(COUNTRY)","Step 03: Verify that field titles is shown in Object Inspector",available=True)
        
        '''Step 04: Right click on Object Inspector-> select Show Field Tree
                    Click on AS Menu->Options, click on Reporting
                    Check "Display the field name"
                    UnCheck "Display field titles"'''
        
        as_utilobj.select_home_button(move_x=400,move_y=829)
        
        as_utilobj.select_component_by_right_click(click="Show Field Tree")
        time.sleep(3)
        
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
            
        as_utilobj.select_element_appstudio_options(list_item="Reporting",check_box="20790")
        time.sleep(2)
        
        as_utilobj.select_element_appstudio_options(check_box="20791")
        time.sleep(2)
                      
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 