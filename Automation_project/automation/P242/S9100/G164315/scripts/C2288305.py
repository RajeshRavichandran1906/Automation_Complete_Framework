'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288305'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility
from common.pages import as_wizard

class C2288305_TestClass(AS_BaseTestCase):
    def test_C2288305(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_wizard_obj= as_wizard.AS_Wizard_Windows(driver)
        
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
           
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="HTML/Document")
        time.sleep(2) 
             
        as_utilobj.Verify_Current_Dialog_Opens("HTML / Document Wizard","Step 01: Verified HTML/Document wizard opens (with a list of Recent HTML Pages/Documents, if any)")
        time.sleep(1)
              
        '''Step 02: Click Next and click Finish.'''
           
        as_utilobj.select_any_dialog("Next >")
           
        as_utilobj.select_any_dialog("Finish")
        time.sleep(3)
             
        as_utilobj.verify_active_tool("App Studio - HtmlPage1 (English)","Step 02: HTML canvas opens with the Components ribbon in focus. Default file name is HtmlPage1. \n Step 03: File/Folder Properties, Properties, Settings, Requests & Data Sources, Tasks & Animations panels are showing on the right side of the canvas.")
        time.sleep(1)
             
        '''Step 03: Close the HtmlPage1 by clicking the X'''
          
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
           
        as_utilobj.close_canvas_item()
        time.sleep(5) 
              
        as_utilobj.verify_active_tool("App Studio","Step 03: Verified HTML page closes without saving and without a save prompt.")
        time.sleep(2)
            
        '''Step 04: Right click New Folder1 under Domains and select New>HTML/Document
                    Select Document (PDF, Excel...) radio button 
                    Click Next and click Finish'''
           
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="HTML/Document")
        time.sleep(2)
            
        as_utilobj.Verify_Current_Dialog_Opens("HTML / Document Wizard","Step 04: Verified HTML/Document wizard opens (with a list of Recent HTML Pages/Documents, if any)")
        time.sleep(2)   
        '''Step 05 & 06: Click Next and click Finish.'''
            
        as_wizard_obj.Html_Document_Wizard("Home","html_document","Document (PDF, Excel...)")  
        time.sleep(6)
            
        as_utilobj.verify_active_tool("App Studio - Document1","Step 05: Verified document canvas Insert is in Focus. \n Step 06: File/Folder Properties and Properties panels are available")
        time.sleep(2)
            
        '''Step 07: Close the HtmlPage1 by clicking the X'''
           
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
           
        as_utilobj.close_canvas_item()
        time.sleep(5) 
            
        as_utilobj.verify_active_tool("App Studio","Step 07: Document page closes without saving and without a save prompt")
        time.sleep(2)
           
        '''Step 08: Right click New Folder1 under Domains and select New>Visualization.'''
                   
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Visualization")
        time.sleep(2)
        
        as_utilobj.verify_active_tool("App Studio - Visual1 - WebFOCUS InfoAssist","Step 08: Verified Visualization tool opens in AS canvas. AS ribbon is minimized, QA tools are disabled, except for New and Open.")
        time.sleep(2)
        
        '''Step 09: Close Visual1 - WebFOCUS InfoAssist+ by clicking on X'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
         
        as_utilobj.close_canvas_item()
        time.sleep(5) 
        
        as_utilobj.verify_active_tool("App Studio","Step 09: Visualization Tool closes")  
        time.sleep(2)
        
        '''Step 10: Right click New Folder1 under Domains and select New>Alert'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="New_Folder1",click="New",click_sub_menu="Alert")
        time.sleep(1)
                         
        as_utilobj.verify_active_tool("App Studio - Alert - WebFOCUS Alert Assist","Step 10: Verified Alert Assist tool opens in AS canvas. AS ribbon is minimized, QA tools are disabled, except for New and Open.")
        time.sleep(2)
        
        '''Step 11: Close Visual1 - WebFOCUS InfoAssist+ by clicking on X'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='New_Folder1',click="Refresh Descendants")
         
        as_utilobj.close_canvas_item()
        time.sleep(5) 
        
        as_utilobj.verify_active_tool("App Studio","Step 11: Verified Alert Assist closes. New Alert was not added to the folder in the tree")  
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()