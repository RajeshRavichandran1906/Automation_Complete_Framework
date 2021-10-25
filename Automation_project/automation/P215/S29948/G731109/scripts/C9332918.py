'''
Created on May 1, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9332918
Test case title: Workbook - Join workflow 
'''

import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C9332918_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9332918_TestClass, self).__init__(driver)
    
    def test_C9332918(self):   
        
        case_id = 'C9332918'
        tool = 'designer'
        report_type = 'workbook'
        master_file = 'new_retail/facts/wf_retail_sales'
        
        utilobj = Selenium_Utility(self.driver)
        
        #Step 1: log into WF
        utilobj.login_wf()    
        utilobj.launch_tool(tool, report_type, master_file)
        expected_dimension_nodes = []
        expected_measure_nodes = ['ID Sales', 'ID Store', 'ID Currency', 'ID Customer', 'ID Discount',
                                   'ID Product', 'ID Time', 'Cost of Goods,Local Currency', 'Cost of Goods', 
                                   'Discount,Local Currency', 'Discount', 'Gross Profit,Local Currency', 
                                   'Gross Profit', 'MSRP,Local Currency', 'MSRP', 'Quantity,Sold', 
                                   'Revenue,Local Currency', 'Revenue']
        utilobj.verify_metadata_tree(expected_dimension_nodes, expected_measure_nodes, case_id, '1')
        
        #Step 2: click Data tab and verify
        utilobj.click_designer_tab('Data')
        utilobj.verify_data_prep_canvas(case_id, '2')
        
        #Step 3: navigate to dimensions folder
        utilobj.navigate_join_tool_tree('facts->dimensions')
        
        #Step 4: scroll the list, drag wf_retail_store and drop it on canvas
        utilobj.join_tool_drag_and_drop_to_canvas('wf_retail_store', case_id, '4')
        
        #Step 5: click Chart 1 tab 
        utilobj.click_designer_tab('Chart 1')
        expected_dimension_nodes = ['Store Info Dimension']
        expected_measure_nodes = ['ID Sales', 'ID Store', 'ID Currency', 'ID Customer', 'ID Discount',
                                   'ID Product', 'ID Time', 'Cost of Goods,Local Currency', 'Cost of Goods', 
                                   'Discount,Local Currency', 'Discount', 'Gross Profit,Local Currency', 
                                   'Gross Profit', 'MSRP,Local Currency', 'MSRP', 'Quantity,Sold', 
                                   'Revenue,Local Currency', 'Revenue', 'Store Info Dimension']
        utilobj.verify_metadata_tree(expected_dimension_nodes, expected_measure_nodes, case_id, '5')
    
        #Step 6, 7: add fields 
        utilobj.add_nodes('store', 'Store Type', 'Revenue')
        expected_preview_xaxix_title = 'Store Type'
        expected_preview_xaxis_labels = ['Store Front', 'Web']
        expected_preview_yaxis_title = 'Revenue'
        expected_preview_yaxis_labels = ['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M', '800M']
        expected_preview_risers = 2
        expected_preview_risers_color = "#5388be"
        utilobj.verify_preview_designer_chart(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '7')
        
        #Step 8: click preview
        utilobj.click_preview_and_verify_in_run_mode_designer(case_id, '8')

        #Step 9: exit preview
        utilobj.exit_preview_and_verify_in_design_mode_designer(case_id, '9')

        #Step 10: save fex
        utilobj.save_fex_as(tool, case_id)

        #Step 11: run workbook in new window
        expected_runtime_xaxix_title = 'Store Type'
        expected_runtime_xaxis_labels = ['Store Front', 'Web']
        expected_runtime_yaxis_title = 'Revenue'
        expected_runtime_yaxis_labels = ['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M', '800M']
        expected_runtime_risers = 2
        expected_tuntime_risers_color = "#5388be"
        utilobj.run_in_new_window(report_type, expected_runtime_xaxix_title, expected_runtime_xaxis_labels, expected_runtime_yaxis_title, expected_runtime_yaxis_labels, expected_runtime_risers, expected_tuntime_risers_color, case_id, '11')
        
        #Step 12: reopen the workbook
        utilobj.reopen_join_fex(expected_preview_xaxix_title, expected_preview_xaxis_labels, expected_preview_yaxis_title, expected_preview_yaxis_labels, expected_preview_risers, expected_preview_risers_color, case_id, '12')
        
        #Step 13: click Data tab to verify
        utilobj.click_designer_tab('Data')
        expected_node_header = ['Join 1', 'wf_retail_sales (T01)', 'wf_retail_store (T02)']
        utilobj.verify_join_nodes(expected_node_header, case_id, '13')
        self.driver.close()
        
if __name__ == "__main__":   
    unittest.main()   