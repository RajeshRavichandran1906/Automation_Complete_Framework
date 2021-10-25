'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287671'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_panels

class C2287671_TestClass(AS_BaseTestCase):
    def test_C2287671(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)  
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01 & 02: Env Detail already invoked.Navigate to and select Domains->S9100'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                    
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                       
        as_utilobj.select_tree_view_pane_item("Domains->S9100") 
        time.sleep(2) 
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Properties")
        time.sleep(1)   
        
        as_utilobj.Verify_Element("File/Folder Properties","Step 02: Verify File/Folder Properties panel shows properties for AS Files, and the right side of the details panels lists files from AS Files folder.",available= True)
        time.sleep(1)   
        
        '''Step 03: Select Domains context'''
             
        as_utilobj.select_file(tree_item="Domains")
        time.sleep(1)   
        
        as_utilobj.verify_element_using_ui("Step 03: Verify File/Folder Properties panel shows properties for Domains context. Title=Domains. Server Path=IBFS:/[hostname]/WFS/Repository",tree_item="Domains",available=True)
        time.sleep(1)   
        
        '''Step 04: Click Configured Environments context'''
        
        as_utilobj.select_file(tree_item="Configured Environments")
        time.sleep(1)   
        
        as_utilobj.verify_element_using_ui("Step 04: Verify File/Folder Properties panel shows 2 properties for the Configured Environment context: Title and Server Path=IBFS.There should be no files listed in the right side of the panel.",tree_item="Configured Environments",available=True)
        time.sleep(1)   
        
        '''Step 05: Set "View items by Name" from the panel's View Options drop down'''
        
        as_panel_obj.environment_panel_file_filter(filter="View Options",click="View items by Name")
        time.sleep(1)
      
        as_utilobj.verify_element_using_ui("Step 05 & 06: Verify File/Folder Properties panel is correct for the selected item, and files shown in the right side of the detail panel are correct.",tree_item="Configured Environments",available=True)
        time.sleep(2) 

        as_panel_obj.environment_panel_file_filter(filter="View Options",click="View items by Title")
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  