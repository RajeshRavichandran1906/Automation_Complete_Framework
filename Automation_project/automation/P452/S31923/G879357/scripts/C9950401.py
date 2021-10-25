"""-------------------------------------------------------------------------------------------
Author Name  : RAJESH RAVICHANDRAN
Automated On : 23-August-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.pages.charts import Pie, Line, TreeMap
from common.locators.designer import page_canvas as Locator

class C9950401_TestClass(BaseTestCase):
    
    def test_C9950401(self):
        
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

        STEP_01_EXPECTED = """
            STEP 01 - Expected : Verify Workbench template icon visible in COMMON in Choose Template dialog.
        """
        Designer.Dialog.ChooseTemplate.Common.verify(['Workbench'], '01', assert_type='in')
        Designer._utils.capture_screenshot("01 - Expected", STEP_01_EXPECTED, True)

        STEP_02 = """
            STEP 02 : Choose the 'Workbench' template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Workbench')  
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify 'Workspace container' and 'Report Output' tab.
        """
        Designer._utils.wait_for_page_loads(60)
        Designer.PageCanvas.Containers.verify_containers_title(['Workspace', 'Output'], '02')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click new tab
        """
        Designer.PageCanvas.Containers.Tab('Output').add_new_tab()
        Designer._utils.wait_for_page_loads(20)
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Verify tab name "Tab 1" and Tab 2" are displayed.
        """
        Designer.PageCanvas.Containers.Tab('Output').verify_tabs_title(['Tab 1', 'Tab 2'], "03")
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Click on option in Output container and select Delete Tab
        """
        Designer.PageCanvas.Containers.Tab('Output').right_click()
        Designer.ContextMenu.select('Delete Tab')
        Designer._utils.capture_screenshot("04", STEP_04)
        
        STEP_05 = """
            STEP 03 : Click the 'Run in New window' icon.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Double click 'Category Sales' from Retail Samples Workspace.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.double_click(content_path)
        Designer._utils.wait_for_page_loads(30)
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        PieChart.wait_for_text('Product Category', 120)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the Report Output tab in Run window.
        """
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '04.01')
        PieChart.verify_legend_title(['Product Category'], '04.02')
        PieChart.verify_number_of_risers(7, '04.03')
        PieChart.verify_total_lables(['1.1B'], '04.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '04.05')
        PieChart.verify_pie_labels(['Revenue'], '04.06')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click 'Regional Sales Trend' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Regional Sales Trend')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the following Context Menu.
        """
        Designer.ContextMenu.verify_options(['Run', 'Run In New Tab'], '05')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click 'Run' options from Context menu.
        """
        Designer.ContextMenu.select('Run')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check the Report Output tab in Run window.
        """
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        LineChart.wait_for_text('Month', 120)
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '06.01')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '06.02')
        LineChart.verify_xaxis_title(['Month'], '06.03')
        LineChart.verify_yaxis_title(['Revenue'], '06.04')
        LineChart.verify_number_of_risers(4, '06.05')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '06.06', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Right click 'Discount by Region' from Retail Samples Workspace.
        """
        Designer.RunMode.PageCanvas.Containers.Workspace('Workspace').Content.right_click('Discount by Region')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click 'Run in new tab' from Context menu.
        """
        Designer.ContextMenu.select('Run In New Tab')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check the Report Output tab in Run window.
        """
        time.sleep(30)
        Designer.RunMode.PageCanvas.Containers.Tab("Output").switch_to_frame()
        TreeMapChart.wait_for_text('Sale Quarter', 120)
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '08.01')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '08.02')
        TreeMapChart.verify_number_of_risers(16, '08.03')
        TreeMapChart.verify_riser_color([(10, 'French_Pass')], '08.04')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the Run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 10 : Click 'Container' from left side panel.
        """
        Designer.SideBar.Container.click()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 10 - Expected : Check the 'Workbench' template is not available in Container tab.
        """
        Designer.ResourcesPanel.Containers.verify_containers(['Workbench'], '10', assert_type='notin')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click 'Save' icon from toolbar and Enter 'C9950401' title text box > Click 'Save' button.
        """
        Designer.ToolBar.save('C9950401')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Edit the saved page
    
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G879357/c9950401&startlocation=IBFS:/WFC/Repository/P452_S31923/G879357
        """
        Designer.API.edit_page('C9950401', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify 'Workspace container' and 'Report Output' tab.
        """
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.PageCanvas.Containers.verify_containers_title(['Workspace', 'Output'], '13')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Logout WF using API without saving:
    
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)

