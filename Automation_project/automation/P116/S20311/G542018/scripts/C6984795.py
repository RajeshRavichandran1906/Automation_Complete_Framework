'''
Created on Nov 19, 2018

@author: KK14897
Testcase ID :  http://172.19.2.180/testrail/index.php?/cases/view/6984796
Testcase Name : Verify a chart shows correct filtered output once filter applied from context menu - Line Chart
'''
import unittest
from common.lib import utillity
from common.wftools import visualization
from common.wftools import active_chart, chart
from common.lib.basetestcase import BaseTestCase

class C6984795_TestClass(BaseTestCase):

    def test_C6984795(self):
        
        """
            TESTCASE OBJECTS
        """
        chart_obj=chart.Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        short_time=25
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
         
        """
            Step 01 : Log in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Execute following URL to create Chart
            http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS20311%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
            Step 03 : Change Output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
            Step 04 : From the Format tab, select Line Chart
        """
        chart_obj.select_ia_ribbon_item('Format', 'Line')
        
        """
            Step 05 : Select data from the left pane (Dimensions and Measures)
            Category under Columns
            Product under Horizontal Axis, & 
            Unit Sales under Vertical Axis
        """
        field_name1='Category'
        field_name2='Product'
        field_name3='Unit Sales'
        preview_expected_column_header_label=['Category : Product', 'Coffee']
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name1, 1, 'Columns', 1)
        
        css1="#"+preview_parent_css+" text[class='colHeader-label!']"
        chart_obj.wait_for_visible_text(css1, field_name1,short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name2, 1, 'Horizontal Axis', 1)
        chart_obj.wait_for_visible_text(css1, 'Category : Product', short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name3, 1, 'Vertical Axis', 1)
        chart_obj.wait_for_visible_text(preview_yaxis_title_css, field_name3, short_time)
        
        """ See corresponding data is displayed in the Live Preview pane."""
        
        exp_yaxis_title_list=['Unit Sales','Unit Sales', 'Unit Sales']
        preview_expected_label_list=['Capuccino', 'Espresso']
        preview_expected_yaxis_label_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        
        chart_obj.verify_y_axis_title_in_preview(exp_yaxis_title_list, msg="Step 05.01")
        chart_obj.verify_column_label(preview_expected_column_header_label, "#"+preview_parent_css, msg='Step 05.02')
        chart_obj.verify_x_axis_label_in_preview(preview_expected_label_list, msg="Step 05.03")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, msg="Step 05.04:")
        
        """
            Step 06:Click the Run button.
        """ 
        chart_obj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=2)
        run_parent_css="MAINTABLE_wbody0"
        run_exp_yaxis_title="#"+run_parent_css+" .chartPanel text[class*='yaxis-title']"
        
        chart_obj.wait_for_visible_text(run_exp_yaxis_title, field_name3)
        run_exp_yaxis_label_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        run_exp_xaxis_label_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
#         run_exp_xaxis_title_list=['Product']
        run_exp_column_label=['Category : Product', 'Coffee', 'Food', 'Gifts']
        
        expected_toolbar_menu_list=['More Options','Advanced Chart','Original Chart', 'Aggregation', 'Sum']
        run_exp_chart_title="Unit Sales by Category, Product"
        active_menubar_css="#MAINTABLE_wmenu0"
        
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 06.01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 06.02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 06.03")
#         chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:04")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 06.04", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 06.05", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 06.06')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='marker!s0!g5!mmarker!r0!c0!']", 1, 50)
        
        """ Step 07 : Hover over on Espresso point in the middle of the Coffee Line chart. Verify context menu displays:
        """
        expected_tooltip=['Category:Coffee', 'Product:Espresso', 'Unit Sales:308986', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_in_run_window('marker!s0!g5!mmarker!r0!c0!', expected_tooltip, 'Step 07.01: Verify Espresso bar tooltip list', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        """ Step 08 :Left-click and drag a box that covers Capuccino and Espresso.
        """
        left_element = utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 [class*='marker!s0!g1!mmarker!r0!c0!']", 'Capuccino')
        right_element =utillobj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 [class*='marker!s0!g5!mmarker!r0!c0!']",'Espresso')
        visual_obj.create_marker_lasso(left_element,right_element,target_xoffset=20,target_yoffset=10)
        
        """ Step 09 : Click Filter Chart
        """
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        """
        Step 10: Click Remove Filter option.
        Verify original chart appears in the output.
        Make sure filter icon is not present.
        """
        column_label_list = ['Category : Product','Coffee','Food','Gifts']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 10.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 3, parent_css="#MAINTABLE_wbody0", msg="Step 10.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 10.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 10.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 10.7',attribute='stroke')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class*='marker!s0!g2!mmarker!r0!c2!']", 1, 50)
        
        """ Step 11 : Hover over the Coffee Grinder point on the Gifts chart. Verify context menu displays:
        """
        expected_tooltip_1=['Category:Gifts', 'Product:Coffee Grinder', 'Unit Sales:186534', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_in_run_window('marker!s0!g2!mmarker!r0!c2!', expected_tooltip_1, 'Step 9.1: Verify Capuccino bar tooltip list', parent_css="#MAINTABLE_wbody0",yoffset=10,use_marker_enable=True)
        
        """ Step 12 : Click Exclude from Chart option.
            Verify the Coffee Grinder Product is removed from the GIFTS Category and that 3 points remain.
            Also verify that the filter icon appears on the Active tool bar.
        """
        visual_obj.select_tooltip('marker!s0!g2!mmarker!r0!c2!','Exclude from Chart',parent_css="MAINTABLE_wbody0",initial_move_xy_dict={'x':1516,'y':784},yoffset=10,use_marker_enable=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 12.1: Verify Filter Button not Visible')
        
        """
        Step 13: Click Remove Filter option.
        Verify original chart appears in the output.
        Make sure filter icon is not present.
        """
        column_label_list = ['Category : Product','Coffee','Food','Gifts']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 13.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 3, parent_css="#MAINTABLE_wbody0", msg="Step 13.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 13.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 13.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 13.7',attribute='stroke')
        
        """
            Step 14 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()