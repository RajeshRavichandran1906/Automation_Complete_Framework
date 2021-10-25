'''
Created on January 8, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2104970
TestCase Name = AHTML: Active Bar Chart with bucket syntax filters only first BY on the X axis (ACT-605).
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base
from common.lib import utillity
from common.wftools import visualization

class C2104970_TestClass(BaseTestCase):

    def test_C2104970(self):
        
        """
        Test case Object's
        """
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        latte_tool_tip = ['Category:  Coffee', 'Product:  Latte', 'Unit Sales:  878063', 'Filter Chart', 'Exclude from Chart']
        latte_remove_x_label = ['Coffee : Capuccino', 'Coffee : Espresso', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 'Gifts : Coffee Grinder', 
                                'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
        x_label = ['Coffee : Capuccino', 'Coffee : Espresso']
        y_label = ['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        run_x_label = ['Coffee : Capuccino', 'Coffee : Espresso', 'Coffee : Latte', 'Food : Biscotti', 'Food : Croissant', 'Food : Scone', 
                       'Gifts : Coffee Grinder', 'Gifts : Coffee Pot', 'Gifts : Mug', 'Gifts : Thermos']
        run_y_label = ['0', '2M', '4M', '6M', '8M', '10M', '12M']
        chart_title = "Unit Sales, Dollar Sales BY Category, Product"
        left_click_tooltip = ['1 point', 'Filter Chart', 'Exclude from Chart']
        group_x_labels = ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        group_y_labels = ['0', '10', '20', '30', '40', '50']
        legend_series = ['Series0', 'Series1', 'Series2', 'Series3', 'Series4']
        
        """
        Test case CSS
        """
        latte_css = "#MAINTABLE_wbody0_f [class='riser!s0!g2!mbar!']"
        
        """ 
        Step 1: Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2: Launch IA Chart using below API link
        http://machine:port/{alias}/iatool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP95_S7063%2FG135480%2FF
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales',mrid='mriddev',mrpass='mrpassdev')
        
        """
        Step 3 : On the Format tab, in the Output Types group, click Active report.
        Expect to see the following empty canvas for the Car file.
        """
        chart_obj.change_output_format_type('active_report')
        chart_obj.verify_x_axis_label_in_preview(group_x_labels, msg='Step 3.1 verify the x axis labels')
        chart_obj.verify_y_axis_label_in_preview(group_y_labels, msg='Step 3.2 verify the y axis labels')
        chart_obj.verify_legends_in_preview(legend_series, msg='Step 3.3: Verify legends')
        
        """
        Step 4 : Select Category & Product for the Horizontal axis and Unit Sales & Dollar Sales for the Vertical axis.
        Expect to see the following Preview pane, with two Measures and two Dimensions.
        The Dimensions(sorts) are in the Horizontal axis area and the Measures(summed fields) are in the Vertical axis area of the Query panel.
        """
        chart_obj.double_click_on_datetree_item('Category', 1)
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='xaxis']", 2, base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('Product', 1)
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='xaxis']", 3, base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='yaxis']", 9, base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1) 
        chart_obj.wait_for_visible_text("#pfjTableChart_1 text[class='legend-labels!s1!']", 'Dollar Sales', base_obj.chart_short_timesleep)
        chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 4.1 verify the x axis labels')
        chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 4.2 verify the y axis labels')
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Unit Sales', 1, "Step 4.3")
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Dollar Sales', 2, "Step 4.4")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Category', 1, "Step 4.5")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Product', 2, "Step 4.6")
        
        """
        Step 5: Click the Run button.
        Expect to see the following Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 11, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(run_x_label, msg="Step 5.1: Verify x axis ")
        active_chart_obj.verify_y_axis_label_in_run_window(run_y_label, msg='Step 5.2: Verify y axis')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 5.3: Verify Chart title', parent_css = '#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", 'bar_blue', attribute='fill', msg='Step 5.4: Verify bar colour')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g1!mbar!']", 'pale_green', attribute='fill', msg='Step 5.5: Verify bar colour')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, msg='Step 5.6: Verify number of risers')
        
        """
        Step 6: Hover over the Unit Sales bar for Coffee/Latte.
        Expect to see the values and Chart exclusion selections.
        """
        chart_obj.verify_active_chart_tooltip('MAINTABLE_wbody0_f', 'riser!s0!g2!mbar!', latte_tool_tip, msg='Step 6.1: Verify latte tooltip')
        
        """
        Step 7: Left click the same Unit Sales Bar for Coffee/Latte.
        Expect to see just the menu for Chart exclusion.
        """
        source_element = util_obj.validate_and_get_webdriver_object(latte_css, 'latte-css')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, source_yoffset=-19, target_xoffset=19, target_yoffset=19)
        visual_obj.verify_lasso_tooltip(left_click_tooltip, msg='Step 7.1: Verify tooltip in latte')
        
        """
        Step 8: Click the Exclude from chart menu option.
        Expect to see only the pair of bars for Coffee/Latte.
        All other Coffee bars should remain.
        Also expect to see the Filter icon appear at the top.
        """
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 10, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(latte_remove_x_label, msg="Step 8.1: Verify all bars except latte is present")
        util_obj.verify_object_visible("#MAINTABLE_wmenu0 div[title=\"Remove Filter\"] img", True, "Step 8.2: Verify filter icon is present")
        
        """
        Step 9: Click the Filter icon at the top.
        Expect to see the pair of bars for Coffee/Latte re-added to the chart.
        This should be the same graph as step 3, with 10 pairs of bars.
        Also expect to see the Filter icon at the top removed.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_0', 4)
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 11, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(run_x_label, msg="Step 9.1: Verify x axis ")
        active_chart_obj.verify_y_axis_label_in_run_window(run_y_label, msg='Step 9.2: Verify y axis')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 9.3: Verify Chart title', parent_css = '#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", 'bar_blue', attribute='fill', msg='Step 9.4: Verify bar colour')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s1!g1!mbar!']", 'pale_green', attribute='fill', msg='Step 9.5: Verify bar colour')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, msg='Step 9.6: Verify number of risers')
        util_obj.verify_object_visible("#MAINTABLE_wmenu0 div[title=\"Remove Filter\"] img", False, "Step 9.7: Verify filter icon is present")
        
        """
        Step 10: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()