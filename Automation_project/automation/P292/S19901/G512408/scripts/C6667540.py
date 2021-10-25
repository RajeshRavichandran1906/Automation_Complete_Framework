'''
Created on December 12, 2018

@author: varun
Testcase Name : Verify action Bar Upload Data option for Dev user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667540
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.wftools import upload_data
from common.lib import core_utility

class C6667540_TestClass(BaseTestCase):
    
    def test_C6667540(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        upload_content_obj = upload_data.ContentTree(self.driver)
        upload_tool_obj = upload_data.ToolBar(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        upload_content_css = "div[title=\"Upload\"] .ibx-label-text"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
        """
        Test case variables
        """
        upload_text = 'Upload'
        content_tree_items = ['Desktop files', 'Delimited Files (CSV/TAB)', 'Excel', 'JSON', 'XML']
        tool_bar_items = ['Start Over', 'Options', 'User', 'Help']
        selected_tab_list = ['Common']
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
        Verify by default 'Common' category button is selected
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_action_bar_tab(selected_tab_list, 'Step 3.1: Verify Common tab is selected')
        
        """
        Step 4: Click on 'Upload Data' action bar under 'Common' category
        Verify the Reporting Server Wizard opened properly
        """
        main_page_obj.select_action_bar_tabs_option('Upload Data')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, upload_text, base_obj.home_page_medium_timesleep)
        upload_content_obj.verify_all_conternt_tree_items(content_tree_items, 'Step 4.1: Verify Content tree in reporting server wizard')
        upload_tool_obj.verify_all_visible_toolbar_buttons(tool_bar_items, "Step 4.2: Verify Tool bar items in reporting server wizard")
        
        """
        Step 5: Close Reporting Server Wizard Window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6: Click on 'Data' category button
        """
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Data')
        
        """
        Step 7: Click on 'Upload Data' action bar under 'Data' category
        """
        main_page_obj.select_action_bar_tabs_option('Upload Data')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, upload_text, base_obj.home_page_medium_timesleep)
        upload_content_obj.verify_all_conternt_tree_items(content_tree_items, 'Step 7.1: Verify Content tree in reporting server wizard')
        upload_tool_obj.verify_all_visible_toolbar_buttons(tool_bar_items, "Step 7.2: Verify Tool bar items in reporting server wizard")
        
        """
        Step 8: Close Reporting Server Wizard Window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()