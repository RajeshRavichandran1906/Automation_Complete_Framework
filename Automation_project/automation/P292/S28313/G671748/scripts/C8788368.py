'''
Created on March 21, 2019

@author: Niranjan
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788368
Testcase Name : Verify action Bar Distribution List for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity, core_utility

class C8788368_TestClass(BaseTestCase):

    def test_C8788368(self):
        
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        action_bar= 'Distribution List'
        category_btn='Schedule'
        expected_title=['Distribution List']
        
        """
        Test case CSS
        """
        content_box_css = ".content-box"
        title_css="div[class*='bi-tab-button tab-button-alignment-top']"
        tab_css="#AddrbookEditor_tabPage"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        
        """
        Step 3: Click on 'Retail Samples' from the resource tree
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Schedule' category button
        """
        main_page_obj.select_action_bar_tab(category_btn)
        util_obj.synchronize_with_visble_text(content_box_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on 'Distribution List' action bar
        """
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
        Verify 'Distribution List' window is displayed 
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(title_css, 'Distribution List', main_page_obj.home_page_long_timesleep)
        title_elem_text=util_obj.validate_and_get_webdriver_object(title_css, "title_css").text
        actual_title=[title_elem_text]
        util_obj.asequal(actual_title,expected_title,"Step5.1: Verify distribution list window is dispalyed")
        util_obj.verify_object_visible(tab_css, True,"Step5.2: Verify the tab available under distribution list")
    
        """
        Step 6: Close 'Distribution List' window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()