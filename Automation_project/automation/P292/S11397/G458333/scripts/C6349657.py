"""-------------------------------------------------------------------------------------------
Created on September 27, 2019
@author: Prabhakaran

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6349657
Test Case Title =  Set Content to Chart
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design, Run as R
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.webfocus.resource_dialog import Resource_Dialog
from common.wftools.chart import Chart
import time
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6349657_TestClass(BaseTestCase):

    def test_C6349657(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_page_run = Run(self.driver)
        resource_dialog = Resource_Dialog(self.driver)
        pd_run = R(self.driver)
        chart = Chart(self.driver)
        wf_loc = WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        expected_datalabel_x=['Oceania','South America','EMEA','North America']
        custom_css_x_labels = " g.group-labels text"
        expected_datalabel_y = ['$0.00', '$50,000,000.00', '$100,000,000.00', '$150,000,000.00', '$200,000,000.00', '$250,000,000.00', '$300,000,000.00', '$350,000,000.00', '$400,000,000.00', '$450,000,000.00', '$500,000,000.00', '$550,000,000.00', '$600,000,000.00']
        custom_css_y_label=" g text.label"
        color_css=" .chartPanel .group-main path[class*='riser!s0!g0!mbar!']"
        run_parent_css= 'jschart_HOLD_0'
        
        """
            STEP 01 : Login WF as developer user.
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 02 : Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_until_element_is_visible(wf_loc.REPOSITORY_TREE_CSS, main_page.home_page_long_timesleep)
        
        """
            STEP 03 : Navigate to "P292_S11397" domain and Click on "G458333" folder.
        """
        main_page.expand_repository_folder(repository_folder)
        
        """
            STEP 04 : Click on "Page" action tile from under Designer category.
        """
        utils.synchronize_with_visble_text(wf_loc.content_area_css, 'Designer', main_page.home_page_long_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(wf_loc.content_area_css, 'Page', main_page.home_page_long_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
        
        """
            STEP 05 : Choose "Blank" template.
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 06 : In Content tab open "Repository Widgets".
        """
        pd_design.expand_and_collapse_content_tab("collapse")
        pd_design.expand_and_collapse_repository_widgets_tab("expand")
        
        """
            STEP 07 : Drag and drop "Link tile" widget on to the page canvas.
        """
        pd_design.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        time.sleep(5)
        
        """
            STEP 08 : Click on "Properties" in Toolbar.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div.pd-right-pane", "Container")
        
        """
            STEP 09 : Click on ellipsis next to "Background" in Link Tile.
        """
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")

        """
            STEP 10 : Click "Domains" from Breadcrumbs in Select background dialog and Expand Retail Samples -> Portals -> Test Widget -> Select "Blue" >Click on "Select Background" button.
            Verify background path text box shows "IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html".
        """
        resource_dialog.select_crumb_item("Domains")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Blue")
        pd_design.resource_dialog().click_button("Select background")
        time.sleep(5)
        
        path_obj = utils.validate_and_get_webdriver_object("div[class*='pd-ps-value'] input[aria-label*='Blue']", "Path css")
        expected_result = path_obj.get_attribute("aria-label")
        msg = "Step 10.01 : Verify background path text box shows 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html'"
        actual_result = "IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html"
        utils.asequal(expected_result, actual_result, msg)
        
        """
            STEP 11 : Click on ellipsis next to "Content".
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        
        """
            STEP 12 : Click "Domains" from Breadcrumbs and Expand Retail Samples -> Charts -> select "Arc - Sales by Region" and click on "Select Content" button.
            Verify content path text box shows "IBFS:/WFC/Repository/Retail_Samples/Charts/Arc-Sales_by_Region.fex".
        """
        resource_dialog.select_crumb_item("Domains")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Charts", "Arc - Sales by Region")
        pd_design.resource_dialog().click_button("Select content")
        time.sleep(5)
        
        path_obj = utils.validate_and_get_webdriver_object("div[class*='pd-ps-value'] input[aria-label*='Sales']", "Path css")
        expected_result = path_obj.get_attribute("aria-label")
        msg = "Step 12.01 : Verify content path text box shows 'IBFS:/WFC/Repository/Retail_Samples/Charts/Arc-Sales_by_Region.fex'"
        actual_result = "IBFS:/WFC/Repository/Retail_Samples/Charts/Sales_by_Region_Arc.fex"
        utils.asequal(expected_result, actual_result, msg)
        
        """
            STEP 13 : Click "Target" dropdown and Select "New Window" option.
        """
        viewer_obj = utils.validate_and_get_webdriver_object("div.ibx-select-open-btn", "Viewer css")
        core_utils.python_left_click(viewer_obj)
        pd_design.wait_for_visible_text("div[class*='pd-page-select-item']:nth-child(1)", "New")
        
        new_window_button_obj = utils.validate_and_get_webdriver_object("div[class*='pd-page-select-item']:nth-child(1)", "Button css")
        core_utils.python_left_click(new_window_button_obj)
 
        """
            STEP 14 : Click "Preview" in Toolbar and Click on link tile widget.
            Verify that "Arc - Sales by Region" chart run in a new window without any error as below.
        """
        pd_design.click_preview()
        
        linktile_obj = utils.validate_and_get_webdriver_object("div.content-repository-widget", "link tile obj")
        core_utils.python_left_click(linktile_obj)
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("#jschart_HOLD_0", "Oceania")
        
        chart.verify_x_axis_label_in_run_window(expected_datalabel_x, xyz_axis_label_css=custom_css_x_labels, msg="Step 14.01 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_y_axis_label_in_run_window(expected_datalabel_y, xyz_axis_label_css=custom_css_y_label, msg="Step 14.02 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_chart_color_using_get_css_property_in_run_window(color_css, "dark_green", attribute='fill', msg="Step 14.03 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_number_of_chart_segment(run_parent_css, 4, "Step 14.04 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        
        """
            STEP 15 : Close new window with "Arc - Sales by Region" chart.
        """
        core_utils.switch_to_previous_window(window_close = True)
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        
        """
            STEP 16 : Return back to designer using blue arrow in preview.
        """
        pd_run.go_back_to_design_from_preview()
        
        """
            STEP 17 : Click "Save" in toolbar Enter "C6349657" and Click "Save" button.
        """
        pd_design.save_page_from_toolbar("C6349657")
        
        """
            STEP 18 : Click the Application menu and Select "Close".
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close = False)
        utils.synchronize_with_visble_text(wf_loc.content_area_css, "C6349657", main_page.home_page_long_timesleep)
        
        """
            STEP 19 : Double click on "C6349657" page and Click on Link tile widget.
            Verify that "Arc - Sales by Region" chart run in a new window without any error as below.
        """
        main_page.double_click_on_content_area_items("C6349657")
        chart.switch_to_frame(frame_css = "iframe[class='ibx-iframe-frame'][src*='c6349657']")
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        
        linktile_obj = utils.validate_and_get_webdriver_object("div.content-repository-widget", "link tile obj")
        core_utils.python_left_click(linktile_obj)
        core_utils.switch_to_default_content()
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("#jschart_HOLD_0", "Oceania")
        
        chart.verify_x_axis_label_in_run_window(expected_datalabel_x, xyz_axis_label_css=custom_css_x_labels, msg="Step 19.01 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_y_axis_label_in_run_window(expected_datalabel_y, xyz_axis_label_css=custom_css_y_label, msg="Step 19.02 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_chart_color_using_get_css_property_in_run_window(color_css, "dark_green", attribute='fill', msg="Step 19.03 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
        chart.verify_number_of_chart_segment(run_parent_css, 4, "Step 19.04 : Verify that 'Arc - Sales by Region' chart run in a new window without any error as below")
    
        """
            STEP 20 : Close new window with "Arc - Sales by Region" chart.
        """
        core_utils.switch_to_previous_window(window_close = False)
        chart.switch_to_frame(frame_css = "iframe[class='ibx-iframe-frame'][src*='c6349657']")
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        core_utils.switch_to_default_content()
        
        """
            STEP 21 : Close the output window.
        """
        main_page_run.close()
        utils.synchronize_with_visble_text(wf_loc.content_area_css, "C6349657", main_page.home_page_long_timesleep)
        
        """
            STEP 22 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()