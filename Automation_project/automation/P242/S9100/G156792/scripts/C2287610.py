'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287610'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2287610_TestClass(AS_BaseTestCase):
    def test_C2287610(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Data Servers>EDASERVE>Applications>ibisamp>right click carinst.fex and select Copy
                    In Environments Tree, rename Data Servers>EDASERVE>Applications>ibisamp>carinst.fex to carinstORG.fex'''
                
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Data Servers->EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_component_by_right_click(right_click_item="carinst.fex",click="Copy")
         
        as_utilobj.select_component_by_right_click(right_click_item="carinst.fex",click="Rename")
                
        keys.typewrite("carinstorg")
        time.sleep(3)
        
        '''Step 02: Right-click environment>Data Servers>EDASERVE>Applications>ibisamp'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="ibisamp",send_keys=['down'])
        time.sleep(2)

        as_utilobj.Verify_Element("Paste","Step 02: Verified - Messagebox when user attempts to paste file that is no longer exists",available=True)
        time.sleep(2)
        
        '''Step 03: Right-click environment>Data Servers>EDASERVE>Applications>ibisamp
                    Rename environment>Data Servers>EDASERVE>Applications>ibisamp>carinstORG.fex to carinst.fex'''
                
        as_utilobj.select_component_by_right_click(right_click_item="carinstorg.fex",click="Rename")
        time.sleep(2)
        
        keys.typewrite("carinst")
        time.sleep(1)
        keys.press("enter")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()     