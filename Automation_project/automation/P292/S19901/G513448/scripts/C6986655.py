'''
Created on October 25, 2018

@author: AA14564
Testcase Name : Portal Menu Defaults
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6986655
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity

class C6986655_TestClass(BaseTestCase):
    
    def test_C6986655(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        content_css = "[title='Content view'] .fa-bar-chart"
        breadcrumb_css = ".crumb-box .ibx-label-text"
        expected_list = ['Portal for Context Menu Testing']
        properties_menu_list = ['Run', 'Remove from Favorites', 'Properties']
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(content_css, 1, 190)
        
        """ Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(breadcrumb_css, 'Domains', 190)
        
        """ Step 3: Click on Favorites View from the sidebar
                    Verify that 'Portal for Context Menu T...' appears
        """
        main_page_obj.select_favorites_from_sidebar()
        util_obj.synchronize_with_visble_text(breadcrumb_css, 'Favorites', 190)
        main_page_obj.verify_items_in_grid_view(expected_list, 'asin', "Step 3: Verify that 'Portal for Context Menu T...' appears")
        
        """ Step 4: Right click on 'Portal for Context Menu T...'
                    Verify that 'Run', 'Remove from Favorites', and 'Properties' context menus are displayed
        """
        main_page_obj.verify_repository_folder_item_context_menu(expected_list[0], properties_menu_list, msg='Step 4')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()    