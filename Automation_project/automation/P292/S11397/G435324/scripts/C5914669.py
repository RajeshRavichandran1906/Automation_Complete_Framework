'''
Created on November 12, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914669
TestCase Name = Select 'Matching behavior' search option and perform search
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C5914669_TestClass(BaseTestCase):

    def test_C5914669(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        display_css = ".files-box-files .ibx-label-text"
        display_text = "There are no results to display"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev1', 'mrpassdev1')
        
        """
        Step 2: Click Retail Samples domain in tree Open Charts folder
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        main_page_obj.expand_repository_folder('Retail Samples')
        
        """
        Step 3: Click settings down arrow in Search box.
        """
        main_page_obj.click_search_input_box_option_dropdown()
        
        """
        Step 4: Click 'Matching behavior' box
        Step 5: Click 'Starts with'
        """
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(select_options=['Starts with'])
        
        """
        Step 6: Type: average
        Verify no results are returned
        """
        main_page_obj.search_input_box_options('write', 'average')
        parse_text = util_obj.validate_and_get_webdriver_object(display_css, 'display_text').text.strip()
        util_obj.asequal(parse_text,display_text,"Step 6.1: Verify no result display")
        
        """
        Step 7: Click settings down arrow in Search box.
        """
        main_page_obj.click_search_input_box_option_dropdown()
        
        """
        Step 8: Click 'Matching behavior' box
        Step 9: Click 'Contains'
        """
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(select_options=['Contains'])
        
        """
        Step 10: Type: average
        Verify 2 items appear:
        IBI RETAIL_SAMPLES Heatmap_Average Margin Product By Country Month
        Treemap - Revenue and Average Margin for Models
        """
        main_page_obj.search_input_box_options('write', 'average')
        main_page_obj.verify_items_in_grid_view(['Heatmap - Average Margin Product By Country (Animation)'], 'asin', 'Step 10.1: Verify heatmap folder is present')
        main_page_obj.verify_items_in_grid_view(['Treemap - Revenue and Average Margin for Models'], 'asin', 'Step 10.2: Verify tree map folder is present')
        
        """
        Step 11: Click Search box and click X to clear Search
        """
        main_page_obj.search_input_box_options('clear')
        
        """
        Step 12: Sign out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()