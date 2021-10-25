'''
Created on Dec 27, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419836
Test Case Title =  Horizontal Dual-Axis Stacked Line Graph 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart
from common.lib import utillity

class C6419836_TestClass(BaseTestCase):

    def test_C6419836(self):
       
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
        Horizontal Dual-Axis Stacked Line Graph and
        Click OK.   
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chart.select_other_chart_type('line', 'horizontal_dual_axis_stacked_line', 11)
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 5, MEDIUM_WAIT_TIME)
        
        """
        Expect to see the following Chart Preview, including areas for Vertical 1 and 2, along with Horizontal axis.
        """
        active_chart.verify_field_listed_under_querytree('Axis', 'Vertical Axis', 1)
        active_chart.verify_field_listed_under_querytree('Axis', 'Horizontal Axis 1', 2)
        active_chart.verify_field_listed_under_querytree('Axis', 'Horizontal Axis 2', 3)
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 03.01')
        active_chart.verify_y_axis_label_in_preview(['0', '20', '40', '60', '80', '100', '120'], msg='Step 03.02')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50', '60', '70', '80'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 03.03')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 03.4')
        active_chart.verify_number_of_risers_in_preview('path', 1, 5, msg='Step 03.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!']", 'bar_blue', parent_css='#TableChart_1', attribute='stroke', msg='Step 03.6')
        
        """
        STEP 04 : Add field Category & Product under the Vertical axis, then
        Budget Dollars & Budget Units under the Horizontal axis 1 and
        Unit Sales under the Horizontal axis 2.
        Three measures are used because additional Measures cannot be distinguished on the graph.
        """
        active_chart.double_click_on_datetree_item('Category', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Category', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Category : Product', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Budget Dollars', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Budget Dollars', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Budget Units', 1)
        active_chart.wait_for_number_of_element(".legend", 1, MEDIUM_WAIT_TIME)
        
        active_chart.drag_field_from_data_tree_to_query_pane('Unit Sales', 1, 'Horizontal Axis 2')
        active_chart.wait_for_visible_text("text[class='y2axis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        """
        Expect to see the following Horizontal Dual Axis Stacked Line Graph Preview panel.  
        """
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 3, MEDIUM_WAIT_TIME)
        active_chart.verify_x_axis_label_in_preview(['Coffee : Capuccino', 'Coffee : Espresso'], msg='Step 04.01')
        active_chart.verify_y_axis_label_in_preview(['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 04.02')
        active_chart.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M'], msg='Step 04.3')
        active_chart.verify_x_axis_title_in_preview(['Category : Product'], msg='Step 04.4')
        active_chart.verify_y_axis_title_in_preview(['Unit Sales'], x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 04.5')
        active_chart.verify_legends_in_preview(['Budget Dollars', 'Budget Units', 'Unit Sales'], msg='Step 04.6')
        active_chart.verify_number_of_risers_in_preview('path', 1, 3, msg='Step 04.7: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!']", 'bar_blue', parent_css='#TableChart_1', attribute='stroke', msg='Step 04.8')
        
        """
        STEP 05 : Click the Run button to generate the Horizontal Dual Axis Stacked Line Graph.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='riser!']", 3, MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Expect top see the following Horizontal Dual Axis Stacked Line Graph.
        Expect to see the three Measures in an Stacked Line Graph with separate Axis scales on the top and bottom of the graph.
        """
        active_chart.verify_x_axis_label_in_run_window(['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos'], msg='Step 05.1')
        active_chart.verify_y_axis_label_in_run_window(['0', '200K', '400K', '600K', '800K', '1,000K'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 05.2')
        active_chart.verify_y_axis_label_in_run_window(['0', '3M', '6M', '9M', '12M', '15M'], msg='Step 05.3')
        active_chart.verify_number_of_risers_in_run_window('path', 1, 3, msg='Step 05.4: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', attribute='stroke', msg='Step 05.5')
        active_chart.verify_x_axis_title_in_run_window(['Category : Product'], msg='Step 05.6')
        active_chart.verify_y_axis_title_in_run_window(['Unit Sales'], x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 05.7')
        active_chart.verify_legends_in_run_window(['Budget Dollars', 'Budget Units', 'Unit Sales'], msg='Step 05.8')
        active_chart.verify_chart_title('Budget Dollars, Budget Units, Unit Sales BY Category, Product', msg='Step 05.9', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.10', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 06 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()