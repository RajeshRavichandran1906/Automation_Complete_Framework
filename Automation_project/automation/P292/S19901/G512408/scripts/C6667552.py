'''
Created on December 13, 2018

@author: varun
Testcase Name : Verify action Bar Alert for Dev User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667552
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility

class C6667552_TestClass(BaseTestCase):
    
    def test_C6667552(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        navigation_css = "#HomeNavigateCluster .bi-component .cluster-box-title"
        content_tree_css = "table tbody span"
        
        """
        Test case variables
        """
        expected_content_items = ['Alert', 'Test', 'Result']
        navigation_text = "Navigation"
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5: Click on 'Alert' action bar
        Verify 'Alert Assist' window is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Alert')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(navigation_css, navigation_text,base_obj.report_medium_timesleep)
        observed_content_tree_element = util_obj.validate_and_get_webdriver_objects(content_tree_css, "content-items")
        observed_content_list = [element.text for element in observed_content_tree_element]
        util_obj.asequal(expected_content_items,observed_content_list,"Step 5.1: Verify Content tree items")
        util_obj.verify_picture_using_sikuli('alert_logo.png', 'Step 5.2: Verify Alert logo is present')
        
        """
        Step 6: Close 'Alert Assist' window
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()