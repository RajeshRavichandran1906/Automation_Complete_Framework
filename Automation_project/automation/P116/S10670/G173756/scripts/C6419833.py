'''
Created on Dec 27, 2018

@author: vpriya

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6419833
TestCase Name = Vertical Dual-Axis Absolute Line Graph
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import chart


class C6419833_TestClass(BaseTestCase):

    def test_C6419833(self):
        
        
        """
        CLASS OBJECTS
        """
        active_chartobj = active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        x_axis_label_preview=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        y_axis_label_preview=['0', '10', '20', '30', '40', '50']
        Preview_legend_list=['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        expected_xlabel_list_preview=['Capuccino : Coffee', 'Espresso : Coffee']
        expected_ylabel_list_preview=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        expected_legend_list_preview=['Budget Dollars', 'Budget Units', 'Unit Sales']
        expected_xlabel_list_run=['Biscotti : Food', 'Capuccino : Coffee', 'Coffee Grinder : Gifts', 'Coffee Pot : Gifts', 'Croissant : Food', 'Espresso : Coffee', 'Latte : Coffee', 'Mug : Gifts', 'Scone : Food', 'Thermos : Gifts']
        expected_ylabel_list_run=['0', '3M', '6M', '9M', '12M']
        expected_legend_list_run=['Budget Dollars', 'Budget Units', 'Unit Sales']
        
        """
        Step 1:Create a Chart with ggsales.mas
        Select AHTML as the output format.
        """
        active_chartobj.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        active_chartobj.change_output_format_type('active_report')
        active_chartobj.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        Expect to see the general Chart Preview panel.
        """
        active_chartobj.verify_field_listed_under_querytree('Axis', 'Vertical Axis', 1,"Step 01.1")
        active_chartobj.verify_field_listed_under_querytree('Axis', 'Horizontal Axis', 2,"Step 01.2")
        active_chartobj.verify_x_axis_label_in_preview(x_axis_label_preview, msg='Step 01.03')
        active_chartobj.verify_y_axis_label_in_preview(y_axis_label_preview, msg='Step 01.04')
        active_chartobj.verify_legends_in_preview(Preview_legend_list,legend_length=5,msg='Step 01.05')
        active_chartobj.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 01.06: Verify number of bar risers')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']",'bar_blue',msg="Step 01.07")
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g0!mbar!']",'pale_green',msg="Step 01.08")
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s2!g0!mbar!']",'dark_green',msg="Step 01.09")
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s3!g0!mbar!']",'pale_yellow_2',msg="Step 01.10")
        
        
        """
        Step 2:From the Format Tab select Chart Types, then Other, then 
        Vertical Dual-Axis Absolute Lines and
        Click OK.
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        time.sleep(2)
        active_chartobj.select_other_chart_type('line','vertical_dual_axis_absolute_line',4)
        
        """
        Expect to see the following Chart Preview, including areas for Horizontal axis and Vertical axis 1 & 2.
        """
        active_chartobj.verify_field_listed_under_querytree('Axis', 'Vertical Axis 1', 1,"Step 02.1")
        active_chartobj.verify_field_listed_under_querytree('Axis', 'Vertical Axis 2', 2,"Step 02.2")
        active_chartobj.verify_field_listed_under_querytree('Axis', 'Horizontal Axis', 3,"Step 02.3")
        active_chartobj.verify_x_axis_label_in_preview(x_axis_label_preview,msg='Step 02.04')
        active_chartobj.verify_y_axis_label_in_preview(y_axis_label_preview, msg='Step 02.05')
        active_chartobj.verify_legends_in_preview(Preview_legend_list,legend_length=5,msg='Step 02.06')
        active_chartobj.verify_number_of_risers_in_preview('path', 1, 5, msg='Step 02.07: Verify number of bar risers')

        """
        Step 3:Add field Category & Product under the Horizontal axis, then
        Budget Dollars & Budget Units under the 
        Vertical axis 1 and
        Unit Sales under the Vertical axis 2.
        Three measures are used because additional Measures cannot be distinguished on the graph.
        """
        active_chartobj.double_click_on_datetree_item('Product', 1)
        active_chartobj.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Product', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Category', 1)
        active_chartobj.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Product : Category', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Budget Dollars', 1)
        active_chartobj.wait_for_visible_text("text[class='yaxis-title']", 'Budget Dollars', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Budget Units', 1)
        active_chartobj.wait_for_number_of_element(".legend", 1, MEDIUM_WAIT_TIME)
        
        active_chartobj.drag_field_from_data_tree_to_query_pane('Unit Sales', 1, 'Vertical Axis 2')
        active_chartobj.wait_for_number_of_element("text[class='y2axis-title']", 1, MEDIUM_WAIT_TIME)
        
        
        """
        Expect to see the following Vertical Dual Axis Absolute Line Graph Preview panel.
        """
        active_chartobj.verify_x_axis_label_in_preview(expected_xlabel_list_preview,msg="Step:3.1")
        active_chartobj.verify_y_axis_label_in_preview(expected_ylabel_list_preview,msg="Step:3.2")
        active_chartobj.verify_y_axis_label_in_preview(['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 03.3')
        active_chartobj.verify_legends_in_preview(expected_legend_list_preview,legend_length=3,msg="Step:03.4")
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class*='riser!s1!g0!mline!']", 'pale_green', parent_css='#TableChart_1', attribute='stroke', msg='Step 03.5')


        """
        Step 4:Click the Run button to generate the Vertical Dual Axis Absolute Line Graph.
        """
        active_chartobj.run_chart_from_toptoolbar()
        active_chartobj.switch_to_frame()
        active_chartobj.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='riser!']", 3, MEDIUM_WAIT_TIME)
        
        """
        Expect top see the following Vertical Dual Axis Absolute Line Graph.
        Expect to see the three Measures in an Absolute Line Graph with separate Axis scales on left and right sides.
        """
        active_chartobj.verify_x_axis_label_in_run_window(expected_xlabel_list_run,msg="Step:04.1")
        active_chartobj.verify_y_axis_label_in_run_window(expected_ylabel_list_run,msg="Step:04.2")
        active_chartobj.verify_y_axis_label_in_run_window(['0', '200K', '400K', '600K', '800K', '1,000K'],xyz_axis_label_css="svg > g text[class^='y2axis-labels']",msg="Step:04.3")
        active_chartobj.verify_legends_in_run_window(expected_legend_list_run,legend_length=3,msg="Step 04.4")
        active_chartobj.verify_chart_color_using_get_css_property_in_run_window("path[class*='riser!s1!g0!mline!']", 'pale_green', attribute='stroke', msg='Step 04.5')
        active_chartobj.verify_x_axis_title_in_run_window(['Product : Category'], msg='Step 04.6')
        active_chartobj.verify_chart_title('Budget Dollars, Budget Units, Unit Sales BY Product, Category', msg='Step 04.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chartobj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 04.8', parent_css='#MAINTABLE_wmenu0')
        active_chartobj.verify_number_of_risers_in_run_window('path', 1, 3, msg='Step 04.9: Verify number of risers')
        active_chartobj.switch_to_default_content()
        
if __name__ == '__main__':
    unittest.main()    
