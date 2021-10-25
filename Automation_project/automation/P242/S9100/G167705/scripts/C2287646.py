'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287646'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287646_TestClass(AS_BaseTestCase):
    def test_C2287646(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
         
        '''Step 01: Select a pre-defined WebFOCUS environment, click WebFOCUS Administration from the QAT'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Data Servers"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=["down"])
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2287646.png","Step 01: Verified element avaliable under WebFOCUS Administration")
        time.sleep(3)
                   
        '''Step 02: In Environments Tree, right-click the WebFOCUS environment and select Sign Out'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
        
        '''Step 03: In Environments Tree, right-click the WebFOCUS environment and select Sign In'''
        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
               
        tree_path="Data Servers"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        as_utilobj.click_element_using_ui(split_button="WebFOCUS Administration",send_keys=["down"])
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2287646.png","Step 02: Verified element avaliable under WebFOCUS Administration")
        time.sleep(2)
            
if __name__=='__main__' :
    unittest.main()   