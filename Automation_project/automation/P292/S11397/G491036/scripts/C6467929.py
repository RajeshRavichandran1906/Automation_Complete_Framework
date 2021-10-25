'''
Created on August 14, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491036&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467929
TestCase Name = Verify Canvas Displays all the portals the Advanced user has access to (V3, V4, and future V5) in thumbnail or list modes
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C6467929_TestClass(BaseTestCase):

    def test_C6467929(self):
        
        """
        TESTCASE VARIABLES
        """
        medium_wait = 45
        crumb_box_css = ".crumb-box .ibx-label-text"
        list_view_image_css = "[class*='fa fa-list']"
        list_view_title_css=".files-box-files-title"
        grid_view_css=".sd-content-title-label-files"
        content_box_css=".explore-box .content-box"
        repository_css = "div[class='ibfs-tree']"
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_portals = ['1TestV3', 'V4 Portal']
        expected_choose_columns_content_menu = ['Size', 'Published', 'Shown']
        expected_search_list=['V4 Portal']
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Advanced User.
        """
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """ Step 2: Click on Content tree from side bar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(repository_css, wfmain_obj.home_page_long_timesleep)
        grid_button=driver.find_element_by_css_selector(".toolbar .toolbar-button-div [class*='fa fa-th']")
        if grid_button.is_displayed()==True:
            wfmain_obj.select_grid_view()
        
#         try:
#             wfmain_obj.select_grid_view()
#         except:
#             pass
        
        """ Step 3: Click Portals from the sidebar.
                    Verify content area displayed in grid view and listed available portals such as V3, V4, and future V5 
                    ("1TestV3" and "V4 Portal" lists for automation environment) and also 'Default Sort' is not displayed in
                     Sort button(top most right corner in the content area)
        """
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", medium_wait)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step 3: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_image_css, True, "Step3.1: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step 3.2: Verify 'Default Sort' is not displayed in Sort button(top right in content area)")
        wfmain_obj.verify_items_in_grid_view(expected_portals, 'asin', "Step 3.3: Verify Retail Samples and V3 portals listed in portal grid view")
        
        """ Step 4: Click on toggle List View button.
                    Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.synchronize_with_number_of_element(list_view_title_css, 1, medium_wait)   
        list_view_content_area_elem=utillobj.validate_and_get_webdriver_object(".files-box-files-area", 'Content area').is_displayed()
        utillobj.asequal(True, list_view_content_area_elem, "Step 4: Verify list_view_content_area_elem object is displayed")   
        
        """ Step 5: Click sorting tool option.
                    Verify 'Size', 'Published' and 'Shown' are not listed in the Sort list.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 5: Verify 'Size', 'Published' and 'Shown' are not listed in the Sort list.", comparision_type='asnotin')

        """ Step 6: Click Search bar and type "V4 Portal" existing portal.
                    Verify searched portal appears in the content area.
        """
        wfmain_obj.search_input_box_options(input_text_msg="V4 Portal")
        wfmain_obj.verify_items_in_list_view(expected_search_list, 'asin', "Step 6: Verify searched V4 portal appears in the content area")

        """ Step 7: For Chrome,IE and Edge browsers: 
                    Click X icon to clear the search box.
                    For Firefox browser:
                    Use the backspace key to clear the search box.
                    Verify all available portals listed in the content area.
        """
        wfmain_obj.search_input_box_options(option_type='clear')
        utillobj.wait_for_page_loads(10)
        utillobj.synchronize_with_visble_text('.content-box', "1TestV3", medium_wait)
        wfmain_obj.verify_items_in_list_view(expected_portals, 'asin', "Step 7: Verify all available portals listed in the content area.")
        
        """ Step 8: Click on toggle Grid View button.
                    Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.synchronize_with_number_of_element(grid_view_css, 1, medium_wait)
        utillobj.verify_object_visible(list_view_image_css, True, "Step 8: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step 8.1: Verify content area back to grid view.") 

        """ Step 9: Right click on "1TestV3" Portal.
                    Verify "1TestV3" Portal context menu with the below option :
                    Run.
                    Remove my customizations.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[0], ['Run', 'Remove my customizations'], msg="Step 9: Verify '1TestV3' Portal context menu with the below options : 'Run', 'Remove my customizations'.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 10: Right click on "V4 Portal".
                    Verify "V4 Portal" context menu with the following options :
                    1. Run.
                    2. Remove my customizations.
                    3. Add to Favorites.
                    4. Properties.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[1], ['Run', 'Remove my customizations', 'Add to Favorites', 'Properties'], msg="Step 10: Verify '1TestV3' Portal context menu with the below options : 'Run', 'Remove my customizations', 'Add to Favorites', 'Properties.")
        
        """ Step 11: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(repository_css, wfmain_obj.home_page_medium_timesleep)
        wfmain_obj.select_option_from_crumb_box('Domains')
        
        """ Step 12: In the banner link, click on the top right username > Click Sign Out.
        """       
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        
