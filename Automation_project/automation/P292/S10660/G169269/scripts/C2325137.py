'''
Created on Sep 25, 2018

@author: vishnu priya.
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325137
TestCase Name =Sign in as basic user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325137_TestClass(BaseTestCase):
    
    def test_C2325137(self):
        
        """
        TESTCASE Objects 
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        '''
        TESTCASE VARIABLES
        '''
        medium_wait = 60
        tree_css = wf_mainpage_locators.WfMainPageLocators.REPOSITORY_TREE_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261'
        expected_folder_contentarea=['Breadcrumb Trail and Search']
        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        
        """Step 3:Expand Domain > P292_S10660>Click G169261
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        wfmain_obj.verify_folders_in_grid_view(expected_folder_contentarea, 'asListEqual',"Step 2:Verify user sees 'Breadcrumb Trail and Search' folder.")
        
        """
        Step 4:Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 5: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()
        
        