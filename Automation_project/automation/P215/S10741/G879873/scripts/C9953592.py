"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 20-October-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer.components import properties_panel as locators

class C9953592_TestClass(BaseTestCase):
    
    def test_C9953592(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Launch Designer:
            http://machine.ibi.com:port/alias/designer?&master=ibisamp/car&item=IBFS:/WFC/Repository&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G784931
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select 'Standard Report' from chart picker tool.
        """
        Designer.ContentPicker.All.select("Standard Report")
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Double click COUNTRY and DEALER_COST.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("COUNTRY")
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Drill Anywhere' check box in content settings.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.DrillAnywhere.check()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Drill Anywhere is enabled.
        """
        Designer._utils.verify_element_enabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '04')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Change output format to 'AHTML'.
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('AHTML')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Drill Anywhere is enabled.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.verify_element_enabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '05')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Change output format to 'HTML'.
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('HTML')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Drill Anywhere is enabled.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.verify_element_enabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Change Output format to 'PDF'.
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('PDF')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Drill Anywhere is disabled.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.verify_element_disabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '07')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Change output format to 'PPTX'.
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('PPTX')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Drill Anywhere is disabled.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.verify_element_disabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '08')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Change output format to 'XLSX'.
        """
        Designer.VisualizationToolBar.OutputFormat.button.click()
        Designer.VisualizationToolBar.OutputFormat.select_output_format('XLSX')
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify Drill Anywhere is disabled.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.verify_element_disabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '09')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Save report as 'C9953592'.
        """
        Designer.ToolBar.save('C9953592')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Edit the saved FEX
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G784931/c9953592.fex&startlocation=IBFS:/WFC/Repository/P452_S31923/G784931
        """
        Designer.API.edit_fex("C9953592", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Verify Drill Anywhere is disabled for XLSX format.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.__scroll_into_view__()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Drill Anywhere is disabled for XLSX format.
        """
        Designer._utils.verify_element_disabled(locators.Settings.drill_anywhere_parent, "Drill Anywhere", '13')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Logout WebFOCUS
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("14", STEP_14)