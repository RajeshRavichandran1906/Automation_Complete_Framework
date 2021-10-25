'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287641'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys_1

class C2287641_TestClass(AS_BaseTestCase):
    def test_C2287641(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
         
        '''Step 01: Right-click Domains>Public and select New
                    Right-click Domains>Public and select New | Procedure'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3) 
                  
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',send_keys=['down','down','right'])
        time.sleep(1)
             
        as_utilobj.Verify_Element("Olap Dimensions","Step 01: Verified - Olap Dimensions does not appear in Procedure list",unavailable=True)
        time.sleep(2)
                       
        keys_1.press(['esc','esc'])
           
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="New",click_sub_menu="Procedure")
        time.sleep(2)
                  
        '''Step 02: In Procedure View panel, right-click top level folder and select New...
                    Click X on the Procedure1 tab to close'''
             
        as_utilobj.select_home_button(move_x=-52,move_y=170)   
        time.sleep(2)
                        
        tree_path="Comment"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(3)
            
        as_utilobj.select_component_by_right_click(right_click_folder='Comment',click="New ...")
            
        as_utilobj.Verify_Element("Olap Dimensio","Step 02: Verified - Olap Dimensions does not appear in Procedure list",unavailable=True)
        time.sleep(2)
            
        keys_1.press(['esc','esc'])
             
        as_utilobj.close_canvas_item()
        time.sleep(4)
                 
        '''Step 03: Expand Data Servers>EDASERVE>Applications>right click on ibisamp and select New'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                 
        tree_path="Data Servers->EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(5) 
            
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",click="New")
        time.sleep(3)
            
        as_utilobj.Verify_Element("Olap Dimensions","Step 03: Verified - Olap Dimensions does not appear under data server list",unavailable=True)
        time.sleep(2)
            
        keys_1.press(['esc','esc'])
        time.sleep(1)
              
        '''Step 04: Click on AS menu-Options->Environments, check "Show Projects Area", click OK
                    Expand projects, right-click any Projects and select New'''
            
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(4)
#                             
#         as_utilobj.check_show_project_area(enable='Show Projects area')
#         time.sleep(6)
#             
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                
#         tree_path="Projects"
#         as_utilobj.select_tree_view_pane_item(tree_path)
#         time.sleep(5)
#             
#         as_utilobj.select_component_by_right_click(right_click_folder="Magnify Search Demonstration",click="New")
#     
#         as_utilobj.Verify_Element("Olap Dimensions","Step 04: Verified - Olap Dimensions does not appear in Project list",unavailable=True)
#         time.sleep(2)
#             
#         as_utilobj.check_show_project_area(disable='Show Projects area')
#         time.sleep(6)
           
        '''Step 05: In Environments Tree, set filter to show Procedure files
                    Navigate to CC - AppStudio->AS Files
                    Right-click olapdim.fex and select Open'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        tree_path="Domains->S9100->olapdim"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(10)
           
        '''Step 06: Click on Procedure View panel'''
         
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
          
        item_list=['Comment','Olap Dimensions','Report']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 06: "+ items + " element avaliable in procedure view panel",available=True)
        time.sleep(5)
          
        '''Step 07: Right-click the top-level folder in Procedure View panel and select New ...'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="File olapdim components",click="New ...")
        time.sleep(1)
          
        as_utilobj.Verify_Current_Dialog_Closes("Olap Dimensis","Step 07: Verified - Olap Dimensions does not appear in Procedure View panel top folder list")
        time.sleep(2)
          
        keys_1.press(['esc','esc'])
        time.sleep(1)
         
        '''Step 08: Double-click Olap Dimensions component
                    Click OK'''
        
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
         
        tree_path="Olap Dimensions"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(8)
        
        as_utilobj.verify_active_tool("App Studio - olapdim","Step 08: Verified - Olap Dimensions need to be invoked and displayed with CAROLAP master file when it is enabled in administration console settings")
        time.sleep(3)
                                                      
        '''Step 09: Click X on olapdim tab to close it'''
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  