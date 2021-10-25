'''
Created on October 23, 2018

@author: Varun
Testcase Name : Verify Canvas Displays all the portals the Admin user has access to (V3, V4, and future V5) in thumbnail or list modes
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325653
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.pages import wf_mainpage as page_main
import pyautogui


class C2325653_TestClass(BaseTestCase):
    
    def test_C2325653(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        pages_obj = page_main.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        content_box_css=".explore-box .content-box"
        expected_portal_list = ['V3 portal','V4 Portal', 'Retail Samples']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
    
        """
        Step 2: Click Portals from the sidebar.
        """
        main_page_obj.select_portals_from_sidebar()
        main_page_obj.verify_items_in_grid_view(expected_portal_list,'asin' ,"Portals verified")
        
        """
        Step 3:Right click on Retail Samples V4 Portal > Choose Properties > Click Advanced tab.
        """
    
        main_page_obj.right_click_folder_item_and_select_menu('Retail Samples', 'Properties',item_name_index=2)
        main_page_obj.select_property_tab_value('Advanced')
        
        """
        Step 4: Type 'Retail Samples' in Tags box > Click Save and Close Properties dialog
        """

        main_page_obj.edit_property_dialog_value('Tags', 'text_value', 'Retail Samples', tab_name='Advanced')
        main_page_obj.select_property_dialog_save_cancel_button("Save")
        main_page_obj.close_property_dialog()
        main_page_obj.verify_favorites_tags(['Retail Samples','Other'], '4')

        """
        Step 5: Click toggle button List View.
        Verify content area shows in list view without Category buttons.
        """
        main_page_obj.select_list_view()
        list_view_css=".files-box-files-title"
        util_obj.synchronize_with_number_of_element(list_view_css, 1, Global_variables.mediumwait)   
        list_view_content_area = util_obj.validate_and_get_webdriver_object(".files-box-files-area","file-box-area").is_displayed()
        util_obj.asequal(True, list_view_content_area, "Step 5: Verify list_view_content_area_elem object is displayed")  
        
        """
        Step 6: Click sorting tool option.
        """
        expected_choose_columns_content_menu = ['Title', 'Name', 'Summary', 'Last modified', 'Created on', 'Owner','Published','Shown']
        main_page_obj.select_choose_columns_in_list_view()
        main_page_obj.verify_choose_columns_context_menu_items(expected_choose_columns_content_menu,"Step 6: Verify drop down menu items in the list view")

        """
        Step 7: Click Search bar and type 'retail' existing portal.
        Verify 'Retail Samples' appears in the content area.
        """
        expected_name_in_content_area=['Retail Samples']
        main_page_obj.search_input_box_options(input_text_msg="retail")
        main_page_obj.verify_items_in_list_view(expected_name_in_content_area, 'asin', "Step 7: Verify Retail Samples and Retail Samples listed in portal list view")
        
        """
        Step 8: For Chrome,IE and Edge browsers: 
        Click X icon to clear the search box.
        For Firefox browser:
        Use the backspace key to clear the search box. 
        """
        main_page_obj.search_input_box_options(option_type='clear')
        main_page_obj.verify_items_in_list_view(expected_portal_list, 'asin', "Step 8: Verify Retail Samples and Retail Samples listed in portal list view")
        
        """
        Step 9: Click toggle button Grid View to switch back to grid view.
        Verify content area back to grid view.
        """
        main_page_obj.select_grid_view()
        main_page_obj.verify_items_in_grid_view(expected_portal_list,'asin' ,"9a: Portals verified")
        grid_view_css=".sd-content-title-label-files"
        util_obj.synchronize_with_number_of_element(grid_view_css, 1, Global_variables.mediumwait)
        util_obj.verify_object_visible(grid_view_css, True, "Step 9b: Verify  list view image object is displaying")
        
        """
        Step 10: Right click on Retail Samples V4 Portal > Choose Properties > Click Advanced tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('Retail Samples', 'Properties',item_name_index=2)
        main_page_obj.select_property_tab_value('Advanced')
        
        """
        Step 11: Using backspace key remove 'Retail Samples' from the tags box > Click Save and Close the properties dialog.
        Verify that the 'Category buttons' (Retail Samples and Others) are not displayed.
        """
        main_page_obj.edit_property_dialog_value('Tags', 'text_value', '', tab_name='Advanced')
        main_page_obj.select_property_dialog_save_cancel_button("Save")
        main_page_obj.close_property_dialog()
        main_page_obj.verify_favorites_tags([], '11')
        
        """
        Step 12: Right click on V3 Portal.
        Verify V3 Portal context menu with the following options :
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
        verify_list = ['Run', 'Edit', 'Customizations', 'Delete', 'Unpublish', 'Security']
        main_page_obj.verify_repository_folder_item_context_menu('V3 portal', verify_list, msg='Step 12: Verify that following options are displayed')
        pages_obj.select_context_menu_item('Customizations')
        pages_obj.verify_context_menu_item(['Remove my customizations', 'Remove customizations for all users'], msg="Step 12.1: Verify that the following options are displayed under Customizations.")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        pages_obj.select_context_menu_item('Security')
        pages_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 12.2: Verify that the following options are displayed under Customizations.")
        content_box_elem = util_obj.validate_and_get_webdriver_object(content_box_css,'content-box')
        core_util_obj.python_left_click(content_box_elem)
    
        """
        Step 13: Right click on V4 Portal.
        Verify V4 Portal context menu with the following options :
        1.Run.
        2.Edit.
        3.Customizations.
        -->Remove my customizations 
        -->Remove customizations for all users
        4.Delete.
        5.Publish/Unpublish.
        6.Show.
        7.Security.
        -->Rules... 
        -->Rules on this resource... 
        -->Effective policy... 
        -->Owner...
        8.Open item location.
        9.Properties.
        """
        verify_list = ['Run', 'Edit', 'Customizations', 'Delete', 'Unpublish','Hide','Security','Open item location','Properties']
        main_page_obj.verify_repository_folder_item_context_menu('V4 Portal', verify_list, msg='Step 13: Verify that following options are displayed')
        pages_obj.select_context_menu_item('Customizations')
        pages_obj.verify_context_menu_item(['Remove my customizations', 'Remove customizations for all users'], msg="Step 13.1: Verify that the following options are displayed under Customizations.")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        pages_obj.select_context_menu_item('Security')
        pages_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 13.2: Verify that the following options are displayed under Customizations.")
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        

if __name__ == '__main__':
    unittest.main()