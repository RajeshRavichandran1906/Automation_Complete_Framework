'''
Created on December 14, 2018

@author: varun
Testcase Name : Action bar showing all categories at the Domain root folder after resizing browser
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261622
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261622_TestClass(BaseTestCase):
    
    def test_C8261622(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """
        Test case CSS
        """
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        domains_css = "div[title=\"Workspaces\"] .ibx-label-text"
        
        """
        Test case variables
        """
        workspace = "Workspaces"
        domain_tab_options = ['Workspace','Folder']
        action_bar_text = "Action Bar"
        folders_text = 'Folders'
        domains_text = workspace
        
        """
        Step 1: Sign into WebFOCUS as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Content Sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on the top workspace root folder.
        Verify that only workspace and 'Folder' action bar are displayed
        """
        main_page_obj.expand_repository_folder(workspace)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text,base_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(domain_tab_options,"Step 3.1: Verify Domain and folder are displayed")
        
        """
        Step 4: Resize the browser.
        The category buttons should not show if you get small enough but only Domain and folder should show
        """
        util_obj.set_browser_window_size()
        util_obj.synchronize_until_element_disappear(action_bar_css, base_obj.home_page_short_timesleep)
        main_page_obj.verify_action_bar_tab_all_options([],"Step 4.1: Verify no Action Bar is displayed")
        observed_domain_text = util_obj.validate_and_get_webdriver_object(domains_css, 'domains-css').text.strip()
        util_obj.asequal(domains_text,observed_domain_text,"Step 4.2: Verify Domains crumb is present")
        observed_folders_text = util_obj.validate_and_get_webdriver_object(folders_text_css, 'folders-text').text.strip()
        util_obj.asequal(folders_text,observed_folders_text,"Step 4.3: Verify the Folders text is present in context area")
        
        """
        Step 5: Maximize the browser.
        """
        self.driver.maximize_window()
        
        """
        Step 6: In the banner link, Click on the top right username > Click Signout
        """
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text,base_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()