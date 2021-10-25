'''
Created on July 13, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491033&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6467920
TestCase Name = Verify what Side Bar options show / are functional for Advanced Users
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C6467920_TestClass(BaseTestCase):

    def test_C6467920(self):
        
        """
        TESTCASE VARIABLES
        """
        
        long_wait = 90
        medium_wait = 45
        short_wait = 30
        list_view_css = "[class*='fa fa-list']"
        grid_view_css = "[class*='fa fa-th']"
        left_panel_css = "div.left-main-panel-button-size"
        crumb_box_css = ".crumb-box .ibx-label-text"
        item_css =".content-box.ibx-widget .files-box .file-item .ibx-label-text"
        list_item_css = ".files-listing .files-box-files-area .grid-cell-data .ibx-label-text"
        content_list=['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        expected_label_content_files_list = ['Items']
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_label_favorites_files_list = ['Items', 'Default sort', 'arrow_upward']
        expected_choose_columns_content_menu = ['Title', 'Name', 'Summary', 'Tags', 'Last modified', 'Created on', 'Size', 'Owner']
        expected_list_view_titles = ['Title', 'Summary', 'Last modified', 'Size']
        expected_portals_list_view_titles = ['arrow_upward\nTitle', 'Summary', 'Last modified']
        expected_favorites_list_view_titles = ['Title', 'Summary', 'Last modified', 'Size']
        expected_portals = ['V4 Portal']
        expected_favorites_default_msg = ['Your Favorites will appear here']
        expected_favorites = ['Quantity Sold By Stores']

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        def verify_title_labels(label_type,expected_list, msg):
            content_title_elem = self.driver.find_element_by_css_selector(".sd-content-title-label-{0}".format(label_type))
            actual_title_list = content_title_elem.text.split('\n')
            utillobj.as_List_equal(expected_list, actual_title_list, msg)
        def verify_list(expected, css, comparision, msg):
            list_title_elems =self.driver.find_elements_by_css_selector(css)
            actual_list_title = [el.text for el in list_title_elems if el.text!='']
            if comparision=='asin':
                for i in expected:
                    utillobj.asin(i, actual_list_title, msg+" displays "+i)
            elif comparision=='asnotin':
                for i in expected:
                    utillobj.as_notin(i, actual_list_title, msg+" doesn't display "+i)
            else:
                utillobj.as_List_equal(expected, actual_list_title, msg)
        
        """ Step 1: Sign into WebFOCUS Home Page as Advanced User.
                    Verify sidebar listed with the following options :
                    1.Content View (By default selected).
                    2.Portals View.
                    3.Favorites View. 
                    4.Ask WebFOCUS.
        """
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        folders_css="[data-ibxp-text*='Folders']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 1: Verify Side bar(left panel) options")
        utillobj.verify_picture_using_sikuli("content.png", "Step 1.1: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("portal.png", "Step 1.2: Verify portals image displayed")
        utillobj.verify_picture_using_sikuli("favourites.png", "Step 1.3: Verify favorites image is displayed")
        utillobj.verify_picture_using_sikuli("ask_webfocus.png", "Step 1.4: Verify Ask WebFOCUS image is displayed")
            
        """ Step 2: Select Retail Samples under Domains.
                    Verify by default content area shows in grid view.
        """
        wfmain_obj.click_repository_folder('Retail Samples')
        wfmain_obj.verify_folder_item_grid_view("My Content", "Charts", "Step 2: Verify content area shows in grid view")
        utillobj.verify_picture_using_sikuli("list_view.png", "Step 2.1: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step 2.2: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step 2.3: Verify content title label folders",  label_type='folders')
        default_sort_status = self.driver.find_element_by_css_selector(".sd-content-title-label-files .content-title-btn-name").is_displayed()
        utillobj.asequal(False, default_sort_status, "Step 2.4: Verify label files (Items) - Default Sort is not displayed")
            
        """ Step 3: Click on toggle list view button.
                    Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        wfmain_obj.verify_list_view("My Content", "Charts", "Step03.1a: Verify content area shows in list view")
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step03.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step03.1c: Verify grid view image object is displaying when list view is selected")
        title_css =".files-listing .files-box-files-title .ibx-label-text"
        verify_list(expected_list_view_titles, title_css, 'asListEqual', "Step03.1d: Verify list view titles")
           
        """ Step 4: Click sorting tool option.
                    Verify drop down menu to choose sorting options for the items in the list view:
                    1.Title.
                    2.Name.
                    3.Summary.
                    4.Tags.
                    5.Last modified.
                    6.Created on.
                    7.Size.
                    8.Owner.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step04: Verify drop down menu items in the list view")
           
        """ Step 5: Click on toggle grid view button.
                    Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        wfmain_obj.verify_folder_item_grid_view("My Content", "Charts", "Step05.1a: Verify content area shows in grid view")
        utillobj.verify_picture_using_sikuli("list_view.png", "Step05.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step05.1c: Verify  list view image object is displaying")
        verify_title_labels('folders', expected_label_content_folders_list, "Step05.2.1: Verify content title label folders")
        verify_title_labels('files', expected_label_content_files_list, "Step05.2.2a: Verify content title label files")
        default_sort_status = self.driver.find_element_by_css_selector(".sd-content-title-label-files .content-title-btn-name").is_displayed()
        utillobj.asequal(False, default_sort_status, "Step05.2.1b: Verify label files - Default Sort is not displayed")
           
        """ Step 6: Click Portals from the sidebar.
                    Verify content area displayed in grid view and listed available portals such as V3, V4, and future V5 (V4 Portal list for automation environment).
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", 45)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step06.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step06.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_portals_files_list, "Step06.2a: Verify content title label files")
        verify_list(expected_portals, item_css, 'asin', "Step06.2b: Verify V4 Portal list for automation environment")
        v4_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl_basic.svg']").is_displayed()
        utillobj.asequal(True, v4_img_status, "Step06.3b: Verify v4 portal image object is displayed")
 
        """ Step 7: Click on toggle list view button.
                    Verify content area displayed in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step07.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step07.1c: Verify grid view image object is displaying when list view is selected")
        title_css =".files-listing .files-box-files-title .grid-cell-title"
        verify_list(expected_portals_list_view_titles, title_css, 'asListEqual', "Step07.1d: Verify list view titles")
           
        """ Step 8: Click on toggle grid view button.
                    Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.verify_picture_using_sikuli("list_view.png", "Step08.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step08.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_portals_files_list, "Step08.2a: Verify content title label files")
        verify_list(expected_portals, item_css, 'asin', "Step08.2b: Verify V3, V4, V5 portals")
        v3_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl.svg']").is_displayed()
        utillobj.asequal(True, v3_img_status, "Step08.3a: Verify v3 portal image object is displayed")
        v4_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl_basic.svg']").is_displayed()
        utillobj.asequal(True, v4_img_status, "Step08.3b: Verify v4 portal image object is displayed")
           
        """ Step 9: Click Favorites from the sidebar.
                    Verify if no content is added to favorites view then below context will appear.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", 45)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step09.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step09.1c: Verify  list view image object is displaying")
        files_box_css =".content-box.ibx-widget .files-box .ibx-label-text"
        verify_list(expected_favorites_default_msg, files_box_css, 'asListEqual', "Step09.2b: Verify no content is added to favorites view")
           
        """ Step 10: Click Content from sidebar > Retail Samples > Reports > Right click on "Quantity Sold By Stores" > Add to Favorites.
                     Verify Favorite added popup opens with a background transparent green layer over the popup.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.right_click_folder_item_and_select_menu("Quantity Sold By Stores", 'Add to Favorites', 'Retail Samples->Reports')
        wfmain_obj.verify_favorites_notify_popup("Step 10: Favorites added")
           
        """ Step 11: Click Favorites from sidebar.
                     Verify content area displayed with added report in grid view.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step11.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step11.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_favorites_files_list, "Step11.2a: Verify favorites title label")
        verify_list(expected_favorites, item_css, 'asListEqual', "Step11.2b: Verify Quantity Sold By Stores report in grid view")
           
        """ Step 12: Click on toggle list view button.
                     Verify content area displayed in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step12.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step12.1c: Verify grid view image object is displaying when list view is selected")
        title_css =".files-listing .files-box-files-title .grid-cell-title"
        verify_list(expected_favorites_list_view_titles, title_css, 'asListEqual', "Step12.1d: Verify list view titles")
        verify_list(expected_favorites, list_item_css, 'asListEqual', "Step12.1e: Verify Quantity Sold By Stores report in list view")
           
        """ Step 13: Click on toggle grid view button.
                     Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step13.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step13.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_favorites_files_list, "Step13.2a: Verify favorites title label")
        verify_list(expected_favorites, item_css, 'asListEqual', "Step13.2b: Verify Quantity Sold By Stores report in grid view")
           
        """ Step 14: Right Click on "Quantity Sold By Stores" > Click Remove favorite.
                     Verify favorite is removed and below context will appear.
        """
        utillobj.synchronize_with_visble_text(files_box_css, "Items", short_wait)
        wfmain_obj.right_click_folder_item_and_select_menu("Quantity Sold By Stores", 'Remove from Favorites')
        utillobj.synchronize_with_visble_text(".files-box-files .ibx-label-text", "Your Favorites will appear here", medium_wait)
        verify_list(expected_favorites, item_css, 'asnotin', "Step14.1: Verify Quantity Sold By Stores report not in grid view")
           
        """ Step 15: Click Ask WebFOCUS from the sidebar.
                     Verify that the Search box is displays with the three options are as follows:
                     1.Search 
                     2.Search options (drop down)
                     Also verify that 'Last Viewed Questions' with Clear (disable) button is shown.
        """
        wfmain_obj.select_ask_webfocus_from_sidebar()
        utillobj.synchronize_with_number_of_element(".ask-title-label", 1, short_wait)
        wfmain_obj.ask_webfocus_search_bar_options('text_box', True, "Step015: Verify text box")
        wfmain_obj.ask_webfocus_search_bar_options('dropdown', True, "Step015.1: Verify Search options (drop down)")
        wfmain_obj.ask_webfocus_content_area('title', 'Last Viewed Questions', 'Step15.2: Verify title')
        wfmain_obj.ask_webfocus_content_area('title_button_state', True, 'Step15.3: Verify Clear (disable) button is shown')
        wfmain_obj.ask_webfocus_content_area('title_button_text', 'Clear', 'Step15.4: Verify title button name is Clear')
          
        """ Step 16: Click on the Collapse side bar icon.
                     Verify that the sidebar is collapsed and following should be displayed:
                     1.Four sidebar menu icons.
                     2.Information Builders text logo will convert into the simplified square Information Builders logo.
        """
        wfmain_obj.collapse_side_bar()
        wfmain_obj.verify_left_panel([], "Step16.1: Verify Side bar(left panel) options doesn't show any text",'')
        utillobj.verify_picture_using_sikuli("collapse_content.png", "Step16.2a: Verify Collapse content image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_portal.png", "Step16.2b: Verify Collapse portals image displayed")
        utillobj.verify_picture_using_sikuli("collapse_favourites.png", "Step16.2c: Verify Collapse favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_ask_webfocus_highlighted.png", "Step16.2d: Verify Collapse ask WebFOCUS image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_logo.png", "Step16.2e: Verify Collapse logo image is displayed")
         
        """ Step 17: In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.
                     Verify that the state of the sidebar should be remembered when the user signs out of the Home Page and signs back in.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        wfmain_obj.verify_left_panel([], "Step17.1: Verify Side bar(left panel) options",'')
        utillobj.verify_picture_using_sikuli("collapse_content.png", "Step17.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_portal.png", "Step17.2b: Verify portals image displayed")
        utillobj.verify_picture_using_sikuli("collapse_favourites.png", "Step17.2c: Verify favorites image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_ask_webfocus_highlighted.png", "Step17.2d: Verify Collapse ask WebFOCUS image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_logo.png", "Step17.2e: Verify collapse logo image is displayed")
        
        """ Step 18: Revert back the Home Page by its default state.
        """
        wfmain_obj.expand_side_bar()
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.verify_left_panel(content_list, "Step18.1: Verify Side bar(left panel) options")
        
        """ Step 19: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        