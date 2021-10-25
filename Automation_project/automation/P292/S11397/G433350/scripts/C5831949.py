'''
Created on July 26, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5831949
TestCase Name = Verify Global Resources folder under resource tree
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import base

class C5831949_TestClass(BaseTestCase):

    def test_C5831949(self):
        
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        
        """ Step 2: Click Domains from navigation bar.
        """
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 3: Collapse Domains if Domains is expanded.
                    Verify that Domains, Web Content and Global Resources are available as main nodes under resource tree.
        """
        wfmain_obj.collapse_repository_folder("Workspaces")
        wfmain_obj.verify_main_node_under_repository_folders('Workspaces', ['Workspaces', 'Web Content', 'Global Resources'], "Step 3: Verify that Domains, Web Content and Global Resources are available as main nodes under resource tree.")
        
        """ Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        