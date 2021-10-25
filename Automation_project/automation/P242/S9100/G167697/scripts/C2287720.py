'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287720'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2287720_TestClass(AS_BaseTestCase):
    def test_C2287720(self):
        
        '''Creating Object Instance'''
        
        driver = self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        time.sleep(1)
        
        '''Step 01 &02 : In Environments Detail, double-click Domains->Public
                    Drag Last Modified column to the left of the Name column
                    Drag Location column between Size and Type columns
                    Drag Size column between Location and Type columns'''
        
        as_utilobj.drag_drop(325,212,825,212) 
        time.sleep(1)
        
        '''Step 03: Click on default domain folder'''
          
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                      
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2) 
        
        as_utilobj.verify_element_using_ui("Step 03: Verify that the column data match the column headings.",list_item_exist="testname.fex",unavailable=True) 
        time.sleep(2)
         
        '''Step 04: Drag Size column between Last modified and Name columns
                    Drag Type column between Last modified and Size columns
                    Drag Location column after Last Modified column'''
        
        as_utilobj.drag_drop(825,212,325,212)
        time.sleep(3)

if __name__=='__main__' :
    unittest.main()    