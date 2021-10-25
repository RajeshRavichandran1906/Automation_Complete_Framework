'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287836'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287836_TestClass(AS_BaseTestCase):
    def test_C2287836(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, Navigate to CC - AppStudio->AS Files
                    Right click on 160526009, select 'Edit In Windows Associated Tool'
                    Close 160526009.fex - Notepad'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_component_by_right_click(right_click_item='160526009',click='Edit in Windows Associated Tool')
        time.sleep(3)
        
        as_utilobj.verify_notepad_content("160526009.fex - Notepad","Step 01: Verified file 160526009 invoked in Windows Associated Tool")
        time.sleep(2)
        
        '''Step 02: Right click on Chart Basic Bar, select 'Edit In Windows Associated Tool'l
                    Close Chart Basic Bar - Notepad'''
        
        as_utilobj.select_component_by_right_click(right_click_item='Chart Basic Bar',click='Edit in Windows Associated Tool')
        time.sleep(3)
        
        as_utilobj.verify_notepad_content("Chart_Basic_Bar.fex - Notepad","Step 02: Verified Chart Basic Bar file invoked in Windows Associated Tool")
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  