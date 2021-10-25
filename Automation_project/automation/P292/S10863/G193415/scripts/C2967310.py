'''
Created on October 23, 2018

@author: Varun
Testcase Name : Verify what Side Bar collapse/expand for a Public User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2967310
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib import base
from common.locators import wf_mainpage_locators

class C2967310_TestClass(BaseTestCase):
    
    def test_C2967310(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        content_list=['Content','Portals']
     
        """
        Step 1: Sign into WebFOCUS Home Page as Public User by clicking the Public access Link.
        Verify sidebar listed with the following options :
        1.Content View (By default selected).
        2.Portals View.
        """
        login_obj.invoke_home_page_with_public_access()
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1,base_obj.home_page_medium_timesleep )
        main_page_obj.verify_left_panel(content_list, 'Step 1.1 Verify Sidebar options')
        
        """
        Step 2: Click on the Collapse side bar icon.
        """
        main_page_obj.collapse_side_bar()
        main_page_obj.verify_left_panel([], "Step2.1: Verify Side bar(left panel) options doesn't show any text",'')
        util_obj.verify_picture_using_sikuli("collapse_content.png", "Step2.2: Verify content image is displayed")
        util_obj.verify_picture_using_sikuli("collapse_portal.png", "Step2.3: Verify portals image displayed")
        util_obj.verify_picture_using_sikuli("collapse_logo.png", "Step2.4: Verify collapse logo image is displayed")
        
        """
        Step 3: In the banner link, click on the top right username > Click Sign In.
        """
        main_page_obj.signin_from_username_dropdown_menu()
        
        """
        Step 4: Again Sign back into WebFOCUS Home Page as Public User by clicking the Public access Link.
        """
        login_obj.invoke_home_page_with_public_access()
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1, base_obj.home_page_medium_timesleep )
        main_page_obj.verify_left_panel(content_list, 'Step 4.1 Verify Sidebar options')
        util_obj.verify_picture_using_sikuli("expanded_logo.png", "Step4.2: Verify expanded logo is displayed")
        util_obj.verify_picture_using_sikuli("expanded_menu_icon.png", "Step4.3: Verify expanded menu icon is displayed")
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign In.
        """
        main_page_obj.signin_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        