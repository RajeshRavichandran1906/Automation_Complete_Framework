'''
Created on Apr 22, 2019

@author: ml12793
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792767
Test case title: Create and Run V5 Portal 
'''
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C8792767_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C8792767_TestClass, self).__init__(driver)
    
    def test_C8792767(self):   
        
        case_id = 'C8792767'
        tool = 'portal designer'
        portal_folder = 'P215_S29948'
        portal_title = 'Smoke Test for V5 Portal'
        
        utilobj = Selenium_Utility(self.driver)
        
        #Step 1: log into WF, click public folder
        utilobj.login_wf()    
        utilobj.click_home_tree_folder(portal_folder)        
        
        #Step 2: click Portal button under Designer tab
        utilobj.launch_designer_by_clicking('Designer', tool)
        
        #Step 3, 4: enter portal title, alias and verify
        utilobj.enter_portal_title_and_alias(portal_folder, portal_title, 'SmokeV5', case_id, '4')
        
        #Step 5: create portal and verify the V5 portal is in the content area and shows as folder
        utilobj.create_portal(case_id, '5')
        
        #Step 6, 7, 8: copy and paste Sales Dashboard to V5 portal
        utilobj.copy_and_paste_fex('Retail Samples->InfoApps', 'Sales Dashboard (Filtered)', portal_folder + '->' + portal_title, case_id, '8')
        
        #Step 9: right click to publish V5 portal
        utilobj.right_click_item_to_perform('home-tree-node', 'publish', portal_title) 
        
        #Step 10: right click to run V5 portal and verify
        utilobj.run_portal(portal_title, case_id, '10')
        
        #Step 11: click quick filter button
        utilobj.click_filter_button(case_id, '11')
        
        #Step 12: choose filter value and verify
        expected_actual_category_sales_total_revenue = '609.9M'
        expected_regional_sales_trend_risers_number = 1
        expected_discount_by_region_label = 'North America'
        expected_regional_profit_by_category_yaxis_upper_bound = '60M'
        expected_tab_container_legend_label = 'North America'
        expected_carousel_container_color_scale_upper_bound = '29.6M'
        utilobj.pd_choose_filter_value_and_verify('North America', expected_actual_category_sales_total_revenue, expected_regional_sales_trend_risers_number, expected_discount_by_region_label, expected_regional_profit_by_category_yaxis_upper_bound, expected_tab_container_legend_label, expected_carousel_container_color_scale_upper_bound, case_id, '12')

        #Step 13: click My Pages folder and verify
        utilobj.click_left_panel_folder('My Pages', case_id, '13')

        #Step 14: click + sign and verify page template dialog
        expected_new_page_dialog_title = 'New Page'
        expected_new_page_dialog_open_existing_text = 'Link to an existing page'
        expected_new_page_dialog_select_template_text = 'Select a template'
        expected_new_page_dialog_template_items_label = ['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        utilobj.pd_verify_new_page_dialog(expected_new_page_dialog_title, expected_new_page_dialog_open_existing_text, expected_new_page_dialog_select_template_text, expected_new_page_dialog_template_items_label, case_id, '14')
        
        #Step 15: choose template and verify
        expected_container_number = 3
        utilobj.pd_choose_page_template('Grid 2-1', expected_container_number, case_id, '15')
        
        #Step 16: close browser tab
        self.driver.close()
        
if __name__ == "__main__":   
    unittest.main()   