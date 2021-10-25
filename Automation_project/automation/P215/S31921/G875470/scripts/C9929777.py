"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 22-September-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929777_TestClass(BaseTestCase):
    
    def test_C9929777(self):
        
        """
            TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        
        STEP_01 = """
            STEP 01 : Create new DF content with CAR using API call:
            http://machine:port/alias/designer?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Double click 'CAR', 'DEALER_COST'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COMP->CAR')
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Drag and drop 'COUNTRY' to Color bucket.
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('COUNTRY', 'Color')
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check the Fields added to query pane and canvas updated.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['CAR'], '03.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST'], '03.02')
        Designer.PropertiesPanel.Settings.Display.Color.verify_available_fields(['COUNTRY'], '03.03')
        Designer.VisualizationCanvas.Bar.wait_for_text('CAR', 60)
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['CAR'], '03.04')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '03.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '03.06')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '03.07')
        Designer.VisualizationCanvas.Bar.verify_legend_title(['COUNTRY'], '03.08')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '03.09')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(10, '03.10')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '03.11')
        Designer._utils.capture_screenshot("03", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Click "Format" tab and Click "General" dropdown
        """
        Designer.PropertiesPanel.select('Format')
        Designer.PropertiesPanel.Format.click_general_dropdown()
        Designer._utils.capture_screenshot("04", STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Check the Following options are available.
        """
        Designer.PropertiesPanel.Format.Dropdown.verify_options(['General', 'Legend', 'Axis', 'Series', 'Matrix options'], '04')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Click "Frame" color space under Frame and Background.
        """
        Designer.PropertiesPanel.Format.General.FrameAndBackground.click_frame()
        Designer._utils.capture_screenshot("05", STEP_05)
        
        STEP_06 = """
            STEP 06 : Select "Red" color.
        """
        Designer.PropertiesPanel.Format.General.FrameAndBackground.ColorPalette.select_color('#ed1c24')
        Designer._utils.capture_screenshot("06", STEP_06)
        
        STEP_6_EXPECTED = """
            STEP 06 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('DATSUN', 60)
        Designer._utils.synchronize_with_number_of_element("rect[class^='riser'][class$='bar!']", 10, 60)
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['CAR'], '06.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '06.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '06.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '06.04')
        Designer.VisualizationCanvas.Bar.verify_legend_title(['COUNTRY'], '06.05')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '06.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(10, '06.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '06.08')
        Designer.VisualizationCanvas.Bar.verify_frame_color('deep_red', '06.09')
        Designer._utils.capture_screenshot("06 - Expected", STEP_6_EXPECTED)
               
        STEP_07 = """
            STEP 07 : Click Preview in the toolbar
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("07", STEP_07)
        
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('CAR', 120)
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['CAR'], '07.01')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '07.02')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['DEALER_COST'], '07.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '07.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_legend_title(['COUNTRY'], '07.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '07.06')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(10, '07.07')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '07.08')
        Designer.VisualizationCanvas.RunMode.Bar.verify_frame_color('deep_red', '07.09')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        
        STEP_08 = """
            STEP 08 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : Click "Save" Enter "C9929777" in Title and Click "Save as" button.
        """
        Designer.ToolBar.save('C9929777_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("10", STEP_10)
        
        STEP_11 = """
            STEP 11 : Restore C9929777_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929777.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929777_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("11", STEP_11)
        
        STEP_11_EXPECTED = """
            STEP 11 - Expected : Check "C9929777_base" is restored successfully with selected frame color.
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('CAR', 120)
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['CAR'], '11.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '11.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '11.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '11.04')
        Designer.VisualizationCanvas.Bar.verify_legend_title(['COUNTRY'], '11.05')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '11.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(10, '11.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '11.08')
        Designer.VisualizationCanvas.Bar.verify_frame_color('deep_red', '11.09')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)