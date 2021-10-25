'''
Created on November 08, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5914661
TestCase Name = Content View - Verify Search drop down options
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility

class C5914661_TestClass(BaseTestCase):

    def test_C5914661(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        title_list = ['Title','Name','Summary','Tag']
        folder_search_css = ".advanced-folder-search"
        content_area_css = '#files-box-area'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        
        """
        Step 3: Click on 'Search options' arrow in the drop-down Search box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        
        """
        Step 4: Click on Search with the 'Title' dropdown control
        Verify Search options are:

        1.Title (By default checked)
        2.Name
        3.Summary and 
        4.Tag.
        """
        main_page_obj.search_dropdown_in_advanced_folder_search( verify_selected='Title',step_number='4.1')
        main_page_obj.search_dropdown_in_advanced_folder_search( verify_list_options=title_list,comparision_type='asequal', step_number='4.2')
        main_page_obj.search_dropdown_in_advanced_folder_search(drop_down_selected_list=['Title'],comparision_type='asequal', step_number='4.3')

        """
        Step 5: Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_util_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        util_obj.synchronize_until_element_disappear(folder_search_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close', 'Step 5.1: Verify Search option drop down closed')
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        