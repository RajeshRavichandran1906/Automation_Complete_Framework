'''
Created on July 16, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491033&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6467917
TestCase Name = Verify what Side Bar options show / are functional for Admin Users
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException

class C6467917_TestClass(BaseTestCase):

    def test_C6467917(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        medium_wait = 100
        short_wait = 30
        list_view_css = "[class*='fa fa-list']"
        grid_view_css = "[class*='fa fa-th']"
        left_panel_css = "div.left-main-panel-button-size"
        crumb_box_css = ".crumb-box .ibx-label-text"
        left_panel_area_css=".main-panel .left-main-panel"
        toolbar_css=".toolbar-button-div"
        folders_css="[data-ibxp-text*='Folders']"
        favorites_content_area_css =".content-box.ibx-widget .files-box .ibx-label-text"
        portal_tag_content_area_css=".sd-category-buttons .ibx-button"
        files_box_css = ".content-box.ibx-widget .files-box .ibx-label-text"
        content_list=['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        expected_label_content_files_list = ['Items']
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_label_favorites_files_list = ['Items', 'Default sort', 'arrow_upward']
        expected_choose_columns_content_menu = ['Title','Name','Summary', 'Tags','Last modified','Created on','Size','Owner','Published','Shown']
        expected_list_view_titles = ['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        expected_portals_list_view_titles = ['arrow_upward\nTitle', 'Summary', 'Last modified', 'Published', 'Shown']
        expected_favorites_list_view_titles = ['Title', 'Summary', 'Last modified', 'Size']
        expected_portals = ['V3 portal', 'V4 Portal']
        expected_favorites_default_msg = 'Your Favorites will appear here'
        expected_favorites = ['Margin by Product Category']
        item_name="Margin by Product Category"

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        def verify_favorites_message(expected, msg):
            """
            This function is used to favorites_message inside content area.
            :usage verify_favorites_message('Your Favorites will appear here', "Step09.2b: Verify no content is added to favorites view")
            """
            list_title_elems =self.driver.find_elements_by_css_selector(favorites_content_area_css)
            actual_list_title = [elem.text.strip() for elem in list_title_elems if elem.text.strip()!='']
            utillobj.as_List_equal(expected, actual_list_title, msg)
        
        def verify_tag_button_in_portal_content_area(tag_button_name, tag_state, msg):
            """
            This function is used to verify tag button state{'checked', 'unchecked'}
            :usage verify_tag_button_in_portal_content_area('P292_S10660', True, "Step 9: verify 'P292_S10660' is checked')
            """
            try:
                tag_button_elems=driver.find_elements_by_css_selector(portal_tag_content_area_css)
            except NoSuchElementException:
                raise AttributeError("tag button not exist in portal content area")
            tag_elem=[elem for elem in tag_button_elems if elem.text.strip()==tag_button_name][0]
            try:
                tag_status=tag_elem.find_element_by_css_selector('.fa-check').is_displayed()
            except NoSuchElementException:
                tag_status=False
            utillobj.asequal(tag_state, tag_status, msg)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
                    Verify sidebar listed with the following options :
                    1.Content View (By default selected).
                    2.Portals View.
                    3.Favorites View. 
                    4.Ask WebFOCUS.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step01.1: Verify Side bar(left panel) options")
        left_panel_area_elem=driver.find_element_by_css_selector(left_panel_area_css)
        utillobj.verify_regional_picture_using_sikuli("content.png", "Step01.2a: Verify content image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("portal.png", "Step01.2b: Verify portals image displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("favourites.png", "Step01.2c: Verify favorites image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("ask_webfocus.png", "Step01.2d: Verify Ask WebFOCUS image is displayed", parent_element=left_panel_area_elem)
           
        """
        Step02: Select Retail Samples under Domains.
        Verify by default content area shows in grid view.
        """
        wfmain_obj.click_repository_folder('Retail Samples')
        wfmain_obj.verify_folder_item_grid_view("My Content", "Charts", "Step02.1a: Verify content area shows in grid view")
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step02.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step02.1c: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step02.2.1: Verify content title label folders", label_type='folders')
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_files_list, "Step02.2.1: Verify content title label folders")
        default_sort_status = self.driver.find_element_by_css_selector(".sd-content-title-label-files .content-title-btn-name").is_displayed()
        utillobj.asequal(False, default_sort_status, "Step02.2.2b: Verify label files - Default Sort is not displayed")
          
        """ Step 3: Click on toggle button list view.
                Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        wfmain_obj.verify_list_view("My Content", "Charts", "Step03.1a: Verify content area shows in list view")
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step03.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step03.1c: Verify grid view image object is displaying when list view is selected")
        wfmain_obj.verify_list_view_title_labels(expected_list_view_titles, "Step03.1d: Verify list view titles")
          
        """ Step 4: Click sorting tool option.
                    Verify drop down menu to choose sorting options for the items in the list view:
                    1.Title.
                    2.Name.
                    3.Summary.
                    4.Tags
                    5.Last modified.
                    6.Created on.
                    7.Size.
                    8.Owner.
                    9.Published.
                    10.Shown.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step04: Verify drop down menu items in the list view")
          
        """ Step 5: Click on toggle button grid view.
                    Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        wfmain_obj.verify_folder_item_grid_view("My Content", "Charts", "Step05.1a: Verify content area shows in grid view")
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step05.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step05.1c: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step05.2.1: Verify content title label folders", label_type='folders')
          
        """ Step 6: Click Portals from the sidebar and Click "P292_S10660" and "Retail Samples" tags at the top of the content area.
                    Verify content area displayed in grid view with the portals (Retail Samples and V4 Portal) 
                    available for selected tags (P292_S10660 and Retail Samples),
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", 45)
        wfmain_obj.select_button_in_portal_content_area('P292_S10660')
        wfmain_obj.select_button_in_portal_content_area('Retail Samples')
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step06.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step06.1c: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step06.2a: Verify content title label files")
        wfmain_obj.verify_items_in_grid_view(expected_portals, 'asin', "Step06.2b: Verify Retail Samples and V4 Portal")
          
        """ Step 7: Click on toggle button list view.
                    Verify content area displayed in list view.
        """
        wfmain_obj.select_list_view()
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("grid_view.png", "Step07.1b: Verify grid view image displayed when list view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(grid_view_css, True, "Step07.1c: Verify grid view image object is displaying when list view is selected")
        wfmain_obj.verify_list_view_title_labels(expected_portals_list_view_titles, "Step07.1d: Verify list view titles")
          
        """ Step 8: Click on toggle button grid view and click "P292_S10660" and "Retail Samples" tags at the top of the content area to unchecked the tags.
                    Verify content area back to grid view and "P292_S10660" and "Retail Samples" tags are not selected.
        """
        wfmain_obj.select_grid_view()
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step08.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step08.1c: Verify  list view image object is displaying")
        wfmain_obj.select_button_in_portal_content_area('P292_S10660')
        wfmain_obj.select_button_in_portal_content_area('Retail Samples')
        verify_tag_button_in_portal_content_area('P292_S10660', False, "Step 08.2: 'P292_S10660' tags not selected.")
        verify_tag_button_in_portal_content_area('Retail Samples', False, "Step 08.2a: 'Retail Samples' tags not selected.")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step08.2b: Verify content title label files")
        
        """ Step 9: Click Favorites from the sidebar.
                    Verify if no content is added to favorites view then below context will appear.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", 45)
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step09.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step09.1c: Verify  list view image object is displaying")
        verify_favorites_message(expected_favorites_default_msg, "Step09.2b: Verify no content is added to favorites view")
          
        """ Step 10: Click Content from sidebar > Retail Samples > Reports > Right click on "Margin by Product Category" > Add to Favorites.
                     Verify Favorite added popup opens with a background transparent green layer over the popup.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.right_click_folder_item_and_select_menu(item_name, 'Add to Favorites', folder_path='Retail Samples->Reports')
        wfmain_obj.verify_favorites_notify_popup("Step10: Favorites added")
         
        """ Step 11: Click Favorites from the sidebar.
                     Verify if the content is added to favorites view, then it is displayed in the content area with the added report in grid view.
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 5, medium_wait)
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step11.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step11.1c: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_favorites_files_list, "Step11.2a: Verify favorites title label")
        wfmain_obj.verify_items_in_grid_view(expected_favorites, 'asin', "Step11.2b: Verify Quantity Sold By Stores report in grid view")
        
        """ Step 12: Click toggle button list view.
                     Verify content area displayed in list view.
        """
        wfmain_obj.select_list_view()
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("grid_view.png", "Step12.1b: Verify grid view image displayed when list view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(grid_view_css, True, "Step12.1c: Verify grid view image object is displaying when list view is selected")
        wfmain_obj.verify_list_view_title_labels(expected_favorites_list_view_titles, "Step12.1d: Verify list view titles")
        wfmain_obj.verify_items_in_list_view(expected_favorites, 'asin', "Step12.1e: Verify Quantity Sold By Stores report in list view")
          
        """ Step 13: Click toggle button grid view.
                     Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        toolbar_elem=driver.find_element_by_css_selector(toolbar_css)
        utillobj.verify_regional_picture_using_sikuli("list_view.png", "Step13.1b: Verify list view image displayed when grid view is selected", parent_element=toolbar_elem)
        utillobj.verify_object_visible(list_view_css, True, "Step13.1c: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_favorites_files_list, "Step13.2a: Verify favorites title label")
        wfmain_obj.verify_items_in_grid_view(expected_favorites, 'asin', "Step13.2b: Verify Quantity Sold By Stores report in grid view")
          
        """ Step 14: Right Click on "Margin by Product Category" > Click Remove favorite.
                     Verify "Margin by Product Category" favorite is removed from the content area.
        """
        utillobj.synchronize_with_visble_text(files_box_css, "Items", short_wait)
        wfmain_obj.right_click_folder_item_and_select_menu(item_name, 'Remove from Favorites')
        utillobj.synchronize_with_visble_text(".files-box-files .ibx-label-text", "Your Favorites will appear here", medium_wait)
        wfmain_obj.verify_items_in_grid_view(expected_favorites, 'asnotin', "Step14.1: Verify Quantity Sold By Stores report not in grid view")
          
        """ Step 15: Click Ask WebFOCUS from the sidebar.
                     Verify that the Search box is displays with the three options are as follows:
                     1.Search by Voice 
                     2.Search 
                     3.Search options (drop down)
                     Also verify that 'Last Viewed Questions' with Clear (disable) button is shown.
        """
        wfmain_obj.select_ask_webfocus_from_sidebar()
        utillobj.synchronize_with_number_of_element(".ask-title-label", 1, short_wait)
        wfmain_obj.ask_webfocus_search_bar_options('text_box', True, "Step015: Verify text box")
        wfmain_obj.ask_webfocus_search_bar_options('speech_mic', True, "Step015.1: Verify Search by Voice")
        wfmain_obj.ask_webfocus_search_bar_options('search_image', True, "Step015.2: Verify Search")
        wfmain_obj.ask_webfocus_search_bar_options('dropdown', True, "Step015.3: Verify Search options (drop down)")
        wfmain_obj.ask_webfocus_content_area('title', 'Last Viewed Questions', 'Step15.4a: Verify title')
        wfmain_obj.ask_webfocus_content_area('title_button_state', True, 'Step15.4b: Verify Clear (disable) button is shown')
        wfmain_obj.ask_webfocus_content_area('title_button_text', 'Clear', 'Step15.4c: Verify title button name is Clear')
         
        """ Step 16: Click on the Collapse side bar icon.
                     Verify that the sidebar is collapsed and following should be displayed:
                     1.Four sidebar menu icons.
                     2.Information Builders text logo will convert into the simplified square Information Builders logo
        """
        wfmain_obj.collapse_side_bar()
        wfmain_obj.verify_left_panel([], "Step16.1: Verify Side bar(left panel) options doesn't show any text",'')
        left_panel_area_elem=driver.find_element_by_css_selector(left_panel_area_css)
        utillobj.verify_regional_picture_using_sikuli("collapse_content.png", "Step16.2a: Verify Collapse content image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_portal.png", "Step16.2b: Verify Collapse portals image displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_favourites.png", "Step16.2c: Verify Collapse favorites image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_ask_webfocus_highlighted.png", "Step16.2d: Verify Collapse ask WebFOCUS image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_logo.png", "Step16.2e: Verify Collapse logo image is displayed", parent_element=left_panel_area_elem)
         
        """ Step 17: Sign Out and Sign back into WebFOCUS Home Page as Admin User.
                     Verify that the state of the sidebar should be remembered when the user signs out of the Home Page and signs back in.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(crumb_box_css, "Mobile Favorites", medium_wait)
        wfmain_obj.verify_left_panel([], "Step17.1: Verify Side bar(left panel) options",'')
        left_panel_area_elem=driver.find_element_by_css_selector(left_panel_area_css)
        utillobj.verify_regional_picture_using_sikuli("collapse_content.png", "Step17.2a: Verify content image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_portal.png", "Step17.2b: Verify portals image displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_favourites.png", "Step17.2c: Verify favorites image is displayed", parent_element=left_panel_area_elem)
        utillobj.verify_regional_picture_using_sikuli("collapse_logo.png", "Step17.2e: Verify collapse logo image is displayed", parent_element=left_panel_area_elem)
         
        """ Step 18: Revert back the Home Page by its default state.
        """
        wfmain_obj.expand_side_bar()
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.verify_left_panel(content_list, "Step18.1: Verify Side bar(left panel) options")
         
        """ Step 19: Sign Out WebFOCUS Home Page.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        