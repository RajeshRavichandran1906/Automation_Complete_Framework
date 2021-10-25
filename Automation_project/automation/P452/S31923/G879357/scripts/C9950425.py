"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh Ravichandran
Automated On : 24-August-2021
-------------------------------------------------------------------------------------------"""
import time
from common.pages.charts import Pie, Line
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer import page_canvas as Locator

class C9950425_TestClass(BaseTestCase):
    
    def test_C9950425(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        PieChart = Pie()
        LineChart = Line()
         
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
            STEP 03 : Right click on 'Report Output' and Select 'convert' > Select 'Basic' option.
        """
        Designer.PageCanvas.Containers.Tab('Output').ToolBar.right_click()
        Designer.ContextMenu.select('Convert to->Basic')
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
        Designer.RunMode.PageCanvas.Containers.Basic("Category Sales").switch_to_frame()
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
        Designer.ContextMenu.verify_options(['Run'], '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'Run' options from Context menu.
        """
        Designer.ContextMenu.select('Run')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the Report Output tab in Run window.
        """
        time.sleep(30)
        Designer.RunMode.PageCanvas.Containers.Basic("Regional Sales Trend").switch_to_frame()
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
            STEP 08 : Click on 'Container' options.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Regional Sales Trend').ToolBar.Options.click()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check the 'Delete' option is not available.
        """
        Designer.ContextMenu.verify_options(['Delete'], '08', assert_type = 'notin')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close the Run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click 'Save' icon from toolbar and Enter 'C9950425' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9950425')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Run designer using API:
    
            https://machine.ibi.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P452_S31923/G879357&BIP_item=c9950425
        """
        Designer.API.run_page('c9950425', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Navigate to Retail Samples > Portal > Small Widgets folder and Double click 'Category Sales'.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.wait_for_page_loads(30)
        Designer.RunMode.PageCanvas.Containers.Basic("Category Sales").switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Check the Report Output tab in Run window.
        """
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '13.01')
        PieChart.verify_legend_title(['Product Category'], '13.02')
        PieChart.verify_number_of_risers(7, '13.03')
        PieChart.verify_total_lables(['1.1B'], '13.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '13.05')
        PieChart.verify_pie_labels(['Revenue'], '13.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Right click 'Regional Sales Trend' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Regional Sales Trend')
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Check the following Context Menu.
        """
        Designer.ContextMenu.verify_options(['Run'], '14')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click 'Run' options from Context menu.
        """
        Designer.ContextMenu.select('Run')
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Check the Report Output tab in Run window.
        """
        time.sleep(30)
        Designer.RunMode.PageCanvas.Containers.Basic("Regional Sales Trend").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '15.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '15.02')
        LineChart.verify_xaxis_title(['Month'], '15.03')
        LineChart.verify_yaxis_title(['Revenue'], '15.04')
        LineChart.verify_number_of_risers(4, '15.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '15.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on 'Container' options.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Regional Sales Trend').ToolBar.Options.click()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Check the 'Delete' option is not available.
        """
        Designer.ContextMenu.verify_options(['Delete'], '16', assert_type = 'notin')
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("17", STEP_17)

