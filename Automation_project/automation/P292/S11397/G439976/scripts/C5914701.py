'''
Created on April 13, 2019

@author: Vpriya

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5914701
TestCase Name = Verify Tags column appears
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5914701_TestClass(BaseTestCase):

    def test_C5914701(self):
        """
        TESTCASE VARIABLES
        """
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator = WfMainPageLocators()
        
        expected_list=['Title', 'Summary', 'Tags', 'Last modified', 'Size', 'Published', 'Shown']
        expected_list_1=['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        
        """ 
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click open Retail Samples -> Reports
        """
        main_page_obj.expand_repository_folder('Retail Samples->Reports')
        util_obj.synchronize_with_visble_text(locator.content_area_css, 'Items', main_page_obj.home_page_long_timesleep)
        
        """
        Step 4: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        
        """
        Step 5:Click Choose columns button
        """
        """
        Step 6:Click on Tags to select
        Verify Tags column appears for all reports as below
        """
        main_page_obj.select_list_view_columns(['Tags'])
        util_obj.synchronize_with_visble_text(".files-box-files-title", "Tags", main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_list_view_title_labels(expected_list,'Step 06.01: Verify Tags column appears for all reports.')
        
        """
        Step 7:Click Choose columns button
        """
        """
        Step 8:Click on Tags to deselect
        Verify Tags column does not appear for all reports as below
        """
        main_page_obj.select_list_view_columns(['Tags'])
        util_obj.synchronize_until_element_disappear("div.files-box-files-title div[data-ibxp-text='Tags']", main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_list_view_title_labels(expected_list_1,'Step 08.01: Verify Tags column does not appear for all reports.')
        
        """
        Step 9: Click toggle button to switch to Grid view
        """
        main_page_obj.select_grid_view()
        util_obj.synchronize_with_visble_text(locator.content_area_css, 'Items', main_page_obj.home_page_long_timesleep)
        
        """
        Step 10: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        