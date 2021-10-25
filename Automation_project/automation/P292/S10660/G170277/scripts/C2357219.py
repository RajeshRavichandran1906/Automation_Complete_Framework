"""-------------------------------------------------------------------------------------------
Created on August 01, 2019
@author: AA14654

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2357219
Test Case Title =  Adding PGX to Collaborative Portal
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables
from common.pages.vfour_miscelaneous import Vfour_Miscelaneous
from common.pages.vfour_portal_properties import Vfour_Portal_Properties
from common.pages.vfour_portal_ribbon import Vfour_Portal_Ribbon
from common.pages.vfour_portal_canvas import Vfour_Portal_Canvas
from common.pages.vfour_portal_run import Vfour_Portal_Run

class C2357219_TestClass(BaseTestCase):

    def test_C2357219(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        g_var = Global_variables()
        portal_misobj = Vfour_Miscelaneous(self.driver)
        portal_properties = Vfour_Portal_Properties(self.driver)
        portal_ribbon = Vfour_Portal_Ribbon(self.driver)
        portal_canvas = Vfour_Portal_Canvas(self.driver)
        portal_run = Vfour_Portal_Run(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        retail_sample_path = "Retail Samples->InfoApps->Sales Dashboard (Filtered)"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        add_page_css = "#dlgTitleExplorer"
        property_css = "#idPropertiesPage"
        filter_icon_css = ".pd-page-header [title='Show filters']"
        filter_grid_css = ".pd-regular-filter-wrapper .pd-filter-grid"
        BIPtree_rows = "#bipResourcesPanel #treeView table>tbody>tr"
        frame_css = "[class*='bi-iframe iframe'][name*='{0}']"
        
        """ Step 1: Login WF as domain developer;
                    Click on Content view from side bar.
        """
        login.invoke_home_page('mrid', 'mrpass')
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_medium_timesleep)
        
        """ Step 2: Expand 'P292_S10660' domain;
                    Click on 'G170277' folder and choose Collaborative Portal action tile from Other category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Other", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Other")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Collaborative Portal", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Collaborative Portal")
        utils.synchronize_with_visble_text(pop_top_css, 'Title', main_page.home_page_long_timesleep)
        
        """ Step 3: Enter "C2357219" in Title and click Create
        """
        main_page.enter_new_folder_title_in_popup_dialog(g_var.current_test_case)
        main_page.click_button_on_popup_dialog('Create')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(add_page_css, '1 Column', main_page.home_page_long_timesleep)
        
        """ Step 4: Select "1 Column" Page Template, click Create button.
        """
        portal_misobj.select_page_template(page_template="1 Column", btn_name='Create')
        utils.synchronize_with_visble_text(property_css, 'Lock Page', main_page.home_page_long_timesleep)
        
        """ Step 5: In Properties uncheck Lock Page.
        """
        portal_properties.edit_input_control('page', 'Lock Page', 'checkbox', checkbox_input='uncheck', msg='Step 04.00: ')
        
        """ Step 6: Press "F8";
                    Expand Retail Samples > InfoApps folder.
        """
        portal_ribbon.invoke_and_verify_wf_resource_tree()
        
        """ Step 7: Drag Sales Dashboard (Filtered) onto the page;
                    Press F8 to close the tree
        """
        portal_canvas.dragdrop_repository_item_to_canvas(retail_sample_path, 'column', 1)
        utils.synchronize_until_element_is_visible_within_parent_object(portal_canvas.get_current_page(), frame_css.format('Panel_1_1'), main_page.home_page_long_timesleep)
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_1')
        utils.synchronize_until_element_is_visible(filter_icon_css, main_page.home_page_long_timesleep*2)
        core_utils.switch_to_default_content()
        portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord', display_status=False)
        
        
        """ Step 8: Click on Height dropdown and select Auto.
                    Verify that the Page filter icon is there
        """
        portal_properties.edit_input_control('panel', 'Height', 'combobox', combobox_input='Auto')
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_1')
        status = utils.validate_and_get_webdriver_object(filter_icon_css, 'filter_icon', parent_object=portal_canvas.get_current_page()).is_displayed()
        actual = 'Page filter icon is visible' if status else 'Page filter icon is not visible'
        utils.asequal('Page filter icon is visible', actual, 'Step 08.00: Verify the Page filter icon is visible.')
        core_utils.switch_to_default_content()
        
        """ Step 9: Save and exit the portal.
        """
        portal_ribbon.select_tool_menu_item('menu_Save')
        portal_ribbon.select_tool_menu_item('menu_Exit')
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, g_var.current_test_case, main_page.home_page_medium_timesleep)
        
        """ Step 10: Run the portal.
                     Verify that the Page filter icon is there
        """
        main_page.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Run')
        core_utils.switch_to_new_window()
        utils.synchronize_until_element_is_visible_within_parent_object(portal_canvas.get_current_page(), frame_css.format('Panel_1_1'), main_page.home_page_long_timesleep)
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_1')
        utils.synchronize_until_element_is_visible(filter_icon_css, main_page.home_page_long_timesleep*2)
        filter_ = utils.validate_and_get_webdriver_object(filter_icon_css, 'filter_icon')
        status = filter_.is_displayed()
        actual = 'Page filter icon is visible' if status else 'Page filter icon is not visible'
        utils.asequal('Page filter icon is visible', actual, 'Step 10.00: Verify the Page filter icon is visible.')
        
        """ Step 11: Click the filter icon.
                     Verify that the filter bar opens up
        """
        core_utils.left_click(filter_)
        utils.synchronize_until_element_is_visible(filter_grid_css, main_page.home_page_long_timesleep)
        filter_grid = utils.validate_and_get_webdriver_object(filter_grid_css, 'filter_icon')
        items_text = filter_grid.text.strip().split('\n')
        utils.asequal(['Region:', 'Category:', 'Model:', 'All', 'Store Front', 'Web', 'From', 'To'], items_text, 'Step 11.00: Verify that the filter bar opens up')
        core_utils.switch_to_default_content()
        
        """ Step 12: Click on Add Page "+" in navigation tab;
                     Select Fluid Canvas in Page Templates;
                     Click Create.
        """
        portal_canvas.add_page('Fluid Canvas')
        
        """ Step 13: Expand Retail Samples > InfoApps folder;
                     Drag Sales Dashboard (Filtered) onto the page.
                     Verify that the Page filter icon is there
        """
        index_num = portal_misobj.expand_tree(retail_sample_path, tree_css=BIPtree_rows)
        tree_objs = utils.validate_and_get_webdriver_objects(BIPtree_rows, 'Resource tree')
        source_obj = utils.validate_and_get_webdriver_object('img.icon', 'Resource tree', parent_object=tree_objs[index_num])
        portal_misobj.drag_drop_in_bip(source_obj, portal_canvas.get_current_page())
        utils.synchronize_until_element_is_visible_within_parent_object(portal_canvas.get_current_page(), frame_css.format('Panel_1_2'), main_page.home_page_long_timesleep)
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_2')
        utils.synchronize_until_element_is_visible(filter_icon_css, main_page.home_page_long_timesleep*2)
        filter_ = utils.validate_and_get_webdriver_object(filter_icon_css, 'filter_icon')
        status = filter_.is_displayed()
        actual = 'Page filter icon is visible' if status else 'Page filter icon is not visible'
        utils.asequal('Page filter icon is visible', actual, 'Step 13.00: Verify the Page filter icon is visible.')
        
        """ Step 14: Click the filter icon.
                     Verify that the filter bar opens up
        """
        core_utils.left_click(filter_)
        utils.synchronize_until_element_is_visible(filter_grid_css, main_page.home_page_long_timesleep)
        filter_grid = utils.validate_and_get_webdriver_object(filter_grid_css, 'filter_icon')
        items_text = filter_grid.text.strip().split('\n')
        utils.asequal(['Region:', 'Category:', 'Model:', 'All', 'Store Front', 'Web', 'From', 'To'], items_text, 'Step 14.00: Verify that the filter bar opens up')
        core_utils.switch_to_default_content()
        
        """ Step 15: Close and rerun the portal.
                     Verify that the Page filter icon is there in Fluid Canvas page.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, g_var.current_test_case, main_page.home_page_medium_timesleep)
        main_page.right_click_folder_item_and_select_menu(g_var.current_test_case, context_menu_item_path='Run')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text('.bip-portal', 'Fluid Canvas', main_page.home_page_long_timesleep)
        portal_canvas.select_page_in_navigation_bar('Fluid Canvas')
        utils.synchronize_until_element_is_visible_within_parent_object(portal_canvas.get_current_page(), frame_css.format('Panel_1_2'), main_page.home_page_long_timesleep)
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_2')
        utils.synchronize_until_element_is_visible(filter_icon_css, main_page.home_page_long_timesleep*2)
        filter_ = utils.validate_and_get_webdriver_object(filter_icon_css, 'filter_icon')
        status = filter_.is_displayed()
        actual = 'Page filter icon is visible' if status else 'Page filter icon is not visible'
        utils.asequal('Page filter icon is visible', actual, 'Step 15.00: Verify the Page filter icon is visible.')
        core_utils.switch_to_default_content()
        
        """ Step 16: Click on 1 Column page.
                     Verify that the Page filter icon is there.
        """
        portal_canvas.select_page_in_navigation_bar('1 Column')
        utils.synchronize_until_element_is_visible_within_parent_object(portal_canvas.get_current_page(), frame_css.format('Panel_1_1'), main_page.home_page_long_timesleep)
        portal_misobj.switch_to_frame_in_bip_page(frame_panel_name='Panel_1_1')
        utils.synchronize_until_element_is_visible(filter_icon_css, main_page.home_page_long_timesleep*2)
        filter_ = utils.validate_and_get_webdriver_object(filter_icon_css, 'filter_icon')
        status = filter_.is_displayed()
        actual = 'Page filter icon is visible' if status else 'Page filter icon is not visible'
        utils.asequal('Page filter icon is visible', actual, 'Step 15.00: Verify the Page filter icon is visible.')
        core_utils.switch_to_default_content()
        
        """ Step 17: Close the portal.
        """
        portal_run.select_or_verify_portal_menu_bar_item(select='Close')
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, g_var.current_test_case, main_page.home_page_medium_timesleep)
        
        """ Step 18: Sign out WF.
        """
        main_page.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()