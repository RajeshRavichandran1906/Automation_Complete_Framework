'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287616'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287616_TestClass(AS_BaseTestCase):
    def test_C2287616(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01: In Environments Tree, right click on a WebFOCUS environment, click Sign Out
                    Right click on a WebFOCUS environment, click Sign In
                    Supply credential for User Name and password 
                    Click Logon'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        '''Step 02: Expand Domains
                    Click Environments on the QAT/Ribbonbar
                    Select the WebFOCUS environment from the list
                    Click Properties
                    Click Cancel twice'''
            
        tree_path= "Domains"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Environments")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Environments List","Step 02: Verify environments list dialog opened")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Properties")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        '''Step 03: Double click on S9100 domain'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path)
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio","Step 03: Verify there must not be a logon prompt at this point. Public folder will expand. No crash happened") 
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  