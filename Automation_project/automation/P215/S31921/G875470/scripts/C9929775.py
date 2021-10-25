"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 27-September-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage

class C9929775_TestClass(BaseTestCase):
    
    def test_C9929775(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()

        STEP_01 = """
            STEP 01 : : Create new DF content with CAR using API call:
            http://machine:port/alias/designer?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Double click 'CAR' and 'DEALER_COST'.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COMP->CAR')
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Check Fields added to query pane and canvas updated.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['CAR'], '02.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST'], '02.02')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click 'Content' under Settings tab.
        """
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click 'Run with Insight' checkbox under 'Interactivity'
        """
        Designer.PropertiesPanel.Settings.ContentSettings.RunWithInsight.check()
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click Run in new window in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the chart output.
        """
        Designer.VisualizationCanvas.RunMode.Insight.Bar.wait_for_text('CAR', 120)
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '05.01')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_xaxis_title(['CAR'], '05.02')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '05.03')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_yaxis_title(['DEALER_COST'], '05.04')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_number_of_risers(10, '05.05')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '05.06')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click 'CAR' under Horizontal axis and Select 'COUNTRY'.
        """ 
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.click_on_field_in_query_bucket('Horizontal Axis', 'CAR')
        Designer.VisualizationCanvas.RunMode.Insight.SelectItemList.select('COUNTRY')
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check CAR is replaced with COUNTRY.
        """
        Designer.VisualizationCanvas.RunMode.Insight.Bar.wait_for_text('COUNTRY', 120)
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_xaxis_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '06.01')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_xaxis_title(['COUNTRY'], '06.02')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '06.03')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_yaxis_title(['DEALER_COST'], '06.04')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_number_of_risers(5, '06.05')
        Designer.VisualizationCanvas.RunMode.Insight.Bar.verify_riser_color([(1, 'bar_blue'), (4, 'bar_blue')], '06.06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'Change chart' option and Select 'Ring Pie' chart.
        """
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.change_chart_type_from_chart_picker_option('Ring Pie')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check Bar chart is converted to Ring Pie chart.
        """
        Designer.VisualizationCanvas.RunMode.Insight.Pie.wait_for_text('DEALER_COST', 20)
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_total_lables(['144K'], '07.01')
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_pie_labels(['DEALER_COST'], '07.02')
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_legend_title(['COUNTRY'], '07.03')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click 'Show Filter' icon and Select 'COUNTRY'.
        """
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.select_header_option_item('filter')
        time.sleep(5)
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.click_add_filter_in_top_filter_panel()
        time.sleep(5)
        Designer.VisualizationCanvas.RunMode.Insight.SelectItemList.select('COUNTRY')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click 'COUNTRY' filter > Select 'ENGLAND', 'ITALY' and 'JAPAN' and Click outside the filter.
        """
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.click_on_filter_shelf_item('COUNTRY')
        time.sleep(5)
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.select_or_verify_filter_grid_values('COUNTRY', item_list=['ENGLAND', 'ITALY', 'JAPAN'])
        Designer.VisualizationCanvas.RunMode.Insight.InteractiveHeader.click_on_blank_area_in_insight_chart()
        time.sleep(5)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check the Chart updated with selected filter values.
        """
        Designer.VisualizationCanvas.RunMode.Insight.Pie.wait_for_text('DEALER_COST', 20)
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_total_lables(['84,600'], '09.01')
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_pie_labels(['DEALER_COST'], '09.02')
        Designer.VisualizationCanvas.RunMode.Insight.Pie.verify_legend_title(['COUNTRY'], '09.03')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click 'Save' Enter 'C9929775' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929775_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Restore C9929775_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929775.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929775_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Check 'C9929775_base' is restored successfully.
        """
        Designer.VisualizationCanvas.Bar.wait_for_text('CAR', 120)
        Designer.VisualizationCanvas.Bar.verify_xaxis_title(['CAR'], '13.01')
        Designer.VisualizationCanvas.Bar.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '13.02')
        Designer.VisualizationCanvas.Bar.verify_yaxis_title(['DEALER_COST'], '13.03')
        Designer.VisualizationCanvas.Bar.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '13.04')
        Designer.VisualizationCanvas.Bar.verify_number_of_risers(10, '13.05')
        Designer.VisualizationCanvas.Bar.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '13.06')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click 'Content' under Settings tab.
        """
        Designer._utils.capture_screenshot("14", STEP_14)
        STEP_14_EXPECTED = """
            STEP 14 - Expected : Check 'Run with Insight' is enabled under 'Interactivity'.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.RunWithInsight.verify_checked('14')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("15", STEP_15)