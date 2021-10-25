"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 05-October-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929953_TestClass(BaseTestCase):
    
    def test_C9929953(self):
        
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
            STEP 02 : Double click 'COUNTRY' , 'DEALER_COST'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click("COUNTRY")
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.ResourcesPanel.Fields.Measures.double_click("DEALER_COST")
        Designer.VisualizationCanvas.Bar.wait_for_text('DEALER_COST')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Drag and drop 'COUNTRY' to 'Drop a Filter or field here'
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_visual_filter_toolbar('COUNTRY')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify Country is added to Filter shelf
        """
        Designer.VisualizationFilterToolbar.verify_field_names(['COUNTRY'], '03')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on COUNTRY from Filter pane
        """
        Designer.VisualizationFilterToolbar.click_on_field('COUNTRY')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : 
        """
        Designer.VisualizationFilterToolbar.Dropdown.Option.verify_options(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '04')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Select England,Italy and Japan and click outside
        """
        Designer.VisualizationFilterToolbar.Dropdown.Option.select_multiple_options(['ENGLAND', 'ITALY', 'JAPAN'], click_outside=True)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Filter and canvas is updated
        """
        Designer.VisualizationFilterToolbar.verify_field_names(['COUNTRY'], '05.01')
        Designer.VisualizationFilterToolbar.verify_field_values(['3 of 5'], '05.02')
        Designer._utils.synchronize_with_number_of_element("[class*='riser!']", 3, 60)
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY'], '05.03')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND', 'ITALY', 'JAPAN'], '05.04')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '05.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '05.06')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K'], '05.07')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(3, '05.08')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '05.09')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Run in new window in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : 
        """
        Designer.VisualizationCanvas.RunMode.Bar.wait_for_text('COUNTRY')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_title(['COUNTRY'], '05.03')
        Designer.VisualizationCanvas.RunMode.Bar.verify_xaxis_labels(['ENGLAND', 'ITALY', 'JAPAN'], '05.04')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['DEALER_COST'], '05.05')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_title(['DEALER_COST'], '05.06')
        Designer.VisualizationCanvas.RunMode.Bar.verify_yaxis_labels(['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K'], '05.07')
        Designer.VisualizationCanvas.RunMode.Bar.verify_number_of_risers(3, '05.08')
        Designer.VisualizationCanvas.RunMode.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '05.09')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click 'Save' enter 'C9929953_base' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929953_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Restore C9929953_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929953.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929953_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected :
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('COUNTRY', time_out=120)
        Designer.VisualizationFilterToolbar.verify_field_names(['COUNTRY'], '10.01')
        Designer.VisualizationFilterToolbar.verify_field_values(['3 of 5'], '10.02')
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['COUNTRY'], '10.03')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ENGLAND', 'ITALY', 'JAPAN'], '10.04')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '10.05')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '10.06')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K'], '10.07')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(3, '10.08')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (3, 'bar_blue')], '10.09')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)