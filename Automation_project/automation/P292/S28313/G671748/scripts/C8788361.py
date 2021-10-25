'''
Created on March 12, 2019

@author: Niranjan
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788361
Testcase Name : Verify action Bar Sample Content option for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility

class C8788361_TestClass(BaseTestCase):

    def test_C8788361(self):
        
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
        action_bar = 'Sample Content'
        category_btn = 'InfoAssist'

        """
        TESTCASE CSS
        """
        content_box_css = ".content-box"
        Cancel_btn=".open-dialog-resources div[class*='dialog-cancel-button']"
        title_bar_css=".open-dialog-resources div[class*='title-bar-caption'] .ibx-label-text"
        
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
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab(category_btn)
        util_obj.synchronize_with_visble_text(content_box_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on 'Sample Content' action bar under 'InfoAssist' category
        """
        main_page_obj.select_action_bar_tabs_option(action_bar)
        PARENT_CSS=".open-dialog-resources div[class*='dialog-cancel-button'] .ibx-label-text"
        util_obj.synchronize_until_element_is_visible(PARENT_CSS,main_page_obj.home_page_long_timesleep)
        
        """
        Verify 'Sample Content' prompt is displayed
        """
        prompt_css = ".open-dialog-resources"
        util_obj.verify_object_visible(prompt_css, True, "Step 5:1 Verify 'Sample Content' prompt is displayed")
        
        util_obj.verify_element_text(title_bar_css, action_bar, "Step 5:2 Verify Sample Content prompt is displayed")
        
        """
        Step 6: Click on 'Cancel' in 'Sample Content' prompt
        """
        Cancel_btn_obj=util_obj.validate_and_get_webdriver_object(Cancel_btn, "Cancel button in Sample Content prompt")
        core_utilobj.left_click(Cancel_btn_obj)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()