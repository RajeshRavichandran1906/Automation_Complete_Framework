'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275198'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import uiautomation as automation

class C2275198_TestClass(AS_BaseTestCase):
    def test_C2275198(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: Open existing report. Press Alt key, press F (for app menu), press M (for message viewer options)'''   
             
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                   
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
                 
        as_utilobj.select_tree_view_pane_item("Domains->S9100->Report1" ) 
        time.sleep(2)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        as_utilobj.select_component_by_right_click(right_click_folder="Domains",click="Refresh Descendants")
        time.sleep(1)

        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_M, waitTime=5)
        time.sleep(2)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2275198.png","Step 01: Verify Message Viewer hotkeys are enabled")
        time.sleep(5)
        
        '''Step 02: Press O (for Message Viewer On)'''
         
        automation.SendKey(automation.Keys.VK_O, waitTime=2)
        time.sleep(2)
         
        as_utilobj.Verify_Element("Message Viewer ON","Step 02: Verify Message Viewer ON hotkey is enabled",unavailable=True)
        time.sleep(2)
         
        '''Step 03: Click on report canvas. Press Alt key, press F (for app menu), press M (for message viewer options), press C (for display command lines)'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_M, waitTime=5)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=2)
        time.sleep(2)
        
        as_utilobj.Verify_Element("Display command lines","Step 03: Verify Display Command Lines is enabled",unavailable=True)
        time.sleep(2)

        '''Step 04: Click on report canvas. Press Alt key, press F (for app menu), press M (for message viewer options), press D (for display dialog mgr. commands)'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_M, waitTime=5)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_D, waitTime=2)
        time.sleep(2)
         
        as_utilobj.Verify_Element("Display dialogue manager commands","Step 04: Verify Display dialogue manager commands is enabled",unavailable=True)
        time.sleep(2)
         
        '''Step 05: Click on report canvas. Press Alt key, press F (for app menu), press M (for message viewer options), press F (for Message Viewer Off)'''
         
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_M, waitTime=5)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=2)
        time.sleep(2)
        
        as_utilobj.Verify_Element("Message Viewer OFF","Step 05: Verify message viewer off is enabled",unavailable=True)
        time.sleep(2)
        
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
if __name__=='__main__' :
    unittest.main()  