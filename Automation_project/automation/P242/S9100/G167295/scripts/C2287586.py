'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287586'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest,time
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2287586_TestClass(AS_BaseTestCase):
    def test_C2287586(self):
        
        '''Creating Object Instance'''
        
        driver = self.driver 
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
         
        as_utilobj.select_home_button()
        
        '''Step 01: Under Home tab, click on drop down arrow next to ? icon, click About,Click OK'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
 
        keys.press(['down','down','down','down','enter'])
        time.sleep(2)   
          
        as_utilobj.Verify_Current_Dialog_Opens("About WebFOCUS App Studio","Step 01: Verify 'Reset Layout' dialog text longer than 256 characters is not truncated in About WebFOCUS Appstudio")
        time.sleep(1)
          
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
                 
        '''Step 02: Click on drop down arrow next to ? icon, click Reset Layout. Click Cancel'''
             
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        keys.press(['down','down','down','enter'])
        time.sleep(2)  
             
        as_utilobj.Verify_Current_Dialog_Opens("Reset Layout","Step 02: Verify 'Reset Layout' dialog text longer than 256 characters is not truncated")
          
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
  
        '''Step 03: Navigate to CC - AppStudio->AS Files & Step 04: Enable the Procedure View panel from Home menu'''
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                            
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)
             
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu='Procedure')
        time.sleep(5)
           
        as_utilobj.select_home_button(move_x=-52,move_y=170)
        time.sleep(1)
          
        as_utilobj.select_component_by_right_click(right_click_folder="Comment",click="New ...",click_sub_menu="Match")
        time.sleep(2)
          
        as_utilobj.select_file_in_dialogs("OK",tree_path="ibisamp",select_file="car.mas")
        time.sleep(3)
    
        '''Step 05,06 & 07: In Procedure View panel, right click Match, choose Open with... - > Native Canva
                    Click on the intersecting blue circles in the Match Preview section of the Match Wizard
                    Click Finish button'''
             
        as_utilobj.verify_element_using_ui("Step 07: Verify Dialog text longer than 256 characters is not truncated in Match section",text_item="Match Wizard - Level 1: Step 2 of 5",)
        time.sleep(1)
          
        as_utilobj.close_canvas_item()
        time.sleep(3)
             
        '''Step 08-11: local project is not automated further'''
             
        '''Step 12:Create a simple report using canvas/tool using CAR file, and add Country field'''
          
        as_utilobj.select_component_by_right_click(right_click_folder="S9100",click="New",click_sub_menu="Report")
        time.sleep(1)
           
        as_utilobj.select_file_in_dialogs("Finish",tree_path="ibisamp",select_file="car.mas")
        time.sleep(1)
          
        '''Step 13: Select COUNTRY field on the canvas and click Hyperlink on the ribbon bar'''
          
        as_utilobj.click_element_using_ui(tree_item="COUNTRY")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(tab_item="Report")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Drill Down")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Add new item")
        time.sleep(1)
        
        keys.hotkey("enter")
        time.sleep(1)
        
        keys.press(['tab','enter'],interval=0.50)
        time.sleep(2)
        
        keys.press(['down','down','enter'])
        time.sleep(1)
            
        as_utilobj.Verify_Current_Dialog_Opens("Drill Down","Step 13: Verify Dialog text longer than 256 characters is not truncated in Report section")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        as_utilobj.select_any_dialog("No")
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()   