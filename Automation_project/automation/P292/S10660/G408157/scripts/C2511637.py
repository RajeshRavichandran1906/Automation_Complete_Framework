"""-------------------------------------------------------------------------------------------
Created on August 05, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2511637
Test Case Title =  HOME 54 Saving any caster items dont automatically refresh the content area 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
# from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C2511637_TestClass(BaseTestCase):

    def test_C2511637(self):
        
        """
            Test case objects    
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
#         locator = WfMainPageLocators()
        
        """
            STEP 1 : Sign into WebFOCUS Home Page as Admin User.
        """
        login.invoke_home_page('mridadm', 'mrpassadm')
        
        """
            STEP 2 : Click Content View from the sidebar > Click on Domains from the resource tree.
            Click on "P292_S10660_G408157" from the tree.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_visble_text(".crumb-box [title] .ibx-label-text", "Workspaces", main_page.home_page_long_timesleep)
        main_page.select_option_from_crumb_box("Workspaces")
        time.sleep(25)
        main_page.expand_repository_folder("P292_S10660_G408157")
        utils.synchronize_with_visble_text("div[class*='files-box-files']", "Access", main_page.home_page_long_timesleep)
        
        """
            STEP 2.1 : Verify Title: "Margin by Product Category - Schedule" is available in the content area.
        """
        main_page.verify_items_in_grid_view(["Margin by Product Category - Schedule"], "asin", "Step 2.1 : Verify Title: 'Margin by Product Category - Schedule' is available in the content area.")
        
        """
            STEP 2.2 : Verify "Alert1" is available under content area:
        """
        main_page.verify_items_in_grid_view(["Alert1"], "asin", "Step 2.2 : Verify 'Alert1' is available under content area:")
        
        """
            STEP 2.3 : Verify "Access List1" is available under the content area:
        """
        main_page.verify_items_in_grid_view(["Access List1"], 'asin', "Step 2.3 : Verify 'Access List1' is available under the content area:")
        
        """
            STEP 2.4 : Verify "Distribution List" is available under content area:
        """
        main_page.verify_items_in_grid_view(['Distribution List'], 'asin', 'Step 2.4 : Verify "Distribution List" is available under content area:')
        
        """
            STEP 3 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()