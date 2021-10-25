'''
Created on May 8, 2019

@author: varun
Testcase Name : Check default menu links for Developer User
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9331935
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity


class C9331935_TestClass(BaseTestCase):
    
    def test_C9331935(self):
        """
        Test case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        workspace = "Workspaces"
        domains_css = ".toolbar"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(workspace)
        
        """
        Step 3: In the banner link, click on the top right username.
        Verify drop down menu with the following options :
        1.Tools
        2.Preferences
        3.Help
        4.Legacy Home Page
        5.Change Password
        6.Sign Out
        """
        expected_name_list = ['Tools', 'Preferences', 'Help', 'Legacy Home Page', 'Change Password', 'Sign Out']
        main_page_obj.verify_username_dropdown_menu(expected_name_list, msg='Step 3.1: Verify the dropdown list')
        
        """
        Step 4: Hover your mouse over the option Tools.
        Verify Tools context menu with the following options :
        1.Deferred Status
        2.Stop Requests
        3.Session Viewer
        4.ReportCaster Explorer
        5.ReportCaster Status
        6.Magnify Search Page
        7. WebFOCUS InfoGraphics
        """
        expected_name_list = ['Deferred Status', 'Stop Requests', 'Session Viewer', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page', 'WebFOCUS Infographics']
        main_page_obj.verify_username_dropdown_menu(expected_name_list, navigate_path='Tools', msg='Step 4.1: Verify the Tools dropdown list')
        
        """
        Step 5: Hover your mouse over the option Help.
        Verify Help context menu with the the following options :

        1.WebFOCUS Online Help
        2.Technical Resources
        3.Community
        4.Information Builders Home
        5.About WebFOCUS
        6.Licenses
        """
        expected_name_list = ['WebFOCUS Online Help', 'Technical Resources', 'Community', 'Information Builders Home', 'About WebFOCUS', 'Licenses']
        main_page_obj.verify_username_dropdown_menu(expected_name_list, navigate_path='Help', msg='Step 5.1: Verify the help dropdown list')
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()