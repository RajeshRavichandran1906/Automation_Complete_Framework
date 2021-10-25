'''
Created on October 25, 2018

@author: AA14564
Testcase Name : Test Run menu
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6670303
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity, core_utility

class C6670303_TestClass(BaseTestCase):
    
    def test_C6670303(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        content_css = "[title='Content view'] .fa-bar-chart"
        breadcrumb_css = ".crumb-box .ibx-label-text"
        expected_list = ['Portal for Context Menu Testing']
        alias_url_path = 'portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        portal_name_css = ".pvd-portal-banner .pvd-portal-title .ibx-label-text"
        
        def verify_portal_run_window():
            core_utilobj.switch_to_new_window()
            util_obj.synchronize_with_visble_text(portal_name_css, expected_list[0], 190)
            util_obj.verify_current_tab_name(expected_list[0], "Step 4: Verify that 'Portal for Context Menu Testing' portal run in a new tab")
            util_obj.verify_current_url(alias_url_path, "Step 4.1: Verify URL as 'http://machinename:port/alias/portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'")
            portal_title_text = util_obj.validate_and_get_webdriver_object(portal_name_css, 'Run banner portal title').text.strip()
            util_obj.asequal(expected_list[0], portal_title_text, 'Step 4.2: Verify portal title.')
            
        """ Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(content_css, 1, 190)
        
        """ Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(breadcrumb_css, 'Domains', 190)
        
        """ Step 3: Click on Favorite View from the sidebar
        """
        main_page_obj.select_favorites_from_sidebar()
        util_obj.synchronize_with_visble_text(breadcrumb_css, 'Favorites', 190)
        
        """ Step 4: Right click on 'Portal for Context Menu T...' > Click Run
                    Verify that 'Portal for Context Menu Testing' portal run in a new tab and 
                    its URL as 'http://machinename:port/alias/portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_list[0], 'Run')
        verify_portal_run_window()
        
        """ Step 5: Close the 'Portal for Context Menu Testing' portal run window
        """
        core_utilobj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element(content_css, 1, 190)
        
        """ Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()    