'''
Created on April 9, 2019

@author: Niranjan\Samuel

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261579
TestCase Name = Searching on Tags should be case insensitive
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility
import time

class C8261579_TestClass(BaseTestCase):

    def test_C8261579(self):
        
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utility_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        fex_name = 'Arc - Sales by Region'
        repository_folder = 'Domains->Retail Samples->Charts'
        
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content tree from side bar
        """  
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on "Retail samples" domain ->Click on Charts folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Right click on Arc-Sales by Region -> Select Properties
        """
        main_page_obj.right_click_folder_item_and_select_menu(fex_name,'Properties')
        time.sleep(15)
        
        """
        Step 5: Click Advanced tab
        """
        main_page_obj.select_property_tab_value('Advanced')
        
        """
        Step 6: Type Sales in Tags text box and click Save
        """
        main_page_obj.edit_property_dialog_value('Tags', 'text_value','Sales', tab_name='Advanced')
        time.sleep(4)
        main_page_obj.select_property_dialog_save_cancel_button('Save')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: Click Cancel to close the properties window
        """
        main_page_obj.select_property_dialog_save_cancel_button('Cancel')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: Click the drop down arrow in search box and select Tag from the list
        """
        main_page_obj.click_search_input_box_option_dropdown()
        main_page_obj.search_dropdown_in_advanced_folder_search(select_options=['Tag'], step_number='Step 8')
        
        """
        Step 9: Click on content area to close the advanced search box
        """
        content_area = util_obj.validate_and_get_webdriver_object(locator_obj.content_area_css, 'content_area')
        core_utility_obj.python_left_click(content_area, 'middle_right')
        util_obj.wait_for_page_loads(5, pause_time=5)
        
        """
        Step 10: In the search box type "sales" with lower case "s".
        Verify "Arc-Sales by Region" display
        """
        main_page_obj.search_input_box_options('write', 'sales')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([fex_name], 'asin', 'Step 10.1: Verify "Arc-Sales by Region" display')
        
        """
        Step 11: In the search box type "Sales" with upper case "S".
        Verify "Arc-Sales by Region" display
        """
        util_obj.wait_for_page_loads(5, pause_time=5)
        main_page_obj.search_input_box_options('write', 'Sales')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([fex_name], 'asin', 'Step 11.1: Verify "Arc-Sales by Region" display')
        
        """
        Step 12: If it is chrome, IE 11 and Edge browsers, hover over the mouse to the search box and click X to clear the search box
        Step 13: If it is FF browser, use the backspace to clear the search box
        Verify Sales is cleared in search box
        """
        main_page_obj.search_input_box_options('clear')
        main_page_obj.search_input_box_options(verify_value='', msg='Verify Sales is cleared in search box')
   
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()