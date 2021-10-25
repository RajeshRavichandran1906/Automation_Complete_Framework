'''@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275217'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275217_TestClass(AS_BaseTestCase):
    def test_C2275217(self):
    
        '''Create instance of object '''
        
        driver=self.driver 
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()

        """Step 1. Select first option under Data, Synonym via Metadata Canvas"""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("D","A")
        time.sleep(1)
        keys.hotkey("M","C")
        time.sleep(1)
        
        '''Data Source Definition Wizard opens'''
        
        as_utilobj.Verify_Current_Dialog_Opens("Data Source Definition Wizard","Step 01: Verify the dialog - 'Data Source Definition Wizard' is displayed")
        time.sleep(1)
         
        """Step 2. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        """Step 3. Click down arrow for Data in the Home Ribbon and select the second option, Synonym"""
 
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("D","A")
        time.sleep(1)
        keys.hotkey("S","Y")
        time.sleep(1)

        '''Select Server Node dialog opens'''
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Server Node","Step 03: Verify the dialog - 'Select Server Node' is displayed")
        time.sleep(1)
          
        """Step 4. Click Cancel on dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
          
        """Step 5. Click down arrow for Data in the Home Ribbon and select the third option, Manage Adapters"""
 
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("D","A")
        time.sleep(1)
        keys.hotkey("M","N")
        time.sleep(1)

        '''Select Server Node dialog opens'''
        
        as_utilobj.Verify_Current_Dialog_Opens("Select Server Node","Step 05: Verify the dialog - 'Select Server Node' is displayed")
        time.sleep(1)

        """Step 6. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
          
        """Step 7. Click down arrow for Data in the Home Ribbon and select fourth option, Data Source Password"""
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("D","A")
        time.sleep(1)
        keys.hotkey("D","P")
        time.sleep(1)

        '''A password input box opens'''
        
        as_utilobj.Verify_Current_Dialog_Opens("Password Dialog","Step 07: Verify Password Dialog is displayed")
        time.sleep(1)

        """Step 8. Click Cancel to close it"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
          
        """Step 9. Click down arrow for Data in the Home Ribbon and select the last option, Rebuild Data Source."""
 
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(2)
        keys.hotkey("D","A")
        time.sleep(1)
        keys.hotkey("R","B")
        time.sleep(1)

        '''Rebuild dialog opens'''
        
        as_utilobj.Verify_Current_Dialog_Opens("Rebuild","Step 09: Verify the dialog - 'Rebuild' is displayed")
        time.sleep(1)
        
        """Step 10. Click Cancel to close dialog"""
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()