'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288366'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time, unittest
from common.lib import as_utility
from common.pages import as_panels

class C2288366_TestClass(AS_BaseTestCase):
    def test_C2288366(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panels_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        as_panels_obj.environment_panel_file_filter(filter="All Files")
          
        '''Step 01: Right click on 110045NonRIA and select Open 
                    Close 110045NonRIA* tab
                    Click No to App Studio saving prompt'''
           
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                           
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
            
        as_utilobj.select_component_by_right_click(right_click_item="110045NonRIA",click="Open")
        time.sleep(8)
           
        as_utilobj.verify_active_tool("App Studio - 110045NonRIA (English)*","Step 01: Page opens in HTML Canvas.")
        time.sleep(4)
           
        as_utilobj.close_canvas_item()
        time.sleep(3)
           
        as_utilobj.select_any_dialog("No")
        time.sleep(1)
          
        '''Step 02: Double click on 110045NonRIA'''
          
        tree_path="110045NonRIA"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(8)
          
        as_utilobj.verify_active_tool("App Studio - 110045NonRIA (English)*","Step 02: Page opens in HTML Canvas.")
        time.sleep(4)
          
        '''Step 03: Click on AS menu and select Save As
                    Type New.html 
                    Click OK
                    Close New tab'''
           
        as_utilobj.select_application_menu_options(send_keys=['down','down','down'])
        time.sleep(2)
           
        as_utilobj.select_any_dialog("OK",rename_file="new")
        time.sleep(3)
            
        as_utilobj.close_canvas_item()
        time.sleep(3)
          
        '''Step 04: In Environments Tree, double click New
                    Close New tab'''
          
        tree_path="new"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        as_utilobj.verify_active_tool("App Studio - new (English)","Step 04: Newly created html file 'New' been invoked in text editor")
        time.sleep(2)
          
        as_utilobj.close_canvas_item()
        time.sleep(4)
 
        '''Step 05: In Environments Tree, right click on New and select Open
                    Close New tab'''
 
        as_utilobj.select_component_by_right_click(right_click_item="new",click="Open")
        time.sleep(3)
         
        as_utilobj.verify_active_tool("App Studio - new (English)","Step 05: Newly created html file 'New' been invoked in text editor")
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        '''Step 06: In Environments Tree, right click on New and select Edit in Windows Associated Tool
                    Close Wordpad'''
 
        as_utilobj.select_component_by_right_click(right_click_item="new",click="Edit in Windows Associated Tool")
        time.sleep(3)
         
        as_utilobj.verify_notepad_content("new.htm - Notepad","Step 06: Newly created html file opens in notepad tool")
        time.sleep(2)
         
        '''Delete the created file'''
        
        as_utilobj.select_component_by_right_click(right_click_item="new",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Note: Newly created html file deleted for reason of next run")
        
if __name__=='__main__' :
    unittest.main()