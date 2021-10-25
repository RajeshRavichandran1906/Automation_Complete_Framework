'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275205'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275205_TestClass(AS_BaseTestCase):
    def test_C2275205(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
                
        '''Step 01: Press Alt, press E (for help menu)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
          
        as_utilobj.verify_picture_using_sikuli("step1_C2275205.png","Step 01: Verify - Help menu expands displaying hotkeys for each option")
        time.sleep(3)
          
        automation.SendKey(automation.Keys.VK_ESCAPE, waitTime=3)
        time.sleep(2)
                
        '''Step 02: Press H (for help topics)'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_H, waitTime=3)
        time.sleep(8)
          
        as_utilobj.Verify_Current_Dialog_Opens("App Studio Help","Step 02: Verify - Help file opens")   
        time.sleep(3)
         
        as_utilobj.click_element_using_ui(close_dialog_window="App Studio Help")        
        time.sleep(1)
                 
        '''Step 03: Close Help window. Press Alt key, press E (for help menu), press F (Focal Point Forums).'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(25)
          
        as_utilobj.Verify_Browser_Content("IEFrame","Step 03: Verify that focal point forums displayed",verify_browser=True,browser_close=True) 
        time.sleep(4)
                     
        '''Step 04: Close Help window. Press Alt key, press E (for help menu), press W (for welcome screen)'''
    
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_W, waitTime=3)
        time.sleep(6)
        
        as_utilobj.Verify_Element("Welcome to App Studio","Step 04: Verify - Welcome screen displays",available=True)
        time.sleep(1)
        
        automation.WindowControl(ClassName="#32770").Close()       
        time.sleep(1)

        '''Step 05: Close Welcome Screen. Press Alt key, press E (for help menu), press A (for about)'''
    
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("About WebFOCUS App Studio","Step 05: Verify - About window opens")
        time.sleep(2)
                
        as_utilobj.select_any_dialog("OK") 
        time.sleep(2)
            
        '''Step 06: Click ok on about window. Press Alt key, press E (for help menu), press R (for reset). '''
    
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_E, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_R, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Current_Dialog_Opens("Reset Layout","Step 06: Verify - Reset Layout confirmation screen displays with 2 options, Yes and No")
        time.sleep(3)
        
        '''Step 07: Say yes to pop up and click OK.'''
    
        as_utilobj.select_any_dialog("OK")     
        time.sleep(1)   
        
if __name__=='__main__' :
    unittest.main()