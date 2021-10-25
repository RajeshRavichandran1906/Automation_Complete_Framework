'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224440'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys
from common.locators import as_uiautomation_mainpage_locators,as_components_ui_locators

class C2304545_TestClass(AS_BaseTestCase):
    def test_C2304545(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        locators=as_uiautomation_mainpage_locators.ASMainpageLocators()
        component_locators=as_components_ui_locators.ASComponentsLocators()
        
        '''Testcase property variables'''
        
        key_pattern=["down","down","down","enter"]
        buttons=["User's Manual","Introducing the Interface","App Studio Technical Library"]
        media_player_window="Now Playing"
        wait_time=[1,2,3,4,5,6,7,8,9,10,11] 
        
        '''Testcase verification'''
        
        browser_window="IEFrame"
        verify_images=["step1_C2304545.png","step2_C2304545.png","step3_C2304545.png","step4_C2304545.png"]
        verify_msg_1="Step 01: Verify Welcome Screen displays"
        verify_msg_2="Step 02: Verify User's Manual invoked in IE Browser"
        verify_msg_3="Step 03: Verify Introducing the Interface video invoked"
        verify_msg_4="Step 04: Verify App Studio Technical Library invokes"
        
        '''Testscript'''
        
        as_utilobj.select_home_button()
        
        '''Step 01 : Click the arrow down next to Help at top right of window and select Display Welcome screen.'''
        
        as_utilobj.click_element_using_ui(split_button_with_offset=locators.help_page_button,x=0.85,y=0.35)
        time.sleep(wait_time[0])
        keys.press(key_pattern)
        time.sleep(wait_time[0])
        
        as_utilobj.verify_picture_using_sikuli(verify_images[0],verify_msg_1)
        time.sleep(wait_time[2])
        
        '''Step 02: Click "User's Manual".'''
         
        as_utilobj.click_element_using_ui(button_item=True,name=buttons[0])
        time.sleep(wait_time[8])
         
        as_utilobj.verify_picture_using_sikuli(verify_images[1],verify_msg_2)
        time.sleep(wait_time[2])
         
        as_utilobj.Verify_Browser_Content(browser_window,msg=None,browser_close=True)
        time.sleep(wait_time[4])
         
        '''Step 03: Click Introducing the Interface '''
        
        as_utilobj.click_element_using_ui(button_item=True,name=buttons[1])
        time.sleep(wait_time[10])
        
        as_utilobj.verify_picture_using_sikuli(verify_images[2],verify_msg_3)
        time.sleep(wait_time[2])
        
        as_utilobj.click_element_using_ui(close_dialog_window=media_player_window)
        time.sleep(wait_time[2])
        
        '''Step 04: Click "Technical Content".'''
        
        as_utilobj.click_element_using_ui(button_item=True,name=buttons[2])
        time.sleep(wait_time[10])
        
        as_utilobj.verify_picture_using_sikuli(verify_images[3],verify_msg_4)
        time.sleep(wait_time[4])
        
        as_utilobj.Verify_Browser_Content(browser_window,msg=None,browser_close=True)
        time.sleep(wait_time[4])
        
        driver.find_element_by_class_name(component_locators.dialog_class_name).find_element_by_name(component_locators.close_button).click()  
        time.sleep(wait_time[1])
        
if __name__=='__main__' :
    unittest.main()  