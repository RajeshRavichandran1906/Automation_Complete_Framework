'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287649'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2287649_TestClass(AS_BaseTestCase):
    def test_C2287649(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right-click Public domains and select New | Procedure
                    Click on AS menu-> Save As'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                  
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
  
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="New",click_sub_menu="Procedure")         
        time.sleep(5)
        
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Refresh Descendants")         
        time.sleep(6)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=2)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=2)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=2)
        time.sleep(2)
         
        '''Step 02: Type "2..dots" for File name then click OK'''
         
        as_utilobj.select_any_dialog("OK",rename_file='2..')
        time.sleep(1)
         
        as_utilobj.Verify_Element("The name contains one or more invalid characters.\nFiles in this folder may not contain spaces, or more than one period character.","Step 01: Verified - Error message been displayed for file name",available=True)
         
        '''Step 03: Click OK
                    Click Cancel
                    Close Procedure1'''
         
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()    