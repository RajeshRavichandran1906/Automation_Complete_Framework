'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287579'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287579_TestClass(AS_BaseTestCase):
    def test_C2287579(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to Procedures file
                    Navigate to Data Servers->EDASERVE->Applications
                    Expand baseapp application
                    Right click on baseapp and select New ->Text Document'''
        
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(1)
#           
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                          
#         tree_path="Data Servers->EDASERVE->Applications->baseapp"
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(2)
#         
#         as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="Text Document")
#         time.sleep(2)
#          
#         as_utilobj.verify_active_tool("App Studio - Edit Text1.txt","Step 01: Verified new text document been opened")
#         time.sleep(2)
#         
#         '''Step 02: Right click on profile.fex and select Open in Text Editor
#                     Close Edit Test1.txt tab
#                     Close Edit profile.fex tab
#                     Collapse Data Servers'''
#         
#         as_utilobj.select_component_by_right_click(right_click_item="profile.fex",click="Open")
#         time.sleep(2)
#         
#         as_utilobj.verify_active_tool("App Studio - profile.fex","Step 02: Verified profile.fex document been invoked")
#         time.sleep(2)
#         
#         as_utilobj.close_canvas_item()
#         time.sleep(3)
#         
#         as_utilobj.close_canvas_item()
#         time.sleep(3)
#         
#         as_utilobj.verify_active_tool("App Studio","Step 03: Verified app studio did not crash")
#         time.sleep(2)
                    
if __name__=='__main__' :
    unittest.main() 