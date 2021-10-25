"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 19-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer
from common.wftools.reports import Reports as Report


class C9927843_TestClass(BaseTestCase):
    
    def test_C9927843(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        DesignerPage = Designer()
        Html5Report = Report().HTML5()
        """
        TEST CASE VAIABLES
        """
        file_name = "C9927843"
        panel_title = "09 - Slider Optional Other"
        control_label = "Move Slider to 5011"
        data_set_01 =  file_name + '_DataSet01'
        data_set_02 =  file_name + '_DataSet02'
        
        STEP_01 = """
            STEP 01 : Login to WF as Developer.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        DesignerPage._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G784942' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G784942')
        HomePage.Workspaces._utils.wait_for_page_loads(20)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualizations")
        DesignerPage._core_utils.switch_to_new_window()
        DesignerPage._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Select Blank template.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage.Dialog.ChooseTemplate.Common.select("Blank")
        DesignerPage._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag '09 - Slider Optional Other' report into the page canvas from P398_S10799 > Reference Items folder.
        """
        DesignerPage.ResourcesPanel.Content.drag_to_page_section("G784942->P452_S31923->P398_S10799->Reference Items->09 - Slider Optional Other")
        DesignerPage._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify report added to the page successfully.
        """
        DesignerPage.PageCanvas.Containers.Basic().ToolBar.verify_title(panel_title, "04.01")
        DesignerPage.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        #Html5Report.convert_to_excel(data_set_01)
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '04.02')
        DesignerPage._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Filters side tab.
            Click Add all filters to page button.
        """
        DesignerPage._core_utils.switch_to_default_content()
        DesignerPage.SideBar.Filters.click()
        DesignerPage.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify slider control bounded to the page with blue border around it. Verify all values in Properties panel.
        """
        DesignerPage.PageCanvas.FilterGrid.wait_for_text(control_label)
        DesignerPage.PageCanvas.FilterGrid.verify_control_labels([control_label], "05.01")
        DesignerPage.PageCanvas.FilterGrid.Control(control_label).Slider.verify_values(['5008', '5000', '5020'], '05.02')
        DesignerPage.PageCanvas.FilterGrid.Control(control_label).verify_border_properties("05.03")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Type.verify_text("Slider", "05.04")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.ID.verify_contains_text("FILTERPANE", "05.05")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Classes.verify_text("", "05.06")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Tooltip.verify_text("", "05.07")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.GlobalName.verify_text("", "05.08")
        DesignerPage.PropertiesPanel.Settings.DataSettings.DefaultValue.verify_placeholder("5008", "05.09")
        DesignerPage.PropertiesPanel.Settings.Parameters.Parameters.verify_text("ID_PRODUCT (I9)", "05.10")
        DesignerPage._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Preview.
        """
        DesignerPage.VisualizationToolBar.RunInNewWindow.click()
        DesignerPage._core_utils.switch_to_new_window()
        DesignerPage._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify page loads successfully with slider control in preview.
        """
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_title, 60)
        DesignerPage.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '06.01')
        DesignerPage.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '06.02')
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(control_label).Slider.verify_values(["5008", "5000", "5020"], "06.03")
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '06.04')
        DesignerPage._core_utils.switch_to_default_content()
        DesignerPage._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Move slider pin to 5011 position.
        """
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(control_label).Slider.move_pin(5011)
        DesignerPage._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify slider condition applied in the page.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(control_label).Slider.verify_values(["5011", "5000", "5020"], "07.01")
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        #Html5Report.convert_to_excel(data_set_02)
        Html5Report.wait_for_text('5011')
        Html5Report.verify_data(data_set_02, '07.02')
        DesignerPage._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the preview.
        """
        DesignerPage._core_utils.switch_to_previous_window()
        DesignerPage._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Move slider pin to 5011 position in design mode.
        """
        DesignerPage.PageCanvas.FilterGrid.Control(control_label).Slider.move_pin(5011)
        DesignerPage._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify slider condition applied in the page.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage.PageCanvas.FilterGrid.Control(control_label).Slider.verify_values(["5011", "5000", "5020"], "09.01")
        DesignerPage.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        Html5Report.wait_for_text('5011')
        Html5Report.verify_data(data_set_02, '09.02')
        DesignerPage._core_utils.switch_to_default_content()
        DesignerPage._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Save and enter C9927843 in Title;
            Click Save button.
        """
        DesignerPage.ToolBar.save(file_name)
        DesignerPage._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Close the designer.
        """
        DesignerPage._core_utils.switch_to_previous_window()
        DesignerPage._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Run C9927843.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file("C9927843")
        HomePage.ContextMenu.select("Run")
        HomePage.RunWindow.wait_for_visible()
        DesignerPage._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify page runs successfully without error.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        HomePage.RunWindow.switch_to_frame()
        DesignerPage.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '12.01')
        DesignerPage.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '12.02')
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(control_label).Slider.verify_values(["5008", "5000", "5020"], "12.03")
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '12.04')
        DesignerPage._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close run window.
        """
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        DesignerPage._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Delete the created Page.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file('C9927843')
        DesignerPage._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Sign Out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        DesignerPage._utils.capture_screenshot("15", STEP_15)

