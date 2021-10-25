'''
Created on August 17, 2019

@author: Niranjan Das

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6467927
TestCase Name = Verify Canvas Displays all the portals the Basic user has access to (V3, V4, and future V5) in thumbnail or list modes
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.locators import wf_mainpage_locators

class C6467927_TestClass(BaseTestCase):

    def test_C6467927(self):
        
        """
        TESTCASE VARIABLES
        """

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        coreutils = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locatorsobj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Step 01: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible(locatorsobj.CONTENT_CSS, wfmain_obj.home_page_long_timesleep)
        
        """
        Step 02: Click Portals from the sidebar and Click "P292_S10660" and "Retail Samples" tags at the top of the content area.
        Verify content area displayed in grid view with the portals (P1,Retail Samples, Retail Samples and V4 Portal) available for selected tags (P292_S10660 and Retail Samples) and also 'Default Sort' is not displayed in Sort button(top most right corner in the content area)
        """
        wfmain_obj.select_portals_from_sidebar()       
        utillobj.synchronize_with_visble_text('.sd-category-buttons', 'Retail Samples', wfmain_obj.home_page_medium_timesleep)
        wfmain_obj.check_tags_in_homepage('P292_S10660')
        wfmain_obj.check_tags_in_homepage('Retail Samples')
        expected_portals = ['P1', 'Retail Samples', 'Retail Samples', 'V4 Portal']
        wfmain_obj.verify_items_in_grid_view(expected_portals, 'asin', "Step 02.01: Verify content area displayed in grid view with the portals (P1,Retail Samples, Retail Samples and V4 Portal)")
        expected_label = ['Items', 'Title', 'arrow_upward']
        wfmain_obj.verify_grid_view_title_labels(expected_label, msg='Step 02.02 : Verify Default Sort is not displayed')
        
        """
        Step 03: Click toggle button List View.
        Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        list_view_css=".files-box-files-title"
        utillobj.synchronize_with_number_of_element(list_view_css, 1, wfmain_obj.home_page_medium_timesleep)   
        list_view_content_area_elem= utillobj.validate_and_get_webdriver_object(".files-box-files-area", "List View").is_displayed()
        utillobj.asequal(True, list_view_content_area_elem, "Step 03.01: Verify list view is displayed")   
        
        """
        Step 04: Click sorting tool option.
        Verify 'Size', 'Published' and 'Shown' are not listed in the Sort list.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        expected_choose_columns_content_menu = ['Size']
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 04.01", "asnotin")

        """
        Step 05: Click Search bar and type "V4 Portal" portal.
        Verify "V4 Portal"portal only appears in the content area.
        """
        wfmain_obj.search_input_box_options(input_text_msg = "V4")
        utillobj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        expected_list=['V4 Portal', 'V4 Portal', 'V4_Portal_Context']
        wfmain_obj.verify_items_in_list_view(expected_list, 'asListEqual', "Step 05.01 : Verify V4 Portal appears")

        """
        Step 06: For Chrome,IE and Edge browsers: 
        Click X icon to clear the search box.
        For Firefox browser:
        Use the backspace key to clear the search box.
        
        Verify all available portals listed in the content area.
        """
        expected_list=['Retail Samples', 'V4 Portal', '1TestV3']
        wfmain_obj.search_input_box_options(option_type='clear')
        utillobj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        wfmain_obj.verify_items_in_list_view(expected_list, 'asin', "Step 06.01: Verify all available portals listed in the content area")
        
        """
        Step 07: Click toggle button Grid View to switch back to grid view.
        Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        grid_view_css=".sd-content-title-label-files"
        utillobj.synchronize_with_number_of_element(grid_view_css, 1, wfmain_obj.home_page_medium_timesleep)
        grid_view_content_area_elem= utillobj.validate_and_get_webdriver_object(".sd-content-title-label-files", "Grid View").is_displayed()
        utillobj.asequal(True, grid_view_content_area_elem, "Step 07.01: Verify list view is displayed") 
        
        """
        Step 08: Right click on "1TestV3" Portal.
        Verify "1TestV3" Portal context menu with the following options : 
        1.Run.
        2.Edit.
        3.Customizations.
        -->Remove my customizations 
        -->Remove customizations for all users
        4.Delete.
        5.Publish/Unpublish.
        6.Security.
        -->Rules... 
        -->Rules on this resource... 
        -->Effective policy... 
        -->Owner...
        """
        expected_context_menu = ['Run', 'Edit', 'Customizations', 'Delete DEL', 'Unpublish', 'Security']
        wfmain_obj.verify_repository_folder_item_context_menu('1TestV3', expected_context_menu, msg="Step 08.01")
        panel_elem = utillobj.validate_and_get_webdriver_object(".main-panel .left-main-panel","left panel")
        coreutils.python_left_click(panel_elem)        
        wfmain_obj.verify_repository_folder_item_context_submenu('1TestV3', 'Customizations', ['Remove my customizations', 'Remove customizations for all users'], msg='Step 08.02')
        wfmain_obj.verify_repository_folder_item_context_submenu('1TestV3', 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg='Step 08.03')
        
        """
        Step 09 : Right click on V4 Portals.
        Verify V4 Portal context menu with the following options :
        1.Run.
        2.Edit.
        3.Customizations.
        -->Remove my customizations 
        -->Remove customizations for all users
        4.Manage Alias.
        5.Delete.
        6.Add to Favorites.
        7.Publish/Unpublish.
        8.Show/Hide.
        9.Security.
        -->Rules... 
        -->Rules on this resource... 
        -->Effective policy... 
        -->Owner...
        10.Open item location.
        11.Properties.
        """
        wfmain_obj.verify_repository_folder_item_context_menu('V4 Portal', ['Run', 'Edit', 'Customizations', 'Manage Alias', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Open item location', 'Properties'], msg="Step 09.01",  item_name_index=2)
        panel_elem = utillobj.validate_and_get_webdriver_object(".main-panel .left-main-panel","left panel")
        coreutils.python_left_click(panel_elem)
        wfmain_obj.verify_repository_folder_item_context_submenu('V4 Portal', 'Customizations', ['Remove my customizations', 'Remove customizations for all users'], msg='Step 09.02',  item_name_index=2)
        wfmain_obj.verify_repository_folder_item_context_submenu('V4 Portal', 'Security', ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg='Step 09.03',  item_name_index=2)
        
        """
        Step 10 : Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)  
        """    
        wfmain_obj.select_content_from_sidebar()
        wfmain_obj.select_option_from_crumb_box('Domains')
        utillobj.synchronize_with_number_of_element(locatorsobj.CONTENT_CSS, 1, wfmain_obj.home_page_long_timesleep)
        
        """
        Step 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()        