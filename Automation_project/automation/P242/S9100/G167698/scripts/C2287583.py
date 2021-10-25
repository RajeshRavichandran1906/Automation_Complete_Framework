'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287583'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287583_TestClass(AS_BaseTestCase):
    def test_C2287583(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
#         '''Step 01: In Environments Tree, set filter to Procedure Files 
#                     From AS Framework folder, right click on Report2 and select Open in Text Editor
#                     Click on Font Style on the Options section 
#                     Click Choose Font and scroll to bottom of list'''
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
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(button_item=True,name="Choose Font")
#         time.sleep(1)
#         
#         as_utilobj.Verify_Element("Webdings","Step 01: Verify that the following fonts do not appear in the Font list: Webdings, Wingdings, Wingdings 2, Wingdings 3, and Symbol",unavailable=True)
#         
#         '''Step 02: Select Small Fonts in the Font list
#                     Size value, type 24 
#                     Click OK'''
#     
#         as_utilobj.click_element_using_ui(edit_element=True,id="1001",send_key="delete") 
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(edit_element=True,id="1001",send_key="delete",write="Small Fonts")
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(edit_element=True,name="Size:",write="24")
#         time.sleep(3)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         '''Step 03: Click Choose Font button
#                     Size value, type 48
#                     Click OK'''
#         
#         as_utilobj.click_element_using_ui(button_item=True,name="Choose Font")
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(edit_element=True,name="Size:",write="48")
#         time.sleep(1)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         as_utilobj.Verify_Element("Size must be between 6 and 24 points.","Step 03: Verified dialog displays as Size must be between 6 and 24 points.",available=True)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         '''Step 04: Click OK in Font dialog alert message
#                     Select Times New Roman for Font
#                     Size value, type 26
#                     Click OK'''
#         
#         as_utilobj.click_element_using_ui(edit_element=True,id="1001",send_key="delete") 
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(edit_element=True,id="1001",send_key="delete",write="Times New Roman")
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(edit_element=True,name="Size:",write="26")
#         time.sleep(3)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         as_utilobj.Verify_Element("Size must be between 6 and 24 points.","Step 04: Verified dialog displays as Size must be between 6 and 24 points.",available=True)
#         time.sleep(1)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         '''Step 05: Click OK in Font dialog alert message
#                     Click Cancel
#                     Click Reset All 
#                     Click OK
#                     Close Edit Report1 tab'''
#         
#         as_utilobj.select_any_dialog("Cancel")
#         time.sleep(1)
#         
#         as_utilobj.click_element_using_ui(button_item=True,name="Reset All")
#         time.sleep(1)
#         
#         as_utilobj.select_any_dialog("OK")
#         time.sleep(1)
#         
#         as_utilobj.close_canvas_item()
#         time.sleep(1)
             
if __name__=='__main__' :
    unittest.main() 