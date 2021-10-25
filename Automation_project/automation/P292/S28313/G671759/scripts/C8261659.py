'''
Created on March 26,2019

@author: varun
Testcase Name : Test portal themes
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261659
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools.designer_portal import Portal
from common.wftools.designer_portal import Two_Level_Side

class C8261659_TestClass(BaseTestCase):
    
    def test_C8261659(self):
        """
        Test_case objects
        """
        designer_portal_obj = Portal(self.driver)
        two_level_side_obj = Two_Level_Side(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        portal_edit_css = ".ibx-dialog-main-box .ibx-dialog-title-box"
        repository_css = ".ibfs-tree"
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Right click on 'v5portal1' and select Edit
        Verify Designer 2018 theme has been selected as below
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains->V5 Domain Testing')
        main_page_obj.select_repository_folder_context_menu('v5portal1', 'Edit')
        util_obj.synchronize_with_number_of_element(portal_edit_css, 1, main_page_obj.home_page_short_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='3.1')
        
        """
        Step 4: Click on Two-level side, Three-level, Two-level top one by one and back to Two-level side navigation
        """
        try: 
            designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        except LookupError:
            pass
        designer_portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        designer_portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        
        """
        Step 5: Click save.
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 6: Right click on 'v5portal1' and select Run     
        Verify portal appears as below
        """
        main_page_obj.select_repository_folder_context_menu('v5portal1', 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, 'v5portal1', main_page_obj.home_page_medium_timesleep)
        portal_title = util_obj.validate_and_get_webdriver_object(portal_title_css, "portal title").text.strip()
        util_obj.asequal(portal_title, 'v5portal1', "Step 6.1: Verify the portal title")
        two_level_side_obj.verify_folders_in_left_sidebar(['My Pages'], "Step 6.2: Verify the folders", assert_type='asin')
        two_level_side_obj.expand_folder_in_left_sidebar('My Pages')
        util_obj.wait_for_page_loads(10)
        two_level_side_obj.verify_pages_under_the_folder_in_left_sidebar('My Pages', ['+'], "Step 6.3: Verify the pages")
        canvas_text = util_obj.validate_and_get_webdriver_object(".files-no-search-results .ibx-label-text", "canvas_text").text.strip()
        util_obj.asequal(canvas_text, 'There are no pages available', "Step 6.4: Verify the canvas text")
        
        """
        Step 7: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 8: Right click on 'v5portal1' and select Edit
        Verify 'Designer 2018' is the theme selected and two-level side navigation is being used
        """
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_repository_folder_context_menu('v5portal1', 'Edit')
        util_obj.synchronize_with_number_of_element(portal_edit_css, 1, main_page_obj.home_page_short_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='8.1')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='8.2')
        
        """
        Step 9: Click on Theme drop down and select Light
        Verify light theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Light')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', step_number='9.1')
        
        """
        Step 10: Click Save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 11: Right click on 'v5portal1' and select Edit
        Verify 'Light' theme is still selected;
        Navigation stays with 'Two-level side'
        """
        main_page_obj.select_repository_folder_context_menu('v5portal1', 'Edit')
        util_obj.synchronize_with_number_of_element(portal_edit_css, 1, main_page_obj.home_page_short_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', step_number='11.1')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='11.2')
        
        """
        Step 12: Click on Theme drop down and select Midnight
        Verify Midnight theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Midnight')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', step_number='12.1')
        
        """
        Step 13: Click Save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 14: Right click on 'v5portal1' and select Edit
        Verify 'Midnight' theme is still selected;
        Navigation stays with 'Two-level side'
        """
        main_page_obj.select_repository_folder_context_menu('v5portal1', 'Edit')
        util_obj.synchronize_with_number_of_element(portal_edit_css, 1, main_page_obj.home_page_short_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', step_number='11.1')
        designer_portal_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check', step_number='11.2')
        
        """
        Step 15: Click on Theme drop down and select 'Designer 2018'
        Verify Designer 2018 theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Designer 2018')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='15.1')
        
        """
        Step 16: Click Save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 17: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()