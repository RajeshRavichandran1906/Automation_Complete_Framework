'''
Created on July 13, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491033&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6467921
TestCase Name = Verify what Side Bar options show / are functional for a Public User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C6467921_TestClass(BaseTestCase):

    def test_C6467921(self):
        
        """
        TESTCASE VARIABLES
        """
        
        long_wait = 190
        medium_wait = 95
        list_view_css = "[class*='fa fa-list']"
        grid_view_css = "[class*='fa fa-th']"
        left_panel_css = "div.left-main-panel-button-size"
        crumb_box_css = ".crumb-box .ibx-label-text"
        item_css =".content-box.ibx-widget .files-box .file-item .ibx-label-text"
        content_list=['Content', 'Portals']
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        expected_label_content_files_list = ['Items']
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_choose_columns_content_menu = ['Title', 'Name', 'Summary', 'Tags', 'Last modified', 'Created on', 'Size', 'Owner']
        expected_list_view_titles = ['Title', 'Summary', 'Last modified', 'Size']
        expected_portals_list_view_titles = ['arrow_upward\nTitle', 'Summary', 'Last modified']
        expected_portals = ['1TestV3']

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
        
        """
        Step01: Sign into WebFOCUS Home Page as Public User by clicking the Public access Link.
                Verify sidebar listed with the following options :
                1.Content View (By default selected).
                2.Portals View.
        """
        wftools_login_obj.invoke_home_page_with_public_access()
        content_css=".left-main-panel .left-main-panel-content-button [data-ibxp-text='Content'] .ibx-label-text"
        utillobj.synchronize_with_visble_text(content_css, 'Content', long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step01.1: Verify Side bar(left panel) options")
        utillobj.verify_picture_using_sikuli("content.png", "Step01.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("portal.png", "Step01.2b: Verify portals image displayed")
        content_img_status = driver.find_element_by_css_selector(".fa-bar-chart").is_displayed()
        utillobj.asequal(True, content_img_status, "Step01.3a: Verify content image object is displayed")
        portal_img_status = driver.find_element_by_css_selector(".fa-circle-o").is_displayed()
        utillobj.asequal(True, portal_img_status, "Step01.3b: Verify portal image object is displayed")
           
        """
        Step02: Select Public under Domains.
                Verify by default content area shows in grid view.
        """
        wfmain_obj.click_repository_folder('Public')
        utillobj.verify_picture_using_sikuli("list_view.png", "Step02.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step02.1c: Verify  list view image object is displaying")
        verify_title_labels('folders', expected_label_content_folders_list, "Step02.2.1: Verify content title label folders")
        verify_title_labels('files', expected_label_content_files_list, "Step02.2.2a: Verify content title label files")
        default_sort_status = self.driver.find_element_by_css_selector(".sd-content-title-label-files .content-title-btn-name").is_displayed()
        utillobj.asequal(False, default_sort_status, "Step02.2.2b: Verify label files (Items) - Default Sort is not displayed")
          
        """
        Step03: Click toggle button
        Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step03.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step03.1c: Verify grid view image object is displaying when list view is selected")
        title_css =".files-listing .files-box-files-title .ibx-label-text"
        verify_list(expected_list_view_titles, title_css, 'asListEqual', "Step03.1d: Verify list view titles")
          
        """
        Step04: Click sorting tool option.
        Verify drop down menu to choose sorting options for the items in the list view:
        1.Title.
        2.Name.
        3.Summary.
        4.Last modified.
        5.Created on.
        6.Size.
        7.Owner.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step04: Verify drop down menu items in the list view")
          
        """
        Step05: Click toggle button to back to grid view.
        Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.verify_picture_using_sikuli("list_view.png", "Step05.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step05.1c: Verify  list view image object is displaying")
        verify_title_labels('folders', expected_label_content_folders_list, "Step05.2.1: Verify content title label folders")
        verify_title_labels('files', expected_label_content_files_list, "Step05.2.2a: Verify content title label files")
        default_sort_status = self.driver.find_element_by_css_selector(".sd-content-title-label-files .content-title-btn-name").is_displayed()
        utillobj.asequal(False, default_sort_status, "Step05.2.1b: Verify label files - Default Sort is not displayed")
          
        """
        Step06: Click Portals from the sidebar.
        Verify content area displayed in grid view and listed available portals such as V3, V4, and future V5 ("1TestV3" Portal list for automation environment).
        """
        utillobj.synchronize_with_number_of_element(left_panel_css, 4, medium_wait)
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", 45)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step06.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step06.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_portals_files_list, "Step06.2a: Verify content title label files")
        verify_list(expected_portals, item_css, 'asin', "Step06.2b: Verify V3, V4, V5 portals")
        v3_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl_basic.svg']").is_displayed()
        utillobj.asequal(True, v3_img_status, "Step06.3a: Verify 1TestV3 portal image object is displayed")

        """
        Step07: Click toggle button to list view
        Verify content area displayed in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.verify_picture_using_sikuli("grid_view.png", "Step07.1b: Verify grid view image displayed when list view is selected")
        utillobj.verify_object_visible(grid_view_css, True, "Step07.1c: Verify grid view image object is displaying when list view is selected")
        title_css =".files-listing .files-box-files-title .grid-cell-title"
        verify_list(expected_portals_list_view_titles, title_css, 'asListEqual', "Step07.1d: Verify list view titles")
          
        """
        Step08: Click toggle button to back to grid view.
        Verify content back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.verify_picture_using_sikuli("list_view.png", "Step08.1b: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_css, True, "Step08.1c: Verify  list view image object is displaying")
        verify_title_labels('files', expected_label_portals_files_list, "Step08.2a: Verify content title label files")
        verify_list(expected_portals, item_css, 'asin', "Step08.2b: Verify V3, V4, V5 portals")
          
        """
        Step09: Click on the Collapse side bar icon.
        Verify that the sidebar is collapsed and following should be displayed:
        1.Two sidebar menu icons.
        2.Information Builders text logo will convert into the simplified square Information Builders logo.
        """
        wfmain_obj.collapse_side_bar()
        wfmain_obj.verify_left_panel([], "Step09.1: Verify Side bar(left panel) options doesn't show any text",'')
        utillobj.verify_picture_using_sikuli("collapse_content.png", "Step09.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("collapse_portal.png", "Step09.2b: Verify portals image displayed")
        utillobj.verify_picture_using_sikuli("collapse_logo.png", "Step09.2c: Verify collapse logo image is displayed")
        
        """
        Step10: In the banner link, click on the top right username > Click Sign In.
        Verify it back to WebFOCUS Sign In Page.
        """
        wfmain_obj.signin_from_username_dropdown_menu()
        singn_form_css=".login-form"
        status=self.driver.find_element_by_css_selector(singn_form_css).is_displayed()
        utillobj.asequal(True, status,"Step 10: Verify it back to WebFOCUS Sign In Page." )
        
        """
        Step11: Again Sign back into WebFOCUS Home Page as Public User by clicking the Public access Link.
        Verify that the state of the sidebar should not remembered for the public user when the user signs out of the Home Page and signs back in.
        """
        wftools_login_obj.invoke_home_page_with_public_access()
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        
        wfmain_obj.verify_left_panel(content_list, "Step11.1: Verify Side bar(left panel) options")
        utillobj.verify_picture_using_sikuli("content.png", "Step11.2a: Verify content image is displayed")
        utillobj.verify_picture_using_sikuli("portal.png", "Step11.2b: Verify portals image displayed")
        
        """
        Step12: In the banner link, click on the top right username > Click Sign In.
        Verify it back to WebFOCUS Sign In Page.
        """
        wfmain_obj.signin_from_username_dropdown_menu()
        status=self.driver.find_element_by_css_selector(singn_form_css).is_displayed()
        utillobj.asequal(True, status,"Step 12:  Verify it back to WebFOCUS Sign In Page.")
        
        
if __name__ == '__main__':
    unittest.main()        