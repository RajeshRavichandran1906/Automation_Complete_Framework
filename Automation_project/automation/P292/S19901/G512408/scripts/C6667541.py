'''
Created on Dec 13, 2018

@author: Vpriya
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667541
Testcase Name : Verify action Bar Connect for Dev User
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.wftools.data_connect import DataConnect

class C6667541_TestClass(BaseTestCase):


    def test_C6667541(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        data_connect_obj=DataConnect(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        expected_buttons_list=['Start Over', 'Options', 'User', 'Help']
        expected_tree_list=['Desktop files', 'Delimited Files (CSV/TAB)', 'Excel', 'JSON', 'XML', 'Server Datasources', 'MS SQL Server JDBC', 'SQLMSSJDBC', 'ESRI ArcGIS']
        expected_title=['Connect to Data']
        title_css="div[title='Connect to Data']"
        option_title_css="div[title='Start Over']"
        
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        Verify by default 'Common' category button is selected
        """
        main_page_obj.click_repository_folder(domain_folder)
        main_page_obj.verify_selected_action_bar_tab(['Common'], "Step 3.1:Verify by default 'Common' category button is selected")     
        
        """
        Step 4: Click on 'Connect' action bar under 'Common' category
        Verify Create Synonym wizard opens with icons and options to upload as below
        """
        main_page_obj.select_action_bar_tabs_option('Connect')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(option_title_css,1,60)
        data_connect_obj.verify_all_visible_toolbar_buttons(expected_buttons_list,"Step:4 verify icons")
        data_connect_obj.verify_specific_conternt_tree_items(expected_tree_list,"Step:4.1 verify content tree")
        title_elem=util_obj.validate_and_get_webdriver_object(title_css,'connect to data')
        title_text=[title_elem.text]
        util_obj.asequal(title_text,expected_title,"Step 4.2 verify title")
        
        """
        Step 5 : Close 'Create Synonym wizard' window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 6 : Click on 'Data' category button
        """
        main_page_obj.select_action_bar_tab("Data")
        
        
        """
        Step 7 : Click on 'Connect' action bar under 'Data' category
        Verify Create Synonym wizard opens with icons and options to upload as below
        """
        main_page_obj.select_action_bar_tabs_option('Connect')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(option_title_css,1,60)
        data_connect_obj.verify_all_visible_toolbar_buttons(expected_buttons_list,"Step:4 verify icons")
        data_connect_obj.verify_specific_conternt_tree_items(expected_tree_list,"Step:4.1 verify content tree")
        title_elem=util_obj.validate_and_get_webdriver_object(title_css,'connect to data')
        title_text=[title_elem.text]
        util_obj.asequal(title_text,expected_title,"Step 4.2 verify title")

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