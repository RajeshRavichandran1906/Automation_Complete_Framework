'''
Created on November 21, 2018

@author: varun
Testcase Name : Search for portal - lower case
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325156
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity

class C2325156_TestClass(BaseTestCase):
    
    def test_C2325156(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_css = "div[title='Portals'] .ibx-label-text"
        portal_items = ['Retail Samples','Retail Samples']
        expected_placeholder_text = "Search Portals"
        content_box_css = ".content-box"
        
        """ 
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on the Portal View from the sidebar.
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(portal_css, 'Portals', main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click on the search text box and type 's' in the Search box
        Verify Retail Samples (twice) appears with the tags P292_S10660 and 'Retail Samples'
        """
        main_page_obj.search_input_box_options(input_text_msg='s')
        util_obj.synchronize_with_visble_text(content_box_css, portal_items[0], main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(portal_items, 'asequal', 'Step 3.1: Verify 2 Retail Samples are present')
        main_page_obj.verify_favorites_tags(['P292_S10660','Retail Samples'], '3.2')
        
        """
        Step 4: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box 
        and click x to clear the search box.
        Step 5: Or else for FF browser, use the backspace to clear the search box.
        Verify search box is cleared and "Search Portals" appears in the box
        """
        main_page_obj.search_input_box_options(option_type ='clear')
        main_page_obj.verify_search_textbox_value(expected_placeholder_text, "Step 4.1: Verify Placeholder in searchbox")
        
        """
        Step 6: In the banner link, click on the top right username > Sign out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()