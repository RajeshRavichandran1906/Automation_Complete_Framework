'''
Created on March 11, 2019

@author: AA14564
Testcase Name : Verify action Bar Connect for Admin User
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8788355
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools.data_connect import DataConnect
from common.lib.webfocus.data_tool_bar import DataToolBar

class C8788355_TestClass(BaseTestCase):


    def test_C8788355(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        data_connect_obj=DataConnect(self.driver)
        data_tool_obj = DataToolBar(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        tool_bar_items=['Start Over', 'Options', 'User', 'Help']
        expected_tree_list=['Desktop files', 'Delimited Files (CSV/TAB)', 'Excel', 'JSON', 'XML', 'Server Datasources', 'MS SQL Server JDBC', 'SQLMSSJDBC', 'ESRI ArcGIS']
        expected_title='Connect to Data'
        expected_connect_text = '-Click on desktop file types to select and upload the file\nor\n-Click on New Datasource to add new connection\n-Click on connection to select DBMS objects (tables/views, etc)'
        selected_tab_list = ['Common']
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        upload_content_css = "[id*='WcMultiframesMainPanel'].wcx-mfmainpanel"
        content_box_css = ".content-box"
        title_css="div[title='Connect to Data']"
        
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(repository_css, 'Retail Samples', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        Verify by default 'Common' category button is selected
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, selected_tab_list[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_selected_action_bar_tab(selected_tab_list, "Step 3.1:Verify by default 'Common' category button is selected")     
        
        """
        Step 4: Click on 'Connect' action bar under 'Common' category
        Verify Create Synonym wizard opens with icons and options to upload as below
        """
        main_page_obj.select_action_bar_tabs_option('Connect')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, expected_tree_list[2], main_page_obj.home_page_medium_timesleep)
        actual_visible_tools  = [toolbar_item.get_attribute('qa') for toolbar_item in  [item_obj for item_obj in data_tool_obj.get_toolbar_items_object() if item_obj.is_displayed()]]
        util_obj.as_List_equal(tool_bar_items, actual_visible_tools, "Step 4: Verify Tool bar items in connect wizard")
        data_connect_obj.verify_specific_conternt_tree_items(expected_tree_list, 'Step 4.1: Verify Content tree in connect wizard')
        actual_title = util_obj.validate_and_get_webdriver_object(title_css,'connect to data').text
        util_obj.asequal(expected_title, actual_title, "Step 4.2 verify Content tree title in connect wizard")
        actual_connect_text = util_obj.validate_and_get_webdriver_object(upload_content_css + " .wcx-multiframes-content-view:nth-last-child(1)", 'Reporting Server Wizard').text
        util_obj.asequal(expected_connect_text, actual_connect_text, 'Step 4.3: Verify Content in reporting server wizard')
        
        """
        Step 5 : Close 'Create Synonym wizard' window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 6 : Click on 'Data' category button
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'Data', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab("Data")
        
        """
        Step 7 : Click on 'Connect' action bar under 'Data' category
        Verify Create Synonym wizard opens with icons and options to upload as below
        """
        main_page_obj.select_action_bar_tabs_option('Connect')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(upload_content_css, expected_tree_list[2], main_page_obj.home_page_medium_timesleep)
        actual_visible_tools  = [toolbar_item.get_attribute('qa') for toolbar_item in  [item_obj for item_obj in data_tool_obj.get_toolbar_items_object() if item_obj.is_displayed()]]
        util_obj.as_List_equal(tool_bar_items, actual_visible_tools, "Step 7: Verify Tool bar items in connect wizard")
        data_connect_obj.verify_specific_conternt_tree_items(expected_tree_list, 'Step 7.1: Verify Content tree in connect wizard')
        actual_title = util_obj.validate_and_get_webdriver_object(title_css,'connect to data').text
        util_obj.asequal(expected_title, actual_title, "Step 7.2 verify Content tree title in connect wizard")
        actual_connect_text = util_obj.validate_and_get_webdriver_object(upload_content_css + " .wcx-multiframes-content-view:nth-last-child(1)", 'Reporting Server Wizard').text
        util_obj.asequal(expected_connect_text, actual_connect_text, 'Step 7.3: Verify Content in reporting server wizard')

        """
        Step 8 : Close 'Create Synonym wizard' window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 9 : In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == "__main__":
    unittest.main()