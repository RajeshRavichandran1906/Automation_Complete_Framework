"""-------------------------------------------------------------------------------------------
Created on June 25, 2019
@author: Magesh/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22589398
Test Case Title =  Verify on Hovering x (delete) icon in the bucket should display a hand symbol 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.designer_chart import Designer_Insight
from common.lib.utillity import UtillityMethods

class C5852521_TestClass(BaseTestCase):

    def test_C5852521(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        insight=Designer_Insight(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"

        """
            STEP 1 : Launch the IA API with chart:
            http://machine:port/alias/ia?&item=IBFS:/WFC/Repository/P309_S10666/G169735&tool=chart&master=ibisamp/car
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Double click on fields "COUNTRY" and "SALES"
        """
        chart.double_click_on_datetree_item("COUNTRY", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "COUNTRY")
        
        chart.double_click_on_datetree_item("SALES", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "SALES")
        
        """
            STEP 02.01 : Verify the canvas,
        """
        chart.verify_x_axis_title_in_preview(['COUNTRY'], msg="step 02.01")
        chart.verify_y_axis_title_in_preview(['SALES'], msg="step 02.02")
        chart.verify_x_axis_label_in_preview(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg="step 02.03")
        chart.verify_y_axis_label_in_preview(['0', '20K', '40K', '60K', '80K', '100K'], msg="step 02.04")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 5, msg="step 02.05")
        
        """
            STEP 3 : Select Format tab > Run With > Insight
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
 
        """
            STEP 4 : Click RUN
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("#runbox_id", "COUNTRY")
            
        """
            STEP 04.01 : Verify the output,
        """
        chart.verify_x_axis_title_in_run_window(['COUNTRY'], parent_css="#runbox_id", msg="step 04.01")
        chart.verify_y_axis_title_in_run_window(['SALES'], parent_css="#runbox_id", msg="step 04.02")
        chart.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], parent_css="#runbox_id", msg="step 04.03" )
        chart.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K'], parent_css="#runbox_id", msg="step 04.04")
        chart.verify_number_of_risers("#runbox_id rect", 1, 5, msg="step 04.05")
        
        insight.verify_insight_querybox_text_options(['Vertical Axis', 'Group', 'Color'], msg="step 04.06")
        insight.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], msg="step 04.07")

        """
            STEP 5 : Now hover over on "SALES" on Insight right top corner.
        """
        Sales_obj = utils.validate_and_get_webdriver_object(".bla_vertical_axis_bucket-buckets", "Sales Css")
        core_utils.move_to_element(Sales_obj)
        
        """
            STEP 6 : Verify the (x) icon appears
        """
        utils.verify_picture_using_sikuli("C5852521_step6.png", "STEP 6 : Verify the (x) icon appears")

        """
            STEP 7 : Hover over on the (x) icon symbol
        """
        actual_mouse_symbol = utils.validate_and_get_webdriver_object(".bla_vertical_axis_bucket-buckets .fa-times", "cross css")
        core_utils.python_move_to_element(actual_mouse_symbol)
        
        """
            STEP 07.01 : Verify that clickable items to have a "hand" hover icon to show it can be clicked,
        """
        actual_mouse_symbol = utils.validate_and_get_webdriver_object(".bla_vertical_axis_bucket-buckets .fa-times", "cross css").value_of_css_property("cursor")
        utils.asequal("pointer", actual_mouse_symbol, "Step 07.01" )
        
        """
            STEP 8 : Click IA > Close > click No.
        """
        chart.switch_to_default_content()
        chart.close_ia_without_save()
        
        """
            STEP 9 :Logout:
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main() 