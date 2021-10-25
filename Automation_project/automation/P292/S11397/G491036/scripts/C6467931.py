'''
Created on September 04, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491036&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6467931
TestCase Name = Verify Canvas Displays all the portals the Public user has access to (V3, V4, and future V5) in thumbnail or list modes
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility
from common.locators import wf_mainpage_locators

class C6467931_TestClass(BaseTestCase):

    def test_C6467931(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        medium_wait = 145
        crumb_box_css = ".crumb-box .ibx-label-text"
        list_view_image_css = "[class*='fa fa-list']"
        list_view_title_css=".files-box-files-title"
        grid_view_css=".sd-content-title-label-files"
        files_box_css = ".content-box.ibx-widget .files-box .ibx-label-text"
        content_box_css=".explore-box .content-box"
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_portals = ['1TestV3', 'V4 Portal']
        expected_choose_columns_content_menu = ['Size']
        expected_search_list=['1TestV3']
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Public User by clicking the Public access Link.
        """
        wftools_login_obj.invoke_home_page_with_public_access()
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        """ Step 2: Click on Content tree from side bar.
        """
        wfmain_obj.select_content_from_sidebar()
        folders_css="[data-ibxp-text*='Folders']"
        utillobj.synchronize_with_visble_text(folders_css, "Folders", medium_wait)
    
        """ Step 3: Click Portals from the sidebar.
                    Verify content area displayed in grid view and listed available portals such as V3, V4, and 
                    future V5 ("1TestV3" Portal list for automation environment) and also 'Default Sort' is not displayed in Sort button(top right in content area)
        """
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", medium_wait)
        utillobj.verify_picture_using_sikuli("list_view.png", "Step 3: Verify list view image displayed when grid view is selected")
        utillobj.verify_object_visible(list_view_image_css, True, "Step 3.1: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step 3.2: Verify 'Default Sort' is not displayed in Sort button(top right in content area)")
        wfmain_obj.verify_items_in_grid_view(expected_portals, 'asin', "Step 3.3: Verify Retail Samples and V3 portals listed in portal grid view")
        
        """ Step 3: Click toggle button List View.
                    Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        utillobj.synchronize_with_number_of_element(list_view_title_css, 1, medium_wait)   
        list_view_content_area_elem=driver.find_element_by_css_selector(".files-box-files-area").is_displayed()
        utillobj.asequal(True, list_view_content_area_elem, "Step 3: Verify list_view_content_area_elem object is displayed")   
        
        """ Step 4: Click sorting tool option.
                    Verify "Size" is not shown in Sort list.
        """
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 4: Verify 'Size' are not listed in the Sort list.", comparision_type='asnotin')

        """ Step 5: Click Search bar and '1TestV3' Portal.
                    Verify '1TestV3' Portal appears in the content area.
        """
        wfmain_obj.search_input_box_options(input_text_msg="1TestV3")
        wfmain_obj.verify_items_in_list_view(expected_search_list, 'asListEqual', "Step 5: Verify searched 1TestV3 appears in the content area")

        """ Step 6: For Chrome,IE and Edge browsers: 
                    Click X icon to clear the search box.
                    For Firefox browser:
                    Use the backspace key to clear the search box.
                    Verify all available portals listed in the content area.
        """
        wfmain_obj.search_input_box_options(option_type='clear')
        wfmain_obj.verify_items_in_list_view(expected_portals, 'asin', "Step 6: Verify all available portals listed in the content area.")
        
        """ Step 7: Click toggle button Grid View.
                    Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        utillobj.synchronize_with_number_of_element(grid_view_css, 1, medium_wait)
        utillobj.verify_object_visible(list_view_image_css, True, "Step 7: Verify  list view image object is displaying")
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step 7.1: Verify content area back to grid view.") 

        """ Step 8: Right click on '1TestV3' Portal
                    Verify '1TestV3' Portal context menu with the below option :
                    Run.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[0], ['Run'], msg="Step 8: Verify '1TestV3' Portal context menu with the below options : 'Run'.")
        content_box_elem = driver.find_element_by_css_selector(content_box_css)
        core_utilobj.python_left_click(content_box_elem)
        
        """ Step 9: Right click on 'V4 Portal'
                    Verify 'V4 Portal' context menu with the below option :
                    Run.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[1], ['Run'], msg="Step 9: Verify 'V4 Portal' Portal context menu with the below options : 'Run'.")
        
        """ Step 10: In the banner link, click on the top right username > Click Sign In. Verify it back to WebFOCUS Sign In Page.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Folders", 45)
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        