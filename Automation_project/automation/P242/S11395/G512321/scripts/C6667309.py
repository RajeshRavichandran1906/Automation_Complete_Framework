'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667309'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C6667309_TestClass(AS_BaseTestCase):
    def test_C6667309(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
         
        '''Step 01: Right click New Folder1 under Domains and select New>Procedure.'''
                  
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.ui_double_click_tree_view_item(tree_path) 
        time.sleep(3)
                
        tree_path="Domains->S9100->New Folder1"
        as_utilobj.ui_double_click_tree_view_item(tree_path)
        time.sleep(6)
            
        as_utilobj.select_component_by_right_click(right_click_folder='New Folder1',click="New",click_sub_menu='Procedure')
        time.sleep(4)
              
        as_utilobj.verify_active_tool('App Studio - Procedure1',"Step 01: Verified Procedure Opens Successfully")
        time.sleep(2)
                   
        """Step 02: Close Procedure1 by clicking the X on the Procedure1 tab"""
             
        as_utilobj.close_canvas_item()
        time.sleep(2)   
               
        as_utilobj.verify_active_tool('App Studio',"Step 02: Verified Procedure Closed Successfully") 
        time.sleep(1)  
              
        '''Step 03: Right click New Folder1 under Domains and select New>Procedure via Text Editor'''
                      
        as_utilobj.select_component_by_right_click(right_click_folder='New Folder1',click="New",click_sub_menu='Procedure via Text Editor')
        time.sleep(2)
              
        as_utilobj.verify_active_tool('App Studio - Edit Procedure1.fex',"Step 03: Verified Procedure via text editor Opens Successfully")   
        time.sleep(1)
               
        '''Step 04: Close Edit Procedure1 by clicking the X on the Edit Procedure1 tab.'''
  
        as_utilobj.close_canvas_item()
        time.sleep(3) 
               
        as_utilobj.verify_active_tool('App Studio',"Step 04: Verified Procedure via text editor Closed Successfully") 
        time.sleep(2)
              
        '''Step 05: Right click New Folder1 under Domains and select New>Report'''
            
        as_utilobj.select_component_by_right_click(right_click_folder='New Folder1',click="New",click_sub_menu='Report')
        time.sleep(3)
          
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source","Step 05: Verified data source dialog invoked for report")
        time.sleep(2)
            
        '''Step 06 & 07: Select ibisamp and Select car.mas and click OK'''
                 
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(8)
            
        as_utilobj.verify_active_tool("App Studio - Report1*","Step 06 & 07: Verified Report Invokes Successfully")
        time.sleep(2)
            
        '''Step 08: Click on Procedure View tab to open panel.Close Report1 tab by clicking X'''
         
        as_utilobj.close_canvas_item()
        time.sleep(5) 
            
        as_utilobj.verify_active_tool("App Studio","Step 08: Verified Report closes without a saved prompt")
        time.sleep(2)
           
        '''Step 09: Right click New Folder1 under Domains and select New>SQL Report.'''
          
        as_utilobj.select_component_by_right_click(right_click_folder='New Folder1',click="New",click_sub_menu='SQL Report')
        time.sleep(2) 
          
        as_utilobj.Verify_Current_Dialog_Opens("SQL Report Wizard - Welcome","Step 09: Verified SQL Report wizard been displayed")
        time.sleep(2)
          
        '''Step 10: Click Cancel on wizard'''
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
          
        as_utilobj.Verify_Current_Dialog_Closes("SQL Report Wizard - Welcome","Step 10: Verified Wizard closes. New report was not added to the folder in the tree")
        time.sleep(1)
         
        '''Step 11: Right click New Folder1 under Domains and select New>Chart.'''
         
        as_utilobj.select_component_by_right_click(right_click_folder='New Folder1',click="New",click_sub_menu='Chart')
        time.sleep(8)
          
        as_utilobj.Verify_Current_Dialog_Opens("Select Data Source","Step 11: Verified Select data source dialog invoked for chart")
        time.sleep(2) 
        
        '''Step 12&13: Select ibisamp and Select car.mas and click OK'''
               
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(10)
          
        as_utilobj.verify_active_tool("App Studio - Chart1","Step 12: Verified Chart canvas opens with the default name Chart1 (or n+1). \n Step 13: Verified Procedure View shows the Chart component highlighted.")
        time.sleep(2) 
          
        '''Step 14: Click on Procedure View tab to open panel.Close Report1 tab by clicking X'''
        
        as_utilobj.close_canvas_item()
        time.sleep(10) 
         
        as_utilobj.verify_active_tool("App Studio","Step 14: Chart closes without a save prompt. Chart is not saved to the folder.")
        time.sleep(2) 
         
if __name__=='__main__' :
    unittest.main()   