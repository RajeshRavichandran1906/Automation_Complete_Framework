'''
Created on October 24, 2018

@author: varun
Testcase Name : Test Run menu
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6670288
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators


class C6670288_TestClass(BaseTestCase):
    
    def test_C6670288(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        url_to_verify = "portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing"
        title_css =  ".pvd-portal-banner .pvd-portal-title .ibx-label-text"
        title_to_verify = "Portal for Context Menu Testing"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
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
        main_page_obj.expand_repository_folder('P292_S19901->G513445')
        
        """
        Step 4: Right click on 'Portal for Context Menu ...' > Click Run
        Verify that 'Portal for Context Menu Testing' run in a new tab and URL displayed as below: 
        http://machinename:port/alias/portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(title_css, 1, Global_variables.mediumwait)
        util_obj.verify_current_url(url_to_verify, 'Step 4.1:URL-Verification')
        title = util_obj.validate_and_get_webdriver_object(title_css, 'Title-css-validation').text.strip()
        util_obj.asequal(title,title_to_verify,'Step 4.2: Title Verification')
        
        """
        Step 5: Close the 'Portal for Context Menu Testing' run window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()