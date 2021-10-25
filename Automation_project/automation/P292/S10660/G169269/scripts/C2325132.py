'''
Created on April 11, 2019

@author: Niranjan/Samuel

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc&group_id=168356
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2325132
TestCase Name = Navigate to My Content as developers
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325132_TestClass(BaseTestCase):

    def test_C2325132(self):
        
        """
        TESTCASE Objects 
        """
        utillobj = utillity.UtillityMethods( self.driver)
        wftools_login_obj = login.Login( self.driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage( self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        '''
        TESTCASE VARIABLES
        '''
        breadcrumb_path = 'Workspaces->P292_S10660->My Content'
        content_area_css = ".content-box"  
        
        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, wfmain_obj.report_medium_timesleep)
        
        """
        Step 2: Expand Domain > P292_S10660>My Content
        Step 3: Click on My Content in the tree.
        Verify breadcrumb trail is "Domains > P292_S10660 > My Content"
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        utillobj.synchronize_with_visble_text(content_area_css, 'Folder', wfmain_obj.report_medium_timesleep)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 3.1')
        
        """ 
        Step 4: Revert back the Home Page by its default state.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, wfmain_obj.report_medium_timesleep)
        wfmain_obj.expand_repository_folder('Workspaces')
        
        """ 
        Step 5: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        