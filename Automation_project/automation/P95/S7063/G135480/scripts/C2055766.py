'''
Created on January 17, 2019

@author: Varun
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2055766
TestCase Name = Act Dash: X-axis labels always qualified w/ coordinated field (ACT-87)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.wftools import visualization
from common.wftools import report
from common.lib import core_utility
from common.wftools import active_report
from common.wftools import active_chart

class C2055766_TestClass(BaseTestCase):

    def test_C2055766(self):
        """
        Test case Object's
        """
        active_chart_obj = active_chart.Active_Chart(self.driver)
        active_report_obj = active_report.Active_Report(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        x_labels = ['ANDERSON', 'LOPEZ', 'SANCHEZ', 'SOPENA', 'WANG']
        y_labels = ['0', '20K', '40K', '60K', '80K', '100K']
        tooltip_list = ['DEPT:ACCOUNTING', 'LASTNAME:ANDERSON', 'SALARY:$32,400.00', 'Filter Chart', 'Exclude from Chart']
        
        """
        Test case CSS
        """
        query_tree_css = "#queryTreeColumn tr:nth-child({0}) td"
        
        """ 
        Step 1: Sign in to WebFOCUS as a basic user
        http://machine:port/{alias}
        Step 2: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/empdata&item=IBFS%3A%2FWFC%2FRepository%2FP95_S18043%2FG439418%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='ibisamp/empdata', report_css="#canvasContainer", no_of_element=1)
         
        """
        Step 3: In InfoAssist, select Chart. Select Measure SALARY (will be on the Y-axis) and select Dimension LASTNAME (will be on the X-axis).
        """
        visual_obj.select_ribbon_item('Insert','chart')
        chart_obj.wait_for_number_of_element("#pfjTableChart_1", 1, chart_obj.chart_medium_timesleep)
        chart_obj.double_click_on_datetree_item('SALARY', 1)
        chart_obj.wait_for_visible_text(query_tree_css.format('7'), 'SALARY', chart_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('LASTNAME', 1)
        chart_obj.wait_for_visible_text(query_tree_css.format('9'), 'LASTNAME', chart_obj.chart_short_timesleep)
         
        """
        Step 4: Drag DEPT to Coordinated.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane('DEPT', 1, 'Coordinated', 1)
        chart_obj.wait_for_visible_text(query_tree_css.format('15'), 'DEPT', chart_obj.chart_short_timesleep)
        chart_obj.verify_x_axis_label_in_preview(x_labels, msg='Step 4.1')
        chart_obj.verify_y_axis_label_in_preview(y_labels, msg='Step 4.2')
        chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', msg='Step 4.3')
        chart_obj.verify_x_axis_title_in_preview(['LASTNAME'], msg='Step 4.4')
        chart_obj.verify_y_axis_title_in_preview(['SALARY'], msg='Step 4.5')
        chart_obj.verify_number_of_risers('#pfjTableChart_1 rect', 1, 5, msg='Step 4.6')
 
        """
        Step 5: Run the report. The X-axis should not have long values of DEPT running diagonally down. 
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 6, chart_obj.chart_short_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_labels, msg='Step 5.1')
        active_chart_obj.verify_y_axis_label_in_run_window(y_labels, msg='Step 5.2')
        active_chart_obj.verify_x_axis_title_in_run_window(['LASTNAME'], msg='Step 5.3')
        active_chart_obj.verify_y_axis_title_in_run_window(['SALARY'],  msg='Step 5.4')
        active_chart_obj.verify_chart_title('SALARY by LASTNAME', 'Step 5.5: Verify the chart title', parent_css='#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', msg='Step 5.6')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 5, msg='Step 5.7')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 5.8', parent_css='#MAINTABLE_wmenu0')
         
        """
        Step 6: Back in the portal, run the attached original repro, C2055766.fex. Current behavior does not display the Department in the Title and the format has changed.
        """
        chart_obj.api_logout()
        active_report_obj.run_active_report_using_api('C2055766.fex', column_css='#MAINTABLE_wbody0_f [class="xaxisOrdinal-labels!g0!mgroupLabel!"]', synchronize_visible_element_text='ANDERSON', repository_path=folder_path)
        active_chart_obj.verify_x_axis_label_in_run_window(x_labels, msg='Step 6.1')
        active_chart_obj.verify_y_axis_label_in_run_window(y_labels, msg='Step 6.2')
        active_chart_obj.verify_x_axis_title_in_run_window(['LASTNAME'], msg='Step 6.3')
        active_chart_obj.verify_y_axis_title_in_run_window(['SALARY'],  msg='Step 6.4')
        active_chart_obj.verify_chart_title('SALARY by LASTNAME', 'Step 6.5: Verify the chart title', parent_css='#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'cerulean_blue', msg='Step 6.6')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 6.7: Verify the number of risers')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 6.8', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 7: Still in the last report, hover the mouse over one of the vertical bars. The full DEPT and LASTNAME value should appear.
        """
        active_chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", tooltip_list, msg='Step 7: Verify the tooltip')
        
        """
        Step 8: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()