"""-------------------------------------------------------------------------------------------
Created on June 19, 2019
@author: Basha/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22589383
Test Case Title =  Insight not available with Gauge chart
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from selenium.webdriver.common.by import By
from common.lib.utillity import UtillityMethods 

class C2509894_TestClass(BaseTestCase):

    def test_C2509894(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utility = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        format_css = "#FormatTab"
        chart_css = "#pfjTableChart_1"
        ok_button_css = "#qbSelectChartTypeDlgOkBtn"
        
        """
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Click Format > Run with > Insight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 3 : Click Format > Chart types Others > Special
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        chart.select_other_chart_type("special", "gauge", 1, close_dialog="None", verify_selection=False)
        
        """
            STEP 4 : Verify "Gauge" charts grayed out
        """ 
        chart_item = self.driver.find_element(By.CSS_SELECTOR, "#ChartTypeButton_Icon_Special_Gauges")
        style_value = chart_item.get_attribute("style")
        status = True if "opacity" in style_value and "0.2" in style_value else False
        msg = "Step {0} : Verify [{1}] is disabled in chart menu".format("4", "Gauge")
        utility.asequal(True, status, msg)
        
        """
            STEP 5 : Click Cancel to dismiss
        """
        chart.select_other_chart_type("special", "gauge", 1, close_dialog="ok", verify_selection=False)
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 6 : Click Format > Run with > Insight to unhighlight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")

        """
            STEP 7 : Click Format > Chart types Others > Special >
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        
        chart.select_other_chart_type("special", "gauge", "1", close_dialog="None", verify_selection=False)
        
        """
            STEP 8 : Verify "Gauge" charts not grayed out
        """
        chart_item = self.driver.find_element(By.CSS_SELECTOR, "#ChartTypeButton_Icon_Special_Gauges")
        style_value = chart_item.get_attribute("style")
        status = True if "opacity" not in style_value else False
        msg = "Step {0} : Verify [{1}] is enabled in chart menu".format("8", "Gauge")
        utility.asequal(True, status, msg)
        
        """
            STEP 9 : Select "Gauge" > OK
        """
        chart.select_other_chart_type("special", "gauge", 1, close_dialog="ok", verify_selection=False)
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 10 : Click Format > Run with
        """
        chart.switch_ia_ribbon_tab("Format")
        chart.wait_for_visible_text(format_css, "Features")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 11 : Verify "Insight" icon grayed out
        """
        chart.verify_ribbon_item_is_disabled("format_insight", "11")
        
        """
            STEP 12 : Click IA > Close > click No.
        """
        chart.close_ia_without_save()
        
        """
            STEP 13 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main()