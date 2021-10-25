'''
Created on December 14, 2018

@author: varun
Testcase Name : Verify Action Bar can be collapsed by the user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261613
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261613_TestClass(BaseTestCase):
    
    def test_C8261613(self):
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
        expand_icon_css = "div[data-ibxp-glyph=\"keyboard_arrow_up\"]:not([style*='none'])"
        collapse_icon_css = "div[data-ibxp-glyph=\"keyboard_arrow_down\"]:not([style*='none'])"
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
        """
        Test case variables
        """
        action_bar_tab_options = ['Folder', 'Upload Data', 'Connect', 'Workbook', 'Chart', 'Report', 'Page']
        action_bar_tab = ['Common', 'Data', 'Designer', 'InfoAssist', 'Schedule', 'Other']
        action_bar_text = "Action Bar"
        folders_text = 'Folders'
        
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
        Step 3: Click on the top 'Domain' root folder.
        Verify that 'Action Bar' title is there with the expanded icon at the end of the action bar.
        """
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text,base_obj.home_page_medium_timesleep)
        action_bar_element = util_obj.validate_and_get_webdriver_object(action_bar_css, 'action-element').text.strip()
        util_obj.asequal(action_bar_text,action_bar_element,"Step 3.1: Verify Action Bar title is present")
        util_obj.verify_object_visible(expand_icon_css, True, "Step 3.2:  Verify Expand icon is present")
        
        """
        Step 4: Click on 'Collapse action bar' icon.
        Verify that 'Action Bar' gets collapsed and it still shows 'Action Bar' title
        """
        main_page_obj.collapse_action_bar()
        action_bar_element = util_obj.validate_and_get_webdriver_object(action_bar_css, 'action-element').text.strip()
        util_obj.asequal(action_bar_text,action_bar_element,"Step 4.1: Verify Action Bar title is still present")
        util_obj.verify_object_visible(collapse_icon_css , True, "Step 4.2:  Verify Collapse icon is present")
        
        """
        Step 5: Click on 'Retail Samples' domain.
        Verify that still 'Action Bar' title shows but it is in the collapsed state.
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        action_bar_element = util_obj.validate_and_get_webdriver_object(action_bar_css, 'action-element').text.strip()
        util_obj.asequal(action_bar_text,action_bar_element,"Step 5.1: Verify Action Bar title is still present")
        util_obj.verify_object_visible(collapse_icon_css , True, "Step 5.2:  Verify Action Bar is in a collapsed state")
        
        """
        Step 6: Click on 'Expand action bar' icon.
        Verify that all the available action bars and category buttons. 
        Also at the end of the action bar, its icon gets expanded
        """
        main_page_obj.expand_action_bar()
        util_obj.verify_object_visible(expand_icon_css, True, "Step 6.1:  Verify Expand icon is present")
        main_page_obj.verify_action_bar_tab_all_options(action_bar_tab_options, "Step 6.2: Verify action tab options")
        main_page_obj.verify_action_bar_all_tabs(action_bar_tab, "Step 6.3: Verify Action Bar tabs")
        
        """
        Step 7: In the banner link, Click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        