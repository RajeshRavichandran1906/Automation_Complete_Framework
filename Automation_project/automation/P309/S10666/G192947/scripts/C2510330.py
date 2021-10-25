"""-------------------------------------------------------------------------------------------
Created on June 24, 2019
@author: Niranjan/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2510330
Test Case Title =  "Change Bin Size" option to change histogram bin value
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.wftools.designer_chart import Designer_Insight
from common.pages.insight_header import Insight_Header
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C2510330_TestClass(BaseTestCase):

    def test_C2510330(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        insight = Designer_Insight(self.driver)
        insight_header= Insight_Header(self.driver)
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        chart_css = "#pfjTableChart_1"
        insight_chart_css = "body[class='ibx-root er-root ibx-loaded ibx-visible']"
        insight_parent_css = "#runbox_id"

        """ 
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
             STEP 2 : Select Format > Run with > Insight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 3 : Click Run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(insight_chart_css, "Vertical Axis")
        
        """
            STEP 4 : Click Chart picker drop down > Select Histogram chart
        """
        insight.select_chart_from_chartpicker("Histogram")
        
        """
            STEP 5 : Add "DEALER_COST" to Measure bucket
        """
        insight_header.search_and_add_field_to_query_bucket("Measure", "DEALER_COST")
        chart.wait_for_visible_text("#runbox_id", "CNT")
        
        """
            STEP 6 : Verify following Histogram chart has been displayed
        """
        chart.verify_x_axis_label_in_run_window(['2,620', '2,880', '4,290', '4,630', '4,910', '5,060', '5,660', '5,800', '6,000', '7,420', '8,300', '8,400', '10,000', '11,000', '11,190', '14,940', '25,000'], msg = "Step 6.01", parent_css = insight_parent_css)
        chart.verify_y_axis_label_in_run_window(['0', '0.4', '0.8', '1.2', '1.6', '2', '2.4'], parent_css =insight_parent_css, msg = "step 6.02")
        chart.verify_x_axis_title_in_run_window(['DEALER_COST_BIN_1'], parent_css = insight_parent_css, msg = "step 6.03")
        chart.verify_y_axis_title_in_run_window(['CNT DEALER_COST'], parent_css = insight_parent_css, msg = "step 6.04")
        chart.verify_number_of_risers("#runbox_id rect", 1, 17, msg = "step 6.05")
        
        """
            STEP 7 : Select the More Options icon (three vertical dots) > Change Bin size
        """
        insight_header.select_or_verify_more_option_menu_item("Change Bin Size")
        chart.wait_for_visible_text("div[class^='insight']", "Change")
        
        """
            STEP 8 : Verify "Change Bin Size"popup displayed
        """
        utils.verify_object_visible("div[class^='insight']", True, "STEP 08.01 : Verify 'Change Bin Size' popup displayed")
        
        """
            STEP 9 : Enter "100" to Bin Size > Click OK
        """
        bin_textbox = utils.validate_and_get_webdriver_object("div[class^='insight'] [class^='bin-text-field'] input", "Bin Textbox")
        coreutils.left_click(bin_textbox)
        bin_textbox.clear()
        bin_textbox.send_keys("100")
        ok_button_obj = utils.validate_and_get_webdriver_object("div[class^='insight'] [class^='ibx-dialog-ok-button']", "Ok button")
        coreutils.left_click(ok_button_obj)
        chart.wait_for_visible_text("#runbox_id", "CNT")
        
        """
            STEP 10 : Verify chart Horizontal value updated
        """
        chart.verify_x_axis_label_in_run_window(['2,600', '2,800', '4,200', '4,600', '4,900', '5,000', '5,600', '5,800', '6,000', '7,400', '8,300', '8,400', '10,000', '11,000', '11,100', '14,900', '25,000'], parent_css = insight_parent_css, msg = "Step 10.01",)
        chart.verify_y_axis_label_in_run_window(['0', '0.4', '0.8', '1.2', '1.6', '2', '2.4'], parent_css =insight_parent_css, msg = "step 10.02")
        chart.verify_x_axis_title_in_run_window(['DEALER_COST_BIN_1'], parent_css = insight_parent_css, msg = "step 10.03")
        chart.verify_y_axis_title_in_run_window(['CNT DEALER_COST'], parent_css = insight_parent_css, msg = "step 10.04")
        chart.verify_number_of_risers("#runbox_id rect", 1, 17, msg = "step 10.05")
        chart.switch_to_default_content()

        """
            STEP 11 : Click IA > Close > click No.
        """
        chart.close_ia_without_save()
 
        """
            STEP 12 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
 
if __name__ == '__main__':
    unittest.main()   