'''
Created on November 22, 2018

@author: varun
Testcase Name : Search Domains - mixed case
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325146
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325146_TestClass(BaseTestCase):
    
    def test_C2325146(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        content_css = ".content-box"
        domains_css = ".toolbar"
        content_items = ['Brand Pie', 'Pie Chart', 'Pie Matrix - Quantity By Region','Pie Matrix - Quantity By Region']
        expected_placeholder_text = "Search Workspaces"
        
        """ 
        Step 1: Sign in to WebFOCUS as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(content_css, 1, 190)
        
        """ 
        Step 2: Click on the Content tree from the sidebar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Workspaces', 160)
        
        """
        Step 3: Click on Domains from the tree
        Verify "Search Domains" appears in the box
        """
        main_page_obj.expand_repository_folder("Domains")
        main_page_obj.verify_search_textbox_value(expected_placeholder_text, "Step 3.1: Verify Placeholder in searchbox")

        """
        Step 4: Type 'PiE' in the search box
        Verify four reports are displayed containing 'PiE' in the title 
        (Brand Pie, Pie Chart, Pie Matrix - Quantity By Region (twice) ) appears
        """
        main_page_obj.search_input_box_options(input_text_msg='PiE')
        util_obj.synchronize_until_element_is_visible(locator_obj.files_item_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(content_items, 'asin', 'Step 4.1: Verify items present in Content area ')
                
        """
        Step 5: If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box
        Step 6: Click X to clear the search box
        Step 7: Or else for FF browser, use the backspace to clear the search box
        Verify search box is cleared and "Search Domains" appears in the box
        Verify four reports (Brand Pie, Pie Chart, Pie Matrix - Quantity By Region (twice) ) are removed from the content area
        """
        main_page_obj.search_input_box_options(option_type ='clear')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        main_page_obj.verify_search_textbox_value(expected_placeholder_text, "Step 5.1: Verify Placeholder in searchbox")
        main_page_obj.verify_items_in_grid_view(content_items, 'asnotin', 'Step 5.2: Verify items not present in Content area')
        
        """
        Step 8: In the banner link, click on the top right username > Sign out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()