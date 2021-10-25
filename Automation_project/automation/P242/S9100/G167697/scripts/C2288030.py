'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288030'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from selenium import webdriver
from common.pages import as_ribbon
from common.lib import as_utility
import pyautogui as keys
import uiautomation as automation

class C2288030_TestClass(AS_BaseTestCase):
    def test_C2288030(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver) 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Unchecked Environments Detail from the View group 
                    Select Reset Layout from the top-right-most menu
                    Select Yes in the Reset Layout dialog
                    Click OK'''
           
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Detail")
        time.sleep(1)
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
     
        keys.press(['down','down','down','enter'])
        time.sleep(2)
         
        as_utilobj.Verify_Current_Dialog_Opens("Reset Layout","Step 01: Verify Reset layout invokes")
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(radio_button="1688")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
         
        '''Step 02: Click on AS menu->Options
                    Select Environments 
                    Click Cancel'''
         
        as_utilobj.select_application_menu_options(options=True)
        time.sleep(1)
         
        as_utilobj.Verify_Current_Dialog_Opens("App Studio Options","Step 02: Verify App studio options invokes")
        time.sleep(1)
         
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
          
        '''Step 03: Click on AS menu->Exit
                    Re-Start App Studio'''
        
        as_utilobj.select_application_menu_options(send_keys=['up'])
        time.sleep(25)
        
        aspath=as_utility.AS_Utillity_Methods.parseinitfile(self,"aspath")
        driver = webdriver.Remote(command_executor='http://localhost:9999',desired_capabilities={'debugConnectToRunningApp': 'false','app': aspath}) 
        time.sleep(40)
        
        automation.WindowControl(ClassName="#32770").Close()
        time.sleep(1)
        
        as_utilobj.verify_element_using_ui("Step 03: Environments Detail panel is closed, and Environments Detail check-box in Home ribbon is un-checked.",check_box="Environments Detail")
        time.sleep(2)
        
        '''Step 04: From View group, Un-check Environments Tree
                    Check Environments Detail'''
                 
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Tree")
        time.sleep(1)
        
        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Detail")
        time.sleep(1)
        
        automation.DragDrop(200,212,325,212)
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()  