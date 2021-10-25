'''
Created on Oct 22, 2018

@author: Vpriya

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2327025
TestCase Name = Verify Canvas Displays all the portals the Developer user has access to (V3, V4, and future V5) in thumbnail or list modes

'''

import unittest,pyautogui
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.pages import wf_mainpage as pages
from common.locators import wf_mainpage_locators

class C2327025_TestClass(BaseTestCase):

    def test_C2327025(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2327025'
        long_wait = 90
        medium_wait = 45
        expected_search_list=['Retail Samples']
        expected_portal_list=['Retail Samples','Retail Samples','V3 portal']
        content_box_css=".explore-box .content-box"
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        pages_obj=pages.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", medium_wait)
        
        """
        Step02: Click Portals from the sidebar.
        Verify content area displayed in grid view with the list of all available portals and also 'Default Sort' is not displayed in Sort button(top right in content area).
        """
        left_panel_css = "div.left-main-panel-button-size"
        crumb_box_css = ".crumb-box .ibx-label-text"
        #list_view_css = "[class*='fa fa-list']"
        expected_label_portals_files_list = ['Items', 'Title', 'arrow_upward']
        expected_portals = ['Retail Samples', 'V3 portal']
        utillobj.synchronize_with_number_of_element(left_panel_css, 4, medium_wait)
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", medium_wait)
        wfmain_obj.verify_grid_view_title_labels(expected_label_portals_files_list, "Step02.a: Verify 'Default Sort' is not displayed in Sort button(top right in content area)")
        wfmain_obj.verify_items_in_grid_view(expected_portals, 'asin', "Step02b: Verify Retail Samples and V3 portals listed in portal grid view")
        v3_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl.svg']").is_displayed()
        utillobj.asequal(True, v3_img_status, "Step02c: Verify v3 portal image object is displayed")
        v4_img_status = driver.find_element_by_css_selector("img[src*='file_type/prtl_basic.svg']").is_displayed()
        utillobj.asequal(True, v4_img_status, "Step02d: Verify v4 portal image object is displayed")
        """
        Step 3:Right click on Retail Samples V4 Portal > Choose Properties > Click Advanced tab.
        
        """
        wfmain_obj.right_click_folder_item_and_select_menu('Retail Samples', 'Properties',item_name_index=2)
        wfmain_obj.select_property_tab_value('Advanced')
        
        """
        Step 4:Type 'Retail Samples' in Tags box > Click Save and Close Properties dialog.
        """
        wfmain_obj.edit_property_dialog_value('Tags', 'text_value', 'Retail Samples', typing_speed=0.5, tab_name='Advanced')
        wfmain_obj.select_property_dialog_save_cancel_button('Save')
        wfmain_obj.close_property_dialog()
        
        """
        Step 5:Click Search bar and type 'retail' existing portal.
        """
        wfmain_obj.search_input_box_options(input_text_msg="retail")
        wfmain_obj.verify_items_in_grid_view(expected_search_list, 'asin', "Step 5: Verify searched retailsamples appears in the content area")
        wfmain_obj.verify_favorites_tags(['Retail Samples','Other'], '5.1',)
        
        """
        Step06: Click toggle button List View.
        Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        list_view_css=".files-box-files-title"
        utillobj.synchronize_with_number_of_element(list_view_css, 1, medium_wait)   
        list_view_content_area_elem=driver.find_element_by_css_selector(".files-box-files-area").is_displayed()
        utillobj.asequal(True, list_view_content_area_elem, "Step 6: Verify list_view_content_area_elem object is displayed")
        
        """
        Step07: Click sorting tool option.
        Verify 'Size',are not listed in the Sort list.
        """
        expected_choose_columns_content_menu = ['Title', 'Name', 'Summary', 'Last modified', 'Created on', 'Owner', 'Published', 'Shown']
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 7: Verify drop down menu items in the list view")
        
        """
        Step08:Click on the Search bar and type any existing portal name.
        Verify searched portal appears in the content area.
        """
        expected_name_in_content_area=['Retail Samples']
        wfmain_obj.search_input_box_options(input_text_msg="retail")
        wfmain_obj.verify_items_in_list_view(expected_name_in_content_area, 'asin', "Step 8: Verify Retail Samples and Retail Samples listed in portal list view")

        """
        Step09:For Chrome,IE and Edge browsers: 
        Click X icon to clear the search box.
        For Firefox browser:
        Use the backspace key to clear the search box.
        
        Verify all available portals listed in the content area.
        """
        wfmain_obj.search_input_box_options(option_type='clear')
        wfmain_obj.verify_items_in_list_view(expected_portal_list, 'asin', "Step 9: Verify Retail Samples and Retail Samples listed in portal list view")
        
        """
        Step10:Click toggle button Grid View to switch back to grid view.
        Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        wfmain_obj.verify_items_in_grid_view(expected_portal_list,'asin' ,"10: Portals verified")
        grid_view_css=".sd-content-title-label-files"
        utillobj.synchronize_with_number_of_element(grid_view_css, 1, medium_wait)
        utillobj.verify_object_visible(grid_view_css, True, "Step 10a: Verify  list view image object is displaying")
        
        """Step 11:Right click on Retail Samples > Choose Properties > Click Advanced tab.
        """
        wfmain_obj.right_click_folder_item_and_select_menu('Retail Samples', 'Properties',item_name_index=2)
        wfmain_obj.select_property_tab_value('Advanced')
        
        """
        Step 12:Using backspace key remove 'Retail Samples' from the tags box > Click Save and Close the properties dialog
        """
        wfmain_obj.edit_property_dialog_value('Tags', 'text_value', '', typing_speed=0.5, tab_name='Advanced')
        wfmain_obj.select_property_dialog_save_cancel_button('Save')
        wfmain_obj.close_property_dialog()
        wfmain_obj.verify_favorites_tags([], '12',)
        
        """ Step 13:Right click on V3 Portal.

        Verify V3 Portal context menu with the following options :
        
        1.Run.
        2.Edit.
        3.Customizations.
        -->Remove my customizations 
        -->Remove customizations for all users
        4.Delete
        5.Publish/Unpublish
        6.Security.
        -->Rules on this resource... 
        -->Effective policy... 
        -->Owner...
        """
        verify_list = ['Run', 'Edit', 'Customizations', 'Delete', 'Unpublish', 'Security']
        wfmain_obj.verify_repository_folder_item_context_menu('V3 portal', verify_list, msg='Step 13: Verify that following options are displayed')
        pages_obj.select_context_menu_item('Customizations')
        pages_obj.verify_context_menu_item(['Remove my customizations', 'Remove customizations for all users'], msg="Step 13.1: Verify that the following options are displayed under Customizations.")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        pages_obj.select_context_menu_item('Security')
        pages_obj.verify_context_menu_item(['Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 13.2: Verify that the following options are displayed under Customizations.")
        content_box_elem = utillobj.validate_and_get_webdriver_object(content_box_css,'content-box')
        core_util_obj.python_left_click(content_box_elem)
        
        """ Step 14:Right click on V4 Portal.

        Verify V3 Portal context menu with the following options :
        
        1.Run.
        2.Edit.
        3.Customizations.
        -->Remove my customizations 
        -->Remove customizations for all users
        4.Delete
        5.Publish/Unpublish
        6.Security.
        -->Rules on this resource... 
        -->Effective policy... 
        -->Owner...
        """
        
        verify_list1 = ['Run', 'Edit', 'Customizations', 'Delete', 'Unpublish', 'Hide', 'Security', 'Open item location', 'Properties']
        wfmain_obj.verify_repository_folder_item_context_menu('V4 Portal', verify_list1, msg='Step 14: Verify that following options are displayed')
        pages_obj.select_context_menu_item('Customizations')
        pages_obj.verify_context_menu_item(['Remove my customizations', 'Remove customizations for all users'], msg="Step 14.1: Verify that the following options are displayed under Customizations.")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        pages_obj.select_context_menu_item('Security')
        pages_obj.verify_context_menu_item(['Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 14.2: Verify that the following options are displayed under Customizations.")
        content_box_elem = utillobj.validate_and_get_webdriver_object(content_box_css,'content-box')
        core_util_obj.python_left_click(content_box_elem)
        
        """
        Step15: In the banner link, click on the top right username > Click Sign Out.
        """       
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        