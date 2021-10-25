'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288344'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2288344_TestClass(AS_BaseTestCase):
    def test_C2288344(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWSubfolder under Domains and select New>WebFOCUS StyleSheet 
                    Click X to close StyleSheet1.sty tab'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
             
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(4)
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="WebFOCUS StyleSheet")
        time.sleep(6)
         
        as_utilobj.verify_active_tool("App Studio - Edit StyleSheet1.sty","Step 1.1: Text editor for style sheets opens. Edit StyleSheet1.sty.")
        time.sleep(2)
        
        as_utilobj.close_canvas_item() 
        time.sleep(2)
         
        as_utilobj.verify_active_tool("App Studio","Step 1.2: Text Editor closes. The new WF Stylesheet was not added in the tree.")
        time.sleep(2)
         
        '''Step 02: Right click FWSubfolder under Domains and select New>Text Document 
                    Click X to close Edit Text1.txt tab'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Text Document")
        time.sleep(5)
         
        as_utilobj.verify_active_tool("App Studio - Edit Text1.txt","Step 2.1: Text editor opens. Edit Text1.txt")
        time.sleep(2)
                 
        as_utilobj.close_canvas_item()
        time.sleep(2)
         
        as_utilobj.verify_active_tool("App Studio","Step 2.2: Text Editor closes. The new text document was not added in the tree.")
        time.sleep(2)
         
        '''Step 03: Right click FWSubfolder under Domains and select New>Schedule 
                    Click X to close Untitled - Schedule '''
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Schedule")
        time.sleep(6)
         
        as_utilobj.verify_active_tool("App Studio - Untitled - Schedule","Step 3.1: ReportCaster Scheduling web tool opens. Untitled - Schedule")
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
         
        as_utilobj.verify_current_active_tool("App Studio","Step 3.2: RC tool closes. The new schedule was not added in the tree.")
        time.sleep(2)
         
        '''Step 04: Right click FWSubfolder under Domains and select New>Distribution List.
                    Click X to close Untitled - Distribution List '''
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Distribution List")
        time.sleep(6)
         
        as_utilobj.verify_active_tool("App Studio - Untitled - Distribution List","Step 4.1: ReportCaster Distribution List web tool opens. Untitled - Distribution List")
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(2)
         
        as_utilobj.verify_active_tool("App Studio","Step 4.1: RC tool closes. The new distribution list was not added in the tree.")
        time.sleep(2)
         
        '''Step 05: Right FWSubfolder under Domains and select New>Library Access List.
                    Click X to close Untitled - Library Access List.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Library Access List")
        time.sleep(6)
        
        as_utilobj.verify_active_tool("App Studio - Untitled - Library Access List","Step 5.1: ReportCaster Library Access List web tool opens. Untitled - Library Access List")
        time.sleep(2)
                
        as_utilobj.close_canvas_item()
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio","Step 5.2: RC tool closes. The new Library Access List was not added in the tree.")
        time.sleep(2)
        
        '''Step 06: Right click FWSubfolder under Domains and select New>Folder.'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu="Folder")
        time.sleep(6)
        
        keys.press("enter")
        
        as_utilobj.Verify_Element("New Folder1","Step 06: A new sub folder appears under the FWSubfolder with default title 'New Folder1' (or next value) and the title is in edit mode.",available=True)
        time.sleep(1)

if __name__=='__main__' :
    unittest.main()