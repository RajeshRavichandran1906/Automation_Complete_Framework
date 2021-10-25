'''
Created on Dec 13, 2018

@author: Magesh

Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667547
Testcase Name : Verify action Bar Sample Content option for Dev User
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables

class C6667547_TestClass(BaseTestCase):

    def test_C6667547(self):
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
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5: Click on 'Sample Content' action bar under 'InfoAssist' category
        """
        main_page_obj.select_action_bar_tabs_option('Sample Content')
        PARENT_CSS=".open-dialog-resources div[class*='dialog-cancel-button'] .ibx-label-text"
        util_obj.synchronize_until_element_is_visible(PARENT_CSS, Global_variables.mediumwait*5)
        
        """
        Verify 'Sample Content' prompt is displayed
        """
        prompt_css = ".open-dialog-resources"
        util_obj.verify_object_visible(prompt_css, True, "Step 5:1 Verify 'Sample Content' prompt is displayed")
        
        title_bar_css=".open-dialog-resources div[class*='title-bar-caption'] .ibx-label-text"
        util_obj.verify_element_text(title_bar_css, 'Sample Content', "Step 5:2 Verify Sample Content prompt is displayed")
        
        """
        Step 6: Click on 'Cancel' in 'Sample Content' prompt
        """
        Cancel_btn=".open-dialog-resources div[class*='dialog-cancel-button']"
        Cancel_btn_obj=util_obj.validate_and_get_webdriver_object(Cancel_btn, "Cancel button in Sample Content prompt")
        core_utilobj.left_click(Cancel_btn_obj)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()