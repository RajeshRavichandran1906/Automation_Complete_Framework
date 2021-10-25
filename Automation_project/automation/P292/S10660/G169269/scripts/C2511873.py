'''
Created on Sep 26, 2018

@author: vishnu priya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511873
TestCase Name = Unable to navigate using Breadcrumbs
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2511873_TestClass(BaseTestCase):

    def test_C2511873(self):
        
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
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search'
        breadcrumb_path1='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples'
        expected_right_arrow_option = ['Retail Samples']
        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """ Step 3: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 2:verify breadcrumb path')
        
        """ Step 4:Click on Retail Samples in the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path1)
        
        """ Step 5:Click the ">" to the left of the Retail Samples in breadcrumbs
            Verify no error occurs and drop down list with all sub folders appears
        """
        wfmain_obj.verify_options_form_right_arrow_in_crumb_box('Breadcrumb Trail and Search', expected_right_arrow_option, 'Step:4')
        
        """ Step 6: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 7: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()  
        