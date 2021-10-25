'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287525'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287525_TestClass(AS_BaseTestCase):
    def test_C2287525(self):
                
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right-click Domains and select Impact Analysis
                    Navigate to Data Servers -> EDASERVE -> Applications -> ibisamp
                    Double click on car.mas
                    Enter COUNTRY as Field Name value'''
              
#         as_utilobj.logout_conf_env(webfocus_environment=True)
#         time.sleep(1)
#                                              
#         tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
#         as_utilobj.select_tree_view_pane_item(tree_path) 
#         time.sleep(3)
#                      
#         as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="Impact Analysis")
#         time.sleep(1)
#               
#         as_utilobj.select_file_in_dialogs("OK",tree_path="Data Servers->EDASERVE - EDASERVE->Applications->ibisamp",select_file="car.mas")
#         time.sleep(3)
#            
#         as_utilobj.click_element_using_ui(edit_element="4104",write="COUNTRY")
#         time.sleep(1)
#           
#         '''Step 02: Choose AppStudio-Team from the Search Paths list
#                     Click Analyze button
#                     Click Description column heading in the Impact Analysis Result section
#                     Resize Location column'''
#          
#         as_utilobj.click_element_using_ui(button_item=True,name="Analyze")
#         time.sleep(1)
#          
#         as_utilobj.click_element_using_ui(header_item="Description")
#         time.sleep(1)
#          
#         as_utilobj.select_home_button()
#         time.sleep(1)
#          
#         as_utilobj.verify_active_tool("App Studio - Impact Analysis","Step 02: Verify clicking in Impact Analysis' results display column headings does not crash product")  
#         time.sleep(1)
#         
#         '''Step 03: Close Impact Analysis tab'''
#         
#         as_utilobj.close_canvas_item()
#         time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()  