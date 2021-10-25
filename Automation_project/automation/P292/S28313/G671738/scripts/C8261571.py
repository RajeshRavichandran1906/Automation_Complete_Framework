'''
Created on October 26, 2018

@author: varun
Testcase Name : Test Remove Favorites using Basic User
Testcase ID : lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261571
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators import wf_mainpage_locators

class C8261571_TestClass(BaseTestCase):
    
    def test_C8261571(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        domain_css = ".toolbar"
        favourite_css = ".crumb-box div[data-ibx-type=\"ibxLabel\"] .ibx-label-text"
        workspace = "Workspaces"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        main_page_obj.select_option_from_crumb_box(workspace)
        
        """
        Step 3: Click on Favorite View from the sidebar
        """
        util_obj.synchronize_with_visble_text(domain_css, workspace, Global_variables.mediumwait)
        main_page_obj.select_favorites_from_sidebar()
        
        """
        Step 4: Right click on 'Portal for Context Menu Testing' > Click Remove from Favorites
        """
        util_obj.synchronize_with_visble_text(favourite_css, 'Favorites', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Remove from Favorites')
        main_page_obj.verify_folders_in_grid_view(['Portal for Context Menu Testing'], 'asnotin', 'Step 4:')
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()