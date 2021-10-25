'''
Created on November 08, 2018

@author: vpriya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=435324&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914664
TestCase Name = Content View - Verify Reset button resets each drop down box to default value
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5914664_TestClass(BaseTestCase):

    def test_C5914664(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        main_page_locators =WfMainPageLocators()
        
        Report_list=['Report - Store Product Metrics','Store Sales Report']
        folder_name_path="Retail Samples"
        item_css="div[class*='sd-content-title-label-files ibx-widget ']"
        content_area_css = '#files-box-area'
        
        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev1', 'mrpassdev1')
        
        
        """
        Step 2:Click Content View from the sidebar > Click on Domains from the resource tree.
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
      
        """
        Step 3:Click on Retail Samples Domain > Click on 'Search Retail Sam...' box and enter 'Report'.
        Verify that reports contain with the name 'Report' listed in the content area
        """
        
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.search_input_box_options(option_type ='write',input_text_msg='Report')
        util_obj.synchronize_with_visble_text(main_page_locators.content_area_css, Report_list[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(Report_list,'asin','Step 3:verify the contains with name report')
        
        """
        Step 4:Click on Search with the 'Title' drop-down control > Select Name
        Verify that Search with the 'Name' drop-down control appears
        """
        main_page_obj.click_search_input_box_option_dropdown()
        main_page_obj.search_dropdown_in_advanced_folder_search(select_options=['Name'])
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Name',step_number='4')
        
        """
        Step 5:Click on Type with the 'Any' drop-down control > Select Procedure
        Step 6:Click on empty space in the 'Search Options' box to close the 'type' drop-down lists
        Verify that Type with the 'Procedure' drop-down control
        """
        
        #main_page_obj.click_search_input_box_option_dropdown()
        main_page_obj.type_dropdown_in_advanced_folder_search(select_options=['Procedure'])
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Procedure',step_number='6')
        
        """
        Step 7:Click on Matching Behavior with the 'Contains' drop-down control > Starts with
        """
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(select_options=['Starts with'])
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(verify_selected='Starts with',step_number='7')
        
        """
        Step 8:Click Reset button
        Verify Report is cleared from the 'Search Domain' box.
        Verify that Original default values appear as follows:
        1.Search with the 'Title' dropdown control
        2.Type with the 'Any' dropdown control
        3.Matching Behavior with the 'Contains' dropdown control
        """
        main_page_obj.button_in_advanced_folder_search(button_name="Reset", select=True)
        util_obj.synchronize_with_number_of_element(item_css, '1', main_page_obj.home_page_medium_timesleep)
        main_page_obj.search_input_box_options(verify_value='',msg='step8.1')
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Title',step_number='8.2')
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Any',step_number='8.3')
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search(verify_selected='Contains',step_number='8.4')
        
        """
        Step 9:Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_utility_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close','Step9 verify the advanced folder dropdown gets closed')
        
        """
        Step 10:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()        