'''
Created on November 1, 2018

@author: Robert
Testcase Name : Create portal with Two-level side navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261722
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.pages import portal_designer
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261722_TestClass(BaseTestCase):
    
    def test_C8261722(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        folder_name_path="P292_S19901->G520448"
        expected_title="v5-navigation-test1"
        content_area_text="There are no pages available"
        content_area_css = ".files-no-search-results .ibx-label-text"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        portal_title_css = "div[class*='portal-title'] .ibx-label-text"
        menu_id_bar="div[class*='menu-admin ibx-widget']"
        left_panel_css = ".bundle-folder-wrapper .pvd-left-main-panel"
        banner_css = ".pvd-portal-banner"
        canvas_css = ".pvd-canvas-container"
        
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(menu_id_bar, 1, 60)
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3. Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Step 3.1. Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Portal', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """ 
        Step 4. Enter title as 'v5-navigation-test1'
        Step 4.1. Name input box is filled automatically as 'v5-navigation-test1'
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', main_page_obj.home_page_medium_timesleep)
        portal_designer_obj.create_or_edit_portal('Title', 'text_box', expected_title, navigation_type='Two-level-side', expire_time=90)
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', expected_title, 'Step 4.1: Verify Name label automatically filled')

        """
        Step 5. Click on Theme dropdown;
        Step 5.1. Select 'Light' theme
        """
        portal_designer_obj.create_or_edit_portal('Theme', 'drop_down', 'Light', navigation_type='Two-level-side', expire_time=90)

        """
        Step 6. Choose Two-level side navigation if not selected by default
        """
        #designer_portal_obj.verify_portal_dialog(label_name, property_type, property_value, msg, navigation_type, placeholder)   
        portal_designer_obj.create_or_edit_portal('Navigation', 'radio_button', 'uncheck', navigation_type='Two-level-side') 

        """ 
        Step 7. Click Create
        Step 7.1. Verify 'New Portal' dialog is closed;
        Step 7.2. Portal title appears in Italic;
        Step 7.3. Portal is unpublished.
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", main_page_obj.home_page_short_timesleep)
        designer_portal_obj.verify_portal_dialog_open_or_close("close", "Step 7. Verify 'New Portal' dialog is closed")
        folder_name_list=['v5-navigation-test1']
        main_page_obj.expand_repository_folders_and_verify(folder_name_path, folder_name_list, 'Step 7.1: Verify repository folders')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(expected_title, 'unpublish', 'Step 7.2: Verify folder published')
        main_page_obj.verify_repository_folder_font_style(expected_title, 'italic', 'Step 7.3: Verify font is italic in content tree')
        
        """
        Step 8. Right click on 'v5-navigation-test1' and select Run
        Step 8.1. Verify portal run mode shows no banner and title as below.
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_title,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_title, main_page_obj.home_page_medium_timesleep)
        util_obj.verify_current_url('portal/P292_S19901/G520448/'+expected_title, 'Step 8.1: URL verification in new window')
        title_css = ".pvd-portal-title .ibx-label-text"
        title_name = util_obj.validate_and_get_webdriver_object(title_css, 'title-css').text.strip()
        util_obj.asequal(title_name,expected_title,"Step 8.2: Title verification")
        content_area_text_search = util_obj.validate_and_get_webdriver_object(content_area_css, 'content-text-css').text.strip()
        util_obj.asequal(content_area_text,content_area_text_search,"Step 8.3: Content area text verification")
        util_obj.verify_picture_using_sikuli("info_build_logo.png","Step 8.4: Verify the Infobuilders icon logo")  
        left_panel_element = util_obj.validate_and_get_webdriver_object(left_panel_css, "left_panel")
        canvas_element = util_obj.validate_and_get_webdriver_object(canvas_css, "canvas")
        banner_element = util_obj.validate_and_get_webdriver_object(banner_css, "banner")
        left_panel_position = core_util_obj.get_web_element_coordinate(left_panel_element)
        canvas_position = core_util_obj.get_web_element_coordinate(canvas_element, element_location='middle_left' )
        banner_position = core_util_obj.get_web_element_coordinate(banner_element, element_location='bottom_middle')
        util_obj.as_LE(left_panel_position['x'],canvas_position['x'],"Step 8.5: Verify left panel is to the left of canvas")
        util_obj.as_GE(left_panel_position['y'],banner_position['y'],"Step 8.6: Verify left panel is to the bottom of banner")  

        """
        Step 9. Close portal run mode
        """
        core_util_obj.switch_to_previous_window()
        """
        Step 10: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()