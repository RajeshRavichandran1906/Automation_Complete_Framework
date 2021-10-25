'''
Created on Sep 19, 2019

@author: Niranjan
Testcase Name : Search using field name with split measures/dimensions active
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261838
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib.global_variables import Global_variables
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
import pyautogui

class C8261838_TestClass(BaseTestCase):
    
    def test_C8261838(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        Step1 = """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('ibisamp/car')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: In the search pane type "SALES"
        Step 02.00 : The SALES field appears under the MEASURES pane of the field list.
        """
        designer_chart_obj.enter_text_in_search_fields(send_keys='SALES')
        designer_chart_obj.wait_for_number_of_element("div[class*='metadata-container'][class*='measure-tree-box'] [class*='tnode-label']", 1)
        designer_chart_obj.verify_fields_in_measures(['SALES'], "Step 2.00: Verify the measures list")
        utils.capture_screenshot("02.00", Step2)
        
        
        Step3 = """
        Step 3: Clear the entry by clicking the x located to the left of the search icon.
        Step 03.00: The search entry box clears and all fields appear in the fields list.
        """
        if Global_variables.browser_name in ['chrome']:
            cross_element = utils.validate_and_get_webdriver_object(".wfc-mdfp-search-box div[data-ibx-type='ibxTextField'] input", "Cross mark")
            core_utils.python_left_click(cross_element, xoffset=-38, element_location='middle_right')            
        else:
            pyautogui.press('backspace',presses=7,interval=0.2, pause=1)
        designer_chart_obj.wait_for_visible_text("div[class*='metadata-container'][class*='measure-tree-box']", "COMP")
        designer_chart_obj.verify_fields_in_measures(['ORIGIN', 'COMP'], "Step 3.00: Verify the measures list")
        designer_chart_obj.verify_fields_in_dimensions(['ORIGIN', 'COUNTRY', 'COMP'], "Step 3.01: Verify the dimenisons list")
        utils.capture_screenshot("03.00", Step3)
        
        """
        Step 4: Sign out using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()