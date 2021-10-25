'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287647'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287647_TestClass(AS_BaseTestCase):
    def test_C2287647(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Detail, right-click Domains->S9100 and select New | Procedure
                    Click Procedure View panel, right-click top-level folder and select New ... | Define'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"               
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)  
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Procedure")
        time.sleep(3)
          
        as_utilobj.select_home_button(move_x=-52,move_y=171)
        time.sleep(1)
                     
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Define")  
        time.sleep(3)
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source","Step 1.1: Verify Select Data Source dialog opens.")
        time.sleep(1)
        
                   
        as_utilobj.verify_picture_using_sikuli("step1_C2287647.png","Step 1.2: The OK button is disabled. The file name field is empty. The Public folder is selected in the left tree.")
        time.sleep(1)
                   
        '''Step 02: Click on ibisamp in the left tree'''
         
        as_utilobj.select_file(tree_item="ibisamp")
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli("step2_C2287647.png","Step 02: Verify master files displayed inside the file list when ibisamp selected")
        time.sleep(2)
         
        '''Step 03: Select car.mas in the right-tree'''
         
        as_utilobj.select_file(list_item="car.mas")
        time.sleep(1)
          
        as_utilobj.verify_picture_using_sikuli("step3_C2287647.png","Step 03: Verify OK button becomes enabled and file name field is populated with car.mas.")
        time.sleep(2)
         
        '''Step 04: Navigate to Domains>Public>Proceduren>EDASERVE Applications>baseapp in the left tree'''
         
        as_utilobj.select_file(tree_item="baseapp")
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli("step1_C2287647.png","Step 04: Verify OK button becomes disabled and file name field is cleared")
        time.sleep(2)
          
        '''Step 05: Click Cancel to close the Select Data Source dialog
                    Click X on the proceduren tab to close'''
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)  
         
        '''Step 06: Navigate to localhost from Environments Detail panel, expand Data Servers>EDASERVE>Applications'''
         
        as_utilobj.select_tree_view_pane_item("Data Servers->EDASERVE->Applications") 
        time.sleep(2) 
        
        '''Step 07: Right-click on baseapp and select New->Report'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="Report")
        time.sleep(3)
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source","Step 6.1: Verify Select Data Source dialog opens.")
        time.sleep(1)
                   
        as_utilobj.verify_picture_using_sikuli("step6_C2287647.png","Step 6.2: Verify OK button is disabled. The file name field is empty. The baseapp folder is selected in the left tree.")
        time.sleep(1)
         
        '''Step 08: Double-click ibisamp in the left tree
                    Select car.mas in the right tree'''
        
        as_utilobj.select_file(tree_item="ibisamp")
        time.sleep(1)
        
        as_utilobj.select_file(list_item="car.mas")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step8_C2287647.png","Step 08: Verify Finish button becomes enabled; the file name field is populated with car.mas")
        time.sleep(2)
        
        '''Step 09: Select baseapp in the left tree
                    Click Cancel to close the Select Data Source dialog'''
         
        as_utilobj.select_file(tree_item="baseapp")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step6_C2287647.png","Step 09: Verify Finish button becomes disabled, and the filename field is cleared.")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()