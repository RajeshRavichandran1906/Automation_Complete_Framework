'''
Created on November 12, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5852975
TestCase Name = Wildcard test
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility

class C5852975_TestClass(BaseTestCase):

    def test_C5852975(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        folder_search_css = ".advanced-folder-search"
        content_area_css = '#files-box-area'
        search_maps_css = ".div-search .txt-search input[placeholder=\"Search Maps\"]"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev1', 'mrpassdev1')
        
        """
        Step 2: Navigate to Retail Samples / InfoApps / Maps in tree.
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains->Retail Samples->InfoApps->Maps')
        
        """
        Step 3: Click on the Advanced search drop down.
        Verify the default advanced search drop down:
        """
        util_obj.synchronize_with_number_of_element(search_maps_css, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_search_input_box_option_dropdown()
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Title', step_number='3.1')
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Any', step_number='3.2')
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(verify_selected='Contains', step_number='3.3')
        
        """
        Step 4: Click on the Search drop down and Select "Name".
        Verify Name is selected in the Search drop down:
        """
        main_page_obj.search_dropdown_in_advanced_folder_search(select_options=["Name"])
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Name', step_number='4.1')
        
        """
        Step 5: Click anywhere outside to close the advanced search drop down.
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_util_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        util_obj.synchronize_until_element_disappear(folder_search_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Type *.htm in the Search text box.
        Verify it displays US Sales Map:
        """
        main_page_obj.search_input_box_options('write', '*.htm')
        main_page_obj.verify_items_in_grid_view(['US Sales Map'], 'asin', 'Step 6.1: Verify the Map present')
        
        """
        Step 7: Click Sign Out and Close the browser.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        