'''
Created on Mar 22, 2019

@author: ml12793

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792287
Test case title: Verify Olap Pane Bottom 
'''
import unittest
from utility.selenium_utility import Selenium_Utility as utilobj
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792287_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792287_TestClass, self).__init__(driver)
    
    def test_C8792287(self):        
        
        case_id = 'C8792287'
        
        utilobj.login_wf(self)
        
        #navigate to group folder and run OLAP report
        utilobj.run_olap_report(self, case_id)        
        
        #Step 5: verify OLAP pane appears at bottom
        utilobj.verify_olap_pane_position(self, 'bottom', case_id, '5') 
        
        #click run in OLAP pane
        utilobj.click_run_in_olap_pane(self)
        
        #Step 7a: verify OLAP pane appears at bottom after clicking run button in OLAP pane
        utilobj.verify_olap_pane_position(self, 'bottom', case_id, '7.1')
        
        #Step 7b: verify output in OLAP Pane control mode
        utilobj.verify_table(self, 'olap_pane', case_id, '7.2')
                
if __name__ == "__main__":   
    unittest.main()
