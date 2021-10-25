"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 09-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.reports import Reports as Report
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9928360_TestClass(BaseTestCase):
    
    def test_C9928360(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        Html5Report = Report().HTML5()
        
        """
        TEST CASE VAIABLES
        """
        file_name = 'C9928360'
        content_name = '08 - Slider Optional All'
        data_set_01 =  file_name + '_DataSet01'
        data_set_02 =  file_name + '_DataSet02'
        control_name = 'Move Slider to 5011'
        
        STEP_01 = """
            STEP 01 : Login to WF as Developer.
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G784942' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G784942')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Select Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag '08 - Slider Optional All' report into the page canvas from P398_S10799 > Reference Items folder.
        """
        Designer.ResourcesPanel.Content.select('G784942->P452_S31923->P398_S10799->Reference Items')
        Designer.ResourcesPanel.Content.drag_to_page_section(content_name)
        Designer.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify report added to the page successfully.
        """
        #Html5Report.convert_to_excel(data_set_01)
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '04.01')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Quick filter.
        """
        Designer.SideBar.Filters.click()
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer.PageCanvas.FilterGrid.wait_for_text('Move Slider')
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify slider control bounded to the page with blue border around it.
            Verify all values in Properties panel.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).verify_border_properties('05.01')
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['5000', '5000', '5020'], '05.02')
        Designer.PropertiesPanel.Settings.GeneralSettings.Type.verify_text('Slider', '05.03')
        Designer.PropertiesPanel.Settings.GeneralSettings.ID.verify_contains_text('FILTERPANEL', '05.04')
        Designer.PropertiesPanel.Settings.GeneralSettings.Classes.verify_text('', '05.05')
        Designer.PropertiesPanel.Settings.GeneralSettings.Tooltip.verify_text('', '05.06')
        Designer.PropertiesPanel.Settings.GeneralSettings.GlobalName.verify_text('', '05.07')
        Designer.PropertiesPanel.Settings.DataSettings.DefaultValue.verify_text('', '05.08')
        Designer.PropertiesPanel.Settings.Parameters.Parameters.verify_text('ID_PRODUCT (I9)', '05.09')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Preview.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text(content_name, 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify page loads successfully in preview.
        """
        Designer.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '06.01')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '06.02')
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['5000', '5000', '5020'], '06.03')
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '06.04')
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the preview.
        """
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click Save and enter C9928360 in Title;
            Click Save button.
        """
        Designer.ToolBar.save(file_name)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Move slider pin to 5011 position in design mode.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.move_pin(5011)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify slider condition applied in the page.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['5011', '5000', '5020'], '09.01')
        Designer.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        #Html5Report.convert_to_excel(data_set_02)
        Html5Report.wait_for_text('5011')
        Html5Report.verify_data(data_set_02, '09.02')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the designer.
        """
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Run created Designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.wait_for_text(content_name, 60)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify page runs successfully without error.
        """
        Designer.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '11.01')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '11.02')
        slider = Designer.RunMode.PageCanvas._locator.FilterGrid.Slider.min_value[1]
        Designer._utils.synchronize_until_element_is_visible(slider, 30)
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['5000', '5000', '5020'], '11.03')
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Html5Report.wait_for_text('Customer')
        Html5Report.verify_data(data_set_01, '11.04')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close run window.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Delete the created designer.
        """
        HomePage.Workspaces.ContentArea.delete_file(file_name)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Sign Out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)