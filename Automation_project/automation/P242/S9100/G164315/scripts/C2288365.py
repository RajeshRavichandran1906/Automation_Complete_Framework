'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288365'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility
import pyautogui

class C2288365_TestClass(AS_BaseTestCase):
    def test_C2288365(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Files and select Unpublish
                    Right click on 110045NonRIA and hover Security'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="110045NonRIA",click="Security")
        time.sleep(2)
         
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: Unpublish HTML File security menu displays: " + items,available=True)
            if items=='Effective Policy...':
                break
             
        pyautogui.press(['esc','esc'])
        time.sleep(1)
        
        '''Step 02: Right click on AS Files and select Publish
                    Right click on 11004NonRIA and hover Security'''

        as_utilobj.select_component_by_right_click(right_click_item="110045NonRIA",click="Security")
        time.sleep(2)
        
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: Publish HTML File security menu displays: " + items,available=True)
            if items=='Effective Policy...':
                break
            
        pyautogui.press(['esc','esc'])
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()     