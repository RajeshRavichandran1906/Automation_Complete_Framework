"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 31-August-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.pages.charts import Pie, TreeMap
from common.locators.designer import page_canvas as Locator
from common.wftools.designer import Designer as DesignerPage

class C9953157_TestClass(BaseTestCase):
    
    def test_C9953157(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        PieChart = Pie()
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
            STEP 02 : Choose the 'Grid 2-1' template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples > Portal > Small Widgets folder;
            Drag and drop Category Sales report onto the Container 1.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_path, 'Container 1')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag and drop Discount by Region report onto the Container 2.
        """
        Designer.ResourcesPanel.Content.drag_to_container('Discount by Region', 'Container 2')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Multi select Category Sales and Discount by Region containers;
            Right click on Category Sales container.
        """
        Designer.PageCanvas.Containers.multi_select_containers(['Category Sales', 'Discount by Region'])
        Designer.PageCanvas.Containers.Basic('Category Sales').ToolBar.right_click()
        Designer._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Combine context menu is available.
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Duplicate Container', 'Combine', 'Delete Container'], '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Combine context menu.
        """
        Designer._utils.capture_screenshot("06", STEP_06)
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Tab, Accordion and Carousel options are available.
        """
        Designer.ContextMenu.verify_options(['Tab', 'Accordion', 'Carousel', 'Panel group'], '06', menu_path='Combine')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Select Tab in context menu.
        """
        Designer.ContextMenu.select('Combine->Tab')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify containers are combined into a Tab container.
        """
        Designer.PageCanvas.Containers.Tab('Container 1').verify_tabs_title(['Category Sales', 'Discount by Region'], '07.01')
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '07.02')
        PieChart.verify_legend_title(['Product Category'], '07.03')
        PieChart.verify_number_of_risers(7, '07.04')
        PieChart.verify_total_lables(['1.1B'], '07.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '07.06')
        PieChart.verify_pie_labels(['Revenue'], '07.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 1').select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '07.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '07.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '07.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '07.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '07.12')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click the 'Run in New window' icon.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Category Sales content in combined container is visible without error.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        PieChart.wait_for_text('Revenue', 180)
        # verifying first tab container chart
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '08.01')
        PieChart.verify_legend_title(['Product Category'], '08.02')
        PieChart.verify_number_of_risers(7, '08.03')
        PieChart.verify_total_lables(['1.1B'], '08.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '08.05')
        PieChart.verify_pie_labels(['Revenue'], '08.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Select Discount by Region tab.
        """
        Designer.RunMode.PageCanvas.Containers.Tab('Container 1').select('Discount by Region')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify Discount by Region content in combined container is visible without error.
        """
        Designer.RunMode.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '09.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '09.02')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '09.03')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '09.04')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '09.05')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click 'Save' icon from toolbar and Enter 'C9953157' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9953157')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Edit the saved page
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G879774/c9953157&startlocation=IBFS:/WFC/Repository/P452_S31923/G879774
        """
        Designer.API.edit_page('C9953157', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify content in combined containers are visible without error.
        """
        Designer.PageCanvas.Containers.Tab('Container 1').verify_tabs_title(['Category Sales', 'Discount by Region'], '13.01')
        # verifying first tab container chart
        Designer.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '13.02')
        PieChart.verify_legend_title(['Product Category'], '13.03')
        PieChart.verify_number_of_risers(7, '13.04')
        PieChart.verify_total_lables(['1.1B'], '13.05')
        PieChart.verify_riser_color([(1, 'bar_blue')], '13.06')
        PieChart.verify_pie_labels(['Revenue'], '13.07')
        Designer._core_utils.switch_to_default_content()
        # Verifying second tab container chart
        Designer.PageCanvas.Containers.Tab('Container 1').select('Discount by Region')
        Designer.PageCanvas.Containers.Tab('Container 1').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '13.08')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '13.09')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '13.10')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '13.11')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '13.12')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)