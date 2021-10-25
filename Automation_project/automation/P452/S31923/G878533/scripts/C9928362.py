"""-------------------------------------------------------------------------------------------
Author Name  : BM13368
Automated On : 10-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer
from common.wftools.reports import Reports as Report

class C9928362_TestClass(BaseTestCase):
    
    def test_C9928362(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        DesignerPage = Designer()
        Html5Report = Report().HTML5()
        
        """
        TEST CASE VAIABLES
        """
        file_name="C9928362"
        panel_title ="11 - Slider Range Optional"
        data_set_01 =  file_name + '_DataSet01'
        data_set_02 =  file_name + '_DataSet02'
        slider_label = "Move Slider"
        
        STEP_01 = """
            STEP 01 : Login to WF as Developer.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G784942' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G784942')
        HomePage.Workspaces._utils.wait_for_page_loads(20)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualization")
        HomePage.Home._core_utils.switch_to_new_window("Designer")
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Select Blank template.
        """
        DesignerPage._utils.wait_for_page_loads(30)
        DesignerPage.Dialog.ChooseTemplate.Common.select("Blank")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag '11 - Slider Range Optional' report into the page canvas from P398_S10799 > Reference Items folder.
        """
        DesignerPage.ResourcesPanel.Content.drag_to_page_section("G784942->P452_S31923->P398_S10799->Reference Items->11 - Slider Range Optional")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify report added to the page successfully.
        """
        DesignerPage.PageCanvas.Containers.Basic(panel_title).ToolBar.verify_title(panel_title, "04.01")
        DesignerPage.PageCanvas.Containers.Basic(panel_title).ToolBar.verify_title(panel_title, "04.02")
        DesignerPage.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        #Html5Report.convert_to_excel(data_set_01)
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '04.03')
        DesignerPage._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Filters side tab.
            Click Add all filters to page button.
        """
        DesignerPage.SideBar.Filters.click()
        DesignerPage.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify slider range filter control created and blue border around it.
        """
        DesignerPage.PageCanvas.FilterGrid.wait_for_text(slider_label)
        DesignerPage.PageCanvas.FilterGrid.verify_control_labels([slider_label], "05.01")
        DesignerPage.PageCanvas.FilterGrid.Control(slider_label).Slider.verify_values(['1 : 5', '1', '5'], "05.02")
        DesignerPage.PageCanvas.FilterGrid.Control(slider_label).verify_border_properties("05.03")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Type.verify_text("Numeric range", "05.04")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.ID.verify_contains_text("FILTERPANE", "05.05")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Classes.verify_text("", "05.06")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.Tooltip.verify_text("", "05.07")
        DesignerPage.PropertiesPanel.Settings.GeneralSettings.GlobalName.verify_text("", "05.08")
        DesignerPage.PropertiesPanel.Settings.DataSettings.DefaultValue.verify_placeholder("_FOC_NULL", "05.09")
        DesignerPage.PropertiesPanel.Settings.Parameters.Parameters.verify_text("QUANTITY_SOLD_FROM (I11C)", "05.10")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Preview.
        """
        DesignerPage.VisualizationToolBar.RunInNewWindow.click()
        DesignerPage._core_utils.switch_to_new_window()
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_title, 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Page loads successfully in preview.
        """
        DesignerPage.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '06.01')
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(slider_label).Slider.verify_values(['1 : 5', '1', '5'], '06.02')
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '06.03')
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the preview.
        """
        DesignerPage._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click Save and enter C9928362 in Title;
            Click Save button.
        """
        DesignerPage.ToolBar.save(file_name)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Close the designer.
        """
        DesignerPage._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Run created Designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select("Run")
        HomePage.RunWindow.switch_to_frame()
        DesignerPage.RunMode.PageCanvas.wait_for_text(panel_title, 60)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify page runs successfully without error.
        """
        DesignerPage.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '10.01')
        DesignerPage.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '10.02')
        slider = DesignerPage.RunMode.PageCanvas._locator.FilterGrid.Slider.min_value[1]
        DesignerPage._utils.synchronize_until_element_is_visible(slider, 30)
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(slider_label).Slider.verify_values(['1 : 5', '1', '5'], '10.03')
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '10.04')
        DesignerPage._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Select range 3:5 in slider range control.
        """
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(slider_label).Slider.move_pin(3)
        DesignerPage.RunMode.PageCanvas.FilterGrid.Control(slider_label).Slider.move_pin(5, pin=2)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify selected condition applied in the page.
        """
        DesignerPage.RunMode.PageCanvas.Containers.Basic(panel_title).switch_to_frame()
        #Html5Report.convert_to_excel(data_set_02)
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_02, '11')
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close run window.
        """
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Delete the created designer.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file(file_name)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Sign Out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

