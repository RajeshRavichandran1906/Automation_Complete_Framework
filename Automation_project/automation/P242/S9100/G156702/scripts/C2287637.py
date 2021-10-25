'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287637'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_panels
import pyautogui as keys
from common.lib import as_utility

class C2287637_TestClass(AS_BaseTestCase):
    def test_C2287637(self):
        
        '''Create instance of object '''
        
        driver=self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panels_obj=as_panels.AS_Panels(driver)
    
        as_utilobj.select_home_button()
                
        '''Step 01: Sign in to WebFOCUS environment as admin
                    Right click on Domains->New Folder 
                    Right click on New Folder1, type ContextMenu, hit Enter 
                    Set Filter in Environments Tree to show Procedure Files''' 
                         
        as_panels_obj.environment_panel_file_filter(filter="Procedure Files")
                 
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                         
        '''Step 02: Expand CC - AppStudio>AS Files> 
                    Double click on AS-2994''' 
                 
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                                
        tree_path="Domains->S9100->AS-2994"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
                
        as_utilobj.verify_active_tool("App Studio - AS-2994","Step 02: Verified Procedure opens and user is placed in report canvas")
        time.sleep(2)
    
        '''Step 03: Click on Procedure View panel 
                    Double click the Define component in the Procedure View panel
                    Change the Define Field Name to MYPROFIT'''
              
        as_utilobj.select_home_button(move_x=-52,move_y=170)
                
        tree_path="Define"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
            
        as_utilobj.select_home_button()   
        as_utilobj.double_click_element_using_offset(793,350) 
        time.sleep(2)
        keys.typewrite("MYPROFIT")
        time.sleep(1)
              
        as_utilobj.verify_active_tool("App Studio - AS-2994*","Step 03: Verified - An asterisk is added to the tab of procedure AS-2994.fex")
        time.sleep(2)
                           
        '''Step 04: Click Save icon'''
                    
        as_utilobj.click_element_using_ui(button_item=True,name="Save")
        time.sleep(3)
             
        as_utilobj.verify_active_tool("App Studio - AS-2994","Step 04: Verified - The asterisk is removed from the tab of procedure AS-2994")
        time.sleep(2)
                                    
        '''Step 05: Click the Report tab'''
                    
        as_utilobj.select_home_button(move_x=-52,move_y=170)
                      
        tree_path="Report"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(2)
                   
        as_utilobj.click_element_using_ui(tree_item_select="MYPROFIT")
        time.sleep(4)
             
        as_utilobj.Verify_Element("MYPROFIT","Step 05: Verified that the define file has been updated to MYPROFIT",available=True)
                          
        '''Step 06: Right click on MYPROFIT->Edit Define Virtual Field, change the Define Field Name to BIGPROFIT'''
             
        as_utilobj.select_component_by_right_click(send_keys=['down','enter'])      
            
        as_utilobj.select_home_button()       
        as_utilobj.double_click_element_using_offset(793,350) 
        time.sleep(2)
            
        keys.typewrite("BIGPROFIT")
        time.sleep(1)
            
        as_utilobj.verify_active_tool("App Studio - AS-2994*","Step 06: Verified - An asterisk is added to the tab of procedure AS-2994.fex")
        time.sleep(2)
                           
        '''Step 07: Click on AS Menu->Save All'''
    
        as_utilobj.click_element_using_ui(button_item=True,name="Save All")
        time.sleep(1)
                
        '''Step 08: Click No to "All documents have been saved. Close all documents?" prompt'''
                
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
             
        as_utilobj.verify_active_tool("App Studio - AS-2994","Step 08: Verified - The asterisk is removed from the tab of procedure AS-2994")
        time.sleep(2)
            
        '''Step 09: Click the Report tab'''
            
        as_utilobj.select_home_button(move_x=-52,move_y=170)
                      
        tree_path="Report"
        as_utilobj.select_tree_view_pane_item(tree_path)
            
        as_utilobj.click_element_using_ui(tree_item_select="BIGPROFIT")
             
        as_utilobj.Verify_Element("BIGPROFIT","Step 09: Verified that the define file has been updated to BIGPROFIT",available=True)
            
        '''Step 10: Close Report Tab'''
            
        as_utilobj.select_component_by_right_click(send_keys=['down','enter']) 
           
        as_utilobj.select_home_button()   
        as_utilobj.double_click_element_using_offset(793,350) 
        time.sleep(2)
        keys.typewrite("PROFIT")
        time.sleep(1)
         
        as_utilobj.select_home_button(move_x=365,move_y=114)
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_panels_obj.environment_panel_file_filter(filter="All Files")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()