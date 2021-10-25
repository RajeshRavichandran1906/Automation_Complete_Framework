'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287832'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
import pyautogui as keys
from common.lib import as_utility

class C2287832_TestClass(AS_BaseTestCase):
    def test_C2287832(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on a configured environment'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)

        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        environment=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")

        as_utilobj.select_component_by_right_click(right_click_folder=environment,send_keys=['down'])
        
        as_utilobj.Verify_Element("Sign Out","Step 01: Verified - Contextual menu includes one option 'Sign Out'",available=True)
        time.sleep(1)
                        
        keys.press('enter')
        time.sleep(3)    
        
        '''Step 02: Right click on a configured environment'''
        
        as_utilobj.select_component_by_right_click(right_click_folder=environment,send_keys=['down'])
        time.sleep(4)
        
        as_utilobj.Verify_Element("Sign In","Step 02: Verified - Contextual menu includes one option 'Sign In'",available=True)
        time.sleep(1)
                        
        keys.press('enter')
        time.sleep(7)    
        
        '''Step 03: Click 'Sign in' (login if you are requested to).'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
        
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        item_list=['Data Servers','Domains']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 03: "+ items + " element avaliable under Configured environment",available=True)
          
if __name__=='__main__' :
    unittest.main()       