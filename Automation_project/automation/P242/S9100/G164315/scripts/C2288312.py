'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288312'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility
import pyautogui

class C2288312_TestClass(AS_BaseTestCase):
    def test_C2288312(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
    
        '''Step 01: Right click New Folder1 under Domains and select New>HTML/Document.'''
            
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                     
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
            
        tree_path="Domains->S9100->New_Folder1"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
         
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Text Document")
        time.sleep(3)
          
        as_utilobj.verify_active_tool("App Studio - Edit Text1.txt","Step 01: Verified Text editor opens")
        time.sleep(1)
          
        '''Step 02: Click X next to Edit Text.txt1 to close.'''
         
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
          
        as_utilobj.close_canvas_item()
        time.sleep(5) 
          
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified Text Editor closes.The new text document was not added to the folder in the tree")
        time.sleep(1)
         
        '''Step 03: In Environments Tree, Domains, right click New Folder1, select New>Schedule.'''
                
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Schedule")
        time.sleep(2)
         
        as_utilobj.verify_active_tool("App Studio - Untitled - Schedule","Step 03: Verified ReportCaster Scheduling web tool opens inside AS canvas. The AS Home ribbon is minimized.")
        time.sleep(1)
         
        '''Step 04: Click X next to Untitled - Schedule to close'''
         
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
          
        as_utilobj.close_canvas_item()
        time.sleep(5) 
         
        as_utilobj.verify_active_tool("App Studio","Step 04: Verified RC Schedule closes. The new schedule was not added to the folder in the tree.")
        time.sleep(3)
         
        '''Step 05: In Environments Tree, Domains, right click New Folder1, select New>Distribution List.'''
            
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Distribution List")
        time.sleep(3)
         
        as_utilobj.verify_active_tool("App Studio - Untitled - Distribution List","Step 05: Verified ReportCaster Distribution List web tool opens inside AS canvas. AS Home ribbon is minimized.")
        time.sleep(2)
         
        '''Step 06: Click X next to Untitled - Distribution List to close.'''
         
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
          
        as_utilobj.close_canvas_item()
        time.sleep(5) 
        
        as_utilobj.verify_active_tool("App Studio","Step 06: Verified RC Distribution List closes. The new distribution list was not added to the folder in the tree.")
        time.sleep(2)
        
        '''Step 07: In Environments Tree, Domains, right click New Folder1, select New>Library Access List.'''
           
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Library Access List")
        time.sleep(3)
         
        as_utilobj.verify_active_tool("App Studio - Untitled - Library Access List","Step 07: Verified RC Library Access List tool opens inside AS canvas.")
        time.sleep(2)
        
        '''Step 08: Click X next to Untitled - Library Access List to close.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
        time.sleep(1)
          
        as_utilobj.close_canvas_item()
        time.sleep(5) 
            
        as_utilobj.verify_active_tool("App Studio","Step 08: Verified RC Library Access List closes. The new Library Access List was not added to the folder in the tree.")
        time.sleep(2)
        
        '''Step 09: In Environments Tree, Domains, right click New Folder1, select New>Folder'''
           
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Folder")
        time.sleep(1)
        
        pyautogui.typewrite("SubNewFolder1")
        time.sleep(1)
        
        as_utilobj.Verify_Element("SubNewFolder1","Step 09: Verified A new folder appears under the selected folder with default title 'New Folder 1' (or next value) and the title is in edit mode",available=True)
        time.sleep(1)
        
        '''Step 10:  Click on any space in Environments Tree'''
        
        pyautogui.press('enter')
        time.sleep(1)
        
        as_utilobj.Verify_Element("SubNewFolder1","Step 10: The title is no longer in edit mode.",available=True)
        time.sleep(1)
        
        '''Deleting the created folder for reason of next TESTRUN'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="Delete")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(1)
        
        print("Note: Created folder been deleted for rreason of next run")
        
if __name__=='__main__' :
    unittest.main()