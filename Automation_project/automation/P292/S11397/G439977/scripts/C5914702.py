'''
Created on April 11, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5914702
TestCase Name = Verify adding Tags as column in List View also adds Tags as sort option in Grid View
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages import wf_mainpage as pages_main
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5914702_TestClass(BaseTestCase):

    def test_C5914702(self):
        """
        TESTCASE VARIABLES
        """
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator = WfMainPageLocators()
        
        """ 
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page_obj.home_page_long_timesleep)
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click on "Retail Samples" domain in resource tree.
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(locator.content_area_css, 'Items', main_page_obj.home_page_long_timesleep)
        
        """
        Step 4: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        util_obj.synchronize_until_element_is_visible("div.files-box-files-title", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click Choose Columns button
        Step 6: Click Tags in drop down list
        """
        main_page_obj.select_list_view_columns(['Tags'])
        util_obj.synchronize_with_visble_text(".files-box-files-title", "Tags", main_page_obj.home_page_long_timesleep)
        
        """
        Step 7: Click toggle button to switch to Grid view
        """
        main_page_obj.select_grid_view()
        util_obj.synchronize_until_element_disappear("div.files-box-files-title", main_page_obj.home_page_short_timesleep)
        
        """
        Step 8: Click on Default Sort
        Verify Tags appears in drop down list:
        """
        title_button = util_obj.validate_and_get_webdriver_object(".content-title-btn-name", 'tag-name')
        core_util_obj.left_click(title_button)
        util_obj.synchronize_with_visble_text("div.ibx-menu-no-icons[aria-hidden='false']", "Title", main_page_obj.home_page_medium_timesleep)
        main_pages_obj.verify_context_menu_item(['Tags'], 'Step 8.1: Verify Tags in drop down list', comparision_type='asin')
        
        """
        Step 9: Click toggle button to switch to List view
        """
        main_page_obj.select_list_view()
        util_obj.synchronize_until_element_is_visible("div.files-box-files-title", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Click Choose Columns button
        Step 11: Click Tags in drop down list to deselect
        """
        main_page_obj.select_list_view_columns(['Tags'])
        util_obj.synchronize_until_element_disappear("div.files-box-files-title div[data-ibxp-text='Tags']", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 12: Click toggle button to switch to Grid view
        """
        main_page_obj.select_grid_view()
        util_obj.synchronize_with_visble_text(locator.content_area_css, 'Items', main_page_obj.home_page_long_timesleep)
        
        """
        Step 13: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        