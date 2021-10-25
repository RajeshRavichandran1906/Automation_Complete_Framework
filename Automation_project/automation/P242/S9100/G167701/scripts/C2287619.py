'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287619'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287619_TestClass(AS_BaseTestCase):
    def test_C2287619(self): 
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Domains, right click on Public->New->Report
                    Click ibisamp->car.mas
                    Click Finish'''

        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(4) 
        
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(2)

        '''Step 02: Double-click COUNTRY, CAR, DEALER_COST 
                    Click on AS menu->Save All
                    Click OK in the Save As dialog (to accept the default name and location)'''
        
        as_utilobj.click_element_using_ui(tree_item='COUNTRY')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tree_item='CAR')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tree_item='DEALER_COST')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(1)
         
        as_utilobj.select_application_menu_options(send_keys=['down','down','down','down'])
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Save As","Step 02: Verify: Extra 'Do you want to save the changes ...?' message after Save All")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)

if __name__=='__main__' :
    unittest.main()                