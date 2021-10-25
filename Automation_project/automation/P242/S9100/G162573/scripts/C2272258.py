'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2272258'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
from common.pages import as_ribbon
import uiautomation as automation

class C2272258_TestClass(AS_BaseTestCase):
    def test_C2272258(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver)
        
        as_utilobj.select_home_button()
          
        '''Signing into Localhost'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
         
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Data Servers->EDASERVE->Applications->baseapp"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="New",click_sub_menu="Synonym via Metadata Canvas")
        time.sleep(2) 
         
        as_utilobj.select_any_dialog("Select")
        time.sleep(15)
        
        as_utilobj.select_any_dialog("Yes")
        time.sleep(30)
        
        '''Clipboard Tab'''
             
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Delete','Delete (Del)',"Step 01: Verified Clipboard Tooltip is Delete (Del) - Erase the selection",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Cut','Cut (Ctrl+X)',"Step 02: Verified Clipboard Tooltip is Cut (CTLR+X) - Cut the selection and put it on the clipboard",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Copy','Copy (Ctrl+C)',"Step 03: Verified Clipboard Tooltip is Copy (Ctrl+C) - Copy the selection and put it on the clipboard",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Paste','Paste (Ctrl+V)',"Step 04: Verified Clipboard Tooltip is Paste (Ctrl+V) - Insert clipboard contents",move_x=5,move_y=5)
        time.sleep(1)
          
        '''Editing Tab'''
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Find','Find (Ctrl+F)',"Step 05: Verified Editing Tooltip is Find (Ctrl+F) - Find the specific text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Find Next',"Step 06: Verified Editing Tooltip is Find Next - Click the Find Next button to find the next match ",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Find Previous',"Step 07: Verified Editing Tooltip is Find Previous - Click the Find Previous button to find the previous match",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Select All','Select All (Ctrl+A)',"Step 08: Verified Editing Tooltip is Select All (Ctrl+A) - Select the entire document",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Diff_Tooltip('Metadata','Replace','Replace (Ctrl+H)',"Step 09: Verified Editing Tooltip is Replace (Ctrl+H) - Replace specific text with different text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Go To',"Step 10: Verified Editing Tooltip is Go To- Moves to a specified location",move_x=5,move_y=5)
        time.sleep(1)
         
        as_ribbon_obj.Verify_Tooltip('Metadata','Invert Case',"Step 11: Verified Editing Tooltip is Invert Case - Invert Case of the selected text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Upper Case',"Step 12: Verified Editing Tooltip is Upper Case - Upper case selected text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Lower Case',"Step 13: Verified Editing Tooltip is Lower Case - Lower Case selected text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Comment Selection',"Step 14: Verified Editing Tooltip is Comment Selection - Comment selected text",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Uncomment Selection',"Step 15: Verified Editing Tooltip is Uncomment Selection - Uncomment selected text",move_x=5,move_y=5)
        time.sleep(1)
          
        '''View Tab'''
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Field',"Step 16: Verified View Tooltip is Field - Switch to Field View",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Segment',"Step 17: Verified View Tooltip is Segment - Switch to Segment View",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','List',"Step 18: Verified View Tooltip is List - Switch to List View",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Modeling',"Step 19: Verified View Tooltip is Modeling - Switch to Modeling View",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Text',"Step 20: Verified View Tooltip is Text - Switch to Synonym Text View",move_x=5,move_y=5)
        time.sleep(1)
         
        as_ribbon_obj.Verify_Tooltip('Metadata','Access File Text',"Step 21: Verified View Tooltip is Access File text - Switch to Access File Text View",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Aerial View',"Step 22: Verified View Tooltip is Aerial View - Shows or Hides Aerial View",move_x=5,move_y=5)
        time.sleep(1)
          
        '''Insert Tab'''
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Insert',"Step 23: Verified Insert Tooltip is Insert - Insert New Node",move_x=5,move_y=5)
        time.sleep(1)
          
        '''Reports Tab'''
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Sample Data',"Step 24: Verified Reports Tooltip is Sample Data - Run Sample data Report",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Data Profiling',"Step 25: Verified Reports Tooltip is Data Profiling - Data Profiling Reports",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Impact Analysis',"Step 26: Verified Reports Tooltip is Impact Analysis - Run Impact Analysis Report",move_x=5,move_y=5)
        time.sleep(1)
          
        '''Tools Tab'''
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Properties',"Step 27: Verified Tools Tooltip is Properties - Show/Hide Properties",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Quick Copy',"Step 28: Verified Tools Tooltip is Quick Copy - Quick Copy",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','DBA',"Step 29: Verified Tools Tooltip is DBA - Shows or Hides DBA",move_x=5,move_y=5)
        time.sleep(1)
          
        as_ribbon_obj.Verify_Tooltip('Metadata','Business View',"Step 30: Verified Tools Tooltip is Business View - Shows or Hides Business View",move_x=5,move_y=5)
        time.sleep(2)
       
        as_ribbon_obj.Verify_Tooltip('Metadata','Options','Step 31: Verified Tools Tooltip is Options - Setup user preferences',move_x=5,move_y=5)
        time.sleep(2)
        
        '''close tool opened in canvas area'''
        
        as_utilobj.select_component_by_right_click(right_click_folder="baseapp",click="Refresh Descendants")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(10)

if __name__=='__main__' :
    unittest.main()