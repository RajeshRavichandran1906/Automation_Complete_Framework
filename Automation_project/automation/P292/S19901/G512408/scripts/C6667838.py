'''
Created on Dec 14, 2018

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667838
Testcase Name : Verify the remembering of Category Button
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6667838_TestClass(BaseTestCase):

    def test_C6667838(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        
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
        Step 3: Click on 'Retail Samples' from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'Data' category button
        """
        main_page_obj.select_action_bar_tab('Data')
        
        """
        Step 4.1: Verify that Upload data, Connect, Metadata, reporting object Action bars are displayed under 'Data' category
        """
        labels_list=['Upload Data','Connect','Metadata','Reporting Object']
        main_page_obj.verify_action_bar_tab_all_options(labels_list, "Step 4.1: Verify that Upload data, Connect, Metadata, reporting object Action bars are displayed under 'Data' category")       
        
        """
        Step 5: Click on 'P292_S19901' from the resource tree
        """
        main_page_obj.click_repository_folder('P292_S19901')
        
        """
        Step 5.1: Verify that still 'Data' category is chosen
        Also, Verify that Upload data, Connect, Metadata, reporting object Action bars are displayed
        """
        main_page_obj.verify_selected_action_bar_tab(['Data'], "Step 5.1: Verify that still 'Data' category is chosen")
        labels_list=['Upload Data','Connect','Metadata','Reporting Object']
        main_page_obj.verify_action_bar_tab_all_options(labels_list, "Step 5.2: Verify that Upload data, Connect, Metadata, reporting object Action bars are displayed")       
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()