"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 14-December-2020
-------------------------------------------------------------------------------------------"""

from common.pages.charts import Bar
from common.wftools.reports import Reports
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9947191_TestClass(BaseTestCase):
    
    def test_C9947191(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        HtmlReport = Reports().HTML5()
        BarChart = Bar()
        
        """
        TEST CASE VAIABLES
        """
        file_name = 'C9947191'
        content_name = 'drill_with_procedure'
        container2 = 'Container 2'
        data_set = file_name  +"_DataSet01"
        
        STEP_01 = """
            STEP 01 : Login WF as domain developer
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G866552' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G866552')
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9947191')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Choose Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag 'drill_with_procedure' onto the Container 1.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name, 'Container 1')
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Select Container 2 content;
            Type 'TestDrill' in the Classes textbox under Content properties.
        """
        Designer.PageCanvas.Containers.Basic(container2).select()
        Designer.PropertiesPanel.Settings.ContainerSettings.Classes.enter_text('TestDrill')
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on Run in new window icon in the toolbar;
            Click on JAPAN in 'drill_with_procedure' panel.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text(container2)
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        HtmlReport.wait_for_text('SALES')
        #HtmlReport.convert_to_excel(data_set)
        HtmlReport.verify_data(data_set, '06.01')
        HtmlReport.click_on_hyperlink_cell(5, 1)
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Container 2 updated with the drill_to procedure and only JAPAN values are visible.
        """
        Designer.RunMode.PageCanvas.Containers.Basic(container2).switch_to_frame()
        BarChart.wait_for_text('CAR')
        BarChart.verify_xaxis_title(['CAR'], '06.01')
        BarChart.verify_yaxis_title(['DEALER_COST'], '06.02')
        BarChart.verify_xaxis_labels(['DATSUN', 'TOYOTA'], '06.03')
        BarChart.verify_yaxis_labels(['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500'], '06.04')
        BarChart.verify_number_of_risers(2, '06.05')
        BarChart.verify_riser_color([(1, 'bar_blue'), (2, 'bar_blue')], '06.06')
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the run window.
        """
        Designer._core_utils.switch_to_default_content()
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click Save and enter C9947191 in Title and click Save;
            Close the designer.
        """
        Designer.ToolBar.save(file_name)
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Right click on 'C9947191' and select Run.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on ITALY in 'drill_with_procedure' panel.
        """
        Designer.RunMode.PageCanvas.wait_for_text(container2)
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        HtmlReport.wait_for_text('SALES')
        HtmlReport.click_on_hyperlink_cell(4, 1)
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Container 2 updated with the drill_to procedure and only ITALY values are visible.
        """
        Designer.RunMode.PageCanvas.Containers.Basic(container2).switch_to_frame()
        BarChart.wait_for_text('28K')
        BarChart.verify_xaxis_title(['CAR'], '10.01')
        BarChart.verify_yaxis_title(['DEALER_COST'], '10.02')
        BarChart.verify_xaxis_labels(['ALFA ROMEO', 'MASERATI'], '10.03')
        BarChart.verify_yaxis_labels(['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K'], '10.04')
        BarChart.verify_number_of_risers(2, '10.05')
        BarChart.verify_riser_color([(1, 'bar_blue'), (2, 'bar_blue')], '10.06')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on W GERMANY in 'drill_with_procedure' panel.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        HtmlReport.click_on_hyperlink_cell(6, 1)
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify only W GERMANY values are visible in panel 2.
        """
        Designer.RunMode.PageCanvas.Containers.Basic(container2).switch_to_frame()
        BarChart.wait_for_text('60K')
        BarChart.verify_xaxis_title(['CAR'], '11.01')
        BarChart.verify_yaxis_title(['DEALER_COST'], '11.02')
        BarChart.verify_xaxis_labels(['AUDI', 'BMW'], '11.03')
        BarChart.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '11.04')
        BarChart.verify_number_of_risers(2, '11.05')
        BarChart.verify_riser_color([(1, 'bar_blue'), (2, 'bar_blue')], '11.06')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)