'''
Created on May 9, 2019

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2326936
TestCase Name = Verify action Bar Blog option for Dev user 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages import wf_mainpage as pages

class C2326936_TestClass(BaseTestCase):

    def test_C2326936(self):
        """
        Test case objects
        """
        main_pages_obj = pages.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Step 1: Sign into WebFOCUS as Developer user.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on "Retail Samples" domain > Click on "other" category button > Click on "Blog" action tile
        Verify the "New Blog" dialog opens with the cursor is in the Title box and OK button is disabled by default.
        """
        main_page_obj.expand_repository_folder('Workspaces->Retail Samples')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Blog')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Blog', main_page_obj.home_page_short_timesleep)
        blog_title = util_obj.validate_and_get_webdriver_object(".ibx-title-bar-caption", 'blog-title').text.strip()
        util_obj.asequal(blog_title, "New Blog", "Step 2.1: Verify blog title")
        title_obj = util_obj.validate_and_get_webdriver_object("#sdtxtFileTitle", 'title')
        input_attribute = util_obj.get_element_attribute(title_obj, 'class')
        util_obj.asin('active', input_attribute, "Step 2.2: Verify that title is highlightened")
        ok_obj = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button", 'ok')
        ok_attribute = util_obj.get_element_attribute(ok_obj, 'class')
        util_obj.asin('button-disabled', ok_attribute, "Step 2.3: Verify that ok is disabled")
        
        """
        Step 3: Enter "New_Blog" as the title and summary as "This is a blog"
        Verify that after entering title OK button is enabled.
        """
        main_page_obj.enter_blog_title_in_popup_dialog('New_Blog')
        main_page_obj.enter_blog_summary_in_popup_dialog('This is a blog')
        ok_obj = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button", 'ok')
        ok_attribute = util_obj.get_element_attribute(ok_obj, 'class')
        util_obj.as_notin('button-disabled', ok_attribute, "Step 2.3: Verify that ok is disabled")
        
        """
        Step 4: Click on Cancel button
        Verify that the blog dialog closes and the blog has NOT been created
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        util_obj.verify_object_visible(".create-new-blog", False, 'Step 4.1: Verify dialog is not visible')
        main_page_obj.verify_items_in_grid_view(['New_Blog'], 'asnotin', 'Step 4.2: Verify new blog not in the content area')
        
        """
        Step 5: Again, Click on "Blog" action tile > Enter "New_Blog" as the title and summary as "This is a blog" > Click the OK button
        Verify that "Comment" window is opened.
        """
        main_page_obj.select_action_bar_tabs_option('Blog')
        main_page_obj.enter_blog_title_in_popup_dialog('New_Blog')
        main_page_obj.enter_blog_summary_in_popup_dialog('This is a blog')
        main_page_obj.click_button_on_popup_dialog('OK')
        core_util_obj.switch_to_new_window()
        util_obj.asequal(self.driver.title, 'Comments', 'Step 5.1: Verify title in a new window')
        
        """
        Step 6: Close the "Comment" window
        Verify that the "New_Blog" is created in the content area.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view(['New_Blog'], 'asin', 'Step 6.1: Verify new blog in the content area')
        
        """
        Step 7: Hover over the "New_Blog"
        Verify the summary as "This is a blog"
        """
        new_blog_obj = main_pages_obj.get_domain_folder_item('New_Blog')
        core_util_obj.move_to_element(new_blog_obj)
        hover_summary = util_obj.validate_and_get_webdriver_object(".file-item-text-box:not([style*='none'])", 'blog').text.strip()
        util_obj.asequal(hover_summary, 'This is a blog', "Step 7.1: Verify the blog summary after hover")
        folder_obj = util_obj.validate_and_get_webdriver_object("div[data-ibxp-text=\"Folders\"]",'folder')
        core_util_obj.move_to_element(folder_obj)
        
        """
        Step 8: Right click on the "New_Blog" > Click on Delete > Click on OK button
        Verify that the "New_Blog" is deleted from the content area under "Retail Samples" domain
        """
        main_page_obj.right_click_folder_item_and_select_menu('New_Blog', 'Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view(['New_Blog'], 'asnotin', 'Step 8.1: Verify new blog in the content area')
        
        """
        Step 9: In the banner link, click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        