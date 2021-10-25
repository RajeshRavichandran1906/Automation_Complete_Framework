'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275204'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275204_TestClass(AS_BaseTestCase):
    def test_C2275204(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj=as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        
        '''Step 01: Press Alt, press S (for Style)'''
                
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
            
        as_utilobj.verify_picture_using_sikuli("step1_C2275204.png","Step 1: Verified - The Style menu expands showing hotkeys for each option")
        time.sleep(2)
                
        '''Step 02: Press A (for aqua)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_A, waitTime=3)
        time.sleep(2)
        
        as_utilobj.Verify_Element("App Studio","Step 2: Verified - Color scheme changes accordingly",available=True)
        time.sleep(1)
                        
        '''Step 03: Press Alt key, press S (for style menu), press S (for silver)'''
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)   

        as_utilobj.Verify_Element("App Studio","Step 3: Verified - Color scheme changes accordingly",available=True)
        time.sleep(1)
                
        '''Step 04: Press Alt key, press S (for style menu), press L (for black)'''
            
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_L, waitTime=3)
        time.sleep(2) 
        
        as_utilobj.Verify_Element("App Studio","Step 4: Verified - Color scheme changes accordingly",available=True)
        time.sleep(1)
                
        '''Step 05: Press Alt key, press S (for style menu), press B (for Blue)'''
            
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_B, waitTime=3)
        time.sleep(2) 
        
        as_utilobj.Verify_Element("App Studio","Step 5: Verified - Color scheme changes accordingly",available=True)
        time.sleep(1)
                
        '''Step 06: Press Alt key, press S (for style menu), press D (for default)'''
            
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_S, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_D, waitTime=3)
        time.sleep(2) 
        
        as_utilobj.Verify_Element("App Studio","Step 6: Verified - Color scheme changes accordingly",available=True)
        time.sleep(1)
                
if __name__=='__main__' :
    unittest.main()              