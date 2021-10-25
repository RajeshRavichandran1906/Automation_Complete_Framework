"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986645
Test Case Title =  Test Run menu using Developers
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C6986645_TestClass(BaseTestCase):

    def test_C6986645(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        ITEM_NAME = 'Portal for Context Menu Testing'
        FOLDER_PATH = 'P292_S19901->G513445'
        EXPECTED_URL = 'portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        PAGE_TITLE_CSS = '.pvd-portal-title'
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developers User
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text("div[title^='Content']", 'Content', 80)
        
        """
            STEP 02 : Content View from the sidebar > Click on Domains from the resource tree 
        """
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_visble_text("div[title='Domains']", 'Domains', 5)
        
        """
            STEP 03 : If not expand Domains > 'P292_S19901' > 'G513445' folder from the resource tree
            STEP 04 : Right click on 'Portal for Context Menu Testing' > Click Run from the resource tree
        """
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME, 'Run', FOLDER_PATH)
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(PAGE_TITLE_CSS, ITEM_NAME, 20)
         
        """
            STEP 04.1 : Verify that 'Portal for Context Menu Testing' opens in a new tab
        """
        ACTUAL_URL = self.driver.current_url
        ACTUAL_PAGE_TITLE = utils.validate_and_get_webdriver_object(PAGE_TITLE_CSS, 'Page title').text.strip()
        utils.asin(EXPECTED_URL, ACTUAL_URL, 'Step 04.01 : Verify V5 portal opens')
        utils.asequal(ACTUAL_PAGE_TITLE, ITEM_NAME, "Step 04.02 : Verify that 'Portal for Context Menu Testing' opens in a new tab")
        
        """
            STEP 05 : Close the run window
        """
        core_utils.switch_to_previous_window()
        
        """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        