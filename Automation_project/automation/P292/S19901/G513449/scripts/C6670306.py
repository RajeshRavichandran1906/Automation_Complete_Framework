'''
Created on October 24, 2018

@author: Robert
Testcase Name : Portal Menu Defaults using Advanced User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6670306
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6670306_TestClass(BaseTestCase):
    
    def test_C6670306(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumbbox_css = ".crumb-box .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Advanced User
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
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
        
        """
        Step 4. Right click on 'Portal for Context Menu Testing' > Click Open item location
        """
        util_obj.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
        
        """
        Step 4.1. Verify that the following context menus are displayed:
            1.Run
            2.Remove my customizations
            3.Add to Favorites and
            4.Properties
        """
        expected_context_menu_item_list=['Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        main_page_obj.verify_repository_folder_item_context_menu('Portal for Context Menu Testing', expected_context_menu_item_list, msg='Step 4.1 Verify the context menu options')
        
        """
        Step 5. In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        