'''
Created on August 01, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=433350&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5831950
TestCase Name = Verify context menus for Global Resources node
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import base

class C5831950_TestClass(BaseTestCase):

    def test_C5831950(self):
        
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        base_obj = base.BasePage(self.driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        
        """ Step 2: Click Domains from navigation bar.
        """
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """ Step 3: ollapse Domains if Domains is expanded.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 4: Right click on Global Resources node.
                    Verify that following options are displayed:
                    1.Expand.
                    2.Refresh.
        """
        wfmain_obj.verify_repository_folder_context_menu('Global Resources', ['Expand', 'Refresh'], msg='Step 4:', comparision_type='asin', verification_state='collpase')
        
        """ Step 5: Expand Global Resources node.
                    Verify that following options are displayed:
                    1.Page Templates.
                    2.Page Templates (Legacy).
                    3.Themes.
        """
        wfmain_obj.expand_repository_folders_and_verify('Global Resources', ['Page Templates', 'Page Templates (Legacy)', 'Themes'], msg="Step 5: Verify that following options 'Page Templates', 'Page Templates (Legacy)', 'Themes' are displayed.")
        
        """ Step 6: Right click on Global Resources node > click Collapse.
                    Verify that Global Resources node is collapsed.
        """
        wfmain_obj.select_repository_folder_context_menu('Global Resources', 'Collapse', verification_state='expand')
        time.sleep(2)
        wfmain_obj.collapse_repository_folders_and_verify('Global Resources', ['Page Templates', 'Page Templates (Legacy)', 'Themes'], msg="Step 6: Verify that Global Resources node is collapsed and 'Page Templates', 'Page Templates (Legacy)', 'Themes' options are not displayed.", comparion_type='asnotin')
        
        """ Step 7: Right click on Global Resources node > click Refresh.
                    Verify that now page is refreshed.
        """
        wfmain_obj.select_repository_folder_context_menu('Global Resources', 'Refresh', verification_state='collpase')
        wfmain_obj.expand_repository_folders_and_verify('Global Resources', ['Page Templates', 'Page Templates (Legacy)', 'Themes'], msg="Step 5: Verify that now page is refreshed and following options 'Page Templates', 'Page Templates (Legacy)', 'Themes' are displayed.")
        
        """ Step 8: Revert back the Home page to its default by clicking Domains under repository tree.
        """
        wfmain_obj.collapse_repository_folder('Domains')
        
        """ Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()