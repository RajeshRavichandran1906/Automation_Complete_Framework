'''
Created on October 25, 2018

@author: Raghunath
Testcase Name : Portal Menu Defaults
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6670291
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib import core_utility

class C6670293_TestClass(BaseTestCase):
    
    def test_C6670293(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        breadcrumb_path="Domains->P292_S19901->G513445"
        folders_css="[data-ibxp-text*='Folders']"
        long_wait = 120
        EXPECTED_URL = 'portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        PAGE_TITLE_CSS = '.pvd-portal-title'
        ITEM_NAME = 'Portal for Context Menu Testing'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)

        
        """
        Step 4: Right click on 'Portal for Context Menu Testing' > Click Run from the resource treee ...'. 
        """
        main_page_obj.select_repository_folder_context_menu('Portal for Context Menu Testing','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(PAGE_TITLE_CSS, ITEM_NAME, 20)
        ACTUAL_URL = self.driver.current_url
        ACTUAL_PAGE_TITLE = util_obj.validate_and_get_webdriver_object(PAGE_TITLE_CSS, 'Page title').text.strip()
        util_obj.asin(EXPECTED_URL, ACTUAL_URL, 'Step 04.01 : Verify V5 portal opens')
        util_obj.asequal(ACTUAL_PAGE_TITLE, ITEM_NAME, "Step 04.02 : Verify that 'Portal for Context Menu Testing' opens in a new tab")
        
        """
        Step 5: Close the run window ...'. 
        """
        core_util_obj.switch_to_previous_window(True)
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    
        