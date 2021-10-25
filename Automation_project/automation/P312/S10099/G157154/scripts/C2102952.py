'''
Created on Feb 28, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102952
TestCase Name = Lasso filter (tooltip) removes prompt filter at run time
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages.core_metadata import CoreMetaData

class C2102952_TestClass(BaseTestCase):

    def test_C2102952(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        driver = self.driver
        Test_Case_ID = 'C2102952'
        master_file = 'baseapp/wf_retail_lite'
        sleep_time = 4
        position = 1
        risers = [1,6,2]
        color = "bar_blue"
        time_out = 200
        num = 1
        source_xoffset = -15
        target_xoffset = 10
        source_element_location = 'middle_left'
        expected_prompt_min_val = 3
        expected_prompt_max_val = 4
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10099&tool=chart&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api(master_file)
            
        """
        Step 02: Double click Revenue & Sale,Year (simple)
        """
        field_name='Revenue'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, risers[0], time_out)
        
        field_name='Sale,Year'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, risers[1], time_out)
        
        x_axis_title=['Sale Year']
        visual.verify_x_axis_title(x_axis_title, msg='Step 2.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 2.2')
        expected_xaxis_label=['2011', '2012', '2013', '2014', '2015', '2016']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[1], msg='Step 2.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 2.6')
        expected_tooltip_list=['Sale Year:2011', 'Revenue:$48,965,069.21', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Drag Sale,Quarter (simple) to filter
        """
        field_name='Sale,Quarter'
        CoreMetaData.collapse_data_field_section(self, 'Filters and Variables')
        visual.right_click_on_datetree_item(field_name, position, context_menu_path='Filter')
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        
        """
        Step 04: Adjust to see only from 3 to 4 quarters
        Step 05: Click OK
        """
        field_type='numeric'
        from_value='3'
        to_value='4'
        visual.filter_from_input_and_to_input(field_type, from_input=from_value)
        visual.filter_from_input_and_to_input(field_type, to_input=to_value, close_dialog_button='ok')
        
        """
        Step 06: Verify filter added filter pane and prompt
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[1], time_out)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        x_axis_title=['Sale Year']
        visual.verify_x_axis_title(x_axis_title, msg='Step 6.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 6.2')
        expected_xaxis_label=['2011', '2012', '2013', '2014', '2015', '2016']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 6.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 6.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[1], msg='Step 6.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 6.6')
        expected_tooltip_list=['Sale Year:2011', 'Revenue:$26,473,128.12', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 6.7: Verify Tooltip') 
        field_name="Sale,Quarter"
        visual.verify_field_in_filterbox(field_name, position, "Step 6.8:")
        title_name="Sale,Quarter"
        visual.verify_prompt_title(title_name)
        visual.verify_slider_min_max_value_in_live_preview(expected_prompt_min_val, msg='Step 6.9')
        visual.verify_slider_min_max_value_in_live_preview(expected_prompt_max_val, msg='Step 6.10', drag_button='max')
        
        """
        Step 07: Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 08: Lasso select 2014 & 2015 in output
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[1], time_out)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g3!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g4!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location=source_element_location)
        
        """
        Step 09: Click Filter chart
        """
        time.sleep(sleep_time)
        tooltip_value="Filter Chart"
        visual.select_lasso_tooltip(tooltip_value)
        
        """
        Step 10: Verify chart displayed filtered output
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[2], time_out)
        x_axis_title=['Sale Year']
        visual.verify_x_axis_title(x_axis_title, msg='Step 10.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 10.2')
        expected_xaxis_label=['2014', '2015']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[2], msg='Step 10.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 10.6')
        prompt_css="#LOBJPrompt_11"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="Sale,Quarter"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        visual.verify_slider_min_max_value_in_run_window(expected_prompt_min_val, msg='Step 10.7')
        visual.verify_slider_min_max_value_in_run_window(expected_prompt_max_val, msg='Step 10.8', drag_button='max')
        
        """
        Step 11: Hover over 2015 riser and verify tooltip value
        """
        expected_tooltip_list=['Sale Year:2015', 'Revenue:$148,836,862.10', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Sale Quarter']
        riser_css="riser!s0!g1!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 11: Verify Tooltip') 
        visual.take_run_window_snapshot(Test_Case_ID, '11')
        
        """
        Step 12: Close run window
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 13: Logout using API(without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()