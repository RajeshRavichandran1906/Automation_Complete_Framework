'''
Created on Dec 13, 2018

@author: Vpriya
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667563
Testcase Name : Verify User can click on metadata and the metadata edit screen will appear
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.wftools.data_metadata import DataMetadata

class C6667563_TestClass(BaseTestCase):


    def test_C6667563(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        data_metadata_obj=DataMetadata(self.driver)
        text_css="div[class*='ibx-widget ibx-flexbox ibx-label ibx-label-no-icon wcx-form-item icon-left']"
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        expected_buttons_list=['New', 'Filter', 'Preferences', 'Impact Analysis', 'Manage', 'Reset']
        expected_tree_list=['foccache(Temporary)', 'retail_samples', 'homeapps (users home)', 'baseapp']
        expected_tree_list_dev=['foccache(Temporary)', 'retail_samples', 'baseapp']
        
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid','mrpassbas')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4:Click on 'Data' category
        """
        main_page_obj.select_action_bar_tab('Data')
        
        """
        Step 5 : Click on 'Metadata' action bar
        Verify Metadata action bar open and reporting server metadata Edit screen will first show
        """
        main_page_obj.select_action_bar_tabs_option('Metadata')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(text_css,1,60)
        data_metadata_obj.verify_all_visible_toolbar_buttons(expected_buttons_list,"Step4:verify toolbar buttons")
        data_metadata_obj.verify_specific_conternt_tree_items(expected_tree_list, "Step 4.1:verify Content tree items")

        
        """
        Step 6 : Close that window
        """
        core_utilobj.switch_to_previous_window()
        
        
        """
        Step 7 : In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        """
        Step 8 : Sign into WebFOCUS Home Page as Dev User
        """
        login_obj.invoke_home_page('mriddev','mrpassdev')
        
        """
        Step 9 : Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 9 : Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 10: Click on 'Data' category
        """
        main_page_obj.select_action_bar_tab('Data')
        
        """
        Step 11 : Click on 'Metadata' action bar
        Verify Metadata action bar open and reporting server metadata Edit screen will first show
        """
        main_page_obj.select_action_bar_tabs_option('Metadata')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(text_css,1,60)
        data_metadata_obj.verify_all_visible_toolbar_buttons(expected_buttons_list,"Step11:verify toolbar buttons")
        data_metadata_obj.verify_specific_conternt_tree_items(expected_tree_list_dev, "Step 11.1:verify Content tree items")
        
        """
        Step 12 : Close that window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 13: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == "__main__":
    unittest.main()