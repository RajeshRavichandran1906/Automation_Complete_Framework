'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288881'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import keyboard as keys

class C2288881_TestClass(AS_BaseTestCase):
    def test_C2288881(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
    
        as_utilobj.select_home_button()
        
        '''Step 01 & 02: Under WebFOCUS Administration drop down menu, select Reporting Server Console
                    Click on Application Settings
                    Close WebFOCUS 82M Server... tab'''''
        
        as_utilobj.logout_conf_env(webfocus_environment=True)
        time.sleep(4)
                                          
        tree_path=as_utility.AS_Utillity_Methods.parseinitfile(self,"webfocus_environment")
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(3)
          
        as_utilobj.click_element_using_ui(split_button='WebFOCUS Administration',send_keys=['down','down','enter'])  
        time.sleep(4)              
                  
        as_utilobj.Verify_Browser_Content("IEFrame","Step 01: Verified reporting server console invoked",verify_browser=True,browser_close=True)
        time.sleep(2)
  
        '''Step 03: Right click on Applications and select New Application Directory
                    Hit Enter
                    Right click on newapp and select New Application Directory
                    Hit Enter'''
          
        tree_path="Data Servers->EDASERVE"
        as_utilobj.select_tree_view_pane_item(tree_path) 
        time.sleep(5)
                
        as_utilobj.select_component_by_right_click(right_click_folder="Applications",click='New Application Directory')
        keys.press('enter')
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="newapp",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp1')
        keys.press('enter')
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="newapp1",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp2')
        keys.press('enter')
        time.sleep(2)
         
        '''Step 04: Right click on sub application newapp and select New Application Directory
                    Hit Enter 
                    Right click on sub sub newapp and select New Application Directory
                    Hit Enter'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="newapp2",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp3')
        keys.press('enter')
        time.sleep(2)
         
        as_utilobj.select_component_by_right_click(right_click_folder="newapp3",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp4')
        keys.press('enter')
        time.sleep(2)
         
        '''Step 05: Right click on sub sub sub newapp and select New Application Directory
                    Hit Enter 
                    Right click on sub sub sub sub sub newapp and select New Application Directory
                    Hit Enter'''
         
        as_utilobj.select_component_by_right_click(right_click_folder="newapp4",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp5')
        keys.press('enter')
        time.sleep(2)
        
        as_utilobj.select_component_by_right_click(right_click_folder="newapp5",click="New",click_sub_menu='Application Directory')
        time.sleep(1)
        keys.write('newapp6')
        keys.press('enter')
        time.sleep(2)
        
        '''Step 06: Right click on sub sub sub sub sub sub newapp and select New Application Directory
                    Hit Enter 
                    Click OK in App Studio window
                    Right click on newapp folder and select Delete
                    Click Yes to delete'''

        as_utilobj.Verify_Current_Dialog_Closes("newapp6","Step 06: Verified error message prompt displays for 6th application directory")
            
        as_utilobj.select_component_by_right_click(right_click_folder="newapp",click='Delete')
        time.sleep(1)
        
        as_utilobj.select_any_dialog("Yes")
            
if __name__=='__main__' :
    unittest.main()  