'''
Created on November 12, 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=435324&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/7170699
TestCase Name = Favorites View - Verify Type drop down options
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility


class C7170699_TestClass(BaseTestCase):

    def test_C7170699(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        matching_list=['Any','Procedure', 'Page', 'Collaborative Portal', 'Data Source', 'HTML File','URL','Library Report']
        content_area_css = '#files-box-area'

        """
        Step 1: Login WF new home page as domain developer.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2:Click Favorites View from the sidebar.
        """
        main_page_obj.select_favorites_from_sidebar()
      
        """
        Step 3:Click on 'Search options' arrow in the drop-down Search box.
        """
        main_page_obj.click_search_input_box_option_dropdown()
        
        """
        Step 4:lick on Type with the 'Any' dropdown control
        Verify Title options as follows:
        1.Any (By default selected)
        2.Procedure
        3.Page
        4.Collaborative Portal
        5.Data Source
        6.HTML File
        7.URL
        8.Library Report
        
        """
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Any', verify_list_options=matching_list,label_text='Type',comparision_type='asequal',step_number='4')
        
        """
        Step 5:Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_utility_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close','Step5 verify the advanced folder dropdown gets closed')
        
        """
        Step 6:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()        