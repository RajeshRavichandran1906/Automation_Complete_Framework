'''
Created on October 17, 2018

@author: Varun
Testcase Name : Verify Page Heading title displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261745
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.wftools import login,wf_mainpage,page_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261745_TestClass(BaseTestCase):
    
    def test_C8261745(self):
        
        """
            Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        verification_title="Page Heading"
        
        """
            Step 1 : Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
            Step 2 : Expand Domain > Click 'Retail Samples' domain
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.wait_for_page_loads(20, pause_time=2)
        main_page_obj.expand_repository_folder("Retail Samples")
        
        """
            Step 3 : Select Designer category > Create a PGX by clicking Page action bar using blank template
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        core_util_obj.update_current_working_area_browser_specification() # For edge browser, updating wrong browser Y value. So script level updating browser Y value
        page_designer_obj.select_page_designer_template('Blank')
        title_css = ".pd-page-title .ibx-label-text"
        util_obj.wait_for_page_loads(20, pause_time=6)
        obtained_title = util_obj.validate_and_get_webdriver_object(title_css, 'Domain-Title').text.strip()
        util_obj.asequal(verification_title, obtained_title,"Step1 : verification of the title")
        
        """
            Step 4 : Close the Page Designer from the application menu
        """
        page_designer_obj.close_page_designer_without_save_page()
        
        """
            Step 5 : In the banner link, click on the top right username > Click Sign Out.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()