'''
Created on Aug 5, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336560
Test case title: VVerify uploading XML data in Designer Chart 
'''

import sys
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C9336560_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336560_TestClass, self).__init__(driver)
    
    def test_C9336560(self):   
        
        case_id = 'C9336560'
        tool = 'chart designer'
        upload_data_type = 'XML'
        if sys.platform == 'linux':
            upload_data_file = '/bipgqashare/filesneededfortestsuites/P215/8206 baseline/G785032/audit_rpart.xml'
        else:
            upload_data_file = '\\ibirisc2\bipgqashare\filesneededfortestsuites\P215\8206 baseline\G785032\audit_rpart.xml'
        master_file = 'audit_rpart'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()    
        
        #Step 1: navigate to case folder
        utilobj.navigate_to_case_folder()   
        
        #Step 2: Launch chart designer        
        utilobj.launch_designer_by_clicking('Common', tool)
        
        #Step 3 - 8: upload data via server console
        utilobj.upload_data(upload_data_type, upload_data_file)
        
        #Step 9: Verify Designer Chart is launched with "audit_rpart" file
        utilobj.verify_preview_designer_chart_default(case_id, master_file, '9')

        #Step 10: add field "Datafield > NAME2"
        utilobj.add_field_by_expanding_tree_node('Datafield', 'NAME2')
         
        #step 11: add field "Value > VALUE1"
        utilobj.add_field_by_expanding_tree_node('Value', 'VALUE1')
         
        #Step 12: verify live preview
        expected_preview_xaxix_title = 'NAME2 : VALUE1'
        expected_preview_xaxis_labels = ['Education : .', 'Employment : .', 'Gender : .', 'Marital : .', 'Occupation : .']
        expected_preview_yaxis_title = None
        expected_preview_yaxis_labels = None
        expected_preview_risers = 5
        expected_preview_risers_color = "#5388be"
        utilobj.verify_preview_designer_chart(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '12')
 
        #Step 13: click preview
        utilobj.click_preview_and_verify_output(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color,case_id, '13')
  
        #Step 14: exit preview
        utilobj.exit_preview()        
         
        #Step 15: save fex
        utilobj.save_fex_as('designer', case_id)
         
        #Step 16: exit chart
        utilobj.exit_tool('designer')
         
        #Step 17: right click to edit
        utilobj.right_click_item_to_perform('file-item', 'edit', case_id)
         
        #Step 18: verify live preview
        utilobj.switch_to_window(2)
        utilobj.verify_preview_designer_chart(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '18')
 
        #Step 19: sign out
        utilobj.logout_wf()
              
if __name__ == "__main__":   
    unittest.main()        