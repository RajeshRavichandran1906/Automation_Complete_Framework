'''
Created on November 08, 2018

@author: vpriya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=435324&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5914665
TestCase Name = Portal View - Verify Search menu options
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility

class C5914665_TestClass(BaseTestCase):

    def test_C5914665(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        content_area_css = '#files-box-area'

        """
        Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        
        """
        Step 2:Click Portals View from the sidebar.
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.wait_for_page_loads(10)
        
      
        """
        Step 3:Click on 'Search options' arrow in the drop-down Search box.
        Verify 'Search options' drop-down box appears with the following options:
        Search with the 'Title' dropdown control
        Type with the 'Any' dropdown control
        Matching Behavior with the 'Contains' dropdown control
        Reset button at the bottom right corner of the 'Search drop-down box
        """
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.wait_for_page_loads(20)
        main_page_obj.search_dropdown_in_advanced_folder_search(verify_selected='Title',step_number='3.1')
        main_page_obj.type_dropdown_in_advanced_folder_search(verify_selected='Any',step_number='3.2')
        main_page_obj.matching_behavior_dropdown_in_advanced_folder_search (verify_selected='Contains',step_number='3.3')
        main_page_obj.button_in_advanced_folder_search(button_name='Reset', location=True,msg='Step 3.4 button isin right side')
        
        """
        Step 4:Click on empty space in the content area
        Verify that 'Search options' drop-down box gets closed
        """
        content_area = util_obj.validate_and_get_webdriver_object(content_area_css, 'content_area')
        core_utility_obj.python_left_click(content_area, element_location='middle_right',xoffset=-60)
        main_page_obj.verify_advanced_folder_search_dialog_open_or_close('close','Step4 verify the advanced folder dropdown gets closed')
        
        """
        Step 6:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()        