'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Designer Chart: Scroll bar doesn't work inside canvas
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261986
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
import time

class C8261986_TestClass(BaseTestCase):
    
    def test_C8261986(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utils = utillity.UtillityMethods(self.driver)
         
        Step1 = """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        utils.capture_screenshot("01.01",Step1)
        
        Step2 = """
        Step 2:Drag "Customer City" to canvas
        Designer chart created with added field and See a scroll bar appears.
        """
        designer_chart_obj.drag_dimension_field_to_canvas("Customer->Customer->Customer,City")
        utils.synchronize_with_visble_text("#arpreview_fdmId_11_fmg", "Customer City", designer_chart_obj.home_page_long_timesleep)
        utils.capture_screenshot("02.01",Step2)
        
        Step3 = """
        Step 3: Try to change the scroll bar
        Verify scroll bar moved and canvas updated.
        """
        source_element =utils.validate_and_get_webdriver_object(".scroll-rp-h","Scrol_bar")
        target_element =utils.validate_and_get_webdriver_object(".scrollBarSpace","Scrol_bar_space")
        utils.drag_drop_using_pyautogui(source_element,target_element)
        utils.verify_object_visible("[class='riser!s0!g499!mbar!']",True,"Step03:01")
        utils.verify_object_visible("[class='xaxisOrdinal-labels!g499!mgroupLabel!']",True,"Step03:02")
        utils.capture_screenshot("03.01",Step3,True)
        
        """
        Step 4:Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()