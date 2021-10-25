"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 07-October-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer.components.properties_panel import Format

class C9929954_TestClass(BaseTestCase):
    
    def test_C9929954(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Create new DF content with wf_retail_lite using API call:
            http://machine:port/alias/designer?master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='retail_samples/wf_retail_lite')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Choropleth Map from chart types.
        """
        Designer.ContentPicker.All.select('Choropleth Map')
        Designer.VisualizationCanvas.wait_for_text('Esri')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Double click 'Store,Country' ; 'Revenue'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('Store->Store Country')
        Designer.VisualizationCanvas.Map.wait_for_text('Esri')
        Designer.ResourcesPanel.Fields.Measures.double_click('Measure Groups->Sales->Revenue')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : 
        """
        Designer._utils.wait_for_page_loads(60)
        Designer.VisualizationCanvas.Map.wait_for_text('Revenue')
        Designer.VisualizationCanvas.Map.verify_legend_title(['Revenue'], '03.01')
        Designer.VisualizationCanvas.Map.verify_legend_labels(['0M', '91M', '182M', '273M', '363.9M', '454.8M', '545.8M'], '03.02')
        Designer.VisualizationCanvas.Map.verify_number_of_risers(34, '03.03')
        Designer.VisualizationCanvas.Map.verify_riser_color([(1, 'Solitude'), (32, 'Solitude')], '03.04')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Select Format tab > General drop down > select Map Options.
        """
        Designer.PropertiesPanel.select('Format')
        Designer.PropertiesPanel.Format.click_general_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('Map options')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click Basemap drop down > select 'World Imagery'
        """
        Designer.PropertiesPanel.Format.MapSettings.click_basemap_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('World Imagery')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify map with selected basemap.
        """
        Designer.VisualizationCanvas.Map.wait_for_text('Earthstar Geographics')
        Designer.VisualizationCanvas.Map.verify_legend_title(['Revenue'], '05.01')
        Designer.VisualizationCanvas.Map.verify_legend_labels(['0M', '91M', '182M', '273M', '363.9M', '454.8M', '545.8M'], '05.02')
        Designer.VisualizationCanvas.Map.verify_number_of_risers(34, '05.03')
        Designer.VisualizationCanvas.Map.verify_riser_color([(1, 'Solitude'), (32, 'Solitude')], '05.04')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Run in new window
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : 
        """
        Designer.VisualizationCanvas.RunMode.Map.wait_for_text('Earthstar Geographics')
        Designer.VisualizationCanvas.RunMode.Map.verify_legend_title(['Revenue'], '06.01')
        Designer.VisualizationCanvas.RunMode.Map.verify_legend_labels(['0M', '91M', '182M', '273M', '363.9M', '454.8M', '545.8M'], '06.02')
        Designer.VisualizationCanvas.RunMode.Map.verify_number_of_risers(34, '06.03')
        Designer.VisualizationCanvas.RunMode.Map.verify_riser_color([(1, 'Solitude'), (32, 'Solitude')], '06.04')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer.VisualizationCanvas.Map.wait_for_text('Earthstar Geographics')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click 'Save' enter 'C9929954_base' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929954_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Restore C9929954_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929954.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929954_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Select Format tab > General drop down > select Map Options.
        """
        Designer.VisualizationCanvas.Map.wait_for_text('Earthstar Geographics')
        Designer.PropertiesPanel.select('Format')
        Designer._utils.wait_for_page_loads(10)
        Designer.PropertiesPanel.Format.click_general_dropdown()
        Designer.PropertiesPanel.Format.Dropdown.select('Map options')
        Designer.VisualizationCanvas.Map.wait_for_text('Earthstar Geographics')
        basemap_object = Designer._webelement._get_object(Format.base_map_default, 'Base Map Text box')
        actual_output = basemap_object.get_attribute('aria-label')
        msg = "Step 11: Verify World Imagery is select as default in Base Map"
        Designer._utils.asequal(actual_output, 'World Imagery', msg)
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : 
        """
        Designer.VisualizationCanvas.Map.verify_legend_title(['Revenue'], '11.01')
        Designer.VisualizationCanvas.Map.verify_legend_labels(['0M', '91M', '182M', '273M', '363.9M', '454.8M', '545.8M'], '11.02')
        Designer.VisualizationCanvas.Map.verify_number_of_risers(34, '11.03')
        Designer.VisualizationCanvas.Map.verify_riser_color([(1, 'Solitude'), (32, 'Solitude')], '11.04')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)
