'''
Created on July 27, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6522016
TestCase Name = Verify Global Resources folder under resource tree for Developer user
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6522016_TestClass(BaseTestCase):

    def test_C6522016(self):
        
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """ Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """ Step 3: Click Domains from navigation bar.
        """
        main_page_obj.expand_repository_folder('Domains')
        
        """ Step 4: Collapse Domains if Domains is expanded.
                    Verify that Web Content and Global Resources are not available under resource tree.
        """
        wfmain_obj.verify_main_node_under_repository_folders('Domains', ['Web Content', 'Global Resources'], "Step 3: Verify that Web Content and Global Resources are not available under resource tree.", comparion_type='asnotin')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()