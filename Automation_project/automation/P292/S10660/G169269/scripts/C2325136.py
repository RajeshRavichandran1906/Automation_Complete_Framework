'''
Created on Sep 25, 2018

@author: vishnu priya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325136
TestCase Name=Select folder from drop down list as developers
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325136_TestClass(BaseTestCase):
    
    def test_C2325136(self):
        
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
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Charts'
        breadcrumb_path1='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Documents'
        expected_grid_item=['Regional Analysis','Sales by Region Dashboard']
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        time.sleep(3)
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", medium_wait)
        
        """ Step 3: Expand Domain > P292_S10660 >G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        """ Step 4: Click on Charts in the content area,Click on > before Charts in breadcrumb trail
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        
        """Step 5:Select Documents from drop down list
           Verify breadcrumb trail is "Domains > P292_S10660_G169261 > Breadcrumb Trail and Search > Retail Samples > Documents".
           Verify Documents is selected in tree and items ('Regional Analysis and Sales by Region Dashboard') in Documents folder appear in canvas area
        """
        wfmain_obj.select_options_form_right_arrow_in_crumb_box('Retail Samples','Documents')
        wfmain_obj.verify_crumb_box(breadcrumb_path1, 'Step 4')
        wfmain_obj.verify_items_in_grid_view(expected_grid_item, 'asin','Step 4.1 verify items in dashboard views' )
        """
        Step 6:Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 7: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()
        