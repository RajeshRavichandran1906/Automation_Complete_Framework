'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288409'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2288409_TestClass(AS_BaseTestCase):
    def test_C2288409(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New-> Folder
                    Right click on AS Framework and select New-> Folder
                    Click on AS Framework'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")
        keys.write('C2288409_1')
        keys.press('enter')
        time.sleep(1)
         
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")
         
        keys.write('C2288409_2')
        keys.press('enter')
        time.sleep(1) 
        
        as_utilobj.Verify_Element("C2288409_2","Step 1: Verified two new folders been created",available=True)
        time.sleep(1)
        
        '''Step 02: Select New Folder1
                    Hold down Ctrl key
                    Select New Folder2'''
        
        as_utilobj.select_multiple_files("C2288409_1", ["C2288409_2"])
        time.sleep(3)
        
        '''Step 03: Right click on selected folders and select Delete 
                    Click Yes
                    Click Yes'''
        
        as_utilobj.select_component_by_right_click(click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("App Studio","Step 03: Verified that created folders are been deleted")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()        