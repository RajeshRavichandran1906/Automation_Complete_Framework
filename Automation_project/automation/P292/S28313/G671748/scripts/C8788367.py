'''
Created on March 20, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788367
Testcase Name : Verify action Bar Access List for Admin user
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility

class C8788367_TestClass(BaseTestCase):
    
    def test_C8788367(self):
        
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
        title_css="div[class*='bi-tab-button tab-button-alignment-top']"
        tab_css="#AccessListEditor_tabPage"
        repository_css = "div[class='ibfs-tree']"
        content_box_css = ".content-box"
        
        """
        Test case variables
        """
        expected_title=['Library Access List']
        domain_folder='Retail Samples'
        action_bar='Access List'
        category_btn='Schedule'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab(category_btn)
        
        """
        Step 5: Click on 'Access List' action bar
        Verify 'Library Access List' window is displayed
        """
        util_obj.synchronize_with_visble_text(content_box_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(title_css, 'Library Access List', main_page_obj.home_page_long_timesleep)
        title_elem_text=util_obj.validate_and_get_webdriver_object(title_css, "title_css").text
        actual_title=[title_elem_text]
        util_obj.asequal(actual_title,expected_title,"Step5.1: Verify access list window is dispalyed")
        util_obj.verify_object_visible(tab_css, True,"Step5.2: Verify the tab available under access list")
        
        """
        Step 6: Close 'Library Access List' window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()