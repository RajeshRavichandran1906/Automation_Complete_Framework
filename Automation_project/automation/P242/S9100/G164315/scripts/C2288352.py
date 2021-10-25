'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288352'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui

class C2288352_TestClass(AS_BaseTestCase):
    def test_C2288352(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWfolder and select Unpublish
                    Right click FWSubfolder and hover over Security'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
    
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Security")
        time.sleep(2)
        
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: In Unpublish sub menu displays: " + items,available=True)
            if items=='Effective Policy...':
                break
            
        pyautogui.press(['esc','esc'])
        time.sleep(1)
            
        '''Step 02: Right click FWfolder and select Publish
                    Right click FWSubfolder and hover over Security'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Unpublish")
        time.sleep(3)
           
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Publish")
        time.sleep(3)
     
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Security")
        time.sleep(2)
        
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: In Publish sub menu displays: " + items,available=True)
            if items=='Effective Policy...':
                break
              
        
if __name__=='__main__' :
    unittest.main()