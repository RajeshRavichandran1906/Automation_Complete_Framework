'''
Created on Aug 1, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336445
Test case title: Verify uploading EXCEL data in Designer Chart 
'''

import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker
import sys

class C9336445_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336445_TestClass, self).__init__(driver)
    
    def test_C9336445(self):   
        
        case_id = 'C9336445'
        tool = 'chart designer'
        upload_data_type = 'Excel'
        if sys.platform == 'linux':
            upload_data_file = '/bipgqashare/filesneededfortestsuites/P215/8206 baseline/G785032/Country Population 2014.xlsx'
        else:
            upload_data_file = '\\ibirisc2\bipgqashare\filesneededfortestsuites\P215\8206 baseline\G785032\Country Population 2014.xlsx'
        master_file = 'country_population_2014'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()    
        
        #Step 1: navigate to case folder
        utilobj.navigate_to_case_folder()   
        
        #Step 2: Launch chart designer        
        utilobj.launch_designer_by_clicking('Common', tool)
        
        #Step 3 - 8: upload data via server console
        utilobj.upload_data(upload_data_type, upload_data_file)
        
        #Step 9: Verify Designer Chart is launched with "country_population_2014" file
        utilobj.verify_preview_designer_chart_default(case_id, master_file, '9')

        #Step 10: add field "COUNTRY_CODE_ISO_3166"
        utilobj.add_field('COUNTRY_CODE_ISO_3166')
        
        #step 11: add field "Population - 2014"
        utilobj.add_field('Population - 2014')
        
        #Step 12: verify live preview
        expected_preview_xaxix_title = 'COUNTRY_CODE_ISO_3166'
        expected_preview_xaxis_labels = ['AR', 'AT', 'AU', 'BE', 'BR', 'CA', 'CH', 'CL', 'CN', 'CO', 'CZ', 'DE', 'DK', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'HU', 'IE', 'IL', 'IN', 'IT', 'JP', 'KR', 'LU', 'MX', 'MY', 'NL', 'NO', 'PH', 'PL', 'PT', 'SE', 'SG', 'TH', 'TN', 'TR', 'TW', 'US', 'ZA']
        expected_preview_yaxis_title = 'Population - 2014'
        expected_preview_yaxis_labels = ['0', '0.4B', '0.8B', '1.2B', '1.6B']
        expected_preview_risers = 42
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