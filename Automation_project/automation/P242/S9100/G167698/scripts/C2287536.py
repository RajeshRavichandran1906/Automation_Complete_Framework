'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287536'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import uiautomation as automation

class C2287536_TestClass(AS_BaseTestCase):
    def test_C2287536(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
          
        '''Step 01: In Environments Tree, AS Framework, right click on Report2 and select Open in Text Editor
                    Line 1, change CAR to EMPDATA
                    From AS Main menu, select Save As
                    Type C2287536.htm for File name, click OK'''
                 
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(1)
#                                                      
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                                
#         tree_path="Domains->S9100"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(2)
#              
#         as_utilobj.select_component_by_right_click(right_click_item="Report1",click="Open in Text Editor")
#         time.sleep(2)
#               
#         as_utilobj.select_home_button(move_x=1000,move_y=900)
#               
#         keys.typewrite("EMPDATA")
#              
#         as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
#         time.sleep(2)
#           
#         as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
#         time.sleep(2)
#           
#         '''Step 02: Type C2287536.htm for File name 
#                     Click OK
#                     Click OK App Studio message box''' 
#          
#         as_utilobj.click_element_using_ui(edit_element=True,id="1516")
#         time.sleep(1)
#          
#         automation.SendKey(automation.Keys.VK_RIGHT,waitTime=1)
#         automation.SendKey(automation.Keys.VK_BACK,waitTime=1)
#         automation.SendKey(automation.Keys.VK_BACK,waitTime=1)
#         automation.SendKey(automation.Keys.VK_BACK,waitTime=1)
#         keys.typewrite("htm")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         as_utilobj.verify_element_using_ui("Step 02: Verified Extension change cannot be permitted prompt been displayed",text_item="Extension change not permitted.")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         '''Step 03: Click Cancel in the Save As dialog
#                     Close Edit Report2 tab
#                     Click No'''
#          
#         as_utilobj.select_any_dialog("Cancel")
#         time.sleep(1)
#          
#         as_utilobj.close_canvas_item()
#         time.sleep(2)
#          
#         as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 03: Verified that a prompt with YES, NO, CANCEL is displayed.")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("No")
#         time.sleep(1)
#            
if __name__=='__main__' :
    unittest.main()         