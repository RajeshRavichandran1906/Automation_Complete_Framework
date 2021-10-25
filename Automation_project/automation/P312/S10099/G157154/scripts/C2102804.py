'''
Created on Feb 27, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102804
TestCase Name = Filter Chart after Remove filter does not have effect on the filter Prompt at runtime
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102804_TestClass(BaseTestCase):

    def test_C2102804(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
#         Test_Case_ID = 'C2102804'
        restore_fex = 'C2102804_Repro'
        sleep_time = 3
        riser_num = [7,1]
        group_label = 7
        time_out = visual.home_page_long_timesleep
        position = 1
        num = 1
        color = "bar_blue"
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?item=IBFS:/WFC/Repository/S10099/C2102804_Repro.fex&tool=idis
        """
        visual.edit_visualization_using_api(restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser_num[0], time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 1.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 1.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 1.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 1.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser_num[0], msg='Step 1.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 1.6')
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 1.7: Verify Tooltip')
        
        """
        Step 02: Add "Product,Category" to Filter, accept default and click ok.
        """
        visual.right_click_on_datetree_item('Product,Category', position, context_menu_path='Filter')
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        btn='ok'
        visual.close_filter_dialog(btn)
        parent_css="#qbFilterBox table>tbody>tr>td img"
        visual.wait_for_number_of_element(parent_css, position, time_out)
        field_name="Product,Category"
        visual.verify_field_in_filterbox(field_name, position, "Step 2.1:")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        title_name="Product,Category"
        visual.verify_prompt_title(title_name)
        item_name="[All]"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 2.2')
        
        """
        Step 03: Run the Visualization.
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, group_label, time_out)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser_num[0], time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser_num[0], msg='Step 3.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 3.6')
        expected_tooltip_list=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g1!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 3.7: Verify Tooltip')
        
        """
        Step 04: Hover over on "Accessories" and click Filter Chart. Noticed Filter prompt is updated the checkbox of only "Accessories".
        """
        time.sleep(sleep_time)
        riser_css='riser!s0!g0!mbar!'
        menu_path='Filter Chart'
        visual.select_tooltip(riser_css, menu_path)
        
        """
        Step 04.1: Filter prompt is updated the checkbox of only "Accessories".:
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser_num[1], time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 4.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 4.2')
        expected_xaxis_label=['Accessories']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 4.3')
        expected_yaxis_label=['0', '30M', '60M', '90M', '120M', '150M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 4.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser_num[1], msg='Step 4.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 4.6')
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Remove Filter', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 4.7: Verify Tooltip')
        prompt_css="#LOBJPrompt_11"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="Product,Category"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        item_name="Accessories"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 4.8')
        
        """
        Step 05: Hover over on "Accessories" and click Remove Filter. Noticed it removes the filter from canvas and updated in Filter.
        """
        time.sleep(sleep_time)
        riser_css='riser!s0!g0!mbar!'
        menu_path='Remove Filter'
        visual.select_tooltip(riser_css, menu_path)
        
        """
        Step 05.1: Filter update:
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser_num[0], time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 5.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, msg='Step 5.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser_num[0], msg='Step 5.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 5.6')
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 5.7: Verify Tooltip')
        prompt_css="#LOBJPrompt_11"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="Product,Category"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        item_name="[All]"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 5.8')
#         visual.take_run_window_snapshot(Test_Case_ID, '05')
        
        """
        Step 06: Launch the IA API to logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()