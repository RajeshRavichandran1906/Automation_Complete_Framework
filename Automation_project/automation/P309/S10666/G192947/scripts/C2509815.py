'''
Created on Jun 20, 2019

@author: Pearlson Joyal

Test Case : http://172.19.2.180/testrail/index.php?/cases/view/2509815
TestCase Name : When Filter Shelf is open, tool tip should say Hide Filter
'''

import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.pages.insight_header import Insight_Header

class C2509815_TestClass(BaseTestCase):

    def test_C2509815(self):
        """
            CLASS OBJECTS 
        """
        chart_obj= chart.Chart(self.driver)
        insight = Insight_Header(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        querypane_css = "#queryBoxColumn"

        """
        STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                 http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite") 
         
        """
        STEP 2 : Add "Product, Category" and "Cost of Goods"
        """
        chart_obj.double_click_on_datetree_item('Product,Category', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Product,Category")
        chart_obj.double_click_on_datetree_item('Cost of Goods', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Cost of Goods")
         
        """
        STEP 3 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight")
         
        """
        STEP 4 : Click Run
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
         
        """
        STEP 5 : Hover over the filter icon in the Option Shelf
        STEP 6 : Verify tooltip displayed "Show Filter"
        """
        insight.verify_option_tooltip("Show Filter", "06.01")        
        
        """
        STEP 7 : Click the filter icon to display the Filter shelf
        """         
        chart_obj.select_header_option_item_in_insight("filter")
        
        """
        STEP 8 : Hover over the filter icon in the Option Shelf
        STEP 9 : Verify tool tip displayed "Hide Filter"
        """             
        insight.verify_option_tooltip("Hide Filter", "09.01")
        
        """
        STEP 10 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
         
        """
        STEP 11 : Logout using API
                  http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()