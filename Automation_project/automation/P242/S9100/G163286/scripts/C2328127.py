'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2328127'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.locators import as_components_ui_locators
import uiautomation as automation_keys

class C2328127_TestClass(AS_BaseTestCase):
    def test_C2328127(self):
        
        '''Create instance of object'''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        environment_path="webfocus_environment"
        select_initial_repository="Domains->S9100"
        open_file_dialog='{Ctrl}(O)'
        sleep=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        verify_open_file_dialog="Open File"
        verify_msg_1="Step 01: Verify Open file dialog opens, default location is your folder under Domains"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Domains, select AS Framework folder
                    Press Ctrl+O.'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(sleep[2])
                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,environment_path)
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(sleep[2])
                   
        as_utilobj.select_tree_view_pane_item(select_initial_repository) 
        time.sleep(sleep[3])
        
        automation_keys.SendKeys((open_file_dialog),interval=0.25,waitTime=1)
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens(verify_open_file_dialog,verify_msg_1)
        time.sleep(1)
        
        '''Step 02: Click Cancel on the Open File dialog.'''
        
        as_utilobj.select_any_dialog(component_locators.cancel_button)
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  