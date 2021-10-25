'''
Created on Sep 27, 2019

@author: Niranjan
Testcase Name : Change Vertical /Horizontal Padding values
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261926
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import designer_chart

class C8261926_TestClass(BaseTestCase):
    
    def test_C8261926(self):
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
        Step 3: Add "COUNTRY" to Row, "CAR" to Column
        """
        designer_chart_obj.drag_dimension_field_to_query_bucket('COUNTRY', 'Row')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.drag_dimension_field_to_query_bucket('COMP->CAR', 'Column')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "CAR", designer_chart_obj.chart_medium_timesleep)
        utils.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Double click "DEALER_COST", "RETAIL_COST".
        """
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('RETAIL_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        table_cell_elem = utils.validate_and_get_webdriver_object('.innerTable rect', 'table cell')
        actual_cell_height = table_cell_elem.get_attribute('height')
        utils.asequal(actual_cell_height, '31', 'Step 04.00 : Verify default chart canvas')
        utils.capture_screenshot("04.00", Step4, expected_image_verify = True)
        
        Step5 = """
        Step 5: Select Format > General drop down > "DataGrid Options".
        """
        designer_chart_obj.select_query_or_format_tab()
        time.sleep(2)
        designer_chart_obj.select_format_access_option('Datagrid options')
        utils.capture_screenshot("05.00", Step5)
          
        Step6 = """
        Step 6: Select Background and Padding
        """
        background_padding_elem = utils.validate_and_get_webdriver_objects("div[data-ibx-type='datagridOptionsPane'] div[class*='glyph-chevron-right']", 'Background and Padding')
        core_utils.left_click(background_padding_elem[0])
        time.sleep(2)
        utils.capture_screenshot("06.00", Step6)
        
        Step7 = """
        Step 7: Change Vertical Padding value to 3 and Horizontal value Padding to 8.
        Step 07.00 : The applied changes reflected in Chart canvas.
        """
        padding_axis_elem = utils.validate_and_get_webdriver_objects('.wfc-chart-property input[role="spinbutton"]', 'Padding value box')
        padding_axis_elem[0].clear()  
        utils.set_text_to_textbox_using_keybord(text_string = '3', text_box_elem = padding_axis_elem[0])
        padding_axis_elem[1].clear()
        utils.set_text_to_textbox_using_keybord(text_string = '8', text_box_elem = padding_axis_elem[1])
        table_cell_elem = utils.validate_and_get_webdriver_object('.innerTable rect', 'table cell')
        actual_cell_height = table_cell_elem.get_attribute('height')
        utils.asequal(actual_cell_height, '21', 'Step 07.00 : Verify change in the chart canvas')
        utils.capture_screenshot("07.00", Step7, expected_image_verify = True)
        
        Step8 = """
        Step 8: Click Preview.
        Step 08.00: The applied changes reflected in Chart preview.
        """
        designer_chart_obj.click_toolbar_item('preview')
        designer_chart_obj.switch_to_run_preview_frame()
        table_cell_elem = utils.validate_and_get_webdriver_object('.chart .innerTableScroll rect', 'table cell')   
        actual_cell_height = table_cell_elem.get_attribute('height')
        utils.asequal(actual_cell_height, '21', 'Step 08.00 : Verify change in the chart preview canvas')
        designer_chart_obj.switch_to_default_content()
        utils.capture_screenshot("08.00", Step8, expected_image_verify = True)
        
        Step9 = """
        Step 9: Click blue icon to return to chart canvas.
        """ 
        designer_chart_obj.go_back_to_design_from_preview()
        utils.capture_screenshot("09.00", Step9)
        
        Step10 = """
        Step 10: Click save icon, type "C8261926" > save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C8261926')
        utils.capture_screenshot("10.00", Step10)
        
        """
        Step 11: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()