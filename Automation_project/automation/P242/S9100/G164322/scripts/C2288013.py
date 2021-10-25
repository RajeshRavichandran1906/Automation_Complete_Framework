'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288013'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2288013_TestClass(AS_BaseTestCase):
    def test_C2288013(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Click on View Options icon
                    Un-check 'Respect Sort Order Property'''
                  
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
        
        as_utilobj.Verify_Element('View items by Title',"Step 01: Verified 'View items by Title' is checked by default",available=True)
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(menu_item=True,name='Respect Sort Order Property')
        time.sleep(1)
         
        '''Step 02: Under CC - AppStudio->AS Framework folder
                    Select 0724RObj
                    Click on File/Folder Properties
                    Prefix Title with 2, hit Enter'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
          
        as_utilobj.select_component_by_right_click(right_click_item='0724RObj',click='Properties')
        time.sleep(1)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.double_click_element_using_offset(1600,165)
        time.sleep(1)
        
        keys.press('2')
        time.sleep(2)
        
        keys.press('enter')
        time.sleep(2)
        
        as_utilobj.Verify_Element('20724RObj',"Step 02: Verified file been renamed in Environment Tree",available=True)
        time.sleep(2)
        
        '''Step 03: Select 20724RObj in Environments Tree
                    Delete "2" prefix from Title, hit Enter
                    Check 'Respect Sort Order Property'''
        
        as_utilobj.select_component_by_right_click(right_click_item='20724RObj',click='Rename')
        time.sleep(1)
        
        keys.write("0724RObj")

        keys.press('enter')
        time.sleep(2)
        
        as_utilobj.Verify_Element('0724RObj',"Step 03: Verified File Reverted back to old name",available=True)
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name='View Options')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name='Respect Sort Order Property')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  