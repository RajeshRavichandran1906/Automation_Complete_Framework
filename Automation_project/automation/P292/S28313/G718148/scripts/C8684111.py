'''
Created on March 7, 2019

@author: Niranjan/Samuel

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/28313&group_by=cases:section_id&group_order=asc&group_id=718148
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8684111
TestCase Name = Check default menu links for Developer User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C8684111_TestClass(BaseTestCase):

    def test_C8684111(self):
        
        """
        TESTCASE VARIABLES
        """
        devuser_username = 'mrid03'
        devuser_password = 'mrpass03'
        folders_css=".menu-btn div[class*='down']"
        

        """
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page(devuser_username, devuser_password)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.expand_repository_folder('Domains')
        
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
        Tools_css = "[class*='fa fa-legal']"
        Preferences_css = "[class*='fa fa-sliders']"
        Help_css = "[data-ibx-type*='MenuItem'] [class*='fa fa-question']"
        Legacy_css = "[class*='fa fa-home']"
        Change_pwd_css = "[class*='fa fa-key']"
        Sign_out_css = "[class*='fa fa-sign-out']"
        utillobj.verify_object_visible(Tools_css, True, "Step03.1a: Verify Tools image object is displaying")
        utillobj.verify_object_visible(Preferences_css, True, "Step03.1b: Verify Preferences image object is displaying")
        utillobj.verify_object_visible(Help_css, True, "Step03.1c: Verify Help image object is displaying")
        utillobj.verify_object_visible(Legacy_css, True, "Step03.1d: Verify Legacy image object is displaying")
        utillobj.verify_object_visible(Change_pwd_css, True, "Step03.1e: Verify Change_pwd image object is displaying")
        utillobj.verify_object_visible(Sign_out_css, True, "Step03.1f: Verify Sign_out image object is displaying")
        utillobj.verify_picture_using_sikuli("tools.png", "Step03.2a: Verify username dropdown option tools image")
        utillobj.verify_picture_using_sikuli("preferences.png", "Step03.2b: Verify username dropdown option preferences image")
        utillobj.verify_picture_using_sikuli("help.png", "Step03.2c: Verify username dropdown option help image")
        utillobj.verify_picture_using_sikuli("home.png", "Step03.2d: Verify username dropdown option home image")
        utillobj.verify_picture_using_sikuli("change_password.png", "Step03.2e: Verify username dropdown option change_password image")
        utillobj.verify_picture_using_sikuli("sign_out.png", "Step03.2f: Verify username dropdown option sign out image")
        
        """
        Step04: Hover your mouse over the option Tools.
        Verify Tools context menu with the following options :
        1.ESRI Configuration Utility
        2.Deferred Status
        3.Stop Requests
        4.Session Viewer
        5.ReportCaster Explorer
        6.ReportCaster Status
        7.Magnify Search Page
        8.WebFOCUS Infographics
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, wfmain_obj.home_page_medium_timesleep)
        tools_list = ['ESRI Configuration Utility', 'Deferred Status', 'Stop Requests', 'Session Viewer', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page']
        wfmain_obj.verify_username_dropdown_menu(tools_list, navigate_path="Tools", msg= "Step04: Verify menu of user name drop down -> Tools",comparision_type='asin')
        
        """
        Step05: Hover your mouse over the option Help.
        Verify Help context menu with the the following options :
        1.WebFOCUS Online Helpl
        2.Technical Resources
        3.Community
        4.Information Builders Home
        5.About WebFOCUS
        6.Licenses
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, wfmain_obj.home_page_medium_timesleep)
        help_list = ['WebFOCUS Online Help','Technical Resources','Community','Information Builders Home','About WebFOCUS','Licenses']
        wfmain_obj.verify_username_dropdown_menu(help_list, navigate_path="Help", msg= "Step05: Verify menu of user name drop down -> Help")
        
        """
        Step06: In the banner link, click on the top right user name > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        