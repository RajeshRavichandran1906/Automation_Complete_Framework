'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288416'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility

class C2288416_TestClass(AS_BaseTestCase):
    def test_C2288416(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click on AS Framework and select New->Collaborative Portal
                    Type FrameworkPortal for File name
                    Click OK'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Collaborative Portal")
        time.sleep(10)
          
        as_utilobj.select_any_dialog("OK",rename_file="FrameworkPortal")
        time.sleep(8)
          
        as_utilobj.click_element_using_ui(text_click="Create")
        time.sleep(1)
          
        as_utilobj.verify_active_tool("App Studio - Portal Designer","Step 01: Verified collaborative portal page created succesfully and QAT menu is disabled")
        time.sleep(2)
          
        '''Step 02: Close Portal Designer tab by clicking X'''
          
        as_utilobj.select_home_button()
        time.sleep(2)
        
        as_utilobj.select_home_button(move_x=376,move_y=21)
        time.sleep(2)
      
        as_utilobj.select_any_dialog("Leave this page")
        time.sleep(1)
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="Refresh Descendants")
        time.sleep(2)
          
        as_utilobj.Verify_Element("FrameworkPortal","Step 02: Verified portal designer is closed and show in the tree",available=True)
        time.sleep(1)
          
        '''Step 03: Right click on FrameworkPortal and select Open
                    Click on AS menu and select Close'''
          
        as_utilobj.select_component_by_right_click(right_click_item="FrameworkPortal",click="Open")
        time.sleep(6)
          
        as_utilobj.verify_active_tool("App Studio - Portal Designer","Step 03: Verified collaborative portal page invoked on Right click and QAT icons are disabled")
        time.sleep(4)
          
        as_utilobj.close_canvas_item()
        time.sleep(4)
          
        '''Step 04: Double click on FrameworkPortal
                    Close Portal Designer tab by clicking X'''
          
        tree_path="FrameworkPortal"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
          
        as_utilobj.verify_active_tool("App Studio - Portal Designer","Step 04: Verified collaborative portal page invoked on double click and QAT icons are disabled")
        time.sleep(4)
          
        as_utilobj.close_canvas_item()
        time.sleep(5)
                   
        '''Step 05: Right click on FrameworkPortal'''
         
        as_utilobj.select_component_by_right_click(right_click_item="FrameworkPortal",send_keys=['down'])
        time.sleep(2)
         
        item_list=['Open','Run','Hide','Security','New','Copy','Rename','Delete','Properties']
        for items in item_list:
            as_utilobj.Verify_Element(items,"Step 05: verified "+ items + " avaliable in right click options of New collaborative Portal",available=True)
            
        
        '''Delete the create colloborative portal'''
            
        as_utilobj.select_component_by_right_click(right_click_folder="FrameworkPortal Resources",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_item="FrameworkPortal",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print('Note: Created files are been deleted for reason of nextrun')
        
if __name__=='__main__' :
    unittest.main()  