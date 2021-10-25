'''
Created on Jul 02, 2019

@author: ml12793

Test case link: http://lnxtestrail/testrail/index.php?/cases/view/9336307
Test case title: Navigating the Paris Home Page  
'''
import unittest
from utility.selenium_utility import Selenium_Utility 
from utility.basetestcasedocker import BaseTestCaseDocker

class C9336307_TestClass(BaseTestCaseDocker):
    
    def __init__(self, driver):  
        super(C9336307_TestClass, self).__init__(driver)
    
    def test_C9336307(self):        
        
        case_id = 'C9336307'
        report_item = 'Arc - Sales by Region'
        
        utilobj = Selenium_Utility(self.driver)
        utilobj.login_wf()
        
        utilobj.go_to_paris_home_page()
        
        expected_tooltips = ['Utilities', 'Settings', 'Help', 'User']
        utilobj.verify_banner_link_menus(expected_tooltips, case_id, '3')
        
        utilobj.click_tab_button('All Content')
        
        utilobj.navigate_domain_folders('Retail Samples->Charts')
        
        utilobj.right_click_item_to_perform(report_item, 'Run')
        utilobj.close_report()
        
        utilobj.right_click_item_to_perform(report_item, 'Add to Favorites')
        
        utilobj.click_tab_button('Home')
        
        utilobj.verify_report_added(report_item, case_id, '8')
        
        utilobj.logout_wf()
              
if __name__ == "__main__":   
    unittest.main()