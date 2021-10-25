"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 28-September-2021
-------------------------------------------------------------------------------------------"""
import time
from common.pages.charts import Bar
from common.lib.basetestcase import BaseTestCase
from common.locators.charts import common as Locators
from common.wftools.designer import Designer as DesignerPage

class C9929778_TestClass(BaseTestCase):
    
    def test_C9929778(self):
        
        """
        TEST CASE OBJECTS
        """
        BarChartRun = Bar()
        Designer = DesignerPage()
        BarChart = Bar(parent_locator=Locators.content_chart) 
        
        STEP_01 = """
            STEP 01 : Create new DF content with empdata using API call:
    
            http://machine:port/alias/designer?master=ibisamp/empdata&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/empdata')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click 'Data' tab on the top.
        """
        Designer.ToolBar.Data.click()
        Designer.Data.switch_to_frame()
        Designer.Data.Canvas._wait_for_text("empdata")
        time.sleep(10)
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Drag and drop 'training.mas' on to empdata.
        """
        Designer._javascript.scroll_element("div.wcx-grid-body", 2400)
        Designer.Data.Source.drag_to_original_data('training', 'empdata')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check 'Join1' is created.
        """
        Designer.Data.Canvas.verify_join_created(['Join 1', 'empdata (T01)', 'training (T02)'], '03')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click 'Visualization' tab on the top.
        """
        Designer.ToolBar.Visualization.click()
        Designer._utils.wait_for_page_loads(60)
        time.sleep(40)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Check the training master file fields is added in to Data pane.
        """
        Designer.ResourcesPanel.Fields.Dimensions._get_tree_object_('TRAINING')
        Designer.ResourcesPanel.Fields.Dimensions.verify_items(['TRAINING'], '04.01', assert_type='in')
        Designer.ResourcesPanel.Fields.Measures.verify_items(['EMPDATA', 'SALARY', 'TRAINING'], '04.02')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Double click 'LASTNAME' and 'EXPENSES'.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('LASTNAME')
        Designer.ResourcesPanel.Fields.Measures.double_click('TRAINING->EXPENSES')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the fields added to query pane and canvas updated.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['LASTNAME'], '05.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['EXPENSES'], '05.02')
        BarChart.wait_for_text('LASTNAME', time_out=120)
        BarChart.verify_xaxis_title(['LASTNAME'], '05.03')
        BarChart.verify_xaxis_labels(['ADAMS', 'ADDAMS', 'ANDERSON', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LIEBER', 'MARTIN', 'MEDINA', 'OLSON', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SO', 'VALINO', 'WANG', 'WHITE'], '05.04')
        BarChart.verify_yaxis_title(['EXPENSES'], '05.05')
        BarChart.verify_yaxis_labels(['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000'], '05.06')
        BarChart.verify_number_of_risers(28, '05.07')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '05.08')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Run in new window in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the chart output.
        """
        BarChartRun.wait_for_text('LASTNAME', time_out=120)
        BarChartRun.verify_xaxis_title(['LASTNAME'], '06.01')
        BarChartRun.verify_xaxis_labels(['ADAMS', 'ADDAMS', 'ANDERSON', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LIEBER', 'MARTIN', 'MEDINA', 'OLSON', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SO', 'VALINO', 'WANG', 'WHITE'], '06.02')
        BarChartRun.verify_yaxis_title(['EXPENSES'], '06.03')
        BarChartRun.verify_yaxis_labels(['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000'], '06.04')
        BarChartRun.verify_number_of_risers(28, '06.05')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '06.06')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click 'Save' Enter 'C9929778' in Title and Click 'Save as' button.
        """
        Designer.ToolBar.save('C9929778_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Restore C9929778_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929778.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929778_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check 'C9929778_base' is restored successfully.
        """
        BarChart.wait_for_text('LASTNAME', time_out=120)
        BarChart.verify_xaxis_title(['LASTNAME'], '10.01')
        BarChart.verify_xaxis_labels(['ADAMS', 'ADDAMS', 'ANDERSON', 'CASSANOVA', 'CASTALANETTA', 'CHISOLM', 'CONRAD', 'CONTI', 'DONATELLO', 'DUBOIS', 'ELLNER', 'FERNSTEIN', 'GORDON', 'GOTLIEB', 'HIRSCHMAN', 'KASHMAN', 'LASTRA', 'LIEBER', 'MARTIN', 'MEDINA', 'OLSON', 'PUMA', 'ROSENTHAL', 'RUSSO', 'SO', 'VALINO', 'WANG', 'WHITE'], '10.02')
        BarChart.verify_yaxis_title(['EXPENSES'], '10.03')
        BarChart.verify_yaxis_labels(['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000'], '10.04')
        BarChart.verify_number_of_risers(28, '10.05')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '10.06')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("11", STEP_11)