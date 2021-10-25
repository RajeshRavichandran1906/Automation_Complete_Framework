'''
Created on July 27, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6522017
TestCase Name = Verify Global Resources folder under resource tree for Basic user
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C6522017_TestClass(BaseTestCase):

    def test_C6522017(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        crumb_box_css = ".crumb-box .ibx-label-text"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        utillobj.synchronize_with_visble_text(crumb_box_css, 'Workspaces', long_wait)
        
        """ Step 2: Click Domains from navigation bar.
        """
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 3: Collapse Domains if Domains is expanded.
                    Verify that Web Content and Global Resources are not available under resource tree.
        """
        wfmain_obj.verify_main_node_under_repository_folders('Workspaces', ['Web Content', 'Global Resources'], "Step 3: Verify that Web Content and Global Resources are not available under resource tree.", comparion_type='asnotin')
        
        """ Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()