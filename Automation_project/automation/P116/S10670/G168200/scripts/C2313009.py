'''
Created on December 31, 2018

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313009
TestCase Name = AHTML: StreamGraph ColorBy chart limit tests.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import chart
from common.lib import base
from common.wftools import active_chart


class C2313009_TestClass(BaseTestCase):

    def test_C2313009(self):
        
        """
        TTest case objects
        """
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj = active_chart.Active_Chart(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        country_query_css = "#queryTreeWindow table tr:nth-child(8) td"
        bodytype_query_css = "#queryTreeWindow table tr:nth-child(9) td"
        x_axis_labels = "#MAINTABLE_wbody0 text[class^='xaxis']"
        retail_cost_css = "#queryTreeWindow table tr:nth-child(4) td"
        car_css = "#queryTreeWindow table tr:nth-child(5) td"
        legends_css = "#MAINTABLE_wbody0_f text[class^='legend-labels!s']"
        
        """
        Test case variables
        """
        alfa_romeo_tooltip = ['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'COUNTRY:ITALY', 'SEATS:2', 'LENGTH:163', 'WIDTH:62', 'WHEELBASE:92.5', 
                              'FUEL_CAP:14.0', 'BHP:0', 'MPG:21', 'ACCEL:0', 'Filter Chart', 'Exclude from Chart']
        final_title = 'DEALER_COST, RETAIL_COST, SALES, RPM, SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY, CAR, COUNTRY, BODYTYPE'
        final_legend_list = ['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'SALES:ENGLAND', 'RPM:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'SALES:FRANCE', 
                             'RPM:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 'SALES:ITALY', 'RPM:ITALY', 'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'SALES:JAPAN',
                              'RPM:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY', 'SALES:W GERMANY', 'RPM:W GERMANY']
        vertical_axis_query_list = ['DEALER_COST','RETAIL_COST','SALES','RPM']
        horizontal_axis_query_list = ['CAR','COUNTRY','BODYTYPE']
        tooltip_query_list = ['SEATS', 'LENGTH', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL'] 
        legend_list = ['SEATS:ENGLAND', 'LENGTH:ENGLAND', 'WIDTH:ENGLAND', 'WHEELBASE:ENGLAND', 'FUEL_CAP:ENGLAND', 'BHP:ENGLAND', 
                       'MPG:ENGLAND', 'ACCEL:ENGLAND', 'SEATS:FRANCE', 'LENGTH:FRANCE', 'WIDTH:FRANCE', 'WHEELBASE:FRANCE', 'FUEL_CAP:FRANCE', 
                       'BHP:FRANCE', 'MPG:FRANCE', 'ACCEL:FRANCE', 'SEATS:ITALY', 'LENGTH:ITALY', 'WIDTH:ITALY', 'WHEELBASE:ITALY']
        tooltip_values = ['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'DEALER_COST:49,500', 'COUNTRY:W GERMANY', 'Filter Chart', 'Exclude from Chart']
        country_variable = 'COUNTRY'
        bodytype_variable = 'BODYTYPE'
        retail_cost_variable = 'RETAIL_COST'
        car_variable = 'CAR'
        chart_title = 'SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY, CAR, COUNTRY, BODYTYPE'
        
        def drag_and_drop_within_query_tree(source_item_name, target_item_name):
            querytree_items = util_obj.validate_and_get_webdriver_objects("#queryTreeColumn table>tbody>tr>td", 'Query panel')
            querytree_list=[el.text.strip() for el in querytree_items]
            source_elem= util_obj.validate_and_get_webdriver_object("img[class='icon']", source_item_name, parent_object=querytree_items[querytree_list.index(source_item_name)])
            source_elem_coordinate=core_util_obj.get_web_element_coordinate(source_elem, element_location='middle', xoffset=25)
            x1=source_elem_coordinate['x']
            y1=source_elem_coordinate['y']
            target_elem= util_obj.validate_and_get_webdriver_object("img[class='icon']", target_item_name, parent_object=querytree_items[querytree_list.index(target_item_name)])
            target_elem_coordinate=core_util_obj.get_web_element_coordinate(target_elem, element_location='middle', xoffset=25, yoffset=5)
            x2=target_elem_coordinate['x']
            y2=target_elem_coordinate['y']
            core_util_obj.drag_and_drop(x1, y1, x2, y2)
            time.sleep(5)
        
        """
        Step 1:Open FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamColorBy.fex&tool=Chart
        """
        chart_obj.invoke_chart_in_edit_mode_using_api('StreamColorBy')
        
        """
        Step 2: Add additional Dimension(X-axis) fields:
        COUNTRY & BODYTYPE.
        Click the Run button.
        """
        chart_obj.double_click_on_datetree_item('COUNTRY', 1)
        chart_obj.wait_for_visible_text(country_query_css, country_variable, base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('BODYTYPE',1)
        chart_obj.wait_for_visible_text(bodytype_query_css, bodytype_variable, base_obj.chart_short_timesleep)
        chart_obj.run_report_from_toptoolbar()
         
        """
        Step 3: Hover over the lower area(light green) for BMW.
        Expect to see the following Tooltip information confirming that CAR, COUNTRY & BODYTYPE are shown, since all values 
        are not visible in the chart X-axis labels.
        """
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 14, base_obj.chart_medium_timesleep)
        chart_obj.verify_tooltip_in_run_window("marker!s8!g4!mmarker!", tooltip_values, 'Step 3.1: Verify tooltip values',parent_css="#MAINTABLE_wbody0", yoffset=50, use_marker_enable=True)
         
        """
        Step 4: Remove Measure(Vertical axis) fields DEALER_COST & RETAIL_COST.
        Add new Measure fields:
        SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL.
        Click the Run button.
        Expect to see all 8 Vertical axis fields appear both on the chart and as entries in the chart legend.
        """
        chart_obj.switch_to_default_content()
        chart_obj.right_click_on_field_under_query_tree('DEALER_COST', 1, 'Delete')
        chart_obj.wait_for_visible_text(retail_cost_css, retail_cost_variable, base_obj.chart_short_timesleep)
        chart_obj.right_click_on_field_under_query_tree('RETAIL_COST', 1, 'Delete')
        chart_obj.wait_for_visible_text(car_css, car_variable, base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('SEATS', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(4) td", 'SEATS', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('LENGTH', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(5) td", 'LENGTH', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('WIDTH', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(6) td", 'WIDTH', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('WHEELBASE', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(7) td", 'WHEELBASE', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('FUEL_CAP', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(8) td", 'FUEL_CAP', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('BHP', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(9) td", 'BHP', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('MPG', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(10) td", 'MPG', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('ACCEL', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(11) td", 'ACCEL', base_obj.chart_short_timesleep)
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(legends_css, 40, base_obj.chart_medium_timesleep)
        chart_obj.verify_legends_in_run_window(legend_list, parent_css='#MAINTABLE_wbody0_f', msg='Step 4.1:')
        active_chart_obj.verify_chart_title(chart_title, 'Step 4.2', parent_css='#MAINTABLE_wbody0_ft')
        
        """
        Step 5: Move all 8 fields from the Vertical axis area to the Tooltip area.
        Expect to see all 8 fields now under the Tooltip area in the Preview pane.
        """
        chart_obj.switch_to_default_content()
        chart_obj.drag_field_within_query_pane('SEATS', 'Tooltip')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'SEATS', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('LENGTH','SEATS')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'LENGTH', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('WIDTH','LENGTH')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'WIDTH', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('WHEELBASE','WIDTH')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'WHEELBASE', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('FUEL_CAP','WHEELBASE')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'FUEL_CAP', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('BHP','FUEL_CAP')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'BHP', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('MPG','BHP')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'MPG', base_obj.chart_short_timesleep)
        drag_and_drop_within_query_tree('ACCEL','MPG')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(19) td", 'ACCEL', base_obj.chart_short_timesleep)
        for iterate,item in enumerate(tooltip_query_list):
            chart_obj.verify_field_listed_under_querytree('Tooltip', item, iterate+1, 'Step 5.1: Verify field under tooltip')
        
        """
        Step 6: Add new fields DEALER_COST, RETAIL_COST, SALES & RPM to the Vertical axis area.
        Expect to see Preview pane, now with DEALER_COST, RETAIL_COST, SALES & RPM under the Vertical axis area.
        """ 
        chart_obj.double_click_on_datetree_item('DEALER_COST', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(4) td", 'DEALER_COST', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('RETAIL_COST', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(5) td", 'RETAIL_COST', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('SALES', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(6) td", 'SALES', base_obj.chart_short_timesleep)
        chart_obj.double_click_on_datetree_item('RPM', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(7) td", 'RPM', base_obj.chart_short_timesleep)
        chart_obj.wait_for_number_of_element("[class^='legend-labels!']", 20, base_obj.chart_medium_timesleep)
        for iterate,item in enumerate(vertical_axis_query_list):
            chart_obj.verify_field_listed_under_querytree('Vertical Axis', item, iterate+1, 'Step 6.1: Verify field under vertical Axis')
        
        """
        Step 7: Click the Run button.
        Expect to see the following Streamgraph,now with 
        4 Vertical axis and 
        3 Horizontal axis fields.
        """
        chart_obj.run_report_from_toptoolbar()
        for iterate,item in enumerate(vertical_axis_query_list):
            chart_obj.verify_field_listed_under_querytree('Vertical Axis', item, iterate+1, 'Step 7.1: Verify 4 fields in Vertical Axis')
        for iterate,item in enumerate(horizontal_axis_query_list):
            chart_obj.verify_field_listed_under_querytree('Horizontal Axis', item, iterate+1, 'Step 7.2: Verify 3 fields in Horizontal Axis') 
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 14, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_chart_title(final_title, 'Step 7.3', parent_css='#MAINTABLE_wbody0_ft')
        chart_obj.verify_legends_in_run_window(final_legend_list, parent_css='#MAINTABLE_wbody0_f', msg='Step 7.4')
        
        """
        Step 8: Hover over the lower area(green) for the first Alfa Romeo Horizontal point.
        Expect to see the following Tooltip information, combining all Vertical axis fields, the applicable Horizontal fields and the 8 Tooltip fields.
        """
        chart_obj.verify_tooltip_in_run_window("marker!s8!g0!mmarker!", alfa_romeo_tooltip, 'Step 8.1: Verify tooltip values',initial_move_xy_dict={'x':434,'y':482},parent_css="#MAINTABLE_wbody0",yoffset=2, use_marker_enable=True)
        
        """
        Step 9: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()     