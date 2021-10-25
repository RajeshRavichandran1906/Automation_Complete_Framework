'''
Created on Dec 26, 2018

@author: Vpriya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7244581
Test Suite Link =  http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/20311&group_by=cases:section_id&group_id=542008&group_order=asc
Test Case Title =  Verify chart filter functionality in Vertical Absolute Line in others tab (under Format menu).
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart, chart,visualization
from common.lib import utillity

class C7244581_TestClass(BaseTestCase):

    def test_C7244581(self):
       
        """
        CLASS OBJECTS
        """
        active_chartobj = active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        X_axis_label_preview=['C141', 'C144']
        y_axis_label_preview=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M', '0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        preview_parent_css="TableChart_1"
        expected_label_list_run=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        x_axis_label_list_run=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        y_axis_label_list_run=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M']
        expected_tooltip_list=['6 points', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list_run=['Region:Northeast', 'Product ID:F101', 'Dollar Sales:907171', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        tooltip_list=['Region:Northeast', 'Product ID:F102', 'Dollar Sales:1802005', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        filter_tooltip=['Region:Northeast', 'Product ID:F103', 'Dollar Sales:1670818', 'Remove Filter']
        
        """
        STEP 01 : Log in to WebFOCUS http://machine:port/{alias}
        STEP 02 : Execute following URL to create Chart 
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS2031%2F
        """
        active_chartobj.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        
        """
        STEP 03 : Select Active Report as Output file format
        """
        active_chartobj.change_output_format_type('active_report')
        active_chartobj.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        STEP 04 :Click Format tab and click Other and Select Line chart
        """
        """
        STEP 05:From Select a chart pop up choose 'Vertical Absolute Line' Click OK
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        time.sleep(2)
        active_chartobj.select_other_chart_type('line', 'vertical_absolute_line', 1)
        active_chartobj.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 5, MEDIUM_WAIT_TIME)
        
        """
        STEP 06:Add fields as follows:
        Region under Rows,
        Unit Sales and Dollar Sales under Vertical Axis
        Product ID under Horizontal Axis
        """
        active_chartobj.drag_field_from_data_tree_to_query_pane('Region', 1, 'Rows')
        active_chartobj.wait_for_visible_text("text[class='rowHeader-label!']", 'Region', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Dollar Sales', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(8)", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Unit Sales', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(9)", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Product ID', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(11)", 'Product ID', MEDIUM_WAIT_TIME)
        
        """
        Expect to see the following chart
        """
        active_chartobj.verify_rows_label_in_preview(['Region', 'Midwest', 'Northeast', 'Southeast', 'West'], msg='Step 06.01')
        active_chartobj.verify_x_axis_label_in_preview(X_axis_label_preview, msg='Step 06.02')
        active_chartobj.verify_y_axis_label_in_preview(y_axis_label_preview, msg='Step 06.03')
        active_chartobj.verify_legends_in_preview(['Dollar Sales', 'Unit Sales'], msg='Step 06.04')
        active_chartobj.verify_number_of_risers('#TableChart_1 path', 2, 4, msg='Step 06.05: Verify total number of risers')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r1!c0!']", 'bar_blue', parent_css='#pfjTableChart_1',attribute='stroke',msg='Step 05.06')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mline!r1!c0!']", 'pale_green', parent_css='#pfjTableChart_1',attribute='stroke',msg='Step 05.06')
        chart_obj.verify_number_of_markers("#TableChart_1",1,2, msg="Step 06.05: Verify total number of Markers")
        
        """
        STEP 07:Click run.
        Verify output.
        """
        active_chartobj.run_chart_from_toptoolbar()
        active_chartobj.switch_to_frame()
        active_chartobj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        active_chartobj.verify_rows_label_in_run_window(expected_label_list_run,msg="Step 7.1")
        active_chartobj.verify_x_axis_label_in_run_window(x_axis_label_list_run,parent_css='#MAINTABLE_wbody0', msg='Step 07.02')
        active_chartobj.verify_y_axis_label_in_run_window(y_axis_label_list_run, parent_css='#MAINTABLE_wbody0', msg='Step 07.03')
        active_chartobj.verify_legends_in_run_window(['Dollar Sales', 'Unit Sales'],msg='Step 07.04')
        active_chartobj.verify_number_of_risers_in_run_window('g', 1, 4,msg="Step 07.05")
        
        """
        STEP 08:Select F101, F102 and F103 points for Unit Sales and Dollar Sales for Northeast region
        """
        source_elem=util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 circle[class='marker!s1!g3!mmarker!r1!c0!']","Source_elem")
        target_elem=util_obj.validate_and_get_webdriver_object("#MAINTABLE_wbody0 circle[class='marker!s0!g5!mmarker!r1!c0!']","target_elem")
        vis_obj.create_marker_lasso(source_elem, target_elem, source_xoffset=-20, source_yoffset=20, target_xoffset=70, target_yoffset=-30)
        
        """
        Step:9 Verify that chart filter context menu appears on the screen with these options:
        6 points
        Filter Chart
        Exclude from Chart
        """
        vis_obj.verify_lasso_tooltip(expected_tooltip_list,msg="Step:9 verify chart filter context menu appears")

        """
        Step:10 Click Filter chart and verify F101, F102 and F103 Product IDs are displayed.
        """
        vis_obj.select_lasso_tooltip("Filter Chart")
        active_chartobj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
        Step:11 Hover over F101 Dollar Sales point and verify this context menu appears:
        Region: Northeast
        Product ID: F101
        Dollar Sales: 907,171
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        chart_obj.verify_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', expected_tooltip_list_run,"Step 11:verify marker tooltip",parent_css="#MAINTABLE_wbody0",use_marker_enable=True)
    
        """
        Step:12 Click Exclude from chart
        """
        chart_obj.select_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', "Exclude from Chart", parent_css="#MAINTABLE_wbody0",use_marker_enable=True)
        active_chartobj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'Dollar Sales', MEDIUM_WAIT_TIME)

        """
        Step:13 Hover over F102 Dollar Sales point and verify this context menu appears:
        
        Region: Northeast
        Product ID: F102
        Dollar Sales: 1802005
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        chart_obj.verify_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', tooltip_list,"Step 13:verify marker tooltip",parent_css="#MAINTABLE_wbody0",use_marker_enable=True)
        
        """
        Step:14 Click Exclude from chart.
        
        Expect to see only points for F103 remain.
        The chart should not be blank or empty.
        A line need at least two values of the Dimension to draw a line.
        """
        chart_obj.select_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', "Exclude from Chart", parent_css="#MAINTABLE_wbody0",use_marker_enable=True)
        active_chartobj.verify_x_axis_label_in_run_window(['F103'],parent_css='#MAINTABLE_wbody0', msg='Step 14.01')
        
        """
        Step:15 Hover over F103 Dollar Sales point and verify this context menu appears:
        Region: Northeast
        Product ID: F102
        Dollar Sales: 1670818
        Remove Filter
        Expect to see the Tooltip values and only an option to Remove Filter.
        """
        active_chartobj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        chart_obj.verify_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', filter_tooltip,"Step 15:verify marker tooltip",parent_css="#MAINTABLE_wbody0",use_marker_enable=True)

        """
        Step:16 Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()