'''
Created on November 08, 2018

@author: varun

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=435324&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914659
TestCase Name = Verify clicking on dropdown arrow in Search box brings up Search menu
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
import time

class C5914659_TestClass(BaseTestCase):

    def test_C5914659(self):
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
        Step 1: Sign into WebFOCUS Home Page as Administrator
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        time.sleep(5)
        
        
        """
        Step 3: Click on 'Search options' arrow in the drop-down Search box
        
        Verify 'Search options' drop-down box appears with the following options:
        Search with the 'Title' dropdown control
        Type with the 'Any' dropdown control
        Matching Behavior with the 'Contains' dropdown control
        Reset button at the bottom right corner of the 'Search drop-down box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.synchronize_with_number_of_element(folder_search_css, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.search_dropdown_in_advanced_folder_search( verify_selected='Title', step_number='3.1')
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Any', step_number='3.2')
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(verify_selected='Contains', step_number='3.3')
        main_page_obj.button_in_advanced_folder_search('Reset', location=True, msg='Step 3.4: Verify Reset button present')
        
        """
        Step 4: Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_util_obj.python_left_click(content_area, element_location='middle_right', xoffset=-60)
        util_obj.synchronize_until_element_disappear(folder_search_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close', 'Step 4.1: Verify Search option drop down closed')
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        