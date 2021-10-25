'''
Created on April 13, 2019

@author: Vpriya

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5914700
TestCase Name = Verify Tags appears in drop down list
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.pages import wf_mainpage as pages_main

class C5914700_TestClass(BaseTestCase):

    def test_C5914700(self):
        
        """
        TESTCASE VARIABLES
        """
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """ 
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click open Retail Samples -> Reports
        """
        main_page_obj.expand_repository_folder('Retail Samples->Reports')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Items', main_page_obj.home_page_long_timesleep)
        
        """
        Step 4: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        
        """
        Step 5:Click Choose columns button
        Verify Tags appears in drop down list as below
        """
        main_page_obj.select_choose_columns_in_list_view()
        main_pages_obj.verify_context_menu_item(['Tags'], 'Step 13.1: Verify Tags in drop down list',comparision_type='asin')
        
        """
        Step 6: Click toggle button to switch to Grid view
        """
        main_page_obj.select_grid_view()
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 7: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        