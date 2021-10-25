'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288308'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2288308_TestClass(AS_BaseTestCase):
    def test_C2288308(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tee, Domains, right click New Folder1, select New>Reporting Object'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                       
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        tree_path="Domains->S9100->New_Folder1"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Reporting Object")
        time.sleep(1)
            
        as_utilobj.verify_active_tool("App Studio - ReportingObject - WebFOCUS Reporting Object","Step 01: Verified Reporting Object - WebFOCUS Reporting Object opens inside AS canvas with open master file dialog. AS Home ribbon is minimized.")
        time.sleep(1)
         
        '''Step 02: Close Visual1 - WebFOCUS InfoAssist+ by clicking on X'''
         
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
          
        as_utilobj.close_canvas_item()
        time.sleep(5) 
         
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified Reporting Object web tool closes. The new Reporting Object was not added to the folder in the tree.") 
        time.sleep(1)
#         
        '''Step 03: In Environments Tree, Domains, right click New Folder1, select New>URL'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="URL")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("Create URL","Step 03: Verified create URL dialog opens")
        
        '''Step 04: Click Cancel'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Closes("Create URL","Step 04: Verified Dialog closes. The new URL was not added to the folder in the tree")
        time.sleep(1)
        
        '''Step 05: In Environments Tree, Domains, right click New Folder1, select New>Cascading Style Sheet'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Cascading Style Sheet")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - CascadingStyleSheet1.css","Step 05: Verified Text Editor for Cascading Style Sheet opens")
        time.sleep(1)
        
        '''Step 06: Click X next to CascadingStyleSheet1.css to close'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
         
        as_utilobj.close_canvas_item()
        time.sleep(5) 
        
        as_utilobj.verify_active_tool("App Studio","Step 06: Verified Text Editor closes. The new CSS is not added to the folder in the tree.") 
        time.sleep(1)
        
        '''Step 07: In Environments Tree, Domains, right click New Folder1, select New>WebFOCUS StyleSheet.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="WebFOCUS StyleSheet")
        time.sleep(1)
        
        as_utilobj.verify_active_tool("App Studio - Edit StyleSheet1.sty","Step 07: Verified Text Editor for WebFOCUS Style Sheet opens")
        time.sleep(1)
        
        '''Step 08: Click X next to Edit Stylesheet1.sty to close'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
         
        as_utilobj.close_canvas_item()
        time.sleep(5) 
        
        as_utilobj.verify_active_tool("App Studio","Step 08: Text Editor closes. The new WF StyleSheet was not added to the folder in the tree.") 
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()