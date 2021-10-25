'''
Created on October 24, 2018

@author: vpriya
Testcase Name : Test Open using double click option using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6986583
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6986583_TestClass(BaseTestCase):
    
    def test_C6986583(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        breadcrumb_path="P292_S19901->G513445"
        breadcrumb_path1="Domains->P292_S19901->G513445->Portal for Context Menu Testing"
        expected_folder_contentarea=['Portal for Context Menu Testing']
        expected_options_list=['Folder', 'Workbook', 'Page','Shortcut']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        main_page_obj.verify_folders_in_grid_view(expected_folder_contentarea, 'asin',"Step 3:Verify user sees 'Portal for Context Menu Testing' folder.")
        
        """
        Step 4: Double click on 'Portal for Context Menu ...' portal folder from the content area
                Verify that 'Portal for Context Menu Testing' folder is open and breadcrumb as 'Domains> P292_S19901>G513445>Portal for Context Menu Testing
                Verify that Action Bar shows four action tiles are 'Folder, Page, Workbook and Shortcut.
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Open',click_option='double_click')
        util_obj.synchronize_with_visble_text('.content-box.ibx-widget .files-box', 'My Pages', 90)
        main_page_obj.verify_repository_folder_icon_plus_minus('Portal for Context Menu Testing', 'collapse', 'Step 4.1: verify')
        main_page_obj.verify_crumb_box(breadcrumb_path1, 'Step 4.2')
        main_page_obj.verify_action_bar_tab_all_options(expected_options_list,'Step 4.4:')
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        