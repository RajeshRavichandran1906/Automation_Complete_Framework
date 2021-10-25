'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288331'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility
import keyboard as keys

class C2288331_TestClass(AS_BaseTestCase):
    def test_C2288331(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, right click Domains-> New Folder
                    Type FWFolder, hit Enter 
                    Right click on FWFolder->New Folder 
                    Type FWSubFolder, hit Enter 
                    Right click on FWSubFolder'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)

        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Folder")
        time.sleep(1)
        
        keys.write("FWSubFolder")
        time.sleep(1)
        
        keys.press('enter')
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",send_keys=["down"])
        
        item_list=['Impact Analysis','New','Upload Data','Security','Rename','Delete','ReportCaster Explorer','Properties','Refresh Descendants']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 01: Before Publishing "+ items + " element avaliable",available=True)
            if items=='Refresh Descendants':
                break
        
        keys.press("esc")
        time.sleep(1)
        
        '''Step 02: Right click FWFolder and select Publish
                    Right click on FWSubFolder'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",send_keys=["down"],click="Unpublish")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",send_keys=["down"],click="Publish")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",send_keys=["down"])
        
        item_list=['Impact Analysis','New','Upload Data','Unpublish','Security','Rename','Delete','ReportCaster Explorer','Properties','Refresh Descendants']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 02: After Publishing "+ items + " element available",available=True)
            if items=='Refresh Descendants':
                break
            
        keys.press('esc')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()   