'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287579'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels
import pyautogui as keys

class C2287576_TestClass(AS_BaseTestCase):
    def test_C2287576(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
          
#         '''Step 01: In Environments Tree, set filter to Procedure Files 
#                     From AS Framework folder, right click on Report1 and select Open in Text Editor
#                     Click on Font Style on the Options section 
#                     Click Choose Font'''
#             
#         as_panel_obj.environment_panel_file_filter(filter="Procedure Files")
#         time.sleep(1)
#             
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
#         time.sleep(1)
#              
#         as_utilobj.click_element_using_ui(button_item=True,name="Font Style")
#             
#         '''Step 02: Select Arial from Font list
#                     Select 16 from Size list
#                     Click OK
#                     Uncheck Automatic for Foreground 
#                     Uncheck Automatic for Background'''
#            
#         as_utilobj.click_element_using_ui(button_item=True,name="Choose Font")
#         time.sleep(1)
#           
#         as_utilobj.click_element_using_ui(list_item="Franklin Gothic")
#         time.sleep(1)
#           
#         as_utilobj.click_element_using_ui(list_item="16")
#         time.sleep(1)
#           
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#           
#         '''Step 03: In Color section, select Comment
#                     Select Red in Foreground list
#                     Select Yellow in Background list'''
#           
#         as_utilobj.click_element_using_ui(list_item="Comment")
#         time.sleep(1)
#                   
#         as_utilobj.click_element_using_ui(button_item=True,name="Forecolor")
#         keys.press(['right','right','enter'])
#         time.sleep(1)
#           
#         as_utilobj.click_element_using_ui(check_box=True,id="1028")
#         time.sleep(1)
#           
#         as_utilobj.click_element_using_ui(button_item=True,name="Backcolor")
#          
#         keys.press(['right','right','right','right','enter'])
#         time.sleep(1)
#           
#         '''Step 04: Click OK
#                     Close Edit Report2'''
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#      
#         as_utilobj.verify_picture_using_sikuli("step4_C2287576.png","Step 04: Verified comment element color been changed")
#          
#         as_utilobj.close_canvas_item()
#         time.sleep(5)
#          
#         '''Step 05: From AS Framework folder, right click on Report1 and select Open in Text Editor
#                     Click on Font Style on the Options section 
#                     Click Choose Font'''
#          
#         as_utilobj.select_component_by_right_click(right_click_item="SimpleReportForChart",click="Open in Text Editor")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Font Style")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Choose Font")
#         time.sleep(1)
#          
#         '''Step 06: Select Times New Roman from Font list
#                     Select 9 from Size list
#                     Click OK
#                     Uncheck Automatic for Foreground 
#                     Uncheck Automatic for Background'''
#          
#         as_utilobj.click_element_using_ui(list_item="Fixedsys")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(list_item="12")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         '''Step 07: In Color section, select Keyword
#                     Select Yellow in Foreground list
#                     Select Black in Background list'''
#          
#         as_utilobj.click_element_using_ui(list_item="Keyword")
#         time.sleep(1)
#                  
#         as_utilobj.click_element_using_ui(button_item=True,name="Forecolor")
#         keys.press(['right','right','right','enter'])
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(check_box=True,id="1028")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Backcolor")
#         keys.press(['right','right','right','right','right','enter'])
#         time.sleep(1)
#          
#         '''Step 08: Click OK
#                     Close Edit Report1'''
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         as_utilobj.verify_picture_using_sikuli("step8_C2287576.png","Step 08: Verified keyword color been changed")
#         time.sleep(1)
#          
#         as_utilobj.close_canvas_item()
#         time.sleep(3)
#          
#         '''Step 09: From AS Framework folder, right click on Report2 and select Open in Text Editor
#                     Click on Font Style on the Options section 
#                     Click Reset All
#                     Click OK'''
#          
#         as_utilobj.select_component_by_right_click(right_click_item="SimpleReportForChart",click="Open in Text Editor")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Font Style")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Reset All")
#         time.sleep(1)
#          
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#          
#         as_utilobj.verify_picture_using_sikuli("step9_C2287576.png","Step 09: Verified font has been resetted")
#         time.sleep(1)
#          
#         as_utilobj.close_canvas_item()
#         time.sleep(2)
#          
#         as_panel_obj.environment_panel_file_filter(filter="All Files")
#         time.sleep(1)
         
if __name__=='__main__' :
    unittest.main() 