'''
Created on March 11, 2019

@author: AA14564
Testcase Name : Verify action Bar Upload Data option for Admin user
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8788354
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.wftools import upload_data
from common.lib import core_utility
from common.lib.webfocus.data_tool_bar import DataToolBar

class C8788354_TestClass(BaseTestCase):
    
    def test_C8788354(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        upload_content_obj = upload_data.ContentTree(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        data_tool_obj = DataToolBar(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        upload_content_css = "[id*='WcMultiframesMainPanel'].wcx-mfmainpanel"
        content_box_css = ".content-box"
        CONTENT_CSS="[class*='content-button'][data-ibxp-text='Content']"
        
        """
        Test case variables
        """
        expected_upload_text = '-Click on desktop file types to select and upload the file'
        content_tree_items = ['Desktop files', 'Delimited Files (CSV/TAB)', 'Excel', 'JSON', 'XML']
        tool_bar_items = ['Start Over', 'Options', 'User', 'Help']
        selected_tab_list = ['Common']
        
        """
        Step 1: Sign into WebFOCUS Home Page as AdminUser
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar
        """
        util_obj.synchronize_with_number_of_element(CONTENT_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(repository_css, 'Retail Samples', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        Verify by default 'Common' category button is selected
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(content_box_css, selected_tab_list[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_action_bar_tab(selected_tab_list, 'Step 3.1: Verify Common tab is selected')
        
        """
        Step 4: Click on 'Upload Data' action bar under 'Common' category
        Verify the Reporting Server Wizard opened properly
        """
        main_page_obj.select_action_bar_tabs_option('Upload Data')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, content_tree_items[-1], main_page_obj.home_page_medium_timesleep)
        upload_content_obj.verify_all_conternt_tree_items(content_tree_items, 'Step 4.1: Verify Content tree in reporting server wizard')
        actual_upload_text = util_obj.validate_and_get_webdriver_object(upload_content_css + " .wcx-multiframes-content-view:nth-last-child(1)", 'Reporting Server Wizard').text
        util_obj.asequal(expected_upload_text, actual_upload_text, 'Step 4.2: Verify Content in reporting server wizard')
        actual_visible_tools  = [toolbar_item.get_attribute('qa') for toolbar_item in  [item_obj for item_obj in data_tool_obj.get_toolbar_items_object() if item_obj.is_displayed()]]
        util_obj.as_List_equal(tool_bar_items, actual_visible_tools, "Step 4.3: Verify Tool bar items in reporting server wizard")
        
        """
        Step 5: Close Reporting Server Wizard Window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6: Click on 'Data' category button
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'Data', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Data')
        
        """
        Step 7: Click on 'Upload Data' action bar under 'Data' category
                Verify the Reporting Server Wizard opened properly
        """
        main_page_obj.select_action_bar_tabs_option('Upload Data')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, content_tree_items[-1], main_page_obj.home_page_medium_timesleep)
        upload_content_obj.verify_all_conternt_tree_items(content_tree_items, 'Step 7.1: Verify Content tree in reporting server wizard')
        actual_upload_text = util_obj.validate_and_get_webdriver_object(upload_content_css + " .wcx-multiframes-content-view:nth-last-child(1)", 'Reporting Server Wizard').text
        util_obj.asequal(expected_upload_text, actual_upload_text, 'Step 7.2: Verify Content in reporting server wizard')
        actual_visible_tools  = [toolbar_item.get_attribute('qa') for toolbar_item in  [item_obj for item_obj in data_tool_obj.get_toolbar_items_object() if item_obj.is_displayed()]]
        util_obj.as_List_equal(tool_bar_items, actual_visible_tools, "Step 7.3: Verify Tool bar items in reporting server wizard")
        
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