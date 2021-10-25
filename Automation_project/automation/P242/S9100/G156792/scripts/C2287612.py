'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287612'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels

class C2287612_TestClass(AS_BaseTestCase):
    def test_C2287612(self): 
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panels_obj=as_panels.AS_Panels(driver)
    
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set filters to show Procedure files
                    Data Servers>EDASERVE>Applications>ibisamp, right-click all files and select Copy'''
        
        as_panels_obj.environment_panel_file_filter(filter='Procedure Files')
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Data Servers->EDASERVE->Applications->ibisamp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
        
        as_utilobj.select_multiple_files("cargraph.fex",["carinst.fex","carinst2.fex","carmgn.fex"])
        time.sleep(3)
    
        as_utilobj.select_component_by_right_click(click="Copy")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Closes("Copy/Progress Bar","Step 01: Verified there is no copy progress dialog/indicator")
        
        as_panels_obj.environment_panel_file_filter(filter='All Files')
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()   