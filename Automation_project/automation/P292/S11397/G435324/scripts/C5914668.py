'''
Created on November 12, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914668
TestCase Name = Select Type search option and perform search
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C5914668_TestClass(BaseTestCase):

    def test_C5914668(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        folder_search_css = ".advanced-folder-search"
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
        Step 6: Click on Search with the 'Type' drop-down control > Select 'Document'
        Step 7: Click on empty space in the 'Search Options' box
        """
        main_page_obj.type_dropdown_in_advanced_folder_search(select_options=['Document'])
        
        """
        Step 8: Click on 'Search Domains' box > Enter 'Upload'
        Verify that 'Upload_Document' appears.
        """
        main_page_obj.search_input_box_options('write', 'Upload')
        main_page_obj.verify_items_in_grid_view(['Upload_Document'], 'asin', 'Step 8: Verify folder is present')
        
        """
        Step 9: Click on 'Search options' arrow in the drop-down Search box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.synchronize_with_number_of_element(folder_search_css, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Click on Search with the 'Type' drop-down control > Select 'Any' to revert as by its default state
        Step 11: Click on empty space in the 'Search Options' box
        """
        main_page_obj.type_dropdown_in_advanced_folder_search(select_options=['Any'])
        
        """
        Step 12: Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_util_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close', 'Step 12.1: Verify Search option drop down closed')
        
        """
        Step 13: Click on 'Search Domains' box and Click X to clear the Search
        """
        main_page_obj.search_input_box_options('clear')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()