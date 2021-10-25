'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2304544'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2304544_TestClass(AS_BaseTestCase):
    def test_C2304544(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
         
        '''Step 01 : Procedure View check-box is checked by default (if you unchecked, check it now). Open existing report in your folder under Content'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Domains->S9100->Report1"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
          
        as_utilobj.verify_element_using_ui("Step 01: Verify Report Invoked successfully and Procedure view tab is showing on the left side of AS window",check_box="Procedure View") 
        time.sleep(2)
          
        '''Step 02 : Hover over the Procedure View tab on the left side of AS window'''
            
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
          
        as_utilobj.verify_element_using_ui("Step 02: Verify Procedure View expands (over tree pane) and reveals the components of the current report",pane_item="133") 
        time.sleep(2)
            
        '''Step 03 : Un-check Procedure View in the View section of Home ribbon'''
            
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
          
        as_utilobj.verify_element_using_ui("Step 03: Verify Procedure View tab disappears from left side of AS frame",check_box="Procedure View")
        time.sleep(2)
            
        '''Step 04 : Re-check Procedure View in the View section of Home ribbon'''
            
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
          
        as_utilobj.verify_element_using_ui("Step 04: Verify Procedure View tab reappears at the left side of AS window",check_box="Procedure View")
        time.sleep(2)
           
        '''Step 05 : Close Procedure view via X at the top right of Procedure View panel'''
          
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
          
        as_utilobj.verify_element_using_ui("Step 05: Verify Procedure View panel closes and Procedure View in Home ribbon is unchecked",check_box="Procedure View")
        time.sleep(2)
            
        '''Step 06 : Close the report, then repeat above steps with a Chart instead of report'''
           
        as_utilobj.close_canvas_item()
        time.sleep(4)
         
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
        
        tree_path="ChartParm"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(12)
        
        '''Step 07 : Hover over the Procedure View tab on the left side of AS window'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_home_button(move_x=-53,move_y=83)
        time.sleep(4)
        
        as_utilobj.verify_element_using_ui("Step 07: Verify Procedure View expands (over tree pane) and reveals the components of the current chart",pane_item="133") 
        time.sleep(3)
        
        '''Step 08: Recheck Procedure View in Home ribbon and close chart.'''
        
        as_utilobj.double_click_element(driver.find_element_by_name("Home"))
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(check_box=True,name="Procedure View")
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 08: Verify Procedure View tab reappears at the left side of AS window and disabled once the chart been closed",check_box="Procedure View")
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(4)
        
if __name__=='__main__' :
    unittest.main()  