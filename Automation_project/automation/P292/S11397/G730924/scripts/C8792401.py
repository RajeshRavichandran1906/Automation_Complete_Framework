'''
Created on March 25, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8792401
Test case Name =  Search for portal - upper case
'''
import unittest
from common.lib.utillity import UtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8792401_TestClass(BaseTestCase):
    def test_C8792401(self):
        """ Testcase objects"""
        login_obj = Login(self.driver)
        util_obj = UtillityMethods(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        locator_obj = WfMainPageLocators()
        
        """Testcase CSS"""
        items_css = "div[data-ibxp-text=\"Items \"] .ibx-label-text"
        
        """
        Step 1: Sign in to WebFOCUS as Developer User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Portal View from the sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.PORTAL_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_portals_from_sidebar()
    
        """
        Step 3: Click on the search text box and type 's' in the Search box           
        Verify Retail Samples (twice) appears with the tags P292_S10660, Public and 'Retail Samples'
        """
        util_obj.synchronize_with_number_of_element(items_css, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.search_input_box_options(input_text_msg='S')
        main_page_obj.verify_items_in_grid_view(['Retail Samples', 'Retail Samples'], 'asin', "Step 3.1: retail samples appears twice")
        main_page_obj.verify_favorites_tags(['P292_S10660', 'Public', 'Retail Samples'], '3.2', 'asin')
        
        """
        Step 4: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box and click x to clear the search box.
        Verify search box is cleared and "Search Portals" appears in the box
        Step 5: Or else for FF browser, use the backspace to clear the search box.
        Verify search box is cleared and "Search Portals" appears in the box
        """
        main_page_obj.search_input_box_options(option_type='clear')
        main_page_obj.verify_search_textbox_value("Search Portals", "Step 4/5: Verify search portal appears in textbox")
        
        """
        Step 6: In the banner link, click on the top right username > Sign out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()