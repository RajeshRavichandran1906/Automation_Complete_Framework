'''
Created on November 22, 2018

@author: varun
Testcase Name : Search for Favorite - upper case
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325159
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325159_TestClass(BaseTestCase):
    
    def test_C2325159(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        favorite_css = "div[title='Favorites'] .ibx-label-text"
        portal_items = ['Sales Metrics YTD']
        expected_placeholder_text = "Search Favorites"
        
        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on the Favorites View from the sidebar.
        """
        main_page_obj.select_favorites_from_sidebar()
        util_obj.synchronize_with_visble_text(favorite_css, 'Favorites', main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click on the Search text box and type 'YTD' in the Search box
        Verify only 'Sales Metrics YTD' report appears
        """
        main_page_obj.search_input_box_options(input_text_msg='YTD')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_items[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(portal_items, 'asin', 'Step 3.1')
        
        """
        Step 4: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box 
        and click x to clear the search box.
        Step 5: Or else for FF browser, use the backspace to clear the search box.
        Verify search box is cleared and "Search Favorites" appears in the box
        """
        main_page_obj.search_input_box_options(option_type ='clear')
        main_page_obj.verify_search_textbox_value(expected_placeholder_text, "Step 4.1: Verify Placeholder in searchbox")
        
        """
        Step 6: In the banner link, click on the top right username > Sign out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()