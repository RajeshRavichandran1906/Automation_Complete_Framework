'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2287570'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2287570_TestClass(AS_BaseTestCase):
    def test_C2287570(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        time.sleep(1)
      
        '''Step 01: Click on the drop down arrow (Customize Quick Access Toolbar) Click "More Commands..."'''
        
        as_utilobj.click_element_using_ui(split_button="Customize Quick Access Toolbar")
        time.sleep(1)
        
        '''Step 02: Choose "More Commands...
                    Double-click each item in the right listbox to remove it
                    Click OK
                    Close App Studio"'''
        
        as_utilobj.click_element_using_ui(menu_item="True",name="More Commands...")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Remove")
        time.sleep(1)
         
        as_utilobj.click_element_using_ui(button_item=True,name="OK")
        time.sleep(2)
        
        as_utilobj.select_home_button()
        time.sleep(3)
        
        as_utilobj.verify_active_tool("App Studio","Step 02: Verify App studio did not crash after removing all icons in Quick Access Toolbar")
        time.sleep(3)
    
        '''Step 03: Restart App Studio
                    Click on the drop down arrow
                    Click "More Commands..."
                    Click Reset'''
        
        as_utilobj.click_element_using_ui(split_button="Customize Quick Access Toolbar")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(menu_item="True",name="More Commands...")
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Reset")
        time.sleep(2)
        
        as_utilobj.click_element_using_ui(button_item=True,name="OK")
        time.sleep(2)
        
        as_utilobj.select_any_dialog("OK")
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  