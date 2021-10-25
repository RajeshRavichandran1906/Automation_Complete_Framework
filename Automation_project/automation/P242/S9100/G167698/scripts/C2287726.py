'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287726'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
from common.pages import as_panels

class C2287726_TestClass(AS_BaseTestCase):
    def test_C2287726(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
         
#         '''Step 01: In Environments Tree, set Filter to HTML files
#                     Navigate to EDASERVE>Applications>ibisamp
#                     Double click on wfmstart.html'''
#         
#         as_panel_obj.environment_panel_file_filter(filter="HTML Files")
#         time.sleep(1)
#            
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(3)
#          
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                            
#         tree_path="Data Servers->EDASERVE->Applications->ibisamp->wfmstart.html"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(5)
#            
#         as_utilobj.verify_active_tool("App Studio - Edit wfmstart.html","Step 01: Verified wfmstart.html opens in AS text editor tab")
#         time.sleep(1)
#            
#         '''Step 02: Click on AS menu and select Save As
#                     Type copyhtml.html for File name
#                     Click OK'''
#            
#         as_utilobj.select_component_by_right_click(right_click_item="wfmstart.html",click="Properties")
#         time.sleep(2)
#          
#         as_utilobj.select_component_by_right_click(right_click_item="ibisamp",click="Refresh Descendants")
#         time.sleep(2)
#             
#         as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
#         time.sleep(2)
#                     
#         as_utilobj.click_element_using_ui(edit_element="1516")
#             
#         keys.hotkey("home")
#         time.sleep(1)
#         keys.hotkey('del','del','del','del', interval=0.25)
#         time.sleep(2)
#         keys.hotkey('del','del','del','del', interval=0.25)
#         time.sleep(2)
#             
#         keys.typewrite("copyhtml")
#             
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(2)
#           
#         as_utilobj.select_component_by_right_click(right_click_item="copyhtml.html",click="Properties")
#         time.sleep(2)
#           
#         as_utilobj.Verify_Element("copyhtml.html","Step 02: Verified the newly created .html file is created and visible in the tree",available=True)
#         time.sleep(1)
#           
#         '''Step 03: Close Edit copyhtml.html tab
#                     Collapse Data Servers'''
#           
#         as_utilobj.close_canvas_item()
#         time.sleep(3)
#          
#         as_utilobj.select_component_by_right_click(right_click_item="copyhtml.html",click="Delete")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("Yes")
#         time.sleep(2)
#          
#         as_panel_obj.environment_panel_file_filter(filter="All Files")
#         time.sleep(1)
                            
if __name__=='__main__' :
    unittest.main() 