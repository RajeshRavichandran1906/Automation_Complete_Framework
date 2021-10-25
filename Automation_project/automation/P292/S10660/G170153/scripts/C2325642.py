'''
Created on Jun 12, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325642
TestCase Name = Check default menu links for Public User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2325642_TestClass(BaseTestCase):

    def test_C2325642(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2325642'
        long_wait = 120
        medium_wait = 60
        short_wait = 30

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Public User by clicking the Public access Link.
        """
        wftools_login_obj.invoke_home_page_with_public_access()
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """
        Step02: In the banner link, click on the top right username (Public User)
        Verify drop down menu with the following options :
        1.Help
        2.Legacy Home Page
        3.Sign In
        """
        username_dropdown_list = ['Help','Legacy Home Page','Sign In']
        wfmain_obj.verify_username_dropdown_menu(username_dropdown_list, msg= "Step02: Verify menu of user name drop down")
        Tools_css = "[class*='fa fa-legal']"
        Help_css = "[data-ibx-type*='MenuItem'] [class*='fa fa-question']"
        Legacy_css = "[class*='fa fa-home']"
        Sign_in_css = "[class*='fa fa-sign-in']"
        utillobj.verify_object_visible(Tools_css, False, "Step02.1a: Verify Tools image object is displaying")
        utillobj.verify_object_visible(Help_css, True, "Step02.1b: Verify Help image object is displaying")
        utillobj.verify_object_visible(Legacy_css, True, "Step02.1c: Verify Legacy image object is displaying")
        utillobj.verify_object_visible(Sign_in_css, True, "Step02.1d: Verify Sign_in image object is displaying")
        utillobj.verify_picture_using_sikuli("help.png", "Step02.2a: Verify username dropdown option help image")
        utillobj.verify_picture_using_sikuli("home.png", "Step02.2b: Verify username dropdown option home image")
        utillobj.verify_picture_using_sikuli("sign_in.png", "Step02.2c: Verify username dropdown option sign in image")
        
        """
        Step03: Hover your mouse over the option Help.
        Verify Help context menu with the the following options :
        1.WebFOCUS Online Help
        2.Information Center
        3.VideoAssist
        4.Technical Library
        5.Community
        6.Information Builders Home
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        help_list = ['WebFOCUS Online Help','Information Center','VideoAssist','Technical Library','Community','Information Builders Home']
        wfmain_obj.verify_username_dropdown_menu(help_list, navigate_path="Help", msg= "Step03: Verify menu of user name drop down -> Help")
        
        """
        Step04: In the banner link, click on the top right username > Click Sign In.
        Verify it back to WebFOCUS Sign In Page.
        """
        wfmain_obj.signin_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        