'''
Created on March 8, 2019

@author: Niranjan/Samuel

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/28313&group_by=cases:section_id&group_id=718145&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8684115
TestCase Name = Check default menu links for Admin User

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C8684115_TestClass(BaseTestCase):

    def test_C8684115(self):
        
        """
        TESTCASE VARIABLE
        """
        folders_css=".menu-btn div[class*='down']"
        

        """
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.expand_repository_folder('Domains')
        
        """
        Step03: In the banner link, click on the top right username.
        Verify drop down menu with the following options :
        1.Administration
        2.Tools
        3.Preferences
        4.Help
        5.Legacy Home Page
        6.Change Password
        7.Sign Out
        """
        username_dropdown_list = ['Administration','Tools','Preferences','Help','Legacy Home Page','Change Password','Sign Out']
        wfmain_obj.verify_username_dropdown_menu(username_dropdown_list, msg= "Step03: Verify menu of user name drop down")
        Administration_css = "[class*='fa fa-lock']"
        Tools_css = "[class*='fa fa-legal']"
        Preferences_css = "[class*='fa fa-sliders']"
        Help_css = "[data-ibx-type*='MenuItem'] [class*='fa fa-question']"
        Legacy_css = "[class*='fa fa-home']"
        Change_pwd_css = "[class*='fa fa-key']"
        Sign_out_css = "[class*='fa fa-sign-out']"
        utillobj.verify_object_visible(Administration_css, True, "Step03.1a: Verify Administration image object is displaying")
        utillobj.verify_object_visible(Tools_css, True, "Step03.1b: Verify Tools image object is displaying")
        utillobj.verify_object_visible(Preferences_css, True, "Step03.1c: Verify Preferences image object is displaying")
        utillobj.verify_object_visible(Help_css, True, "Step03.1d: Verify Help image object is displaying")
        utillobj.verify_object_visible(Legacy_css, True, "Step03.1e: Verify Legacy image object is displaying")
        utillobj.verify_object_visible(Change_pwd_css, True, "Step03.1f: Verify Change_pwd image object is displaying")
        utillobj.verify_object_visible(Sign_out_css, True, "Step03.1g: Verify Sign_out image object is displaying")
        utillobj.verify_picture_using_sikuli("Administration.png", "Step03.2a: Verify username dropdown option Administration image")
        utillobj.verify_picture_using_sikuli("tools.png", "Step03.2b: Verify username dropdown option tools image")
        utillobj.verify_picture_using_sikuli("preferences.png", "Step03.2c: Verify username dropdown option preferences image")
        utillobj.verify_picture_using_sikuli("help.png", "Step03.2d: Verify username dropdown option help image")
        utillobj.verify_picture_using_sikuli("home.png", "Step03.2e: Verify username dropdown option home image")
        utillobj.verify_picture_using_sikuli("change_password.png", "Step03.2f: Verify username dropdown option change_password image")
        utillobj.verify_picture_using_sikuli("sign_out.png", "Step03.2g: Verify username dropdown option sign out image")
         
        """
        Step04: Hover the mouse to the option Administration.
        Verify Administration context menu with the following options :
        1.Security Center
        2.Administration Console
        3.Manage Private Resources
        4.Mode Normal (Checked by default)
        5.Mode Manager
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, wfmain_obj.home_page_medium_timesleep)
        admin_list = ['Security Center', 'Administration Console', 'Manage Private Resources', 'Mode Normal', 'Mode Manager']
        for element in admin_list:
            wfmain_obj.verify_username_dropdown_menu([element], navigate_path="Administration", msg= "Step04: Verify menu of Administration drop down -> Administration", comparision_type='asin')
        
        
        """
        Step05: Hover your mouse over the option Tools.
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
        wfmain_obj.verify_username_dropdown_menu(tools_list, navigate_path="Tools", msg= "Step05: Verify menu of user name drop down -> Tools", comparision_type='asin')
        
        """
        Step06: Hover your mouse over the option Help.
        Verify Help context menu with the the following options :
        1.WebFOCUS Online Help
        2.Technical Resources
        3.Community
        4.Information Builders Home
        5.About WebFOCUS
        6.Licenses
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, wfmain_obj.home_page_medium_timesleep)
        help_list = ['WebFOCUS Online Help','Technical Resources','Community','Information Builders Home','About WebFOCUS','Licenses']
        wfmain_obj.verify_username_dropdown_menu(help_list, navigate_path="Help", msg= "Step06: Verify menu of user name drop down -> Help")
        
        """
        Step07: In the banner link, click on the top right user name > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        