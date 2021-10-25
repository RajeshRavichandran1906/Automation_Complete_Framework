"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 21-September-2021
-------------------------------------------------------------------------------------------"""

from common.pages.charts import Bar
from common.lib.basetestcase import BaseTestCase
from common.locators.charts import common as Locators
from common.wftools.designer import Designer as DesignerPage

class C9929773_TestClass(BaseTestCase):
    
    def test_C9929773(self):
        
        """
            TEST CASE OBJECTS
        """
        BarChartRun = Bar()
        Designer = DesignerPage()
        BarChart = Bar(parent_locator=Locators.content_chart) 
        
        STEP_01 = """
            STEP 01 : Create new DF content with CAR using API call:
            http://machine:port/alias/designer?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Double click 'CAR' and 'DEALER_COST'
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COMP->CAR')
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Drag and Drop 'COUNTRY' to Color bucket
        """
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('COUNTRY', 'Color')
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check fields added to query pane and canvas updated
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['CAR'], '03.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST'], '03.02')
        Designer.PropertiesPanel.Settings.Display.Color.verify_available_fields(['COUNTRY'], '03.03')
        BarChart.wait_for_text('CAR', 60)
        BarChart.verify_xaxis_title(['CAR'], '03.04')
        BarChart.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '03.05')
        BarChart.verify_yaxis_title(['DEALER_COST'], '03.06')
        BarChart.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '03.07')
        BarChart.verify_legend_title(['COUNTRY'], '03.08')
        BarChart.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '03.09')
        BarChart.verify_number_of_risers(10, '03.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '03.11')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click run in new window
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot('04', STEP_04)
        
        STEP_04_EXPECTED = """
            STEP 04 - Expected : Check the chart output
        """
        BarChartRun.wait_for_text('CAR', 120)
        BarChartRun.verify_xaxis_title(['CAR'], '04.01')
        BarChartRun.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '04.02')
        BarChartRun.verify_yaxis_title(['DEALER_COST'], '04.03')
        BarChartRun.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '04.04')
        BarChartRun.verify_legend_title(['COUNTRY'], '04.05')
        BarChartRun.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '04.06')
        BarChartRun.verify_number_of_risers(10, '04.07')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '04.08')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Close the Output window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot('05', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click "Save" Enter "C9929773_base" in Title and Click "Save as" button.
        """
        Designer.ToolBar.save('C9929773_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot('06', STEP_06)
        
        STEP_07 = """
            STEP 07 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot('07', STEP_07)
        
        STEP_08 = """
            STEP 08 : Run C9929773_base fex from Home page using API:
            http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP215_S31921%252FG875470%252F&BIP_item=c9929773_base.fex
        """
        Designer.API.run_fex('C9929773_base', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot('08', STEP_08)
        
        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check the chart output.
        """
        BarChartRun.wait_for_text('CAR', 120)
        BarChartRun.verify_xaxis_title(['CAR'], '08.01')
        BarChartRun.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '08.02')
        BarChartRun.verify_yaxis_title(['DEALER_COST'], '08.03')
        BarChartRun.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '08.04')
        BarChartRun.verify_legend_title(['COUNTRY'], '08.05')
        BarChartRun.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '08.06')
        BarChartRun.verify_number_of_risers(10, '08.07')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '08.08')
        Designer._utils.capture_screenshot('08 - Expected', STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot('09', STEP_09)
        
        STEP_10 = """
            STEP 10 : Restore C9929773_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929773_base.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929773_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot('10', STEP_10)
        
        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check "C9929773_base" is restored successfully.
        """
        BarChart.wait_for_text('CAR', 120)
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['CAR'], '10.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST'], '10.02')
        Designer.PropertiesPanel.Settings.Display.Color.verify_available_fields(['COUNTRY'], '10.03')
        BarChart.verify_xaxis_title(['CAR'], '10.04')
        BarChart.verify_xaxis_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '10.05')
        BarChart.verify_yaxis_title(['DEALER_COST'], '10.06')
        BarChart.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '10.07')
        BarChart.verify_legend_title(['COUNTRY'], '10.08')
        BarChart.verify_legend_labels(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], '10.09')
        BarChart.verify_number_of_risers(10, '10.10')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'brick_red')], '10.11')
        Designer._utils.capture_screenshot('10 - Expected', STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Logout using API:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot('11', STEP_11)