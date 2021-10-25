'''
Created on October 22, 2018

@author: Varun

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2327024
TestCase Name = Verify Canvas Displays all the portals the Advanced user has access to (V3, V4, and future V5) in thumbnail or list modes
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility


class C2327024_TestClass(BaseTestCase):

    def test_C2327024(self):
        
        """
        TESTCASE VARIABLES
        """
        medium_wait = 45
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        expected_portal_list = ['V3 portal','V4 Portal', 'Retail Samples']
        utillobj = utillity.UtillityMethods(self.driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Step01: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')

        """
        Step02: Click Portals from the sidebar.
        Verify content area displayed in grid view with the list of all available portals and also 'Default Sort' is not displayed in Sort button(top right in content area).
        """
        main_page_obj.select_portals_from_sidebar()
        main_page_obj.verify_items_in_grid_view(expected_portal_list,'asin' ,"Portals verified")
        
        """
        Step03: Click toggle button List View.
        Verify content area shows in list view.
        """
        wfmain_obj.select_list_view()
        list_view_css=".files-box-files-title"
        utillobj.synchronize_with_number_of_element(list_view_css, 1, medium_wait)   
        list_view_content_area = utillobj.validate_and_get_webdriver_object(".files-box-files-area","file-box-area").is_displayed()
        utillobj.asequal(True, list_view_content_area, "Step 3: Verify list_view_content_area_elem object is displayed")   
        
        """
        Step04: Click sorting tool option.
        Verify 'Size', 'Published' and 'Shown' are not listed in the Sort list.
        """
        expected_choose_columns_content_menu = ['Title', 'Name', 'Summary', 'Last modified', 'Created on', 'Owner']
        wfmain_obj.select_choose_columns_in_list_view()
        wfmain_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 4: Verify drop down menu items in the list view")

        """
        Step05:Click on the Search bar and type any existing portal name.
        Verify searched portal appears in the content area.
        """
        expected_name_in_content_area=['Retail Samples']
        wfmain_obj.search_input_box_options(input_text_msg="retail")
        wfmain_obj.verify_items_in_list_view(expected_name_in_content_area, 'asin', "Step 5: Verify Retail Samples and Retail Samples listed in portal list view")

        """
        Step06:For Chrome,IE and Edge browsers: 
        Click X icon to clear the search box.
        For Firefox browser:
        Use the backspace key to clear the search box.
        
        Verify all available portals listed in the content area.
        """
        wfmain_obj.search_input_box_options(option_type='clear')
        wfmain_obj.verify_items_in_list_view(expected_portal_list, 'asin', "Step 6: Verify Retail Samples and Retail Samples listed in portal list view")
        
        """
        Step07:Click toggle button Grid View to switch back to grid view.
        Verify content area back to grid view.
        """
        wfmain_obj.select_grid_view()
        main_page_obj.verify_items_in_grid_view(expected_portal_list,'asin' ,"7a: Portals verified")
        grid_view_css=".sd-content-title-label-files"
        utillobj.synchronize_with_number_of_element(grid_view_css, 1, medium_wait)
        utillobj.verify_object_visible(grid_view_css, True, "Step 7b: Verify  list view image object is displaying")

        """
        Step08: Right click on V3 Portals.
        Verify V3 Portal context menu with the below option :
        Run.
        """
        wfmain_obj.verify_repository_folder_item_context_menu('V3 portal', ['Run'],msg="Step 8:")
        scroll_css="div[class*='files-box-files']"
        scroll_obj=self.driver.find_element_by_css_selector(scroll_css)
        core_util_obj.left_click(scroll_obj)
        
        """
        Step09: Right click on V4 Portals.
        Verify V4 Portal context menu with the following options :
        Run.
        Properties.
        """
        wfmain_obj.verify_repository_folder_item_context_menu('V4 Portal', ['Run','Properties'], msg="Step 9:")
        
        """
        Step10: In the banner link, click on the top right username > Click Sign Out.
        """       
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        