"""-------------------------------------------------------------------------------------------
Author Name  : RAJESH RAVICHANDRAN
Automated On : 25-August-2021
-------------------------------------------------------------------------------------------"""
import time
from common.pages.charts import Pie, Line, TreeMap
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer import page_canvas as Locator

class C9950426_TestClass(BaseTestCase):
    
    def test_C9950426(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        PieChart = Pie()
        LineChart = Line()
        TreeMapChart = TreeMap()
        
        """
        TEST CASE VAIABLES
        """
        content_path = "Retail Samples->Portal->Small Widgets->Category Sales"
        
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G879357&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G879357&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the 'Workbench' template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Workbench')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Right click on 'Report Output' and Select 'convert' > Select 'Carousel' option.
        """
        Designer.PageCanvas.Containers.Tab('Output').ToolBar.right_click()
        Designer.ContextMenu.select('Convert to->Carousel')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click the 'Run in New window' icon.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Navigate to Retail Samples > Portal > Small Widgets folder and Double click 'Category Sales'.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.wait_for_page_loads(30)
        Designer.RunMode.PageCanvas.Containers.Basic("Output").switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the Report Output tab in Run window.
        """
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '05.01')
        PieChart.verify_legend_title(['Product Category'], '05.02')
        PieChart.verify_number_of_risers(7, '05.03')
        PieChart.verify_total_lables(['1.1B'], '05.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '05.05')
        PieChart.verify_pie_labels(['Revenue'], '05.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click 'Regional Sales Trend' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Regional Sales Trend')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the following Context Menu.
        """
        Designer.ContextMenu.verify_options(['Run', 'Run In New Slide'], '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'Run' options from Context menu.
        """
        Designer.ContextMenu.select('Run')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the Report Output tab in Run window.
        """
        Designer.RunMode.PageCanvas.Containers.Basic("Output").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '07.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '07.02')
        LineChart.verify_xaxis_title(['Month'], '07.03')
        LineChart.verify_yaxis_title(['Revenue'], '07.04')
        LineChart.verify_number_of_risers(4, '07.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '07.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click 'Discount by Region' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Discount by Region')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click 'Run in New slide' from Context menu.
        """
        Designer.ContextMenu.select('Run In New Slide')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check the Report Output tab in Run window.
        """
        time.sleep(30)
        Designer.RunMode.PageCanvas.Containers.Carousel('Output').switch_to_frame(2)
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '09.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '09.02')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '09.03')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '09.04')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '09.05')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on 'Container' options.
        """
        Designer.RunMode.PageCanvas.Containers.Carousel('Output').ToolBar.Options.click()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check the 'Delete Slide' option is available.
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Delete slide'], '10')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on 'Delete Slide' option.
        """
        Designer.ContextMenu.select('Delete slide')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Check the Report Output tab in Run window.
        """
        Designer.RunMode.PageCanvas.Containers.Basic("Output").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '11.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '11.02')
        LineChart.verify_xaxis_title(['Month'], '11.03')
        LineChart.verify_yaxis_title(['Revenue'], '11.04')
        LineChart.verify_number_of_risers(4, '11.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '11.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the Run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click 'Save' icon from toolbar and Enter 'C9950426' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9950426')
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
    
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P452_S31923/G879357&BIP_item=c9950426
        """
        Designer.API.run_page('c9950426', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Navigate to Retail Samples > Portal > Small Widgets folder and Double click 'Category Sales'.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.wait_for_page_loads(30)
        Designer.RunMode.PageCanvas.Containers.Carousel("Output").switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Check the Report Output tab in Run window.
        """
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '16.01')
        PieChart.verify_legend_title(['Product Category'], '16.02')
        PieChart.verify_number_of_risers(7, '16.03')
        PieChart.verify_total_lables(['1.1B'], '16.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '16.05')
        PieChart.verify_pie_labels(['Revenue'], '16.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Right click 'Regional Sales Trend' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Regional Sales Trend')
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Check the following Context Menu.
        """
        Designer.ContextMenu.verify_options(['Run', 'Run In New Slide'], '14')
        Designer._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click 'Run' options from Context menu.
        """
        Designer.ContextMenu.select('Run')
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Check the Report Output tab in Run window.
        """
        Designer.RunMode.PageCanvas.Containers.Carousel("Output").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '18.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '18.02')
        LineChart.verify_xaxis_title(['Month'], '18.03')
        LineChart.verify_yaxis_title(['Revenue'], '18.04')
        LineChart.verify_number_of_risers(4, '18.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '18.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Right click 'Discount by Region' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Discount by Region')
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Click 'Run in New slide' from Context menu.
        """
        Designer.ContextMenu.select('Run In New Slide')  
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Check the Report Output tab in Run window.
        """
        time.sleep(30)
        Designer.RunMode.PageCanvas.Containers.Carousel('Output').switch_to_frame(2)
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '20.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '20.02')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '20.03')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '20.04')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '20.05')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Click on 'Container' options.
        """
        Designer.RunMode.PageCanvas.Containers.Carousel('Output').ToolBar.Options.click()
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Check the 'Delete Slide' option is available.
        """
        Designer.ContextMenu.verify_options(['Refresh', 'Delete slide'], '21')
        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Click on 'Delete Slide' option.
        """
        Designer.ContextMenu.select('Delete slide')
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Check the Report Output tab in Run window.
        """
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Basic("Output").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '22.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '22.02')
        LineChart.verify_xaxis_title(['Month'], '22.03')
        LineChart.verify_yaxis_title(['Revenue'], '22.04')
        LineChart.verify_number_of_risers(4, '22.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '22.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("23", STEP_23)

