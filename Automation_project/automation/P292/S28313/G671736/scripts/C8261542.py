'''
Created on April 12, 2019

@author: Niranjan/Samuel
Testcase Name : Test Run menu
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261542
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import designer_portal

class C8261542_TestClass(BaseTestCase):
    
    def test_C8261542(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj = designer_portal.Two_Level_Side(self.driver)
        
        """
        TESTCASE CSS
        """
        PAGE_TITLE_CSS = '.pvd-portal-title'
        
        """
        TESTCASE VARIABLES
        """
        breadcrumb_path="Domains->P292_S19901->G513445"
        EXPECTED_URL = 'portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        ITEM_NAME = 'Portal for Context Menu Testing'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        
        """
        Step 4: Right click on 'Portal for Context Menu Testing' > Click Run from the resource tree
        Verify that 'Portal for Context Menu Testing' opens in a new tab
        """
        main_page_obj.select_repository_folder_context_menu('Portal for Context Menu Testing','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(PAGE_TITLE_CSS, ITEM_NAME, main_page_obj.home_page_medium_timesleep)
        ACTUAL_URL = self.driver.current_url
        ACTUAL_PAGE_TITLE = util_obj.validate_and_get_webdriver_object(PAGE_TITLE_CSS, 'Page title').text.strip()
        util_obj.asin(EXPECTED_URL, ACTUAL_URL, 'Step 04.01 : Verify V5 portal opens')
        util_obj.asequal(ACTUAL_PAGE_TITLE, ITEM_NAME, "Step 04.02 : Verify that 'Portal for Context Menu Testing' opens in a new tab")
        designer_portal_obj.verify_folders_in_left_sidebar(['My Pages'], 'Step 04.03: Verify that portal sidebar')
        
        """
        Step 5: Close the run window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()