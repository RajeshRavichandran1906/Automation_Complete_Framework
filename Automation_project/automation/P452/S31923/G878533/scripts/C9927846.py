"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 11-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.reports import Reports as Report
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9927846_TestClass(BaseTestCase):
    
    def test_C9927846(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        Html5Report = Report().HTML5()
        
        """
        TEST CASE VAIABLES
        """
        file_name = 'C9927846'
        content_name = '12 - Slider Range Optional Other'
        data_set_01 =  file_name + '_DataSet01'
        data_set_02 =  file_name + '_DataSet02'
        control_name = 'Move Slider'
        slider_values = ['2 : 4', '1', '5']
        
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
            STEP 04 : Drag '12 - Slider Range Optional Other' report into the page canvas from P398_S10799 > Reference Items folder.
        """
        Designer.ResourcesPanel.Content.select('G784942->P452_S31923->P398_S10799->Reference Items')
        Designer.ResourcesPanel.Content.drag_to_page_section(content_name)
        Designer.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify report added to the page successfully.
        """
        Html5Report.wait_for_text('EMEA')
        #Html5Report.convert_to_excel(data_set_01, end_row=26)
        Html5Report.verify_data(data_set_01, '04.01', end_row=26)
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Filters side tab.
            Click Add all filters to page button.
        """
        Designer.SideBar.Filters.click()
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer.PageCanvas.FilterGrid.wait_for_text(control_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify slider range control created with default range 2:4 and blue border around it.
            Verify all values in Properties panel.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).verify_border_properties('05.01')
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(slider_values, '05.02')
        Designer.PropertiesPanel.Settings.GeneralSettings.Type.verify_text('Numeric range', '05.03')
        Designer.PropertiesPanel.Settings.GeneralSettings.ID.verify_contains_text('FILTERPANEL', '05.04')
        Designer.PropertiesPanel.Settings.GeneralSettings.Classes.verify_text('', '05.05')
        Designer.PropertiesPanel.Settings.GeneralSettings.Tooltip.verify_text('', '05.06')
        Designer.PropertiesPanel.Settings.GeneralSettings.GlobalName.verify_text('', '05.07')
        Designer.PropertiesPanel.Settings.DataSettings.DefaultValue2.verify_text('', '05.08')
        Designer.PropertiesPanel.Settings.DataSettings.DefaultValue.verify_text('', '05.09')
        Designer.PropertiesPanel.Settings.Parameters.Parameters.verify_text('QUANTITY_SOLD_FROM (I11C)', '05.10')
        Designer.PropertiesPanel.Settings.Parameters.Parameters2.verify_text('QUANTITY_SOLD_TO (I11C)', '05.11')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Preview.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text(content_name, 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify page loads successfully with slider range control in preview.
        """
        Designer.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '06.01')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '06.02')
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(slider_values, '06.03')
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Html5Report.wait_for_text('EMEA')
        Html5Report.verify_data(data_set_01, '06.04')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Move first slider pin to 3 and second slider pin to 5.
        """
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.move_pin(3, pin=1)
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.move_pin(5, pin=2)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify slider condition applied in the page.
        """
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['3 : 5', '1', '5'], '07.01')
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Html5Report.wait_for_text('6,308')
        #Html5Report.convert_to_excel(data_set_02, end_row=26)
        Html5Report.verify_data(data_set_02, '07.02', end_row=26)
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the preview.
        """
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click Save and enter C9927846 in Title;
            Click Save button.
        """
        Designer.ToolBar.save(file_name)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Move first slider pin to 3 and second slider pin to 5.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.move_pin(3, pin=1)
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.move_pin(5, pin=2)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify slider condition applied in the page.
        """
        Designer.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(['3 : 5', '1', '5'], '10.01')
        Designer.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Designer._utils.wait_for_page_loads(30)
        Html5Report.wait_for_text('6,308')
        Html5Report.verify_data(data_set_02, '10.02', end_row=26)
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the designer.
        """
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Run created Designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.wait_for_text(content_name, 60)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify page runs successfully without error.
        """
        Designer.RunMode.PageCanvas.Heading.verify_heading('Page Heading', '12.01')
        Designer.RunMode.PageCanvas.Containers.verify_number_of_containers(1, '12.02')
        Designer.RunMode.PageCanvas.FilterGrid.Control(control_name).Slider.verify_values(slider_values, '12.03')
        Designer.RunMode.PageCanvas.Containers.Basic(content_name).switch_to_frame()
        Html5Report.wait_for_text('EMEA')
        Html5Report.verify_data(data_set_01, '12.04')
        Designer._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)
        
        STEP_13 = """
            STEP 13 : Close run window.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Delete the created designer.
        """
        HomePage.Workspaces.ContentArea.delete_file(file_name)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Sign Out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)