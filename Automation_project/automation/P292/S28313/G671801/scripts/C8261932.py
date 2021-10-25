'''
Created on Sep 30, 2019

@author: Niranjan
Testcase Name : Check Data grid :"Fit to container width"
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261932
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import designer_chart

class C8261932_TestClass(BaseTestCase):
    
    def test_C8261932(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        Step1 = """
        Step 1: Launch the API to create new Deisgner chart with Car.
        http://domain.com:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2F&master=ibisamp%2FCar&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('ibisamp/car', mrid='mrid', mrpass ='mrpass')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: Select "DataGrid" from Chart picker component.
        """
        designer_chart_obj.select_chart_from_chart_picker('datagrid')
        utils.capture_screenshot("02.00", Step2)
        
        Step3 = """
        Step 3: Double click "Country", "DEALER_COST".
        """
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Click Format tab (brush icon)
        """
        designer_chart_obj.select_query_or_format_tab()
        time.sleep(2)
        utils.capture_screenshot("04.00", Step4)
        
        Step5 = """
        Step 5: Click General dropdown > Select Datagrid options
        """
        designer_chart_obj.select_format_access_option('Datagrid options')
        utils.capture_screenshot("05.00", Step5)
          
        Step6 = """
        Step 6: Expand Other
        """
        other_elem = utils.validate_and_get_webdriver_object("div[data-ibx-name='datagridOtherPage'] div[class*='glyph-chevron-right']", 'Other')
        core_utils.left_click(other_elem)
        time.sleep(2)
        utils.capture_screenshot("06.00", Step6)
        
        Step7 = """
        Step 7: Check "Fit to container width"
        Step 07.00 : Verify the Report is stretched on canvas
        """
        container_width_button_elem = utils.validate_and_get_webdriver_object('div[data-ibx-name="datagridOtherPage"] .wfc-fp-acc-box div[data-user-data="fitToContainerWidth"] div[class*="check-box"]', 'fit to container width')
        core_utils.left_click(container_width_button_elem)
        table_cell_elem = utils.validate_and_get_webdriver_object('.innerTable rect', 'table cell')
        actual_cell_width = table_cell_elem.get_attribute('width')
        actual_cell_height = table_cell_elem.get_attribute('height')
        expected_cell = [actual_cell_width, actual_cell_height]
        utils.asequal(expected_cell, ['1059', '31'] , 'Step 07.00 : Verify the Report is stretched on canvas')
        utils.capture_screenshot("07.00", Step7, expected_image_verify = True)
        
        Step8 = """
        Step 8: Click Preview button to run Designer chart
        Step 08.00: Verify the output is stretched and dimension will display at far left of grid, measure will display at far right of grid.
        """
        designer_chart_obj.click_toolbar_item('preview')
        designer_chart_obj.switch_to_run_preview_frame()
        table_cell_elem = utils.validate_and_get_webdriver_object('#jschart_HOLD_0 .innerTable .reorder_placeholder_PageGroup rect', 'table cell') 
        actual_cell_width = table_cell_elem.get_attribute('width')
        actual_cell_height = table_cell_elem.get_attribute('height')
        expected_cell = [actual_cell_width, actual_cell_height]
        utils.asequal(expected_cell, ['1539', '31'] , 'Step 08.00 : Verify the Report is stretched on canvas')
        designer_chart_obj.switch_to_default_content()
        utils.capture_screenshot("08.00", Step8)
        
        Step9 = """
        Step 9: Click Save and Enter title as "C8261932" > Save
        """ 
        designer_chart_obj.go_back_to_design_from_preview()
        designer_chart_obj.save_designer_chart_from_toolbar('C8261932')
        utils.capture_screenshot("09.00", Step9)
        
        Step10 = """
        Step 10: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        utils.capture_screenshot("10.00", Step10)
       
        Step11 = """
        Step 11: Restore the saved Chart Designer using API link.
        http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774/c8261932.fex
        Step 11.00 : Verify report is preserved after restore
        """ 
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api(fex ='c8261932' , mrid = 'mrid', mrpass ='mrpass')
        designer_chart_obj.wait_for_number_of_element('.innerTable rect', 5)
        table_cell_elem = utils.validate_and_get_webdriver_object('.innerTable rect', 'table cell')
        actual_cell_width = table_cell_elem.get_attribute('width')
        actual_cell_height = table_cell_elem.get_attribute('height')
        expected_cell = [actual_cell_width, actual_cell_height]
        utils.asequal(expected_cell, ['1059', '31'] , 'Step 11.00 : Verify report is preserved after restore')
        utils.capture_screenshot("11.00", Step11)
        
        Step12 = """
        Step 12: Click Format tab (brush icon)
        """
        designer_chart_obj.select_query_or_format_tab()
        time.sleep(2)
        utils.capture_screenshot("12.00", Step12)
        
        Step13 = """
        Step 13: Click General dropdown > Select Datagrid options
        """
        designer_chart_obj.select_format_access_option('Datagrid options')
        utils.capture_screenshot("13.00", Step13)
        
        Step14 = """
        Step 14: Expand Other and Uncheck "Fit to container width"
        Step 14.00 : Report is displayed back to default
        """
        other_elem = utils.validate_and_get_webdriver_object("div[data-ibx-name='datagridOtherPage'] div[class*='glyph-chevron-right']", 'Other')
        core_utils.left_click(other_elem)
        time.sleep(2)
        container_width_button_elem = utils.validate_and_get_webdriver_object('div[data-ibx-name="datagridOtherPage"] .wfc-fp-acc-box div[data-user-data="fitToContainerWidth"] div[class*="check-box"]', 'fit to container width')
        core_utils.left_click(container_width_button_elem)
        time.sleep(2)
        table_cell_elem = utils.validate_and_get_webdriver_object('.innerTable rect', 'table cell')
        actual_cell_width = table_cell_elem.get_attribute('width')
        actual_cell_height = table_cell_elem.get_attribute('height')
        expected_cell = [actual_cell_width, actual_cell_height]
        utils.asequal(expected_cell, ['146', '31'] , 'Step 14.00 : Verify Report is displayed back to default')
        utils.capture_screenshot("14.00", Step14)
        
        Step15 = """
        Step 15: Click Preview button to run Designer chart
        Step 15.00 : Verify output is not stretched
        """
        designer_chart_obj.click_toolbar_item('preview')
        designer_chart_obj.switch_to_run_preview_frame()
        table_cell_elem = utils.validate_and_get_webdriver_object('#jschart_HOLD_0 .innerTable .reorder_placeholder_PageGroup rect', 'table cell') 
        actual_cell_width = table_cell_elem.get_attribute('width')
        actual_cell_height = table_cell_elem.get_attribute('height')
        expected_cell = [actual_cell_width, actual_cell_height]
        utils.asequal(expected_cell, ['146', '31'] , 'Step 15.00 : Verify report is not stretched')
        designer_chart_obj.switch_to_default_content()
        utils.capture_screenshot("15.00", Step15)
        
        """
        Step 16: Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()