'''
Created on Dec 17, 2018

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667554
Testcase Name : Verify action Bar Distribution List for Dev User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables

class C6667554_TestClass(BaseTestCase):

    def test_C6667554(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on 'Retail Samples' from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'Schedule' category button
        """
        main_page_obj.select_action_bar_tab('Schedule')
        
        """
        Step 5: Click on 'Distribution List' action bar
        """
        main_page_obj.select_action_bar_tabs_option('Distribution List')
        
        """
        Verify 'Distribution List' window is displayed 
        """
        core_utilobj.switch_to_new_window()
        RC_APPLICATION_BTN_CSS = "#addressbook_container img[src*='reportcaster']"
        util_obj.synchronize_with_number_of_element(RC_APPLICATION_BTN_CSS, 1, Global_variables.mediumwait*5)
        actual_window_title=self.driver.title
        expected_window_title="Untitled - Distribution List"
        util_obj.asequal(expected_window_title, actual_window_title, "Step 5.1: Verify 'Distribution List' window is displayed")
        util_obj.verify_object_visible(RC_APPLICATION_BTN_CSS, True, "Step 5.2: Verify 'Distribution List' window is displayed")
        table_header_css="#addressbook_container table td[class='grid-header']"
        table_header=util_obj.validate_and_get_webdriver_objects(table_header_css, "'Burst Value', 'E-mail' displayed in 'Distribution List' window")
        act_list=[el.text.strip() for el in table_header]
        exp_list=['Burst Value', 'E-mail']
        util_obj.verify_list_values(exp_list, act_list, "Step 5.3: Verify 'Distribution List' window is displayed")
        
        """
        Step 6: Close 'Distribution List' window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()