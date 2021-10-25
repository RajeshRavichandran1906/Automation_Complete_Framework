'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288334'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility
from common.pages import as_panels

class C2288334_TestClass(AS_BaseTestCase):
    def test_C2288334(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        as_panel_obj=as_panels.AS_Panels(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: In Environments Tree, set Filter to All Files
                    Right click FWSubfolder under Domains and select New>Procedure.'''
           
        as_panel_obj.environment_panel_file_filter(filter="All Files")
              
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
           
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu='Procedure')
        time.sleep(3)
           
        as_utilobj.verify_active_tool("App Studio - Procedure1","Step 01: Verified Procedure Opens")
        time.sleep(2)
                   
        '''Step 02: Close Procedure1 by clicking the X on the Procedure1 tab'''
              
        as_utilobj.close_canvas_item()
        time.sleep(1)   
            
        as_utilobj.verify_active_tool("App Studio","Step 02: Verified Procedure Closed and new procedure was not added to the folder")   
        time.sleep(1)
             
        '''Step 03: Right click FWSubfolder under Domains and select New>Procedure via Text Editor.'''
                     
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="New",click_sub_menu='Procedure via Text Editor')
        time.sleep(2)
            
        as_utilobj.verify_active_tool('App Studio - Edit Procedure1.fex',"Step 03: Verified Procedure via text editor Opens Successfully")   
        time.sleep(2)
               
        '''Step 04: Close Edit Procedure1 by clicking the X on the Edit Procedure1 tab.'''
             
        as_utilobj.close_canvas_item()
        time.sleep(1)  
            
        as_utilobj.verify_active_tool('App Studio',"Step 04: Verified Procedure via text editor Closed Successfully") 
        time.sleep(2)
             
        '''Step 05: Right click FWSubfolder under Domains and select New>Report.
                    Navigate to ibisamp, click car.mas
                    Click Finish'''
                    
        as_utilobj.select_component_by_right_click(right_click_folder='FWSubFolder',click="New",click_sub_menu='Report')
        time.sleep(5)
         
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source","Step 05: Verified data source dialog invoked for report")
        time.sleep(2)
                
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(4)
            
        as_utilobj.verify_active_tool("App Studio - Report1*","Step 05: Verified Report Invokes Successfully")
        time.sleep(2)   
        
        '''Step 06: Close Report1'''
         
        as_utilobj.close_canvas_item()
        time.sleep(1) 
            
        as_utilobj.verify_active_tool("App Studio","Step 06: Verified Report closes without a saved prompt")
        time.sleep(2)
            
        '''Step 07: Right click FWSubfolder under Domains and select New>SQL Report
                    Select "Type SQL statement in this report request" radio button 
                    Click Next
                    Click Next'''
          
        as_utilobj.select_component_by_right_click(right_click_folder='FWSubFolder',click="New",click_sub_menu='SQL Report')
        time.sleep(1) 
        
        as_utilobj.click_element_using_ui(radio_button="7020")
          
        as_utilobj.select_any_dialog("Next >")
        time.sleep(5)
          
        as_utilobj.select_any_dialog("Next >")
        time.sleep(1)
          
        as_utilobj.Verify_Current_Dialog_Opens("SQL Report Wizard - Enter SQL statements","Step 07: Verified SQL Report Wizard - Data access information")
        time.sleep(1)
           
        '''Step 08: Click Cancel on wizard'''
           
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
           
        as_utilobj.Verify_Current_Dialog_Closes("SQL Report Wizard - Enter SQL statements","Step 08: Verified SQL Report Wizard closed. The new SQL report was not added to sub folder in the tree")
        time.sleep(1)
         
        '''Step 09: Right click FWSubfolder under Domains and select New>Chart
                    Navigate to ibisamp, click car.mas
                    Click Finish'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='FWSubFolder',click="New",click_sub_menu='Chart')
        time.sleep(10)
             
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(4)
         
        as_utilobj.verify_active_tool("App Studio - Chart1","Step 09: Verified Chart canvas opens with the default name Chart1 (or n+1).")
        time.sleep(2)
         
        '''Step 10: Close Chart1'''
                 
        as_utilobj.close_canvas_item()
        time.sleep(4)
         
        as_utilobj.verify_active_tool("App Studio","Step 10: Chart closes without a save prompt. Chart is not added to the folder.")
        time.sleep(1)
         
if __name__=='__main__' :
    unittest.main()           