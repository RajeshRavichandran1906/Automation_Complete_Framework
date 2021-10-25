'''@author: Adithyaa AK 

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_id=156690&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223848'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2223848_TestClass(AS_BaseTestCase):
    def test_C2223848(self):
    
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
         
        '''Step 01: Click on the Chart icon in the Home Ribbon'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="Chart") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Chart Wizard","Step 01: Chart wizard opens. Available options are: Create Chart, Create SQL Chart & Open Existing")
        time.sleep(1)
        
        '''Step 02: Click "Create Chart'''
        
        as_utilobj.click_element_using_ui(button_item=True,id="1584") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Chart Wizard - Creating a new chart procedure","Step 02: Verify create Chart wizard invokes with choosing the location for new Chart ")
        time.sleep(1)
        
        '''Step 03: Click "Back", click "Create SQL Chart"'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="< Back") 
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,id="1576") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Chart Wizard","Step 03: Verify location to create SQL Chart window displayed")
        time.sleep(1)
        
        '''Step 04: Click "Back", click "Open Existing"'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="< Back") 
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,id="1577") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Chart Wizard - Opening Existing File","Step 04: Verify location to open the existing file window displayed")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Cancel") 
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  