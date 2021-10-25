'''
Created on Apr 9, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792775
Test case title: Launch IA Visualization, save and restore  
'''
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792775_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792775_TestClass, self).__init__(driver)
    
    def test_C8792775(self):        
        
        case_id = 'C8792775'
        tool = 'ia'
        report_type= 'idis'
        master_file = 'ibisamp/car'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()
        
        #launch IA visualization using url api call
        utilobj.launch_tool(tool, report_type, master_file)
        utilobj.verify_preview_ia_visualization_default(case_id, '1')
        
        #double click to add field and verify preview
        utilobj.double_click_to_add_field(tool, 'COUNTRY')
        utilobj.double_click_to_add_field(tool, 'SALES')
        expected_preview_xaxix_title = 'COUNTRY'
        expected_preview_xaxis_labels = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_preview_yaxis_title = 'SALES'
        expected_preview_yaxis_labels = ['0', '20K', '40K', '60K', '80K', '100K']
        expected_preview_risers = 5
        expected_preview_risers_color = "#5388be"
        utilobj.verify_preview_ia_visualization(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '2')
                 
        #save fex
        utilobj.save_fex_as(tool, case_id)
         
        #edit save fex and verify preview
        utilobj.edit_saved_fex(tool, report_type, case_id)
        utilobj.verify_preview_ia_visualization(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '4')
              
if __name__ == "__main__":   
    unittest.main()
