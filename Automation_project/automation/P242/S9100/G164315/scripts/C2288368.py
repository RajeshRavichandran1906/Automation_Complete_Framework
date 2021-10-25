'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288368'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility

class C2288368_TestClass(AS_BaseTestCase):
    def test_C2288368(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click 110045Ria and select Run. 
                    Close HtmlPage tab'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="110045RIA",click="Run")
        time.sleep(2)

        as_utilobj.Verify_Browser_Content("IEFrame","Step 01: 11045RIA HTML File invokes - ",item_list=['Tab #1','Tab #3','Tab Two Aqua'])
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()