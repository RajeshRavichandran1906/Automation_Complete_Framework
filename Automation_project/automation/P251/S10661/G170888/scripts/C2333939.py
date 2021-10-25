"""-------------------------------------------------------------------------------------------
Created on July 01, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22593265
Test Case Title =  Verify Matrix pie chart with no data values
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods

class C2333939_TestClass(BaseTestCase):

    def test_C2333939(self):
        
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
            STEP 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S10661%2FG170888&tool=chart&master=ibisamp/car
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(chart_css, "Group 0")
 
        """
            STEP 2 : Click Format tab > PIE chart in chart types
        """
        chart.select_ia_ribbon_item("Format", "pie")
        utils.synchronize_until_element_is_visible("path[class='riser!s0!g0!mwedge!']", 30)
 
        """
            STEP 3 : Double click 'Car' and 'Sales'
        """
        chart.double_click_on_datetree_item("CAR", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "CAR")

        chart.double_click_on_datetree_item("SALES", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "SALES")
        
        """
            STEP 4 : Drag and drop 'Sales' to Rows and Columns bucket to add
        """
        chart.drag_field_from_data_tree_to_query_pane("SALES", 1, "Rows", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "SALES")
        
        chart.drag_field_from_data_tree_to_query_pane("SALES", 1, "Columns", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "SALES")

        """
            STEP 5 : Verify following preview displayed
            STEP 05.01 : Expected to see for no data values should not be displayed empty pie
        """
        chart.verify_number_of_risers("#pfjTableChart_1 path[class*='mwedge']", 1, 13, msg="step 05.01")
        chart.verify_legends_in_preview(['CAR', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg="step 05.02")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mwedge!r1!c1!", "bar_blue", msg="step 05.03 verify color")
        chart.verify_chart_color("pfjTableChart_1", "riser!s2!g0!mwedge!r3!c3!", "dark_green", msg="step 05.04 verify color")
        chart.verify_chart_color("pfjTableChart_1", "riser!s3!g0!mwedge!r12!c12!", "pale_yellow_2", msg="step 05.05 verify color")
        chart.verify_chart_color("pfjTableChart_1", "riser!s4!g0!mwedge!r5!c5!", "sunset_orange", msg="step 05.06 verify color")
        chart.verify_rows_label_in_preview(['SALES', '0', '4800', '7800', '8900', '8950', '12000', '12400'], msg="step 05.07")
        chart.verify_column_label_in_preview(['SALES', '0', '4800', '7800', '8900', '8950', '12000', '12400', '13000', '14000', '15600', '18940'], msg="step 05.08")
        chart.verify_pie_label_in_single_group_in_preview(['SALES', 'SALES', 'SALES', 'SALES', 'SALES', 'SALES', '', '', '', '', '', '', ''], msg="step 05.09")
        chart.verify_chart_color("pfjTableChart_1", "riser!mwedge!r0!c0!", "white", msg="step 05.10")
        
        """
            STEP 6 : Click Run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#jschart_HOLD_0", "SALES")

        """
            STEP 7 : Hover on run time chart and verify tooltip values
        """
        chart.verify_tooltip_in_run_window("riser!s0!g0!mwedge!r1!c1!", ['SALES:4800', 'SALES:4800', 'CAR:ALFA ROMEO', 'SALES:4800  (100.00%)'], msg="STEP 7 : Hover on run time chart and verify tooltip values")
        
        """
            STEP 8 : Click IA > Close > click No.
        """
        chart.switch_to_default_content()
        chart.close_ia_without_save()

        """
            STEP 9 : Logout using API (without saving)
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main() 