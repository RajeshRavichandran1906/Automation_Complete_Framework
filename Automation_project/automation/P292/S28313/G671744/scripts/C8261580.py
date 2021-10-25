'''
Created on April 10, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261580
TestCase Name = Verify adding Tags in List View enables sorting by Tags in Grid View
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages import wf_mainpage as pages_main
import time

class C8261580_TestClass(BaseTestCase):

    def test_C8261580(self):
        """
        TESTCASE VARIABLES
        """
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """ 
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on "Retail samples" domain ->Click on Search folder
        """
        main_page_obj.select_option_from_crumb_box('Workspaces')
        main_page_obj.click_repository_folder('Retail Samples')
        main_page_obj.expand_repository_folder('Retail Samples->Search')
        util_obj.wait_for_page_loads(10)
        
        """
        Step 4: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        util_obj.wait_for_page_loads(10)
        
        """
        Step 5: Click Choose Columns button ->Click Tags in drop down list
        """
        main_page_obj.select_list_view_columns(['Tags'])
        
        """
        Step 6: Click on the content area to close the drop down list 
        """
        content_area = util_obj.validate_and_get_webdriver_object(".files-box .files-listing", 'file-listing')
        core_util_obj.left_click(content_area, element_location='bottom_right')
        
        """
        Step 7: Click toggle button to switch to Grid view
        """
        main_page_obj.select_grid_view()
        util_obj.wait_for_page_loads(10)
        
        """
        Step 8: Type * in Search box
        Verify Tags appear above all items in content area
        """
        main_page_obj.search_input_box_options(input_text_msg='*')
        util_obj.wait_for_page_loads(10)
        time.sleep(4)
        main_page_obj.verify_favorites_tags(['Brand', 'Business Region', 'Comparison', 'Cost', 'Customer', 'Model', 'Product', 'Profit', 'Revenue', 'Sales Metrics', 'Store'], 08.01)
        
        """
        Step 9: Click Title Sort ->Click Tags in drop down list
        Verify Tags is selected as the sort:
        Verify items are sorted by Tags:
        """
        title_button = util_obj.validate_and_get_webdriver_object(".content-title-btn-name", 'tag-name')
        core_util_obj.left_click(title_button)
        util_obj.wait_for_page_loads(10)
        main_pages_obj.select_context_menu_item('Tags')
        sort_button_text = util_obj.validate_and_get_webdriver_object(".content-title-btn-name", 'sort_button').text.strip()
        util_obj.asequal('Tags', sort_button_text, 'Step 09.02: Verify Tags are used for sort')
        main_page_obj.verify_favorites_tags(['Brand', 'Business Region', 'Comparison', 'Cost', 'Customer', 'Model', 'Product', 'Profit', 'Revenue', 'Sales Metrics', 'Store'], 09.03)
        
        """
        Step 10: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        util_obj.wait_for_page_loads(10)
        
        """
        Step 11: Click Choose Columns button ->Click Tags in drop down list to deselect
        """
        main_page_obj.select_list_view_columns(['Tags'])
        
        """
        Step 12: Click on the content area to close the drop down list
        """
        content_area = util_obj.validate_and_get_webdriver_object(".files-box .files-listing", 'file-listing')
        core_util_obj.left_click(content_area, element_location='bottom_right')
        
        """
        Step 13: Click toggle button to switch to Grid view ->Click Refresh button
        Verify Tag is now the sort
        """
        main_page_obj.select_grid_view()
        util_obj.wait_for_page_loads(10)
        refresh_button = util_obj.validate_and_get_webdriver_object(".toolbar-button-div .btn-refresh", 'refresh buttom')
        core_util_obj.python_left_click(refresh_button)
        util_obj.wait_for_page_loads(10)
        sort_button_text = util_obj.validate_and_get_webdriver_object(".content-title-btn-name", 'sort_button').text.strip()
        util_obj.asequal('Tags', sort_button_text, 'Step 13.01: Verify Tags are used for sort')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        