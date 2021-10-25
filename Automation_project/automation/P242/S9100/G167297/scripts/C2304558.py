'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?//cases/view/2304558'''

from common.lib.as_basetestcase import AS_BaseTestCase
import time,unittest
from common.lib import as_utility
import pyautogui as keys

class C2304558_TestClass(AS_BaseTestCase):
    def test_C2304558(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver)
        
        as_utilobj.select_home_button()
        time.sleep(1)
    
        '''Step 01: Right click "Home" on the Content section of the Home ribbon'''
        
        keys.click(button='right')
        time.sleep(1)
        
        keys.press("down")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step1_C2304558.png","Step 01: Verify Content section of the Home ribbon displays")
        time.sleep(1)
        
        '''Step 02: Click on "Customize Quick Access Toolbar...'''
        
        as_utilobj.click_element_using_ui(menu_item=True,name="Customize Quick Access Toolbar...")
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Customize","Step 02: Verify Customize Quick Access Toolbar diplays")
        time.sleep(1)
        
        '''Step 03: Click Cancel. Right click "Home" and click "Show Quick Access Toolbar Below the Ribbon'''
        
        as_utilobj.select_any_dialog("Cancel")
        time.sleep(1)
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        keys.click(button='right')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name="Show Quick Access Toolbar Below the Ribbon")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step3_C2304558.png","Step 03: Verify Show Quick Access Toolbar displays below the Ribbon")
        time.sleep(1) 
        
        '''Step 04: Right click "Home" and click "Minimize the Ribbon'''
        
        as_utilobj.select_home_button()
        time.sleep(1)
        
        keys.click(button='right')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name="Minimize the Ribbon")
        time.sleep(1)
        
        as_utilobj.verify_picture_using_sikuli("step4_C2304558.png","Step 04: Verify the ribbon is minimised")
        time.sleep(1) 
         
        '''Step 05: Right click "Home" and click "Show Quick Access Toolbar Above the Ribbon'''
         
        as_utilobj.select_home_button()
        time.sleep(1)
        
        keys.click(button='right')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name="Show Quick Access Toolbar Above the Ribbon")
        time.sleep(1)
         
        '''Step 06: Right click "Home" and unchecked "Minimize the Ribbon'''
         
        as_utilobj.select_home_button()
        time.sleep(1)
        
        keys.click(button='right')
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item=True,name="Minimize the Ribbon")
        time.sleep(1)
        
        as_utilobj.Verify_Element("Report","Step 06: Verify home Ribbon is replaced")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  