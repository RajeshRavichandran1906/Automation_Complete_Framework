'''
Created on April 16, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5824997
TestCase Name = Sign in as domain developer
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.pages import wf_mainpage as pages_main

class C5824997_TestClass(BaseTestCase):

    def test_C5824997(self):
        
        """
        TESTCASE VARIABLES
        """
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """ 
        Step 1: Login WF as domain developer
        Verify P292_S10863_G193429 domain appears in tree
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(20)
        main_pages_obj.verify_repository_folders('Domains', ['P292_S10863_G193429'], "Step 01.01: Verify the folder present", comparion_type='asin')
        
        """
        Step 2: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()