'''
Created on Jun 19, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325635
TestCase Name = Check default menu links for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.pages import wf_mainpage
from common.locators import wf_mainpage_locators
from common.lib import utillity
from common.wftools.wf_mainpage import Wf_Mainpage

class C2325635_TestClass(BaseTestCase):

    def test_C2325635(self):
        
        """
        TESTCASE VARIABLES
        """
        Admin_username = 'mrid'
        Admin_password = 'mrpass'
        long_wait = 120
        medium_wait = 60

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = Wf_Mainpage(driver)
        pages_wf_obj = wf_mainpage.Wf_Mainpage(driver)
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        folders_css=".menu-btn div[class*='down']"
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        """
        Step01: Sign into WebFOCUS Home Page as Administrator
        """
        wftools_login_obj.invoke_home_page(Admin_username, Admin_password)
        utillobj.synchronize_with_visble_text(content_css, "Content", medium_wait)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", medium_wait)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
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
        wfmain_obj.verify_username_dropdown_menu(username_dropdown_list, msg= "Step02: Verify menu of user name drop down")
        admin_css = "[class*='fa fa-lock']"
        Tools_css = "[class*='fa fa-legal']"
        Preferences_css = "[class*='fa fa-sliders']"
        Help_css = "[data-ibx-type*='MenuItem'] [class*='fa fa-question']"
        Legacy_css = "[class*='fa fa-home']"
        Change_pwd_css = "[class*='fa fa-key']"
        Sign_out_css = "[class*='fa fa-sign-out']"
        utillobj.verify_object_visible(admin_css, True, "Step02.1a: Verify admin image object is displaying")
        utillobj.verify_object_visible(Tools_css, True, "Step02.1a: Verify Tools image object is displaying")
        utillobj.verify_object_visible(Preferences_css, True, "Step02.1b: Verify Preferences image object is displaying")
        utillobj.verify_object_visible(Help_css, True, "Step02.1c: Verify Help image object is displaying")
        utillobj.verify_object_visible(Legacy_css, True, "Step02.1d: Verify Legacy image object is displaying")
        utillobj.verify_object_visible(Change_pwd_css, True, "Step02.1e: Verify Change_pwd image object is displaying")
        utillobj.verify_object_visible(Sign_out_css, True, "Step02.1f: Verify Sign_out image object is displaying")
        utillobj.verify_picture_using_sikuli("administration.png", "Step02.2a: Verify username dropdown option administration image")
        utillobj.verify_picture_using_sikuli("admin_tools.png", "Step02.2a: Verify username dropdown option tools image")
        utillobj.verify_picture_using_sikuli("preferences.png", "Step02.2b: Verify username dropdown option preferences image")
        utillobj.verify_picture_using_sikuli("help.png", "Step02.2c: Verify username dropdown option help image")
        utillobj.verify_picture_using_sikuli("home.png", "Step02.2d: Verify username dropdown option home image")
        utillobj.verify_picture_using_sikuli("change_password.png", "Step02.2e: Verify username dropdown option change_password image")
        utillobj.verify_picture_using_sikuli("sign_out.png", "Step02.2f: Verify username dropdown option sign out image")
        
        """
        Step04: Hover the mouse to the option Administration.
        Verify Administration context menu with the following options :
        1.Security Center
        2.Administration Console
        3.Manage Private Resources
        4.Mode Normal (Checked by default)
        5.Mode Manager
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        administration_list = ['Security Center', 'Administration Console', 'Manage Private Resources', 'Mode Normal', 'Mode Manager']
        wfmain_obj.select_username_dropdown_menu(navigate_path="Administration")
        mode_css = "[data-ibx-name='miModeNormal']"
        utillobj.synchronize_with_number_of_element(mode_css, 1, long_wait)
        pages_wf_obj.verify_context_menu_item(administration_list, msg="Step03: Verify menu of user name drop down -> Administration")
#         wfmain_obj.verify_username_dropdown_menu(administration_list, navigate_path="Administration", msg= "Step03: Verify menu of user name drop down -> Administration")
        check_modenoraml_status = self.driver.find_element_by_css_selector("[data-ibx-name='miModeNormal']").get_attribute('aria-checked')
        utillobj.asequal('true', check_modenoraml_status, "Step03.1a: Verify Mode Normal is checked")
        check_modemanager_status = self.driver.find_element_by_css_selector("[data-ibx-name='miModeManager']").get_attribute('aria-checked')
        utillobj.asequal('false', check_modemanager_status, "Step03.1b: Verify Mode Manager is unchecked")
        
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
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        tools_list = ['ESRI Configuration Utility', 'Deferred Status', 'Stop Requests', 'Session Viewer', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page']
        wfmain_obj.verify_username_dropdown_menu(tools_list, navigate_path="Tools", msg= "Step04: Verify menu of user name drop down -> Tools")

        """
        Step06: Hover your mouse over the option Help.
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
        wfmain_obj.verify_username_dropdown_menu(help_list, navigate_path="Help", msg= "Step05: Verify menu of user name drop down -> Help")
        
        """
        Step07: In the banner link, click on the top right username > Click Sign Out.
        """
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        