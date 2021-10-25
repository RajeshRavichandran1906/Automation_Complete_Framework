"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 20-September-2021
-------------------------------------------------------------------------------------------"""

from common.pages.charts import Bar
from common.lib.basetestcase import BaseTestCase
from common.locators.charts import common as Locators
from common.wftools.designer import Designer as DesignerPage

class C9929770_TestClass(BaseTestCase):
    
    def test_C9929770(self):
        
        """
            TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        BarChart = Bar(parent_locator=Locators.content_chart) 
        BarChartRun = Bar()
        
        
        STEP_01 = """
            STEP 01 : Create new DF content with CAR using API call:
            http://machine:port/alias/designer?master=ibisamp/car&item=IBFS:/WFC/Repository/P215_S31921/G875470&tool=framework
        """ 
        Designer.API.invoke_new_visualization(credential_keys=('mriddev', 'mrpassdev'), master_file='ibisamp/car')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Add fields 'COUNTRY' and 'CAR' to horizontal bucket, 'DEALER_COST' and 'RETAIL_COST' to vertical bucket.
        """
        Designer.ResourcesPanel.Fields.Dimensions.double_click('COUNTRY')
        Designer.ResourcesPanel.Fields.Dimensions.drag_to_bucket('COMP->CAR', 'Horizontal', 'COUNTRY', target_obj_loc="bottom_middle")
        Designer.ResourcesPanel.Fields.Measures.double_click('DEALER_COST')
        Designer.ResourcesPanel.Fields.Measures.double_click('RETAIL_COST')
        Designer._utils.capture_screenshot("02", STEP_02)
        
        STEP_02_EXPECTED = """
            STEP 02 - Expected :  Check Fields added to query pane and canvas updated.
        """
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['COUNTRY', 'CAR'], '02.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST', 'RETAIL_COST'], '02.02')
        BarChart.wait_for_text('COUNTRY', 60)
        BarChart.verify_xaxis_title(['COUNTRY : CAR'], '02.03')
        BarChart.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '02.04')
        BarChart.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '02.05')
        BarChart.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '02.06')
        BarChart.verify_number_of_risers(20, '02.07')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '02.08')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED)
        
        STEP_03 = """
            STEP 03 : Click Run in new window.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_03_EXPECTED = """
            STEP 03 - Expected : Check the chart output.
        """
        BarChartRun.wait_for_text('COUNTRY', 120)
        BarChartRun.verify_xaxis_title(['COUNTRY : CAR'], '03.01')
        BarChartRun.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '03.02')
        BarChartRun.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '03.03')
        BarChartRun.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '03.04')
        BarChartRun.verify_number_of_risers(20, '03.05')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '03.06')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)
        
        STEP_04 = """
            STEP 04 : Close the Designer Preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("04", STEP_04)
        
        STEP_05 = """
            STEP 05 : Click "Save" Enter "C9929770_base" in Title and Click "Save as" button.
        """
        Designer.ToolBar.save('C9929770_base')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Logout using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Run C9929770_base fex from Home page using API:
            http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP215_S31921%252FG875470%252F&BIP_item=c9929770.fex
        """
        Designer.API.run_fex('C9929770_base', credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("07", STEP_07)
        
        STEP_07_EXPECTED = """
            STEP 07 - Expected: Check the chart output.
        """      
        BarChartRun.wait_for_text('COUNTRY', 120)
        BarChartRun.verify_xaxis_title(['COUNTRY : CAR'], '07.01')
        BarChartRun.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '07.02')
        BarChartRun.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '07.03')
        BarChartRun.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '07.04')
        BarChartRun.verify_number_of_risers(20, '07.05')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '07.06')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        
        STEP_08 = """
            STEP 08 : Logout using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp        
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : Restore C9929770_base fex using API:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P215_S31921/G875470/c9929770.fex&startlocation=IBFS:/WFC/Repository/P215_S31921/G875470
        """
        Designer.API.edit_fex("C9929770_base", credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("09", STEP_09)
        
        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check "C9929770_base" is restored successfully.
        """
        BarChart.wait_for_text('COUNTRY', 120)
        Designer.PropertiesPanel.Settings.Display.Horizontal.verify_available_fields(['COUNTRY', 'CAR'], '09.01')
        Designer.PropertiesPanel.Settings.Display.Vertical.verify_available_fields(['DEALER_COST', 'RETAIL_COST'], '09.02')
        BarChart.verify_xaxis_title(['COUNTRY : CAR'], '09.03')
        BarChart.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '09.04')
        BarChart.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '09.05')
        BarChart.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '09.06')
        BarChart.verify_number_of_risers(20, '09.07')
        BarChart.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '09.08')
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        
        STEP_10 = """
            STEP 10 : Click Run in New window
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("10", STEP_10)
    
        STEP_10_EXPECTED = """
            STEP 10 - Expected : Check the chart output.
        """
        BarChartRun.wait_for_text('COUNTRY', 120)
        BarChartRun.verify_xaxis_title(['COUNTRY : CAR'], '10.01')
        BarChartRun.verify_xaxis_labels(['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW'], '10.02')
        BarChartRun.verify_yaxis_labels(['0', '20K', '40K', '60K', '80K', '100K', '120K'], '10.03')
        BarChartRun.verify_legend_labels(['DEALER_COST', 'RETAIL_COST'], '10.04')
        BarChartRun.verify_number_of_risers(20, '10.05')
        BarChartRun.verify_riser_color([(1, 'bar_blue'), (9, 'bar_blue')], '10.06')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Close Run in new window
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("11", STEP_11)
        
        STEP_12 = """
            STEP 12 : Logout using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("12", STEP_12)