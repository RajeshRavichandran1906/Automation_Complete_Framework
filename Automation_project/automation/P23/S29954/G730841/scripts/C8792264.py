'''
Created on Mar 20, 2019

@author: ml12793

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792264
Test case title: Verify Olap Control Button 
'''
import unittest
from utility.selenium_utility import Selenium_Utility as utilobj
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792264_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792264_TestClass, self).__init__(driver)
    
    def test_C8792264(self):        
        
        case_id = 'C8792264'
        
        utilobj.login_wf(self)
        
        #navigate to group folder and run OLAP report
        utilobj.run_olap_report(self, case_id)  
        
        #Step 5: verify OLAP button control position
        utilobj.verify_olap_button_control_position(self, case_id, '5')      
        
        #bring up OLAP panel and click run
        utilobj.activate_olap_panel_and_run(self)

        #Step 8a: verify OLAP button control position after clicking run button in OLAP panel
        utilobj.verify_olap_button_control_position(self, case_id, '8.1') 
        
        #Step 8b: verify output
        utilobj.verify_table(self, 'olap_pane_control', case_id, '8.2')
                
if __name__ == "__main__":   
    unittest.main()