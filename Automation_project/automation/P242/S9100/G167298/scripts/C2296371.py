'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2296371'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2296371_TestClass(AS_BaseTestCase):
    def test_C2296371(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
          
        as_utilobj.select_home_button()
        
        '''Step 01: Click on Command Console'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(1)
                                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Command Console")
        time.sleep(1) 
        
        as_utilobj.verify_picture_using_sikuli("step1_C2296371.png","Step 01: Verify command console opens")
        time.sleep(8)
        
        as_utilobj.close_canvas_item()
        time.sleep(4) 
        
if __name__=='__main__' :
    unittest.main()                 