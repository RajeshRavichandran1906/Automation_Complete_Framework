'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287643'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.pages import as_ribbon
from common.lib import as_utility
import uiautomation as automation

class C2287643_TestClass(AS_BaseTestCase):
    def test_C2287643(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_ribbon_obj= as_ribbon.AS_Ribbon(driver) 
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''ENVIRONMENT TREE'''
             
        '''Step 01: In Environments Tree, right-click Domains>Public and select Security | Rules...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Security Rules - Public tab by clicking X'''
                 
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)  
                
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Rules...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 01: Verify the Open File dialog appear when Rules... is opened")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
               
        '''Step 02: Right-click Domains>Public and select Security | Rules on this Resource...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Security Rules - Public tab by clicking X'''
               
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Rules on this Resource...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 02: Verify the Open File dialog appear when Rules on this Resource... is opened")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
               
        '''Step 03: Right-click Domains>Public and select Security | Effective Policy...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Security Rules - Public tab by clicking X'''
              
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Effective Policy...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 03: Verify the Open File dialog appear when Effective Policy.... is opened")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
        
        '''ENVIRONMENT DETAILS'''
          
        '''Step 06: Check Environments Detail in the View group
                    Right-click Domains>Public and select Security | Rules...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Security Rules - Public tab by clicking X'''
        
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Tree")
        time.sleep(1)
        
        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Detail")
        time.sleep(1)
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
              
        tree_path="Domains->S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(6)  
                
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Rules...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 04: Verify the Open File dialog appear when Rules... is opened in Environment Detail")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
             
        '''Step 07: Right-click Domains>Public and select Security | Rules on this Resource...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Rules on this Resources - Public tab by clicking X'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Rules on this Resource...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 05: Verify the Open File dialog appear when Rules on this Resource... is opened in Environment Detail")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
        
        '''Step 08: Right-click Domains>Public and select Security | Effective Policy...
                    Click Open on the QAT or AS menu
                    Click Cancel
                    Close the Rules on this Resources - Public tab by clicking X'''
        
        as_utilobj.select_component_by_right_click(right_click_folder='S9100',click="Security",click_sub_menu='Effective Policy...')
        time.sleep(4)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Open...") 
        time.sleep(1)
                
        as_utilobj.Verify_Current_Dialog_Opens("Open File","Step 06: Verify the Open File dialog appear when Effective Policy.... is opened")
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        automation.SendKey(automation.Keys.VK_MENU, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_F, waitTime=3)
        time.sleep(2)
        automation.SendKey(automation.Keys.VK_C, waitTime=3)
        time.sleep(2)
        
        as_ribbon_obj.verify_click_checkbox("No Message",uncheck="Environments Detail")
        time.sleep(1)
        
        as_ribbon_obj.verify_click_checkbox("No Message",click="Environments Tree")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  