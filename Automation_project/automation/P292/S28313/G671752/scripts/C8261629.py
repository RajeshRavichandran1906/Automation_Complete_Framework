'''
Created on April 10, 2018

@author: Niranjan/Samuel
Testcase Name : Test Shortcut action bar
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261629
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools.designer_portal import Three_Level
from common.lib.webfocus import resource_dialog

class C8261629_TestClass(BaseTestCase):
    
    def test_C8261629(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        three_level_side_obj = Three_Level(self.driver)
        resource_dialog_obj = resource_dialog.Resource_Dialog(self.driver)
        
        """
        Test case CSS
        """
        portal_title_css = "[class*='pvd-portal-title']"
        pop_top_css = ".pop-top"
        canvas_text_css = '.pd-page-runner'
        
        """
        Test case variables
        """
        domain_folder = 'Workspaces->V5 Domain Testing->v5portal1'
        action_bar = 'Shortcut'
        action_tile = 'Other'
        portal = 'v5portal1'
        work_book = 'Workbook_New - Shortcut'
        page_new = 'Page_new - Shortcut'
        page = 'Page 1'
        ok_button = 'OK'
        del_btn = 'Delete'
        folder = 'v5folder1'
        selection_type = 'double'
        expected_canvas_text = ['Item does not exist IBFS:/WFC/Repository/V5_Domain_Testing/v5portal1/v5folder1/page_1 (1212)']
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')

        """
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
         
        """
        Step 3: Expand 'V5 Domain Testing';
        Click on v5portal1
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Shortcut action tile from Action bar
        """
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
        Step 5: Double click on v5portal1
        """
        util_obj.synchronize_with_visble_text(pop_top_css, portal, main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview(portal, selection_type)
        util_obj.synchronize_with_visble_text(pop_top_css, 'Cancel', main_page_obj.home_page_medium_timesleep)
          
        """
        Step 6: Click cancel
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: Click on Shortcut action tile from Action Bar
        """
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
        Step 8: Double click on v5portal1->v5folder1 and click Page 1
        """
        util_obj.synchronize_with_visble_text(pop_top_css, portal, main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview(portal, selection_type)
        util_obj.synchronize_with_visble_text(pop_top_css, folder, main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview(folder, selection_type)
        util_obj.synchronize_with_visble_text(pop_top_css, page, main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview(page)
        
        """
        Step 9: Click Select button
        """
        main_page_obj.click_button_on_popup_dialog('Select')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Right click on page1 and click Publish
        Verify page 1 shortcut is published
        """
        main_page_obj.right_click_folder_item_and_select_menu(page, 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [title*='Page 1']", main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish(page, 'publish', 'Step 10.1: Verify page 1 shortcut is published')
        
        """
        Step 11: Click on V5 Domain Testing
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Common', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 12: Click Other category button and click shortcut action tile
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
         
        """
        Step 13: Click Browse button then select "Workbook_New" from under v5portal1 and click Select button
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Browse', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Browse')
        util_obj.synchronize_with_visble_text(pop_top_css, portal, main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview(portal, selection_type)
        util_obj.synchronize_with_visble_text(pop_top_css, 'Workbook_New', main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview('Workbook_New')
        main_page_obj.click_button_on_popup_dialog('Select')
        
        """
        Step 14: Click OK
        """
        util_obj.synchronize_with_visble_text(pop_top_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 15: Click Other category button and click shortcut action tile
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
        Step 16: Click Browse button then select "Page_New" from under 'V5 Domain Testing' and click Select button
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Browse', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Browse')
        util_obj.synchronize_with_visble_text(pop_top_css, 'Page_new', main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview('Page_new')
        main_page_obj.click_button_on_popup_dialog('Select')
        
        """
        Step 17: Click OK
        """
        util_obj.synchronize_with_visble_text(pop_top_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 18: Right click on 'Workbook_New-shortcut' and click Publish
        Verify 'Workbook_New-shortcut' has been published
        """
        main_page_obj.right_click_folder_item_and_select_menu(work_book, 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [title*='Workbook_New - Shortcut']", main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish(work_book, 'publish', 'Step 18.1: Verify Workbook_New-shortcut has been published')

        """
        Step 19: Right click on 'Page_New-shortcut' and click Publish
        Verify 'Page_New-shortcut' has been published
        """
        main_page_obj.right_click_folder_item_and_select_menu(page_new, 'Publish')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_new, main_page_obj.home_page_medium_timesleep)
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [title*='Page_new - Shortcut']", main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish(page_new, 'publish', 'Step 19.1: Verify Page_New-shortcut has been published')
        
        """
        Step 20: Right click on page (original page) from under 'v5portal1 -> v5folder1' and click Delete
        Verify page 1 has been deleted
        """
        main_page_obj.expand_repository_folder(domain_folder+'->'+'v5folder1')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(page, del_btn)
        util_obj.synchronize_with_visble_text(pop_top_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([page], 'asnotin', 'Step 20.1: Verify page 1 has been deleted')
        
        """
        Step 21: Right click on portal and click Run
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(portal_title_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 22: Click expand V5folder1 and click on page from side bar
        Verify Item does not exist message appears as below
        """
        three_level_side_obj.select_item_from_left_navigation_bar(page)
        actual_canvas_text =util_obj.validate_and_get_webdriver_object(canvas_text_css, 'actual canvas text').text
        util_obj.verify_list_values(expected_canvas_text, [actual_canvas_text], 'Step 22.1: Verify Item does not exist message appears as below')
        
        """
        Step 23: Close the portal run window
        """
        core_utill_obj.switch_to_previous_window()

        """
        Step 24: Right click on 'Workbook_New-shortcut' then click Delete and click ok
        Verify 'Workbook_New-shortcut' has been deleted
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(work_book, del_btn)
        util_obj.synchronize_with_visble_text(pop_top_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([work_book], 'asnotin', 'Step 24.1: Verify Workbook_New-shortcut has been deleted')
        
        """
        Step 25: Right click on 'Page_New-shortcut' then click Delete and click ok
        Verify 'Page_New-shortcut' has been deleted
        """
        main_page_obj.right_click_folder_item_and_select_menu(page_new, del_btn)
        util_obj.synchronize_with_visble_text(pop_top_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([page_new], 'asnotin', 'Step 25.1: Verify Page_New-shortcut has been deleted')
        
        """
        Step 26: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()