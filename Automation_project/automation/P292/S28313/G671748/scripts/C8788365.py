'''
Created on March 14, 2019

@author: AA14564

Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8788365
Testcase Name : Verify action Bar Blog option for Admin user
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.pages import wf_mainpage as mainpage
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables

class C8788365_TestClass(BaseTestCase):

    def test_C8788365(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        wfmainpage_obj = mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        main_page_obj=wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        expected_summary="this is Test blog"
        expected_window_title='Comments'
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        title_box_css="#sdtxtFileTitle input[class$='focused']"
        content_box_css = ".content-box"
        comment_css = "[id^='BipAnnotationsLabel'][class='bi-label annotations_new']"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text('.crumb-box [title] .ibx-label-text', 'Workspaces',  Global_variables.longwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'Retail Samples' from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, 'Other', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Other' category button
        """
        main_page_obj.select_action_bar_tab('Other')
        
        """
        Step 5: Click on 'Blog' action bar under 'Other' category
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'Blog', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Blog')
        
        """
        Step 5.1: Verify that the cursor is in the Title box by default
        Also, Verify that the OK button is disabled until you start to enter a title
        """
        util_obj.verify_object_visible(title_box_css, True, 'Step 5.1: Verify that the cursor is in the Title box by default')
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(button_name='OK', msg="Step 5.2: Verify that the OK button is disabled until you start to enter a title", enable=False)
        
        """
        Step 6: Enter 'C6667551' in the title
        Enter "this is Test blog" in the summary
        """
        main_page_obj.enter_blog_title_in_popup_dialog(title='C6667551')
        main_page_obj.enter_blog_summary_in_popup_dialog(summary="this is Test blog")
        time.sleep(Global_variables.longwait)
        
        """
        Step 7: Click the cancel button
        """
        main_page_obj.click_button_on_popup_dialog(button_name='Cancel')
        
        """
        Step 8: Again Click on 'Blog' action bar
        """
        main_page_obj.select_action_bar_tabs_option('Blog')
        
        """
        Step 9: Enter 'C6667551' in the title
        Enter "this is Test blog" in the summary and click Ok
        """
        main_page_obj.enter_blog_title_in_popup_dialog(title='C6667551')
        main_page_obj.enter_blog_summary_in_popup_dialog(summary="this is Test blog")
        time.sleep(Global_variables.longwait)
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        util_obj.wait_for_page_loads(10)
        
        """
        Verify 'Comments' window opens
        """
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(comment_css, 1, Global_variables.mediumwait*5)
        actual_window_title=self.driver.title
        util_obj.asequal(expected_window_title, actual_window_title, "Step 9.1: Verify 'Comments' window opens")
        util_obj.verify_element_text(comment_css, 'Add comment...', "Step 9.2: Verify 'Comments' window opens")
        
        """
        Step 10: Close that window
        """
        core_utilobj.switch_to_previous_window()
        
        """
        Step 10.1: Verify 'C6667551' is displayed in content area
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'C6667551', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['C6667551'], 'asin', "Step 10.1:")
        
        """
        Step 11: Hover over 'C6667551'
        Verify that you see the summary
        """
        blog_item = wfmainpage_obj.get_domain_folder_item('C6667551')
        core_utilobj.python_move_to_element(blog_item)
        time.sleep(Global_variables.shortwait)
        actual_summary = blog_item.find_element_by_css_selector("div[class='file-item-text-box']").text.strip()
        util_obj.asequal(expected_summary, actual_summary, "Step 11: Verify that you see the summary")
        
        """
        Step 12: Right Click on 'C6667551' > Delete > Ok
        """
        main_page_obj.right_click_folder_item_and_select_menu(item_name="this is Test blog\nC6667551", context_menu_item_path='Delete')
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        
        """
        Step 13: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()