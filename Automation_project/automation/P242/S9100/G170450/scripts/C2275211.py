'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275211'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation
import pyautogui as keys

class C2275211_TestClass(AS_BaseTestCase):
    def test_C2275211(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
    
        '''Step 1a: Double click a report to open in report canvas'''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
        
        tree_path="Domains->S9100->Report1"            
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)  
   
        '''Step 1b: Press Alt key, press 09 (for Run menu), press O (for message viewer on). Click the Run drop down menu and review the options'''
            
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        keys.hotkey('0','9')
        time.sleep(1)
        automation.SendKey(automation.Keys.VK_O, waitTime=3)
        time.sleep(3)
    
        automation.SplitButtonControl(Name="Run").Click(ratioX=0.82,ratioY=0.30,waitTime=1)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2275211.png","Step 01: Verify - Message Viewer On is selected")
        time.sleep(3)
        
        '''Step 02: Press Alt key, press 09 (for Run menu), press C (for display command lines). Click the Run drop down menu and review the options'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        keys.hotkey('0','9')
        time.sleep(1)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(3)
    
        automation.SplitButtonControl(Name="Run").Click(ratioX =0.82, ratioY =0.30,waitTime=2)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli("step2_C2275211.png","Step 02: Verify - Display Command Lines is selected")
        time.sleep(1)
         
        '''Step 03: Press Alt key, press 09 (for Run menu), press D (for display dialogue manager commands). Click the Run drop down menu and review the options'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        keys.hotkey('0','9')
        time.sleep(1)
        automation.SendKey(automation.Keys.VK_D, waitTime=3)
        time.sleep(3)
    
        automation.SplitButtonControl(Name="Run").Click(ratioX =0.82, ratioY =0.30,waitTime=2)
        time.sleep(1)
         
        as_utilobj.verify_picture_using_sikuli("step3_C2275211.png","Step 3: Verified - Display Dialogue Manager commands is selected")
        time.sleep(1)
         
        '''Step 04: Press Alt key, press 09 (for Run menu), press F (for message viewer off). Click the Run drop down menu and review the options'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        keys.hotkey('0','9')
        time.sleep(1)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(3)
    
        automation.SplitButtonControl(Name="Run").Click(ratioX =0.82, ratioY =0.30,waitTime=2)
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step4_C2275211.png","Step 4: Verified - Message Viewer Off is selected")
        time.sleep(1)
        
        '''Step 05: Close the report'''
         
        as_utilobj.close_canvas_item()
        time.sleep(4)

if __name__=='__main__' :
    unittest.main()  