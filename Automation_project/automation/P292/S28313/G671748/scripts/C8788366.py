'''
Created on March 14, 2019

@author: AA14564
Testcase Name : Verify action Bar Alert for Admin User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8788366
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility

class C8788366_TestClass(BaseTestCase):
    
    def test_C8788366(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        content_tree_css = "table tbody span"
        repository_css = "div[class='ibfs-tree']"
        content_box_css = ".content-box"
        
        """
        Test case variables
        """
        expected_content_items = ['Alert', 'Test', 'Result']
        domain_folder = 'Retail Samples'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, 'InfoAssist', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5: Click on 'Alert' action bar
        Verify 'Alert Assist' window is displayed
        """
        util_obj.synchronize_with_visble_text(content_box_css, expected_content_items[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(expected_content_items[0])
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(content_tree_css, expected_content_items[0], main_page_obj.home_page_medium_timesleep)
        observed_content_tree_element = util_obj.validate_and_get_webdriver_objects(content_tree_css, "content-items")
        observed_content_list = [element.text for element in observed_content_tree_element]
        util_obj.asequal(expected_content_items,observed_content_list,"Step 5.1: Verify Content tree items")
        util_obj.verify_picture_using_sikuli('alert_logo.png', 'Step 5.2: Verify Alert logo is present')
        
        """
        Step 6: Close 'Alert Assist' window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()