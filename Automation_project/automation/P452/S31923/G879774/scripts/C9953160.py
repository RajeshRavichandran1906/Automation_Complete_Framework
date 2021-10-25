"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 02-September-2021
-------------------------------------------------------------------------------------------"""
from common.locators.charts import common
from common.pages.charts import HtmlContent, Bar
from common.lib.basetestcase import BaseTestCase
from common.locators.designer import page_canvas as Locator
from common.wftools.designer import Designer as DesignerPage

class C9953160_TestClass(BaseTestCase):
    
    def test_C9953160(self):
        
        """
        TEST CASE OBJECTS
        """
        BarChart = Bar()
        BarChartInsight = Bar(parent_locator=common.insight_chart)
        Designer = DesignerPage()
        HtmlContentchart = HtmlContent()
        
        """
        TEST CASE VAIABLES
        """
        content_path = "G879774->P452_S31923->Retail Samples->Portal->Test Widgets->Blue"
        content_path_2 = "Test Widgets->Portal->Charts->Insight - Stacked bar monthly revenue for year"
        insight_icon = "rect[class*='annotation']"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G879774&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G879774&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the 'Blank' template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples > Portal > Test Widgets folder;
            Drag and drop Blue report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_path)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag and drop Gray report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_container('Gray', 'Blue', container_location='top_right', x=80, y=10)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Multi select both the containers.
            Right click on Blue container.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Blue', 'Gray'])
        Designer.PageCanvas.Containers.Basic('Blue').ToolBar.right_click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Combine context menu is available.
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Duplicate Container', 'Combine', 'Delete Container'], '06')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Select Combine > Carousel.
        """
        Designer.ContextMenu.select('Combine->Carousel')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify containers are combined into a Carousel container.
        """
        Designer.PageCanvas.Containers.Carousel('Container 3').verify_no_of_sliders(2, '06.01')
        Designer.PageCanvas.Containers.Carousel('Container 3').click_on_slide_pin(1)
        Designer.PageCanvas.Containers.Carousel('Container 3').switch_to_frame(1)
        HtmlContentchart.verify_content_background('blue', '06.02')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Carousel('Container 3').click_on_slide_pin(2)
        Designer.PageCanvas.Containers.Carousel('Container 3').switch_to_frame(2)
        HtmlContentchart.verify_content_background('dim_gray1', '06.04')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Navigate to Retail Samples > Charts folder.
            Drag and drop 'Insight - Stacked bar monthly revenue for year' report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_path_2, 'Container 3', container_location='top_right', x=80, y=10)
        Designer._utils.wait_for_page_loads(60)
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Multi select containers and right click and select Combine > Carousel.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Container 3', 'Insight - Stacked bar monthly revenue for year'])
        Designer.PageCanvas.Containers.Accordion('Container 3').ToolBar.right_click()
        Designer.ContextMenu.select('Combine->Carousel')
        Designer._utils.wait_for_page_loads(60)
        Designer._utils.capture_screenshot("08", STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify containers are combined into a Carousel container.
        """
        Designer.PageCanvas.Containers.Carousel('Container 5').verify_no_of_sliders(3, '08.01')
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(1)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(1)
        HtmlContentchart.verify_content_background('blue', '08.02')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(2)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(2)
        HtmlContentchart.verify_content_background('dim_gray1', '08.03')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(3)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(3)
        BarChart.wait_for_text('Product', 60)
        BarChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '08.04')
        BarChart.verify_xaxis_title(['Sale Month'], '08.05')
        BarChart.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '08.06')
        BarChart.verify_yaxis_title(['Revenue'], '08.07')
        BarChart.verify_number_of_risers(84, '08.08')
        BarChart.verify_legend_title(['Product Category'], '08.09')
        BarChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '08.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '08.11')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click the 'Run in New window' icon.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify combined carousel container is visible without error.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').verify_no_of_sliders(3, '09.01')
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(1)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(1)
        HtmlContentchart.verify_content_background('blue', '09.02')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(2)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(2)
        HtmlContentchart.verify_content_background('dim_gray1', '09.03')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(3)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(3)
        BarChart.wait_for_text('Product', 60)
        BarChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '09.04')
        BarChart.verify_xaxis_title(['Sale Month'], '09.05')
        BarChart.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '09.06')
        BarChart.verify_yaxis_title(['Revenue'], '09.07')
        BarChart.verify_number_of_risers(84, '09.08')
        BarChart.verify_legend_title(['Product Category'], '09.09')
        BarChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '09.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '09.11')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Select third slide;
            Click on Explore with Insight icon.
        """
        Designer._core_utils.python_left_click(Designer._utils.validate_and_get_webdriver_object(insight_icon, 'Insight icon'))
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Insight window opens in new tab.
        """
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        BarChartInsight.wait_for_text('Revenue', 180)
        BarChartInsight.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '10.01')
        BarChartInsight.verify_xaxis_title(['Sale Month'], '10.02')
        BarChartInsight.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '10.03')
        BarChartInsight.verify_yaxis_title(['Revenue'], '10.04')
        BarChartInsight.verify_number_of_risers(84, '10.05')
        BarChartInsight.verify_legend_title(['Product Category'], '10.06')
        BarChartInsight.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.07')
        BarChartInsight.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '10.08')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the Insight tab.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click 'Save' icon from toolbar and Enter 'C9953160' in title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9953160')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Run designer using API:
    
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P452_S31923/G879774&BIP_item=c9953160
        """
        Designer.API.run_page('C9953160', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify combined carousel container is visible without error.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').verify_no_of_sliders(3, '15.01')
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(1)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(1)
        HtmlContentchart.verify_content_background('blue', '15.02')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(2)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(2)
        HtmlContentchart.verify_content_background('dim_gray1', '15.03')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(3)
        Designer.RunMode.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(3)
        BarChart.wait_for_text('Product', 60)
        BarChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '15.04')
        BarChart.verify_xaxis_title(['Sale Month'], '15.05')
        BarChart.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '15.06')
        BarChart.verify_yaxis_title(['Revenue'], '15.07')
        BarChart.verify_number_of_risers(84, '15.08')
        BarChart.verify_legend_title(['Product Category'], '15.09')
        BarChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '15.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '15.11')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Select third slide;
            Click on Explore with Insight icon.
        """
        Designer._core_utils.python_left_click(Designer._utils.validate_and_get_webdriver_object(insight_icon, 'Insight icon'))
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify Insight window opens in new tab.
        """
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        BarChartInsight.wait_for_text('Revenue', 180)
        BarChartInsight.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '16.01')
        BarChartInsight.verify_xaxis_title(['Sale Month'], '16.02')
        BarChartInsight.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '16.03')
        BarChartInsight.verify_yaxis_title(['Revenue'], '16.04')
        BarChartInsight.verify_number_of_risers(84, '16.05')
        BarChartInsight.verify_legend_title(['Product Category'], '16.06')
        BarChartInsight.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.07')
        BarChartInsight.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '16.08')
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Close the Insight tab.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Edit the saved page
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G879774/c9953160&startlocation=IBFS:/WFC/Repository/P452_S31923/G879774
        """
        Designer.API.edit_page('C9953160', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify content in combined containers are visible without error.
        """
        Designer.PageCanvas.Containers.Carousel('Container 5').verify_no_of_sliders(3, '19.01')
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(1)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(1)
        HtmlContentchart.verify_content_background('blue', '19.02')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(2)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(2)
        HtmlContentchart.verify_content_background('dim_gray1', '19.03')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Carousel('Container 5').click_on_slide_pin(3)
        Designer.PageCanvas.Containers.Carousel('Container 5').switch_to_frame(3)
        BarChart.wait_for_text('Product', 60)
        BarChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '19.04')
        BarChart.verify_xaxis_title(['Sale Month'], '19.05')
        BarChart.verify_yaxis_labels(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M'], '19.06')
        BarChart.verify_yaxis_title(['Revenue'], '19.07')
        BarChart.verify_number_of_risers(84, '19.08')
        BarChart.verify_legend_title(['Product Category'], '19.09')
        BarChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '19.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '19.11')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("20", STEP_20)

