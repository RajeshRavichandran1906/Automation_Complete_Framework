'''
Created on Jun 7, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325641
TestCase Name = Check default menu links for Advanced User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C2325641_TestClass(BaseTestCase):

    def test_C2325641(self):
        
        """
        TESTCASE VARIABLES
        """
        
        devuser_username = 'mrid03'
        devuser_password = 'mrpass03'
        long_wait = 120
        medium_wait = 60

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page(devuser_username, devuser_password)
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        items_css="[data-ibxp-text*='Items']"
        utillobj.synchronize_with_number_of_element(items_css, 1, long_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        files_box_css = ".content-box.ibx-widget .files-box"
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """
        Step02: In the banner link, click on the top right username.
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
        utillobj.verify_object_visible(Tools_css, True, "Step02.1a: Verify Tools image object is displaying")
        utillobj.verify_object_visible(Preferences_css, True, "Step02.1b: Verify Preferences image object is displaying")
        utillobj.verify_object_visible(Help_css, True, "Step02.1c: Verify Help image object is displaying")
        utillobj.verify_object_visible(Legacy_css, True, "Step02.1d: Verify Legacy image object is displaying")
        utillobj.verify_object_visible(Change_pwd_css, True, "Step02.1e: Verify Change_pwd image object is displaying")
        utillobj.verify_object_visible(Sign_out_css, True, "Step02.1f: Verify Sign_out image object is displaying")
        utillobj.verify_picture_using_sikuli("tools.png", "Step02.2a: Verify username dropdown option tools image")
        utillobj.verify_picture_using_sikuli("preferences.png", "Step02.2b: Verify username dropdown option preferences image")
        utillobj.verify_picture_using_sikuli("help.png", "Step02.2c: Verify username dropdown option help image")
        utillobj.verify_picture_using_sikuli("home.png", "Step02.2d: Verify username dropdown option home image")
        utillobj.verify_picture_using_sikuli("change_password.png", "Step02.2e: Verify username dropdown option change_password image")
        utillobj.verify_picture_using_sikuli("sign_out.png", "Step02.2f: Verify username dropdown option sign out image")
        
        """
        Step03: Hover your mouse over the option Tools.
        Verify Tools context menu with the following options :
        1.ESRI Configuration Utility
        2.Deferred Status
        3.Stop Requests
        4.Session Viewer
        5.ReportCaster Explorer
        6.ReportCaster Status
        7.Magnify Search Page
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        tools_list = ['ESRI Configuration Utility', 'Deferred Status', 'Stop Requests', 'Session Viewer', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page']
        wfmain_obj.verify_username_dropdown_menu(tools_list, navigate_path="Tools", msg= "Step03: Verify menu of user name drop down -> Tools")
        
        """
        Step04: Hover your mouse over the option Help.
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
        Step05: In the banner link, click on the top right user name > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        