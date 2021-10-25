'''
Created on May 08, 2019

@author: Niranjan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261573
TestCase Name = Search folder with PGX page, CSS, JS and Strings appear
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer

class C8261573_TestClass(BaseTestCase):

    def test_C8261573(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        page_obj=page_designer.Design(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->Retail Samples->Reports'
        no_search_css=".files-no-search-results"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        
        """
        Step 01:01: Sign in to WebFOCUS as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02:01: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        grid_view = self.driver.find_element_by_css_selector(".toolbar .toolbar-button-div [class*='fa fa-list']").is_displayed()
        if grid_view == False:
            main_page_obj.select_grid_view()
        else:
            pass
        
        """
        Step 03:01:Click on "Reports" folder under "Retail samples"
        """
        main_page_obj.click_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Common', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Common')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04:01: Click Page action tile under common category button
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_utill_obj.switch_to_new_window()
        
        """
        Step 05:01: Select Blank template and click save in toolbar then click Save button
        """
        """
        Step 06:01: Close the page
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_obj.select_page_designer_template("Blank")
        page_obj.save_page_from_toolbar_with_default_name()
        core_utill_obj.switch_to_previous_window(window_close=True)
        
        """
        Step 07:01: Type * in Search box
        Verify that only the items appear and NO custom or css files from the PGX
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Item', main_page_obj.home_page_medium_timesleep)
        main_page_obj.search_input_box_options(input_text_msg='*')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Item', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Page Custom CSS','Page Custom JS','Page Strings'], 'asnotin','Step 07.01: Verified that NO custom or css files from the PGX appears')
        
        """
        Step 08:01: Type custom in Search box
        Verify you get "There are no results to display"
        """
        main_page_obj.search_input_box_options(input_text_msg='Custom')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'There are no results to display', main_page_obj.home_page_medium_timesleep)
        search_elem=util_obj.validate_and_get_webdriver_object(no_search_css,'search_results')
        expected_text=search_elem.text
        actual_text="There are no results to display"
        util_obj.asequal(actual_text,expected_text,"Step 08:01: Verified {}".format(expected_text))
        
        """
        Step 09:01: Click the X in the search box
        """
        main_page_obj.search_input_box_options(option_type='clear')
        
        """
        Step 10:01: Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()