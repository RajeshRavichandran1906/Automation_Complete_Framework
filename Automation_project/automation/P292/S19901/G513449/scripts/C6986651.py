'''
Created on October 24, 2018

@author: Robert
Testcase Name : Test Open item location menu using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6986651
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6986651_TestClass(BaseTestCase):
    
    def test_C6986651(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        project_id = util_obj.parseinitfile('project_id')
        suite_id = util_obj.parseinitfile('suite_id')
        group_id = util_obj.parseinitfile('group_id')
        folder_path="{0}_{1}->{2}".format(project_id, suite_id, group_id)
        crumbbox_css = ".crumb-box .ibx-label-text"
        ibi_logo_css="div[class^='home-banner ibx-widget'] div.banner-logo"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(ibi_logo_css, 1, 40, 1)
        
        """
        Step 2. Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3. Click on Portal View from the sidebar
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
        
        """
        Step 4. Right click on 'Portal for Context Menu Testing' > Click Open item location
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Open item location')
        element_css="div[class^='folder-item folder-item-selected']"
        util_obj.synchronize_with_visble_text(element_css, 'Portal for Context Menu Testing', 45)
        
        """
        Step 4.1. Verify that user now in the content area under the place where the portal was created (Domains > P292_S19901 > G513445) and it is highlighted in blue and the domain/folders is in grey
        """
        grid_list=['Portal for Context Menu Testing']
        main_page_obj.verify_folders_in_grid_view(grid_list, 'asin', 'Step 4.1. Verify the portal in grid view')
        util_obj.verify_element_text(element_css, 'Portal for Context Menu Testing', 'Step 4.1. Verify highlighted item')
        main_page_obj.verify_crumb_box('Domains->{0}'.format(folder_path), "Step 04.02 : Verify that place where the portal was created (Domains > P292_S19901 > G513445)")
        
        """
        Step 5. Right click on 'Portal for Context Menu T...'
        Step 5.1. Verify that following Context Menu appears as same in the below screenshot
        """
        expected_context_menu_item_list=['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        main_page_obj.verify_repository_folder_item_context_menu('Portal for Context Menu Testing', expected_context_menu_item_list, folder_path,'Step 5.1 Verify the context menu options')
        
        """
        Step 6. In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()