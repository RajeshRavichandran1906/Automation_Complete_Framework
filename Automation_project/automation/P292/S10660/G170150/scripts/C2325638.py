'''
Created on May 24, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325638
TestCase Name = Check default menu links for Basic User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2325638_TestClass(BaseTestCase):

    def test_C2325638(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2325638'
        basicuser_username = 'mrid01'
        basicuser_password = 'mrpass01'
        long_wait = 120
        medium_wait = 60
        short_wait = 30

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        files_box_css = ".sd-content-title-label-folders .content-title-label .ibx-label-text"
        
        """
        Step01: Sign into WebFOCUS Home Page as Administrator
        """
        wftools_login_obj.invoke_home_page(basicuser_username, basicuser_password)
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """
        Step03: In the banner link, click on the top right username.
        Verify drop down menu with the following options :
        1.Tools
        2.Preferences
        3.Help
        4.Legacy Home Page
        5.Change Password
        6.Sign Out
        """
        username_dropdown_list = ['Tools','Preferences','Help','Legacy Home Page','Change Password','Sign Out']
        wfmain_obj.verify_username_dropdown_menu(username_dropdown_list, msg= "Step02: Verify menu of user name drop down")
        
        """
        Step04: Hover your mouse over the option Tools.
        Verify Tools context menu with the following options :
        1.Deferred Status
        2.Stop Requests
        3.Magnify Search Page
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        tools_list = ['Deferred Status', 'Stop Requests', 'Magnify Search Page']
        wfmain_obj.verify_username_dropdown_menu(tools_list, navigate_path="Tools", msg= "Step03: Verify menu of user name drop down -> Tools")
        
        """
        Step05: Hover your mouse over the option Help.
        Verify Help context menu with the the following options :
        1.WebFOCUS Online Help
        2.Information Center
        3.VideoAssist
        4.Technical Library
        5.Community
        6.Information Builders Home
        7.About WebFOCUS
        8.Licenses
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        help_list = ['WebFOCUS Online Help','Information Center','VideoAssist','Technical Library','Community','Information Builders Home','About WebFOCUS','Licenses']
        wfmain_obj.verify_username_dropdown_menu(help_list, navigate_path="Help", msg= "Step04: Verify menu of user name drop down -> Help")
        
        """
        Step06: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        