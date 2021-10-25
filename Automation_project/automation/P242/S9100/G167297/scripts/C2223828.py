'''
@author: Adithyaa AK

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9100&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223828'''

from common.lib.as_basetestcase import AS_BaseTestCase
import unittest, time
from common.lib import as_utility

class C2223828_TestClass(AS_BaseTestCase):
    def test_C2223828(self):
        
        '''Create instance of object '''
        
        driver=self.driver
        as_utilobj= as_utility.AS_Utillity_Methods(driver) 
        
        as_utilobj.select_home_button()
        
        '''Step 01: Click on the Report icon in the Home Ribbon'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="Report") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Report Wizard","Step 01: Report wizard opens. Available options are: Create Report, Create SQL Report & Open Existing")
        time.sleep(1)
        
        '''Step 02: Click "Create Report'''
        
        as_utilobj.click_element_using_ui(button_item=True,id="1584") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Report Wizard - Select Procedure Location","Step 02: Verify create report wizard invokes with choosing the location for new report ")
        time.sleep(1)
        
        '''Step 03: Click "Back", click "Create SQL Report"'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="< Back") 
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,id="1576") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Report Wizard","Step 03: Verify location to create SQL report window displayed")
        time.sleep(1)
        
        '''Step 04: Click "Back", click "Open Existing"'''
        
        as_utilobj.click_element_using_ui(button_item=True,name="< Back") 
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,id="1577") 
        time.sleep(1)
        
        as_utilobj.Verify_Current_Dialog_Opens("Report Wizard","Step 04: Verify location to open the existing file window displayed")
        time.sleep(1)
        
        as_utilobj.click_element_using_ui(button_item=True,name="Cancel") 
        time.sleep(1)
        
if __name__=='__main__' :
    unittest.main()  