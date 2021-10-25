'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Click Help icon Inside Designer chart opens Help window
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261992
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.pages import vfour_miscelaneous
from common.lib import core_utility
import time

class C8261992_TestClass(BaseTestCase):
    
    def test_C8261992(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        portal_misobj = vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
    
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        
        """
        Step 2:Click Help button ( far right)
        Help window is launched.
        """
        designer_chart_obj.click_toolbar_item('help')
        core_utility_obj.switch_to_new_window()
        portal_misobj.verify_help_window_left_panel('Creating Charts','Step 2: Verify that you are in the Chart Designer Overview section.')
        msg='Step 2.1: Verify that you are in the Portal Designer Overview section.'
        portal_misobj.verify_help_window_right_panel(['WebFOCUS Online Help>Creating Content'], msg, right_panel_css="div.help_breadcrumbs")
        core_utility_obj.switch_to_previous_window()
        
        """
        Logout using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()