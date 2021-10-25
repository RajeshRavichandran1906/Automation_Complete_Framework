'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288385'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui

class C2288385_TestClass(AS_BaseTestCase):
    def test_C2288385(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains->S9100
                    Right click on ActiveChart and hover over the Schedule option'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_item="ActiveChart",click="Schedule")
        time.sleep(1)
         
        item_list=['Email...','FTP...','Printer...','Report Library...','Managed Reporting...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: "+ items + " element avaliable in right click options of Schedule",available=True)
        time.sleep(1)
             
        pyautogui.press(['esc','esc'])
        time.sleep(2)
        
        '''Step 02: Right click on ActiveChart and hover over the Security option'''
                               
        as_utilobj.select_component_by_right_click(right_click_item="ActiveChart",click="Security")
        time.sleep(1)
         
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: "+ items + " element avaliable in right click options of fex file before publishing",available=True)
        time.sleep(1)
             
        pyautogui.press(['esc','esc'])
        time.sleep(1)
    
        '''Step 03: Right click on AS Framework folder and select publish
                    Right click on ActiveChart and hover over the Security option'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Unpublish")
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Publish")
        time.sleep(3)
        
        as_utilobj.select_component_by_right_click(right_click_item="ActiveChart",click="Security")
        time.sleep(1)
        
        item_list=['Rules...','Rules on this Resource...','Effective Policy...']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 03: "+ items + " element avaliable in right click options of fex file after publishing",available=True)
        time.sleep(1)
            
        pyautogui.press(['esc','esc'])
        time.sleep(1) 
          
if __name__=='__main__' :
    unittest.main()