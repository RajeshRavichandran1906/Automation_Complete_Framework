'''
Created on Apr 08, 2019

@author: ml12793

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792737
Test case title: Launch Designer Report, save and restore  
'''
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792737_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792737_TestClass, self).__init__(driver)
    
    def test_C8792737(self):        
        
        case_id = 'C8792737'
        tool = 'designer'
        report_type= 'report'
        master_file = 'ibisamp/car'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()
        
        #launch designer report using url api call and verify preview
        utilobj.launch_tool(tool, report_type, master_file)
        utilobj.verify_preview_designer_report_default(case_id, '1')
        
        #double click to add field and verify preview
        utilobj.double_click_to_add_field(tool, 'COUNTRY')
        expected_preview = ['COUNTRY', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        utilobj.verify_preview_designer_report(expected_preview, case_id, '2')
        
        #save fex
        utilobj.save_fex_as(tool, case_id)
        
        #edit save fex and verify preview
        utilobj.edit_saved_fex(tool, report_type, case_id.replace('C', 'c'))
        utilobj.verify_preview_designer_report(expected_preview, case_id, '4')
              
if __name__ == "__main__":   
    unittest.main()