'''
Created on December 13, 2018

@author: Vpriya
Testcase Name : Verify action Bar Access List for Dev user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261606
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility

class C8261606_TestClass(BaseTestCase):
    
    def test_C8261606(self):
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
        title_css="div[class*='bi-tab-button tab-button-alignment-top']"
        
        
        """
        Test case variables
        """
        folders_text = 'Folders'
        expected_title=['Library Access List']
        tab_css="#AccessListEditor_tabPage"
        
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
        main_page_obj.select_action_bar_tab('Schedule')
        
        """
        Step 5: Click on 'Access List' action bar
        Verify 'Library Access List' window is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Access List')
        core_util_obj.switch_to_new_window()
        title_elem_text=util_obj.validate_and_get_webdriver_object(title_css, "title_css").text
        actual_title=[title_elem_text]
        util_obj.asequal(actual_title,expected_title,"Step5:verify access list window is dispalyed")
        util_obj.verify_object_visible(tab_css, True,"Step5:Verify the tab available under access list")
        
        """
        Step 6: Close 'Library Access List' window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()