'''
Created on November 09, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5914667
TestCase Name = Content View - Select Summary search option and perform search
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.pages import wf_mainpage as pages

class C5914667_TestClass(BaseTestCase):

    def test_C5914667(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        pages_obj = pages.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        folder_search_css = ".advanced-folder-search"
        matrix_css = ".file-item-text-box:not([style*='none'])"
        matrix_text ='matrix'
        content_area_css = '#files-box-area'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev1', 'mrpassdev1')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        
        """
        Step 3: If Domain is not expanded then expand domain
        Step 4: Click on 'Retail Samples' domain from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        
        """
        Step 5: Click on 'Search options' arrow in the drop-down Search box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        
        """
        Step 6: Click on Search with the 'Title' drop-down control > Select 'Summary'
        """
        main_page_obj.search_dropdown_in_advanced_folder_search(select_options=['Summary'])
        
        """
        Step 7: Click on 'Search Domains' box > Enter 'matrix'
        Verify that 'Quantity Sold By Stores' report contains with a summary as 'matrix' appears.
        """
        main_page_obj.search_input_box_options('write', 'matrix')
        
        """
        Step 8: Hover over 'Quantity Sold By Stores' report
        """
        report_element = pages_obj.get_domain_folder_item('Quantity Sold By Stores')
        core_util_obj.python_move_to_element(report_element)
        core_util_obj.move_to_element(report_element)
        element_display = util_obj.validate_and_get_webdriver_object(matrix_css,'matrix_element').text.strip()
        util_obj.asequal(element_display,matrix_text,'Step 8: Verify Matrix display on folder')
        
        """
        Step 9: Click on 'Search options' arrow in the drop-down Search box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.synchronize_with_number_of_element(folder_search_css, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Click on Search with the 'Search' drop-down control > Select 'Title' to revert as by its default state
        """
        main_page_obj.search_dropdown_in_advanced_folder_search(select_options=['Title'])
        
        """
        Step 11: Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        Verify that 'Quantity Sold By Stores' report is removed and 'There are no results to display' in the content area
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_util_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        util_obj.synchronize_until_element_disappear(folder_search_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close', 'Step 5.1: Verify Search option drop down closed')
        main_page_obj.verify_folders_in_grid_view(['Quantity Sold By Stores'], 'asnotin', 'Step 11.2: Verify folder not present')
    
        """
        Step 12: Click on 'Search Domains' box and Click X to clear the Search
        """
        main_page_obj.search_input_box_options('clear')

        """
        Step 13: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
        