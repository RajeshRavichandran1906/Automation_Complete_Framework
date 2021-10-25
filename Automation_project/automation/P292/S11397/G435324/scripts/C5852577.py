'''
Created on November 12, 2018

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5852577
TestCase Name = Portals search
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
import time

class C5852577_TestClass(BaseTestCase):

    def test_C5852577(self):
        """
        TESTCASE VARIABLES
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        folder_search_css = ".advanced-folder-search"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Portals in sidebar
        """
        main_page_obj.select_portals_from_sidebar()
        time.sleep(5)
        
        """
        Step 3: Click settings down arrow in Search box.
        """
        main_page_obj.click_search_input_box_option_dropdown()
        util_obj.synchronize_with_number_of_element(folder_search_css, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click Type box and select Collaborative Portal
        """
        main_page_obj.type_dropdown_in_advanced_folder_search(select_options=['Collaborative Portal'])
        
        """
        Step 5: Type 'Retail' in Search box
        Verify only the Collaborative portal 'Retail Samples' appears:
        """
        main_page_obj.search_input_box_options('write', 'Retail')
        main_page_obj.verify_items_in_grid_view(['Retail Samples'], 'asin', 'Step 5.1: Verify the portal present')
        main_page_obj.verify_folder_icon_in_content_area('Retail Samples', 'portal', '5.2')
        
        """
        Step 6: Click Search box and click X to clear Search
        """
        main_page_obj.search_input_box_options('clear')
        
        """
        Step 7: Sign out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    