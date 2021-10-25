'''
Created on September 18, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325131
TestCase Name = Navigate to domain as developers
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325131_TestClass(BaseTestCase):

    def test_C2325131(self):
        
        """
        TESTCASE Objects 
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        medium_wait = 60
        
        '''
        TESTCASE VARIABLES
        '''
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search'
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", medium_wait)
        
        """ Step 3: Expand Domain > P292_S10660>G169261>Click "Breadcrumb Trail and Search" in tree
                    Verify breadcrumb trail is "Domains > P292_S10660_G169261 > Breadcrumb Trail and Search"
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 3')
        
        """ Step 4: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 5: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        