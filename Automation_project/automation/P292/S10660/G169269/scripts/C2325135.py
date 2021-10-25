'''
Created on September 19, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325135
TestCase Name = Click on > before Charts in breadcrumb trail as developers
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325135_TestClass(BaseTestCase):

    def test_C2325135(self):
        
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
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Charts'
        expected_right_arrow_option = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile' , 'Hidden Content']
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", wfmain_obj.home_page_medium_timesleep)
        
        """ Step 2: Expand Domain > P292_S10660 >G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        """ Step 3: Click on Charts in the content area
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        
        """ Step 4: Click on > before Charts in breadcrumb trail
                    Verify drop down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile and Hidden Content
        """
        wfmain_obj.verify_options_form_right_arrow_in_crumb_box('Retail Samples', expected_right_arrow_option, '4', comparision_type='asin')
        
        """ Step 5: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", wfmain_obj.home_page_medium_timesleep)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 6: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        