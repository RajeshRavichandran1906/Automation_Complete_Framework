"""-------------------------------------------------------------------------------------------
Created on October 24, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6668387
Test Case Title =  Verify Information Builders text logo functionality for Basic User
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C6668387_TestClass(BaseTestCase):

    def test_C6668387(self):
        
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
        EXPECTED_URL = 'www.informationbuilders.com'
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        wf_login.invoke_home_page('mridbas', 'mrpassbas')
        utils.synchronize_with_visble_text(".crumb-box  [title='Domains']", 'Domains', 120)
        
        """
            STEP 02 : Collapse sidebar icon.
        """
        wf_home.collapse_side_bar()
        
        """
            STEP 02.1 : Verify that it shows Information builders logo icon
        """
        utils.verify_picture_using_sikuli("collapse_logo1.png", "Step 02.01 : Verify that it shows Information builders logo icon")
        
        """
            STEP 03 : Click on Information builders logo.
        """
        wf_home.click_on_banner_logo()
        
        """
            STEP 03.1 : Verify that it opens information builders site (http://www.informationbuilders.com/) in a new tab.
        """
        core_utils.switch_to_new_window()
        actual_url = self.driver.current_url
        utils.asin(EXPECTED_URL, actual_url, 'Step 03.01 : Verify information builders site in a new tab')
        
        """
            STEP 04 : Close Business Intelligence and Data Management Software tab.
        """
        core_utils.switch_to_previous_window()
        
        """
            STEP 05 : Click on Expand sidebar icon.
        """
        wf_home.expand_side_bar()
        
        """
            STEP 05.1 : Verify that it shows Information Builders text logo.
        """
        utils.verify_picture_using_sikuli("expanded_menu_icon.png", "Step 05.01 : Verify that it shows Information Builders text logo.")
        
        """
            STEP 06 : Click on Information Builders text logo.
        """
        wf_home.click_on_banner_logo()
        
        """
            STEP 06.1 : Verify that it opens information builders site (http://www.informationbuilders.com/) in a new tab.
        """
        core_utils.switch_to_new_window()
        actual_url = self.driver.current_url
        utils.asin(EXPECTED_URL, actual_url, 'Step 06.01 : Verify information builders site in a new tab')
        core_utils.switch_to_previous_window()
        
        """
            STEP 07.1 : Revert back the Home Page by its default state (Click on Content View and Click on Domains)
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        