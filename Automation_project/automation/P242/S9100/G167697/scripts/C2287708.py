'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287708'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
import keyboard as keys_1

class C2287708_TestClass(AS_BaseTestCase):
    def test_C2287708(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
    
        '''Step 01 & 02: Navigate to Domains->S9100
                    Enlarge the Name column to see full name length'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2) 
    
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="0724RObj.fex",click="Rename")  
        time.sleep(1)    
             
        '''Step 02: Right click on xReport1, select Rename
                    Type 00xReport1, hit Enter'''
        
        keys_1.write("testname")  
        keys.press("enter")
        time.sleep(2)   
        
        as_utilobj.verify_element_using_ui("Step 02: Verify All files should disappear temporarily disappear from View",list_item_exist="testname.fex",available=True) 
        time.sleep(2)   
         
        '''Step 03: Right click on 00xReport1, select Rename
                    Type xReport1, hit Enters appear from View'''
        
        as_utilobj.select_component_by_right_click(right_click_item_env_detail="testname.fex",click="Rename") 
        time.sleep(1)    
        
        keys_1.write("0724RObj")  
        keys.press("enter")
        time.sleep(2)
         
if __name__=='__main__' :
    unittest.main()     