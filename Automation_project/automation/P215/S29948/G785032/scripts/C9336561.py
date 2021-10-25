'''
Created on Aug 6, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336561
Test case title: Verify uploading CSV data in Designer Report
'''

import sys
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C9336561_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336561_TestClass, self).__init__(driver)
    
    def test_C9336561(self):   
        
        case_id = 'C9336561'
        tool = 'report designer'
        upload_data_type = 'Delimited Files (CSV/TAB)'
        if sys.platform == 'linux':
            upload_data_file = '/bipgqashare/filesneededfortestsuites/P215/8206 baseline/G785032/Addmission_missing.csv'
        else:
            upload_data_file = '\\ibirisc2\bipgqashare\filesneededfortestsuites\P215\8206 baseline\G785032\Addmission_missing.csv'
        master_file = 'addmission_missing'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()    
        
        #Step 1: navigate to case folder
        utilobj.navigate_to_case_folder()   
        
        #Step 2: Launch report designer        
        utilobj.launch_designer_by_clicking('Common', tool)
        
        #Step 3 - 8: upload data via server console
        utilobj.upload_data(upload_data_type, upload_data_file)
        
        #Step 9: Verify Designer Report is launched with "addmission_missing" file
        utilobj.verify_preview_designer_report_default_with_file(case_id, master_file, '9')
 
        #Step 10: add field "GENDER"
        utilobj.add_field('GENDER')
          
        #step 11: add field "GPA"
        utilobj.add_field('GPA')
          
        #Step 12: verify live preview
        expected_preview = ['GENDER', 'GPA', '.', '7.01', 'Female', '653.80', 'Male', '685.75']
        utilobj.verify_preview_designer_report(expected_preview, case_id, '12')
  
        #Step 13: click preview
        utilobj.click_preview_and_verify_report_output(expected_preview, case_id, '13')
   
        #Step 14: exit preview
        utilobj.exit_preview()        
          
        #Step 15: save fex
        utilobj.save_fex_as('designer', case_id)
          
        #Step 16: exit designer
        utilobj.exit_tool('designer')
          
        #Step 17: right click to edit
        utilobj.right_click_item_to_perform('file-item', 'edit', case_id)
          
        #Step 18: verify live preview
        utilobj.switch_to_window(2)
        utilobj.verify_preview_designer_report(expected_preview, case_id, '18')
  
        #Step 19: sign out
        utilobj.logout_wf()
              
if __name__ == "__main__":   
    unittest.main()  