"""-------------------------------------------------------------------------------------------
Created on July 01, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22592962&group_by=cases:section_id&group_id=159427&group_order=asc
Test Case Title =  SCATTER AHTML:JSCHART:Mouse hover shown NaN for X-axis title
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods

class C2276154_TestClass(BaseTestCase):

    def test_C2276154(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        
        """
            STEP 1 : Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159427&tool=chart&master=ibisamp/car
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
            STEP 2 : Select Format tab > Chart types > Scatter.
        """
        chart.select_ia_ribbon_item("Format", "scatter")
        utils.synchronize_until_element_is_visible("path[class='riser!s0!g2!mmarker!']", 30)
        
        """
            STEP 3 : Double click "RETAIL_COST".
        """
        chart.double_click_on_datetree_item("RETAIL_COST", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "RETAIL_COST")

        """
            STEP 4 : Drag/drop "COUNTRY" to horizontal axis
        """
        chart.drag_field_from_data_tree_to_query_pane("COUNTRY", 1, "Horizontal Axis", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "COUNTRY")
        
        """
            STEP 5 : Change output format "Active report
        """
        chart.change_output_format_type("active_report")

        """
            STEP 6 : Click Run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#MAINTABLE_0_fmg", "ENGLAND")

        """
            STEP 7 : Hover over the scatter chart
            STEP 8 : Verify tool tip should not displayed "NAN" Value
        """
        chart.verify_tooltip_in_run_window("riser!s0!g0!mmarker!", ['COUNTRY:ENGLAND', 'RETAIL_COST:45,319', 'Filter Chart', 'Exclude from Chart'], parent_css = "#MAINTABLE_0_fmg",  msg="STEP 8 : Verify tool tip should not displayed 'NAN' Value")
        chart.switch_to_default_content()

        """
            STEP 9 : Logout using API
            http://domain:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        

if __name__ == '__main__':
    unittest.main() 