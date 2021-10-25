"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 06-September-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.pages.charts import Pie, TreeMap, Bar, Scatter
from common.locators.designer import page_canvas as Locator
from common.wftools.designer import Designer as DesignerPage

class C9953162_TestClass(BaseTestCase):
    
    def test_C9953162(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        PieChart = Pie()
        BarChart = Bar() 
        ScatterChart = Scatter()
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
            STEP 03 : Right click on section and select Insert section below.
        """
        Designer.PageCanvas.Section.right_click(1)
        Designer.ContextMenu.select('Insert section below')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples > Portal > Small Widgets folder;
            Drag and drop Category Sales report onto the Section 1.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_path)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Drag and drop Discount by Region report onto the Section 2.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section('Discount by Region', section_index=2)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Multi select both the containers.
            Right click on Category Sales container in Section 1.
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
            STEP 07 : Select Combine > Tab.
        """
        Designer.ContextMenu.select('Combine->Tab')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify combined tab container is in Section 1.
        """
        Designer.PageCanvas.Containers.Tab('Container 3').verify_tabs_title(['Category Sales', 'Discount by Region'], '07.01')
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 3').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '07.02')
        PieChart.verify_legend_title(['Product Category'], '07.03')
        PieChart.verify_number_of_risers(7, '07.04')
        PieChart.verify_total_lables(['1.1B'], '07.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '07.06')
        PieChart.verify_pie_labels(['Revenue'], '07.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 3').select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 3').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '07.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '07.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '07.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '07.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '07.12')
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 3'], 1, '07.13')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Drag and drop Regional Profit by Category report onto the Section 2.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section('Regional Profit by Category', section_index=2)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Multi select both the containers.
            Right click on Regional Profit by Category container in Section 2.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Container 3', 'Regional Profit by Category'])
        Designer.PageCanvas.Containers.Basic('Regional Profit by Category').ToolBar.right_click()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Select Combine > Tab.
        """
        Designer.ContextMenu.select('Combine->Tab')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify combined tab container is in Section 2.
        """
        Designer.PageCanvas.Containers.Tab('Container 5').verify_tabs_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '10.01')
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.02')
        PieChart.verify_legend_title(['Product Category'], '10.03')
        PieChart.verify_number_of_risers(7, '10.04')
        PieChart.verify_total_lables(['1.1B'], '10.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '10.06')
        PieChart.verify_pie_labels(['Revenue'], '10.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 5').select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '10.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '10.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '10.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '10.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '10.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart
        Designer.PageCanvas.Containers.Tab('Container 5').select('Regional Profit by Category')
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '10.13')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '10.14')
        BarChart.verify_yaxis_title(['Gross Profit'], '10.15')
        BarChart.verify_number_of_risers(28, '10.16')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '10.17')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 5'], 2, '10.18')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on Container side tab.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Double click on Panel group to add it to the Section 1.
        """
        Designer.ResourcesPanel.Containers.double_click('Panel group')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click Content side tab
            Drag and drop Average Cost v Sales onto the panel group.
        """
        Designer.SideBar.Content.click()
        Designer.ResourcesPanel.Content.drag_to_page_section('Average Cost v Sales', 1, section_location='middle_left', x=20, y=0) 
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Multi select Average Cost v Sales and tab container in Section 2.
            Right click on Average Cost v Sales container.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Average Cost v Sales', 'Container 5'])
        Designer.PageCanvas.Containers.Basic('Average Cost v Sales').ToolBar.right_click()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Select Combine > Tab.
        """
        Designer.ContextMenu.select('Combine->Tab')
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify combined tab container is in panel group in Section 1.
        """
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 8').switch_to_frame()
        ScatterChart.wait_for_text('Revenue', 120) 
        ScatterChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '15.01')
        ScatterChart.verify_yaxis_title(['Gross Profit'], '15.02')
        ScatterChart.verify_xaxis_title(['Revenue'], '15.03')
        ScatterChart.verify_number_of_risers(21, '15.04')
        ScatterChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_yellow')], '15.05')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Tab('Container 8').click_overflow_icon()
        Designer.ContextMenu.select('Category Sales')
        # verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 8').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '15.06')
        PieChart.verify_number_of_risers(7, '15.07')
        PieChart.verify_total_lables(['1.1B'], '15.8')
        PieChart.verify_riser_color([(1, 'bar_blue')], '15.9')
        PieChart.verify_pie_labels(['Revenue'], '15.10')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart
        Designer.PageCanvas.Containers.Tab('Container 8').click_overflow_icon()
        Designer.ContextMenu.select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 8').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '15.11')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '15.12')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North Am...', 'Oceania', 'South Am...'], '15.13', label_len=7)
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '15.14')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '15.15')
        Designer._core_utils.switch_to_default_content()
        # Verifying fourth tab container chart
        Designer.PageCanvas.Containers.Tab('Container 8').click_overflow_icon()
        Designer.ContextMenu.select('Regional Profit by Category')
        Designer.PageCanvas.Containers.Tab('Container 8').switch_to_frame()
        BarChart.wait_for_text('Gross', 120)
        BarChart.verify_yaxis_labels(['0', '60M', '120M'], '15.16')
        BarChart.verify_yaxis_title(['Gross Profit'], '15.17')
        BarChart.verify_number_of_risers(28, '15.18')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '15.19')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 8'], 1, '15.20')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click Undo icon.
        """
        Designer.ToolBar.Undo.click()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify combined tab containers are restored back.
        """
        # verifying first container chart in section 1
        Designer.PageCanvas.Containers.Basic('Average Cost v Sales').switch_to_frame()
        ScatterChart.wait_for_text('Revenue', 120) 
        ScatterChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '16.01')
        ScatterChart.verify_yaxis_title(['Gross Profit'], '16.02')
        ScatterChart.verify_xaxis_title(['Revenue'], '16.03')
        ScatterChart.verify_number_of_risers(21, '16.04')
        ScatterChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_yellow')], '16.05')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Average Cost v Sales'], 1, '16.06')
        Designer.PageCanvas.Containers.Tab('Container 5').verify_tabs_title(['Category Sales', 'Discount by Region', 'Regional Profit by Category'], '16.07')
        # verifying seco tab container chart in section 2
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.08')
        PieChart.verify_legend_title(['Product Category'], '16.09')
        PieChart.verify_number_of_risers(7, '16.10')
        PieChart.verify_total_lables(['1.1B'], '16.11')
        PieChart.verify_riser_color([(1, 'bar_blue')], '16.12')
        PieChart.verify_pie_labels(['Revenue'], '16.13')
        Designer._core_utils.switch_to_default_content()
        # Verifying second tab container chart in section 2
        Designer.PageCanvas.Containers.Tab('Container 5').select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '16.14')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '16.15')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '16.16')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '16.17')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '16.18')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart in seciton 2
        Designer.PageCanvas.Containers.Tab('Container 5').select('Regional Profit by Category')
        Designer.PageCanvas.Containers.Tab('Container 5').switch_to_frame()
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.19')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '16.20')
        BarChart.verify_yaxis_title(['Gross Profit'], '16.21')
        BarChart.verify_number_of_risers(28, '16.22')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '16.23')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 5'], 2, '16.24')
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Multi select Average Cost v Sales and tab container in Section 2.
            Right click on tab container in Section 2.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Average Cost v Sales', 'Container 5'])
        Designer.PageCanvas.Containers.Tab('Container 5').ToolBar.right_click()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Select Combine > Tab.
        """
        Designer.ContextMenu.select('Combine->Tab')
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify combined container is in Section 2.
        """
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        ScatterChart.wait_for_text('Revenue', 120) 
        ScatterChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '18.01')
        ScatterChart.verify_yaxis_title(['Gross Profit'], '18.02')
        ScatterChart.verify_xaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M'], '18.03')
        ScatterChart.verify_xaxis_title(['Revenue'], '18.04')
        ScatterChart.verify_number_of_risers(21, '18.05')
        ScatterChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_yellow')], '18.06')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Category Sales')
        # verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '18.07')
        PieChart.verify_legend_title(['Product Category'], '18.08')
        PieChart.verify_number_of_risers(7, '18.09')
        PieChart.verify_total_lables(['1.1B'], '18.10')
        PieChart.verify_riser_color([(1, 'bar_blue')], '18.11')
        PieChart.verify_pie_labels(['Revenue'], '18.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '18.13')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '18.14')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '18.15')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '18.16')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '18.17')
        Designer._core_utils.switch_to_default_content()
        # Verifying fourth tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Regional Profit by Category')
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '18.18')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '18.19')
        BarChart.verify_yaxis_title(['Gross Profit'], '18.20')
        BarChart.verify_number_of_risers(28, '18.21')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '18.22')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 9'], 2, '18.23')
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Click 'Save' icon from toolbar and Enter 'C9953162' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9953162')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Logout WF using API without saving:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Run designer using API:
    
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P452_S31923/G879774&BIP_item=c9953162
        """
        Designer.API.run_page('C9953162', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify tab container is visible in the Section 2.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        # verifying first tab container chart
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        ScatterChart.wait_for_text('Revenue', 120) 
        ScatterChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '21.01')
        ScatterChart.verify_yaxis_title(['Gross Profit'], '21.02')
        ScatterChart.verify_xaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M'], '21.03')
        ScatterChart.verify_xaxis_title(['Revenue'], '21.04')
        ScatterChart.verify_number_of_risers(21, '21.05')
        ScatterChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_yellow')], '21.06')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').select('Category Sales')
        # verifying second tab container chart
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '21.07')
        PieChart.verify_legend_title(['Product Category'], '21.08')
        PieChart.verify_number_of_risers(7, '21.09')
        PieChart.verify_total_lables(['1.1B'], '21.10')
        PieChart.verify_riser_color([(1, 'bar_blue')], '21.11')
        PieChart.verify_pie_labels(['Revenue'], '21.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').select('Discount by Region')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '21.13')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '21.14')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '21.15')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '21.16')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '21.17')
        Designer._core_utils.switch_to_default_content()
        # Verifying fourth tab container chart
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').select('Regional Profit by Category')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '21.18')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '21.19')
        BarChart.verify_yaxis_title(['Gross Profit'], '21.20')
        BarChart.verify_number_of_risers(28, '21.21')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '21.22')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Section.verify_containers_in_section(['Container 9'], 2, '21.23')
        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_23 = """
            STEP 23 : Edit the saved page
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G879774/c9953162&startlocation=IBFS:/WFC/Repository/P452_S31923/G879774
        """
        Designer.API.edit_page('C9953162', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("23", STEP_23)

        STEP_23_EXPECTED = """
            STEP 23 - Expected : Verify tab container is visible in the Section 2.
        """
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        ScatterChart.wait_for_text('Revenue', 120) 
        ScatterChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M'], '23.01')
        ScatterChart.verify_yaxis_title(['Gross Profit'], '23.02')
        ScatterChart.verify_xaxis_labels(['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M'], '23.03')
        ScatterChart.verify_xaxis_title(['Revenue'], '23.04')
        ScatterChart.verify_number_of_risers(21, '23.05')
        ScatterChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_yellow')], '23.06')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Category Sales')
        # verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '23.07')
        PieChart.verify_legend_title(['Product Category'], '23.08')
        PieChart.verify_number_of_risers(7, '23.09')
        PieChart.verify_total_lables(['1.1B'], '23.10')
        PieChart.verify_riser_color([(1, 'bar_blue')], '23.11')
        PieChart.verify_pie_labels(['Revenue'], '23.12')
        Designer._core_utils.switch_to_default_content()
        # Verifying third tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '23.13')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '23.14')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '23.15')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '23.16')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '23.17')
        Designer._core_utils.switch_to_default_content()
        # Verifying fourth tab container chart
        Designer.PageCanvas.Containers.Tab('Container 9').click_overflow_icon()
        Designer.ContextMenu.select('Regional Profit by Category')
        Designer.PageCanvas.Containers.Tab('Container 9').switch_to_frame()
        BarChart.wait_for_text('Accessories', 120)
        BarChart.verify_xaxis_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '23.18')
        BarChart.verify_yaxis_labels(['0', '20M', '40M', '60M', '80M', '100M'], '23.19')
        BarChart.verify_yaxis_title(['Gross Profit'], '23.20')
        BarChart.verify_number_of_risers(28, '23.21')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'pale_green')], '23.22')
        Designer._utils.switch_to_default_content()
        Designer.PageCanvas.Section.verify_containers_in_section(['Container 9'], 2, '23.23')
        Designer._utils.capture_screenshot("23 - Expected", STEP_23_EXPECTED, True)

        STEP_24 = """
            STEP 24 : Logout WF using API without:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("24", STEP_24)