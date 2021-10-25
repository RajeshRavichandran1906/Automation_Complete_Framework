"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 01-September-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.pages.charts import Pie, TreeMap, Bar
from common.wftools.designer import Designer as DesignerPage

class C9953158_TestClass(BaseTestCase):
    
    def test_C9953158(self):
        
        """
        TEST CASE OBJECTS
        """
        PieChart = Pie()
        BarChart = Bar() 
        Designer = DesignerPage()
        TreeMapChart = TreeMap()
    
        """
        TEST CASE VAIABLES
        """
        content_path = "G879774->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales"
        
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
            STEP 03 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples > Portal > Small Widgets folder;
            Drag and drop Category Sales report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_path)
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag and drop Discount by Region report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_container('Discount by Region', 'Category Sales', container_location='top_right', x=80, y=10)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on Filters side tab;
            Click Add all filters to page button.
        """
        Designer.SideBar.Filters.click()
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Multi select both the containers.
            Right click on Category Sales container.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Category Sales', 'Discount by Region'])
        Designer.PageCanvas.Containers.Basic('Category Sales').ToolBar.right_click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Combine context menu is available.
        """ 
        Designer.ContextMenu.verify_options(['Refresh', 'Duplicate Container', 'Combine', 'Delete Container'], '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Select Combine > Accordion.
        """
        Designer.ContextMenu.select('Combine->Accordion')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify containers are combined into a Accordion container.
        """
        Designer.PageCanvas.Containers.Accordion('Container 3').verify_areas_title(['Category Sales', 'Discount by Region'], '07.01')
        Designer.PageCanvas.Containers.Accordion('Container 3').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '07.02')
        PieChart.verify_legend_title(['Product Category'], '07.03')
        PieChart.verify_number_of_risers(7, '07.04')
        PieChart.verify_total_lables(['1.1B'], '07.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '07.06')
        PieChart.verify_pie_labels(['Revenue'], '07.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.PageCanvas.Containers.Accordion('Container 3').expand_area('Discount by Region')
        Designer.PageCanvas.Containers.Accordion('Container 3').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '07.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '07.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '07.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '07.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '07.12')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on Content side tab;
            Drag and drop Regional Profit by Category report onto the page canvas.
        """
        Designer.SideBar.Content.click()
        Designer.ResourcesPanel.Content.drag_to_container('Regional Profit by Category', 'Container 3', container_location='top_right', x=80, y=10)
        Designer._utils.wait_for_page_loads(60)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Multi select containers and right click and select Combine > Accordion.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Container 3', 'Regional Profit by Category'])
        Designer.PageCanvas.Containers.Accordion('Container 3').ToolBar.right_click()
        Designer.ContextMenu.select('Combine->Accordion')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify containers are combined into a Accordion.
        """
        Designer.PageCanvas.Containers.Accordion('Container 5').verify_areas_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '09.01')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '07.02')
        PieChart.verify_legend_title(['Product Category'], '07.03')
        PieChart.verify_number_of_risers(7, '07.04')
        PieChart.verify_total_lables(['1.1B'], '07.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '07.06')
        PieChart.verify_pie_labels(['Revenue'], '07.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '07.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '07.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '07.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '07.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '07.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third Accordion container chart
        Designer.PageCanvas.Containers.Accordion('Container 5').expand_area('Regional Profit by Category')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Regional Profit by Category')
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '07.13')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '07.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '07.15')
        BarChart.verify_number_of_risers(28, '07.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '07.17')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        
        STEP_10 = """
            STEP 10 : Click the 'Run in New window' icon.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Category Sales content in combined container is visible without error.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer.RunMode.PageCanvas.wait_for_text('Page', 120)
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').verify_areas_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '10.01')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.02')
        PieChart.verify_legend_title(['Product Category'], '10.03')
        PieChart.verify_number_of_risers(7, '10.04')
        PieChart.verify_total_lables(['1.1B'], '10.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '10.06')
        PieChart.verify_pie_labels(['Revenue'], '10.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '10.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '10.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '10.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '10.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '10.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Regional Profit by Category')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Regional Profit by Category')
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.13')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '10.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '10.15')
        BarChart.verify_number_of_risers(28, '10.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '10.17')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Select Accessories and Camcorder in Category: filter control.
        """
        Designer.RunMode.PageCanvas.FilterGrid.Control('Category:').click(location='middle')
        Designer.RunMode.PageCanvas.FilterGrid.Dropdown.select('Accessories')
        Designer.RunMode.PageCanvas.FilterGrid.Dropdown.select('Camcorder')
        Designer.RunMode.PageCanvas.FilterGrid.Control('Category:').click()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify filter condition is applied in the Category Sales content.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Category Sales')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder'], '11.01')
        PieChart.verify_legend_title(['Product Category'], '11.02')
        PieChart.verify_number_of_risers(2, '11.03')
        PieChart.verify_total_lables(['284.1M'], '11.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '11.05')
        PieChart.verify_pie_labels(['Revenue'], '11.06')
        PieChart._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Select Discount by Region tab.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Discount by Region content in combined container is visible without error.
        """
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '12.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '12.02')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '12.03')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '12.04')
        TreeMapChart.verify_riser_color([(1, 'Cobalt'), (9, 'variety_blue')], '12.05')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click 'Save' icon from toolbar and Enter 'C9953158' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9953158')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Run designer using API:
    
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P452_S31923/G879774&BIP_item=c9953158
        """
        Designer.API.run_page('C9953158', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify page with combined container is visible.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer.RunMode.PageCanvas.wait_for_text('Page', 120)
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').verify_areas_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '16.01')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.02')
        PieChart.verify_legend_title(['Product Category'], '16.03')
        PieChart.verify_number_of_risers(7, '16.04')
        PieChart.verify_total_lables(['1.1B'], '16.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '16.06')
        PieChart.verify_pie_labels(['Revenue'], '16.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '16.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '16.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '16.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '16.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '16.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Regional Profit by Category')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Regional Profit by Category')
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.13')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '16.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '16.15')
        BarChart.verify_number_of_risers(28, '16.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '16.17')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Select North America in region filter control.
            Select Regional Profit by Category area.
        """
        Designer.RunMode.PageCanvas.FilterGrid.Control('Region:').click(location='middle')
        Designer.RunMode.PageCanvas.FilterGrid.Dropdown.select('North America')
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify filter condition is applied in the page.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').verify_areas_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '17.01')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Category Sales')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '17.02')
        PieChart.verify_legend_title(['Product Category'], '17.03')
        PieChart.verify_number_of_risers(7, '17.04')
        PieChart.verify_total_lables(['609.9M'], '17.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '17.06')
        PieChart.verify_pie_labels(['Revenue'], '17.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('North America', 120)
        TreeMapChart.verify_number_of_risers(4, '17.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '17.09')
        TreeMapChart.verify_yaxis_labels(['North America'], '17.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '17.11')
        TreeMapChart.verify_riser_color([(1, 'pattens_blue_2'), (4, 'variety_blue')], '17.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third Accordion container chart
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').expand_area('Regional Profit by Category')
        Designer.RunMode.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Regional Profit by Category')
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '17.13')
        BarChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '17.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '17.15')
        BarChart.verify_number_of_risers(7, '17.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (5, 'bar_blue')], '17.17')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Edit the saved page
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G879774/c9953158&startlocation=IBFS:/WFC/Repository/P452_S31923/G879774
        """
        Designer.API.edit_page('C9953158', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify content in combined containers are visible without error.
        """
        Designer.PageCanvas.Containers.Accordion('Container 5').verify_areas_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '19.01')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Category Sales')
        # verifying first Accordion container chart
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '19.02')
        PieChart.verify_legend_title(['Product Category'], '19.03')
        PieChart.verify_number_of_risers(7, '19.04')
        PieChart.verify_total_lables(['1.1B'], '19.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '19.06')
        PieChart.verify_pie_labels(['Revenue'], '19.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second Accordion container chart
        Designer.PageCanvas.Containers.Accordion('Container 5').expand_area('Discount by Region')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Discount by Region')
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '19.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '19.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '19.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '19.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '19.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third Accordion container chart
        Designer.PageCanvas.Containers.Accordion('Container 5').expand_area('Regional Profit by Category')
        Designer.PageCanvas.Containers.Accordion('Container 5').switch_to_frame('Regional Profit by Category')
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '19.13')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '19.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '19.15')
        BarChart.verify_number_of_risers(28, '19.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '19.17')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("20", STEP_20)

