'''
Created on Dec 27, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419831
Test Case Title =  Horizontal Dual-Axis Clustered Bar Chart
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart
from common.lib import utillity

class C6419831_TestClass(BaseTestCase):

    def test_C6419831(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        preview_parent_css="TableChart_1"
        
        """
        STEP 01 : Log in to WebFOCUS: http://machine:port/{alias}
        STEP 02 : Open IA.
        Create a Chart with ggsales.mas
        Select AHTML as the output format.
        """
        active_chart.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chart.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        active_chart.change_output_format_type('active_report')
        active_chart.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        Expect to see the following generalized Preview panel.
        """
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 02.01')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 02.02')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 02.03')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 02.04: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#TableChart_1', msg='Step 02.05')
        
        """
        Step 03 : From the Format Tab select Chart Types, then Other, then
        Horizontal Dual-Axis Clustered Bars and
        Click OK. 
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chart.select_other_chart_type('bar', 'horizontal_dual_axis_clustered_bars', 16)
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" svg > g text[class^='y2axis-labels']", 10, MEDIUM_WAIT_TIME)
        
        """
        Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """
        active_chart.verify_field_listed_under_querytree('Axis', 'Vertical Axis', 1)
        active_chart.verify_field_listed_under_querytree('Axis', 'Horizontal Axis 1', 2)
        active_chart.verify_field_listed_under_querytree('Axis', 'Horizontal Axis 2', 3)
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 03.01')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 03.02')
        active_chart.verify_y_axis_label_in_preview(['0', '5', '10', '15', '20', '25', '30', '35', '40', '45'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 03.03')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 03.04')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 03.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#TableChart_1', msg='Step 03.06')
        
        
        """
        STEP 04 : Add field Product under Vertical axis, then
        Unit Sales & Budget Units under Horizontal axis 1 and
        Dollar Sales & Budget Dollars under Horizontal axis 2
        """
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Product', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Unit Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Budget Units', 1)
        active_chart.wait_for_number_of_element(".legend", 1, MEDIUM_WAIT_TIME)
        
        active_chart.drag_field_from_data_tree_to_query_pane('Dollar Sales', 1, 'Horizontal Axis 2')
        active_chart.wait_for_visible_text("text[class='y2axis-title']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        active_chart.drag_field_from_data_tree_to_query_pane('Budget Dollars', 1, 'Horizontal Axis 2', bucket_position=2)
        active_chart.wait_for_visible_text("text[class='legend-labels!s3!']", 'Budget Dollars', MEDIUM_WAIT_TIME)
        
        """
        Expect to see the following Horizontal Dual Axis Clustered Bar Preview panel.
        """
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" rect[class*='riser!']", 8, MEDIUM_WAIT_TIME)
        active_chart.verify_x_axis_label_in_preview(['Capuccino', 'Espresso'], msg='Step 04.01')
        active_chart.verify_y_axis_label_in_preview(['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K'], msg='Step 04.02')
        active_chart.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 04.3')
        active_chart.verify_x_axis_title_in_preview(['Product'], msg='Step 04.4')
        active_chart.verify_legends_in_preview(['Unit Sales', 'Budget Units', 'Dollar Sales', 'Budget Dollars'], msg='Step 04.5')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 8, msg='Step 04.6: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#TableChart_1', msg='Step 04.7')
        
        """
        STEP 05 : Click the Run button to generate the Horizontal Dual Axis Clustered Bar Chart.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 40, MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Expect to see the following Horizontal Dual Axis Clustered Bar Chart.
        Expect to see two sets of Axis scales on the top and bottom of the graph.        
        """
        active_chart.verify_x_axis_label_in_run_window(['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], msg='Step 05.1')
        active_chart.verify_y_axis_label_in_run_window(['0', '3M', '6M', '9M', '12M'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 05.2')
        active_chart.verify_y_axis_label_in_run_window(['0', '200K', '400K', '600K', '800K', '1,000K'], msg='Step 05.3')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 40, msg='Step 05.4: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 05.5')
        active_chart.verify_x_axis_title_in_run_window(['Product'], msg='Step 05.6')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Budget Units', 'Dollar Sales', 'Budget Dollars'], msg='Step 05.7')
        active_chart.verify_chart_title('Unit Sales, Budget Units, Dollar Sales, Budget Dollars BY Product', msg='Step 05.8', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.9', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 06 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()