"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 01-October-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929952_TestClass(BaseTestCase):
    
    def test_C9929952(self):
        
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
            STEP 02 : Add 'COUNTRY', 'CAR' to Horizontal 'DEALER_COST' and 'RETAIL_COST'  to Vertical
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("COUNTRY")
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket("COMP->CAR", "Horizontal", "COUNTRY", target_obj_loc="bottom_middle")
        Designer.VisualizationCanvas.Bar.wait_for_text('CAR')
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        Designer.VisualizationCanvas.Bar.wait_for_text('DEALER_COST')
        Designer.ResourcesPanel.Fields.Measures.double_click("RETAIL_COST")
        Designer.VisualizationCanvas.Bar.wait_for_text('RETAIL_COST')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Drag and drop 'COUNTRY' to Chart heading (from data pane)
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_heading("COUNTRY")
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Verify text is highlighted by default and apply the following styling
            Click Font style dropdown > Select BATANG
            Font size dropdown > Select 14
            Click Font color > select 'Red'
        """
        Designer.VisualizationCanvas.Header.switch_to_frame()
        Designer.VisualizationCanvas.Header.verify_highlighted_text('<CAR.ORIGIN.COUNTRY', '04')
        Designer._utils.switch_to_default_content()
        Designer.VisualizationCanvas.FormattingToolbar.FontName.click()
        Designer.VisualizationCanvas.FormattingToolbar.SelectItem.select('BATANG')
        Designer.VisualizationCanvas.FormattingToolbar.click_font_size_dropdown()
        Designer.VisualizationCanvas.FormattingToolbar.SelectItem.select('14')
        Designer.VisualizationCanvas.FormattingToolbar.Color.click()
        Designer.VisualizationCanvas.FormattingToolbar.select_color_palette("#ed1c24")
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Close the Formatting toolbar
        """
        Designer.VisualizationCanvas.FormattingToolbar.Close.click()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : 
        """
        Designer.VisualizationCanvas.Header.switch_to_frame()
        Designer.VisualizationCanvas.Header.wait_for_text('ENGLAND')
        Designer.VisualizationCanvas.Header.verify_text(['ENGLAND'], '05.01', assert_type='in')
        Designer.VisualizationCanvas.Header.verify_text_color('deep_red', '05.02')
        Designer.VisualizationCanvas.Header.verify_text_size('14', '05.03')
        Designer._utils.switch_to_default_content()
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY : CAR'], '05.04')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '05.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '05.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(20, '05.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '05.08')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '05.09')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click 'Content' under Settings tab.
        """
        Designer._utils.capture_screenshot("06", STEP_06)
        STEP_07 = """
            STEP 07 : Click 'Enable footing' checkbox under 'Headings & Footings'.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.EnableFooting.check()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Drag a field 'SALES' from the field list to the footing.
        """
        Designer.ResourcesPanel.Fields.Measures.drag_to_footing('SALES')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Close the Formatting toolbar
        """
        Designer.VisualizationCanvas.FormattingToolbar.Close.click()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Footing displayed in chart.
        """
        Designer.VisualizationCanvas.Footer.switch_to_frame()
        Designer.VisualizationCanvas.Footer.wait_for_text('1200')
        Designer.VisualizationCanvas.Footer.verify_text(['12000'], '09.01', assert_type='in')
        Designer._utils.switch_to_default_content()
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY : CAR'], '09.02')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '09.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '09.04')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(20, '09.05')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '09.06')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '09.07')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Run in new window in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected :
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('COUNTRY', 120)
        Designer.VisualizationCanvas.RunMode.Heading.verify_text(['ENGLAND'], '10.01', assert_type='in')
        Designer.VisualizationCanvas.RunMode.Heading.verify_text_color('deep_red', '10.02')
        Designer.VisualizationCanvas.RunMode.Heading.verify_text_size('14', '10.03')
        Designer.VisualizationCanvas.RunMode.Footing.verify_text(['12000'], '10.04', assert_type='in')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['COUNTRY : CAR'], '10.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '10.06')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '10.07')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(20, '10.08')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '10.09')
        Designer.VisualizationCanvas.RunMode.Bar.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '10.10')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close the Designer Run in new window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click 'Save' enter 'C9929952_base' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929952_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : STEP 09 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Restore C9929952_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929952.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929952_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : 
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY', 120)
        Designer.VisualizationCanvas.Header.switch_to_frame()
        Designer.VisualizationCanvas.Header.wait_for_text('ENGLAND')
        Designer.VisualizationCanvas.Header.verify_text(['ENGLAND'], '14.01', assert_type='in')
        Designer.VisualizationCanvas.Header.verify_text_color('deep_red', '14.02')
        Designer.VisualizationCanvas.Header.verify_text_size('14', '14.03')
        Designer._utils.switch_to_default_content()
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY : CAR'], '14.04')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '14.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '14.06')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(20, '14.07')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '14.08')
        Designer.VisualizationCanvas.Bar.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '14.09')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)
    
        STEP_15 = """
            STEP 15 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("15", STEP_15)

