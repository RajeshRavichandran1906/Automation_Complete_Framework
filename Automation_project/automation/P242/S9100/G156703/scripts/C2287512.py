'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287512'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287512_TestClass(AS_BaseTestCase):
    def test_C2287512(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Expand the Configured Environments->Web Applications 
                    Right click on baseapp->New->HTML Page
                    Close Edit HtmlPage1.htm'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                 
        tree_path="Web Applications->baseapp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="HTML Page")
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio - Edit HtmlPage1.htm","Step 01: Verified - HTML file opens and displayed as 'Edit HtmlPage1.htm'")
        time.sleep(2)
                
        as_utilobj.close_canvas_item()

if __name__=='__main__' :
    unittest.main()  