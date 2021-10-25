'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287582'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys
from common.pages import as_panels

class C2287582_TestClass(AS_BaseTestCase):
    def test_C2287582(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
#         '''Step 01: In Environments Tree, right click on Domains->New Folder 
#                     Type d.e and hit Enter 
#                     Right click on d.e and select New->Text Document
#                     Type TABLE 
#                     Close Edit Text1.txt tab'''
#          
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(1)
#            
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#          
#         tree_path="Domains"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(2)
#                           
#         as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="New Folder")
#         time.sleep(2)
#          
#         keys.write("de")
#         keys.press("enter")
#         time.sleep(2)
#          
#         as_utilobj.select_component_by_right_click(right_click_folder="de",click="New",click_sub_menu="Text Document")
#         time.sleep(2)
#          
#         keys.write('TYPE')
#         time.sleep(1)
#          
#         as_utilobj.close_canvas_item()
#         time.sleep(3)
#          
#         '''Step 02: Click Yes for App Studio saving prompt
#                     Click OK'''
#          
#         as_utilobj.select_any_dialog("Yes")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         as_utilobj.verify_active_tool("App Studio","Step 01: Verified Creating new file in domain whose name has a period, at save get 'file exists")
#         time.sleep(1)
#             
#         '''Step 02: In Environments Tree, set Filter to Other Files
#                     Expand d.e'''
#          
#         as_panel_obj.environment_panel_file_filter(filter="Other Files")
#         time.sleep(3)
#          
#         as_utilobj.select_tree_view_pane_item("de")
#         time.sleep(1)
#          
#         as_utilobj.verify_element_using_ui("Step 02: Verified text file created",tree_item="Text1",available=True)
#         time.sleep(2)
#          
#         as_utilobj.select_component_by_right_click(right_click_folder="de",click="Delete")
#         time.sleep(2)
#          
#         as_utilobj.select_any_dialog("Yes")
#         time.sleep(1)
#          
#         as_panel_obj.environment_panel_file_filter(filter="All Files")
#         time.sleep(1)
        
if __name__=='__main__' :
    unittest.main() 