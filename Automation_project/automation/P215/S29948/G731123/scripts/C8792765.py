'''
Created on Apr 17, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792765
Test case title: Creating Page Designer with a Filter bar
'''

import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792765_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792765_TestClass, self).__init__(driver)
    
    def test_C8792765(self):   
        
        case_id = 'C8792765'
        page_folder = 'P215_S29948'
        tool = 'page designer'
        
        utilobj = Selenium_Utility(self.driver)
        
        #Step 1: log into WF
        utilobj.login_wf()    
        
        #Step 2: click Public folder
        utilobj.click_home_tree_folder(page_folder)        
        
        #Step 3: click Page Action button and verify Page Template dialog
        utilobj.launch_designer_by_clicking('Common', tool)
        expected_new_page_dialog_title = 'New Page'
        expected_new_page_dialog_open_existing_text = 'Copy an existing page'
        expected_new_page_dialog_select_template_text = 'Select a template'
        expected_new_page_dialog_template_items_label = ['Blank', 'Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1', 'InfoApp 1']
        utilobj.verify_new_page_dialog(expected_new_page_dialog_title, expected_new_page_dialog_open_existing_text, expected_new_page_dialog_select_template_text, expected_new_page_dialog_template_items_label, case_id, '3')
        
        #Step 4: choose blank template
        utilobj.select_page_template('Blank')
        
        #Step 5: navigate to fex folder and drag and drop fex to canvas
        utilobj.navigate_pd_tree(page_folder, 'Retail Samples->Portal->Small Widgets')
        utilobj.drag_and_drop_to_canvas('Category Sales')
        utilobj.verify_quick_filter_button(case_id, '5')
        
        #Step 6: click quick filter button and verify filter bar contains 6 controls
        utilobj.click_and_verify_filter_bar(6, case_id, '6')
        
        #Step 7: click preview button and verify page in run mode
        utilobj.click_preview_and_verify_in_run_mode(case_id, '7') 
        
        #Step 8: exit preview and verity page in design mode
        utilobj.exit_preview_and_verify_in_design_mode(case_id, '8')
        
        #Step 9: click to maximize container and verify
        utilobj.maximize_container_and_verify(case_id, '9')
        
        #Step 10, 11: save page
        utilobj.save_fex_as(tool, 'Smoke Test for PD Page')  
        
        #Step 12: double click to run saved page
        utilobj.double_click_to_run('Smoke Test for PD Page')
        
        #Step 13, 14: choose "Accessories" for Category and verify
        utilobj.choose_filter_value_and_verify('Category', 'Accessories', case_id, '14')
         
if __name__ == "__main__":   
    unittest.main()   