'''
Created on April 10, 2019

@author: Niranjan\Samuel

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261572
TestCase Name = Folder Search
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261572_TestClass(BaseTestCase):

    def test_C8261572(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->Retail Samples'
        expected_list = ['Items', 'Title', 'arrow_upward']
        
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from the side bar
        """  
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        grid_view = self.driver.find_element_by_css_selector(".toolbar .toolbar-button-div [class*='fa fa-list']").is_displayed()
        if grid_view == False:
            main_page_obj.select_grid_view()
        else:
            pass
        
        """
        Step 3: Click on "Retail samples"
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Type "sales" in the search box
        Verify that it is set to title sort and NOT default sort.
        """
        main_page_obj.search_input_box_options('write', 'sales')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Title', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_grid_view_title_labels(expected_list, 'Step 04.01: Verify that it is set to title sort and NOT default sort')
        
        """
        Step 5: Click the X in the search box
        Verify sales is deleted
        """
        main_page_obj.search_input_box_options('clear')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        main_page_obj.search_input_box_options(verify_value='', msg='Step 05.01: Verify sales is deleted')
        
        """
        Step 6: Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()