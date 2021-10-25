"""-------------------------------------------------------------------------------------------
Created on September 30, 2019
@author: Vishnu Priya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6349658
Test Case Title =  Set Content to HTML
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

class C6349658_TestClass(BaseTestCase):

    def test_C6349658(self):
        
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
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        Step1 = """
            STEP 01 : Login WF as developer user.
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Navigate to "P292_S11397" domain and Click on "G458333" folder.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.capture_screenshot("03.01", Step3)
         
        Step4 = """
            STEP 04 : Click on "Page" action tile from under Designer category.
        """
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
        utils.capture_screenshot("04.01", Step4)
        
        Step5 = """
            STEP 05 : Choose "Blank" template.
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : In Content tab open "Repository Widgets".
        """
        pd_design.expand_and_collapse_content_tab("collapse")
        pd_design.expand_and_collapse_repository_widgets_tab("expand")
        utils.capture_screenshot("06.01", Step6)
        
        Step7 = """
            STEP 07 : Drag and drop "Link tile" widget on to the page canvas.
        """
        pd_design.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        time.sleep(5)
        utils.capture_screenshot("07.01", Step7)
        
        Step8 = """
            STEP 08 : Click on "Properties" in Toolbar.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div.pd-right-pane", "Container")
        utils.capture_screenshot("08.01", Step8)
        
        Step9 = """
            STEP 09 : Click on ellipsis next to "Background" in Link Tile.
        """ 
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        utils.capture_screenshot("09.01", Step9)
        
        Step10 = """
            STEP 10 : Click "Domains" from Breadcrumbs in Select background dialog and Expand Retail Samples > Portals > Test Widget > Select "Blue" >Click on "Select Background" button.
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
        utils.capture_screenshot("10.01", Step10, expected_image_verify = True)
        
        Step11 = """
            STEP 11 : Click on ellipsis next to "Content".
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        utils.capture_screenshot("11.01", Step11)
        
        Step12 = """
            STEP 12 : Click "Domains" from Breadcrumbs and Expand Retail Samples >InfoApps >Customizable Chart >select "Product Sales Analysis" and Click on "Select Content" button.
            Verify content path text box shows "IBFS:/WFC/Repository/Retail_Samples/InfoApps/Customizable_Chart/Product_Sales_Analysis.htm".
        """
        resource_dialog.select_crumb_item("Domains")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->InfoApps->Customizable Chart", "Product Sales Analysis")
        pd_design.resource_dialog().click_button("Select content")
        time.sleep(5)
        
        path_obj = utils.validate_and_get_webdriver_object("div[class*='pd-ps-value'] input[aria-label*='Sales']", "Path css")
        expected_result = path_obj.get_attribute("aria-label")
        msg = "Step 12.01 : Verify content path text box shows'IBFS:/WFC/Repository/Retail_Samples/InfoApps/Customizable_Chart/Product_Sales_Analysis.htm'"
        actual_result = "IBFS:/WFC/Repository/Retail_Samples/InfoApps/Customizable_Chart/Product_Sales_Analysis.htm"
        utils.asequal(expected_result, actual_result, msg)
        utils.capture_screenshot("12.01", Step12, expected_image_verify = True)
        
        Step13 = """
            STEP 13 : Click "Target" dropdown and Select "New Window" option.
        """
        viewer_obj = utils.validate_and_get_webdriver_object("div.ibx-select-open-btn", "Viewer css")
        core_utils.python_left_click(viewer_obj)
        pd_design.wait_for_visible_text("div[class*='pd-page-select-item']:nth-child(1)", "New")
        
        new_window_button_obj = utils.validate_and_get_webdriver_object("div[class*='pd-page-select-item']:nth-child(1)", "Button css")
        core_utils.python_left_click(new_window_button_obj)
        utils.capture_screenshot("13.01", Step13)
        
        Step14 = """
            STEP 14 : Click "Preview" in Toolbar and Click on link tile widget.
            Verify that "Product Sales Analysis" HTML run in a new window without any error as below.
        """
        pd_design.click_preview()
        
        linktile_obj = utils.validate_and_get_webdriver_object("div.content-repository-widget", "link tile obj")
        core_utils.python_left_click(linktile_obj)
        core_utils.switch_to_new_window()
        core_utils.switch_to_frame(frame_css = "iframe[class*='IBI_Report-iFrame']")
        chart.wait_for_visible_text("#jschart_HOLD_0", "Sale Year")
        
        chart.verify_x_axis_label_in_run_window(['2011', '2012', '2013', '2014', '2015', '2016'], msg = "Step 14.01 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_y_axis_label_in_run_window(['0', '30M', '60M', '90M', '120M', '150M'], msg = "Step 14.02 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_x_axis_title_in_run_window(['Sale Year'], msg = "Step 14.03 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_y_axis_title_in_run_window(['Gross Profit'], msg = "Step 14.04 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 14.05 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 7, 6, msg = "Step 14.06 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g5!mbar!", "bar_blue", msg = "Step 14.07 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.switch_to_default_content()
        utils.capture_screenshot("14.01", Step14, expected_image_verify = True)
        
        Step15 = """
            STEP 15 : Close the new window with "Product Sales Analysis" HTML.
        """
        core_utils.switch_to_previous_window(window_close = True)
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        utils.capture_screenshot("15.01", Step15)
        
        Step16 = """
            STEP 16 : Return back to designer using blue arrow in preview.
        """
        pd_run.go_back_to_design_from_preview()
        utils.capture_screenshot("16.01", Step16)
        
        Step17 = """
            STEP 17 : Click "Save" in toolbar Enter "C6349658" and Click "Save" button.
        """
        pd_design.save_page_from_toolbar("C6349658")
        utils.capture_screenshot("17.01", Step17)
        
        Step18 = """
            STEP 18 : Click the Application menu and Select "Close".
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close = False)
        utils.capture_screenshot("18.01", Step18)
        
        Step19 = """
            STEP 19 : Double click on "C6349658" page and Click on Link tile widget.
            Verify that "Product Sales Analysis" HTML run in a new window without any error as below.
        """
        main_page.double_click_on_content_area_items("C6349658")
        chart.switch_to_frame(frame_css = "iframe[class='ibx-iframe-frame'][src*='c6349658']")
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        
        linktile_obj = utils.validate_and_get_webdriver_object("div.content-repository-widget", "link tile obj")
        core_utils.python_left_click(linktile_obj)
        core_utils.switch_to_default_content()
        core_utils.switch_to_new_window()
        core_utils.switch_to_frame(frame_css = "iframe[class*='IBI_Report-iFrame']")
        chart.wait_for_visible_text("#jschart_HOLD_0", "Sale Year")
        
        chart.verify_x_axis_label_in_run_window(['2011', '2012', '2013', '2014', '2015', '2016'], msg = "Step 19.01 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_y_axis_label_in_run_window(['0', '30M', '60M', '90M', '120M', '150M'], msg = "Step 19.02 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_x_axis_title_in_run_window(['Sale Year'], msg = "Step 19.03 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_y_axis_title_in_run_window(['Gross Profit'], msg = "Step 19.04 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = "Step 19.05 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_number_of_risers("#jschart_HOLD_0 rect", 7, 6, msg = "Step 19.06 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.verify_chart_color("jschart_HOLD_0", "riser!s0!g5!mbar!", "bar_blue", msg = "Step 19.07 : Verify that 'Product Sales Analysis' HTML run in a new window without any error as below")
        chart.switch_to_default_content()
        utils.capture_screenshot("19.01", Step19, expected_image_verify = True)
        
        Step20 = """
            STEP 20 : Close the new window with "Product Sales Analysis" HTML.
        """
        core_utils.switch_to_previous_window(window_close = True)
        chart.switch_to_frame(frame_css = "iframe[class='ibx-iframe-frame'][src*='c6349658']")
        pd_design.wait_for_visible_text("div.pd-page-title", "Page")
        core_utils.switch_to_default_content()
        utils.capture_screenshot("20.01", Step20)
        
        Step21 = """
            STEP 21 : Close the output window.
        """
        main_page_run.close()
        pd_design.wait_for_visible_text("div.files-box-files", "C6349658")
        utils.capture_screenshot("21.01", Step21)
        
        Step22 = """
            STEP 22 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        utils.capture_screenshot("22.01", Step22)

if __name__ == '__main__':
    unittest.main()
    