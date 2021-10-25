'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288333'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility
import pyautogui

class C2288333_TestClass(AS_BaseTestCase):
    def test_C2288333(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Domains, right click FWSubfolder and hover over New'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New")
        time.sleep(1)
        
        item_list=['Procedure','Procedure via Text Editor','Report','SQL Report','Chart','SQL Chart','HTML/Document','Visualization','Alert','Reporting Object','URL','Collaborative Portal','Portal Page','JavaScript File','Cascading Style Sheet','WebFOCUS StyleSheet','Text Document','Schedule','Distribution List','Library Access List','Folder','Blog']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: Verified "+ items + " element avaliable",available=True)
            if items=='Blog':
                break
        
        pyautogui.press(["esc","esc"])
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  