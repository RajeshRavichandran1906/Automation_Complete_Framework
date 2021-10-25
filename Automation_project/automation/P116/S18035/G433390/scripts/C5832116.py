'''
Created on January 4, 2019

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5832116
Testcase Name : Verify 3D Surface in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base

class C5832116_TestClass(BaseTestCase):

    def test_C5832116(self):
        """
            TESTCASE Functions Object
        """
        base_obj = base.BasePage(self.driver)
        chart_obj = chart.Chart(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        
        """
        Test case css
        """
        x_axis_css = "#pfjTableChart_1 text[class^='xaxis']"
        y_axis_css = "#pfjTableChart_1 text[class^='yaxis']"
        run_window_css = "#MAINTABLE_wbody0_f"
        
        """
        Test case variables
        """
        three_d_x_labels = ['Capuccino', 'Espresso']
        three_d_y_labels = ['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000', '3,000,000', '3,500,000', '4,000,000']
        three_d_z_labels = ['Dollar Sales', 'Unit Sales']
        x_axis_labels = ['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        y_axis_labels = ['0', '2M', '4M', '6M', '8M', '10M', '12M']
        three_d_y_axis_labels = ['0', '2,000,000', '4,000,000', '6,000,000', '8,000,000', '10,000,000', '12,000,000']
        legends = ['Dollar Sales', 'Unit Sales']
        chart_title = 'Dollar Sales, Unit Sales by Product'
        
        """
        Step 1: Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 2: Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FS18035%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
        Step 3: Change output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
        Step 4: Add fields Product, Dollar Sales, Unit Sales.
        """
        chart_obj.double_click_on_datetree_item('Product', 1)
        chart_obj.wait_for_number_of_element(x_axis_css, 3, base_obj.chart_medium_timesleep)
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        chart_obj.wait_for_number_of_element(y_axis_css, 10, base_obj.chart_medium_timesleep)
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_number_of_element(y_axis_css, 9, base_obj.chart_medium_timesleep)
        
        """
        Step 5: Click the Run button.
        Expect to see the following Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0 text[class^='xaxis']", 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_axis_labels, parent_css="#MAINTABLE_wbody0", msg='Step 5.1 : Verify x-label')
        chart_obj.verify_y_axis_label_in_run_window(y_axis_labels, parent_css="#MAINTABLE_wbody0", msg='Step 5.2 : Verify y-label')
        active_chart_obj.verify_legends_in_run_window(legends, parent_css=run_window_css, msg='Step 5.3: Verify the legends')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 5.4: Verify the title', parent_css='#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, parent_css=run_window_css, msg='Step 5.5: Verify the number of risers')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', parent_css=run_window_css, attribute='fill', msg='Step 5.6: Verify the blue riser colour')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('rect[class="riser!s1!g0!mbar!"]', 'pale_green', parent_css=run_window_css, attribute='fill', msg='Step 5.7: Verify the green riser colour')
        chart_obj.switch_to_default_content()
        
        """
        Step 6: Select Format > Other.
        From Select a chart pop up choose 
        3D Surface.
        Click OK.
        Expect to see the Clustered bar chart converted into the Preview pane for 3D Surface.
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('threed', 'threed_surface', 13)
        active_chart_obj.verify_x_axis_label_in_preview(three_d_x_labels, msg='Step 6.1: Verify the x labels')
        active_chart_obj.verify_y_axis_label_in_preview(three_d_y_labels, msg='Step 6.2: Verify the y labels')
        active_chart_obj.verify_z_axis_label_in_preview(three_d_z_labels, msg='Step 6.3: Verify the z labels')
        active_chart_obj.verify_legends_in_preview(three_d_z_labels, msg='Step 6.4: Verify legends')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mbar!']", 'pale_green', attribute='fill', msg='Step 6.5: Verify the riser color')
        
        """
        Step 7: Click the Run button.
        Expect to see the following 3D Surface.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 10, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_axis_labels, parent_css=run_window_css, msg='Step 7.1: Verify the x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(three_d_y_axis_labels, parent_css=run_window_css, msg='Step 7.2: Verify y axis labels')
        active_chart_obj.verify_z_axis_label_in_run_window(legends, parent_css=run_window_css, msg='Step 7.3: Verify z axis labels')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window('path[class="riser!s1!g0!mbar!"]', 'pale_green', parent_css=run_window_css, attribute='fill', msg='Step 7.4: Verify the riser colour')
        active_chart_obj.verify_legends_in_run_window(legends, parent_css=run_window_css, msg='Step 7.5: Verify the legends')
        
        """
        Step 8: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()