'''
Created on November 15, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914671
TestCase Name = Changing Preference display from Title to Name should change default Search Options setting
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.pages import wf_mainpage as pages

class C5914671_TestClass(BaseTestCase):

    def test_C5914671(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        pages_obj = pages.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        dialog_box_css = ".ibx-dialog-main-box .ibx-dialog-title-box"
        name_radio_button_css = "div[data-ibxp-name=\"preferencesName\"] .ibx-radio-button-simple-marker"
        title_radio_button_css = "div[data-ibxp-name=\"preferencesTitle\"] .ibx-radio-button-simple-marker"
        ok_button_css = ".ibx-dialog-ok-button:not([aria-disabled='true'])"
        search_dropdown_css = ".toolbar .menu-btn-advanced-search"
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: From the new Home Page click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on banner links > Preferences
        """
        pages_obj.select_username_dropdown_menu('Preferences')
        util_obj.synchronize_with_number_of_element(dialog_box_css, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 4: Display: Click Name radio button
        Click OK
        """
        name_radio_element = util_obj.validate_and_get_webdriver_object(name_radio_button_css, "name_radio_button")
        core_util_obj.python_left_click(name_radio_element)
        util_obj.synchronize_with_number_of_element(ok_button_css, 1, main_page_obj.home_page_medium_timesleep)
        ok_element = util_obj.validate_and_get_webdriver_object(ok_button_css, "ok button")
        core_util_obj.python_left_click(ok_element)
        util_obj.synchronize_until_element_disappear(ok_button_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 5: Click drop down in Search box to display Advanced Search
        Verify Search is by Name
        """
        util_obj.synchronize_until_element_is_visible(search_dropdown_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.synchronize_until_element_is_visible(search_dropdown_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Name', step_number='05.01')
        
        """
        Step 6: Click on banner links > Preferences
        """
        pages_obj.select_username_dropdown_menu('Preferences')
        util_obj.synchronize_with_number_of_element(dialog_box_css, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: Change Display from Name to Title
        Click OK
        """
        title_radio_element = util_obj.validate_and_get_webdriver_object(title_radio_button_css,"title_radio_button")
        core_util_obj.python_left_click(title_radio_element)
        util_obj.synchronize_with_number_of_element(ok_button_css, 1, main_page_obj.home_page_medium_timesleep)
        ok_element = util_obj.validate_and_get_webdriver_object(ok_button_css, "ok button")
        core_util_obj.python_left_click(ok_element)
        util_obj.synchronize_until_element_disappear(ok_button_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 8: Click drop down in Search box to display Advanced Search
        Verify Search is by Title
        """
        util_obj.synchronize_until_element_is_visible(search_dropdown_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_search_input_box_option_dropdown()
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Title', step_number='08.01')
        
        """
        Step 9: Sign out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()