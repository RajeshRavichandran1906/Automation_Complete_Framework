'''
Created on December 28, 2018

@author: AA14564

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10564&group_by=cases:section_id&group_id=164143&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2286941
TestCase Name = Verify default extensions show in chart picker
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart 
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript

class C2286941_TestClass(BaseTestCase):

    def test_C2286941(self):
        
        """
        TESTCASE Object's
        """
        active_chart_obj = Active_Chart(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        j_script = JavaScript(self.driver)
        html5_extension_css = "#ChartTypeGroup_html5_extensions"
        arc_css = "[id='ChartTypeButton_Icon_com.ibi.arc']"
        liquid_gauge_css = "[id='ChartTypeButton_Icon_com.ibi.liquid_gauge']"
        sankey_flow_chart_css = "[id='ChartTypeButton_Icon_com.ibi.sankey']"
        close_button_css =".active.window .window-close-button"
        
        """
        Step 1: Sign in to WebFOCUS as a developer user
                http://machine:port/{alias}
        """
        """
        Step 2: Create chart using below URL
                http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FP95_S10564%2FG164143%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/car')
        
        """
        Step 3: Select Format > Chart Type > Other > HTML5 Extensions.
        """
        active_chart_obj.select_chart_type('Other')
        util_obj.synchronize_with_visble_text(html5_extension_css, 'HTML5 Extension', 90)
        chart_type_elem=util_obj.validate_and_get_webdriver_object(html5_extension_css, 'HTML5 Extension')
        core_util_obj.left_click(chart_type_elem)
        util_obj.synchronize_with_number_of_element(arc_css, 1, 190)
        
        """
        Step 4: Verify 3 charts are showing in the chart picker: Arc, Liquid Gauge and Sankey Flow Chart.
        """
        arc_object = util_obj.validate_and_get_webdriver_object(arc_css, 'Arc char')
        j_script.scrollIntoView(arc_object)
        time.sleep(2)
        util_obj.verify_picture_using_sikuli('arc.png', "Step 4: Verify 'Arc' charts are showing in the HTML5 Extension chart picker")
        liquid_gauge_object = util_obj.validate_and_get_webdriver_object(liquid_gauge_css, 'Liquid Gauge')
        j_script.scrollIntoView(liquid_gauge_object)
        time.sleep(2)
        util_obj.verify_picture_using_sikuli('liquid_gauge.png', "Step 4.1: Verify 'Liquid Gauge' charts are showing in the HTML5 Extension chart picker")
        sankey_flow_chart_object = util_obj.validate_and_get_webdriver_object(sankey_flow_chart_css, 'Sankey Flow Chart')
        j_script.scrollIntoView(sankey_flow_chart_object)
        time.sleep(2)
        util_obj.verify_picture_using_sikuli('sankey_flow_chart.png', "Step 4.2: Verify 'Sankey Flow Chart' charts are showing in the HTML5 Extension chart picker")
        close_button_object = util_obj.validate_and_get_webdriver_object(close_button_css, 'Close window button')
        core_util_obj.left_click(close_button_object)
        
        """
        Step 5: Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()