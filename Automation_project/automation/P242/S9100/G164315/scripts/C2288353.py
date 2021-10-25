'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288353'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui
from selenium.common.exceptions import NoSuchElementException

class C2288353_TestClass(AS_BaseTestCase):
    def test_C2288353(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01: Right click FWSubfolder ->Security and select Rules 
                    Close Security Rules - FWSubfolder window'''
         
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
         
        tree_path="Domains->S9100->FWSubFolder"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Security",click_sub_menu="Rules...")
        time.sleep(2)
        
        as_utilobj.verify_current_active_tool("App Studio - Security Rules - FWSubFolder","Step 01: WebFOCUS Security window opens displaying Groups and Users and the rules for each",text_to_verify="Groups & Users")
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
         
        '''Step 02: Right click FWSubfolder ->Security and select Rules on this Resource
                    Close Rules on This Resource - FWSubfolder window'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Security",click_sub_menu="Rules on this Resource...")
        time.sleep(2)
 
        as_utilobj.verify_current_active_tool("App Studio - Rules on this Resource - FWSubFolder","Step 02: WebFOCUS Rules on this Resource security window opens",text_to_verify="Include Inherited Rules")
        time.sleep(2)
         
        as_utilobj.close_canvas_item()
        time.sleep(3)
        
        '''Step 03: Right click FWSubfolder ->Security and select Effective Policy
                    Close Effective Policy - FWSubfolder window'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",click="Security",click_sub_menu="Effective Policy...")
        time.sleep(2)

        as_utilobj.verify_current_active_tool("App Studio - Effective Policy - FWSubFolder","Step 03: WebFOCUS Effective Policy security window opens",text_to_verify="Select a specific operation to view the effective Policy on this resource")
        time.sleep(2)
        
        as_utilobj.close_canvas_item() 
        time.sleep(3)
        
        '''Step 04: Right click FWSubfolder ->Security and select Owner
                    Close Set Owner - FWSubfolder window'''
        
        tree_path="S9100"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(2)

        as_utilobj.select_component_by_right_click(right_click_folder="FWSubFolder",send_keys=['down','down','down','down','down','right','down','down','down'])
        time.sleep(3)
        
        try:
            booln=driver.find_element_by_name("Owner..").is_displayed()
            if booln==True:
                pyautogui.press('enter')
                time.sleep(1)
                as_utilobj.verify_current_active_tool("App Studio - Effective Policy - FWSubFolder","Step 04: WebFOCUS Owner security window opens",text_to_verify="Set Resource Owner")
                time.sleep(2)
                as_utilobj.close_canvas_item() 
                time.sleep(1) 
        except NoSuchElementException:
            print("Step 04: WebFOCUS Owner security window opens") 
            
        pyautogui.press(['esc','esc'])
        time.sleep(2)
        
if __name__=='__main__' :
    unittest.main()