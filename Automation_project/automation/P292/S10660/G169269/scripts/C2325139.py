'''
Created on September 25, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325139
TestCase Name = Navigate to Breadcrumb Trail and Search/Retail Samples/Visualizations in tree
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325139_TestClass(BaseTestCase):

    def test_C2325139(self):
        
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
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations'
        expected_right_arrow_option = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile']
        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        
        """ Step 3: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        """ Step 4: Click on Visualizations in tree
                    Verify breadcrumb trail is "Domains > Breadcrumb Trail and Search > Retail Samples > Visualizations".
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 3')
        
        """ Step 5: Click on > before Visualizations in breadcrumb trail
                    Verify drop down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile
        """
        wfmain_obj.verify_options_form_right_arrow_in_crumb_box('Retail Samples', expected_right_arrow_option, '4')
        
        """ Step 6: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 7: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        