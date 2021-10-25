'''
Created on December 13, 2018

@author: varun
Testcase Name : Verify action Bar Page option for Dev
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261601
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility
from common.wftools import page_designer
import time

class C8261601_TestClass(BaseTestCase):
    
    def test_C8261601(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        page_preview_obj = page_designer.Preview(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        blank_title_css = ".pd-page-title .ibx-label-text"
        blank_section_css ="div[data-ibx-type=\"pdPageSection\"]"
        pd_new_page_css = ".pd-new-page .ibx-dialog-main-box"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        Test case variables
        """
        save_title = 'C6667548_0'
        save_title_two = 'C6667548_1'
        blank_title = 'Page Heading'
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Designer' category button > 'Page' action bar
        Verify New Page dialog box opens
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_new_page_css, 1 , base_obj.home_page_medium_timesleep)
        util_obj.verify_object_visible(pd_new_page_css, True, "Step 4.1: Verify New Page dialog box opens")

        """
        Step 5: Select 'Blank' template
        Verify the canvas shows Blank template
        """
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_number_of_element(blank_section_css, 1, base_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_visble_text(blank_title_css, blank_title, base_obj.home_page_short_timesleep)
        page_preview_obj.verify_containers_title([], "Step 5.1: Verify the Page is blank")
        
        """
        Step 6: Click on Application menu > Save > enter title 'C6667548_0' > Save
        """
        page_designer_obj.save_page_from_toolbar(save_title)
        
        """
        Step 7: Click on Application menu > Close
        Verify the created 'C6667548_0' is displayed in content area
        Also, Verify the correct thumbnail appears
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([save_title],'asin', 'Step 7.1: Verify the saved paged in content area')
        util_obj.verify_picture_using_sikuli('blank_thumbnail.png', 'Step 7.2: Verify the Thumbnail Appears')
        
        """
        Step 8: Right Click on 'C6667548_0' > Delete > Ok
        Verify the created 'C6667548_0' is not displayed in content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(save_title, 'Delete')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        time.sleep(main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view([save_title],'asnotin', 'Step 8.1: Verify the saved paged not in content area')
        
        """
        Step 9: Click on 'Common' category button > 'Page' action bar
        Verify New Page dialog box opens 
        """
        main_page_obj.select_action_bar_tab('Common')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_new_page_css, 1 , base_obj.home_page_medium_timesleep)
        util_obj.verify_object_visible(pd_new_page_css, True, "Step 9.1: Verify New Page dialog box opens")
        
        """
        Step 10: Select 'Blank' template
        Verify the canvas shows Blank template
        """
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_number_of_element(blank_section_css, 1, base_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_visble_text(blank_title_css, blank_title, base_obj.home_page_short_timesleep)
        page_preview_obj.verify_containers_title([], "Step 10.1: Verify the Page is blank")
        
        """
        Step 11: Click on Application menu > Save > enter title 'C6667548_1' > Save
        """
        page_designer_obj.save_page_from_toolbar(save_title_two)
        
        """
        Step 12: Click on Application menu > Close
        Verify the created 'C6667548_1' is displayed in content area
        Also, Verify the correct thumbnail appears
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([save_title_two],'asin', 'Step 12.1: Verify the saved paged in content area')
        util_obj.verify_picture_using_sikuli('blank_thumbnail.png', 'Step 12.2: Verify the Thumbnail Appears')
        
        """
        Step 13: Right Click on 'C6667548_1' > Delete > Ok
        Verify the created 'C6667548_1' is not displayed in content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(save_title_two, 'Delete')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        time.sleep(main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view([save_title_two],'asnotin', 'Step 13.1: Verify the saved paged not in content area')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()