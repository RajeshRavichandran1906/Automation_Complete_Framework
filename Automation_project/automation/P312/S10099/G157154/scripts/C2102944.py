'''
Created on Feb 28, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102944
TestCase Name = selecting a value with "&" in filter prompt is not reflecting in canvas.
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102944_TestClass(BaseTestCase):

    def test_C2102944(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        Test_Case_ID = 'C2102944'
        master_file = 'ibisamp/empdata'
        sleep_time = 4
        position = 1
        risers = [8,2,3]
        group_label = 3
        color = "bar_blue"
        time_out = 200
        num = 1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10099&tool=idis&master=baseapp/empdata
        """
        visual.invoke_visualization_using_api(master_file)
            
        """
        Step 02: Add fields DEPT, SALARY.
        """
        field_name='DEPT'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, risers[0], time_out)
        
        field_name='SALARY'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxis-title']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        
        x_axis_title=['DEPT']
        visual.verify_x_axis_title(x_axis_title, msg='Step 2.1')
        y_axis_title=['SALARY']
        visual.verify_y_axis_title(y_axis_title, msg='Step 2.2')
        expected_xaxis_label=['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING &#x26; DVLPMT', 'SALES']

#         expected_xaxis_label=['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[0], msg='Step 2.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 2.6')
        expected_tooltip_list=['DEPT:ACCOUNTING', 'SALARY:$283,300.00', 'Filter Chart', 'Exclude from Chart']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Drag/drop DEPT to Filter pane, uncheck "All", then select values ACCOUNTING, CONSULTING, click ok.
        """
        field_name='DEPT'
        visual.right_click_on_datetree_item(field_name, position, context_menu_path='Filter')
        parent_css="#avFilterOkBtn"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        field_value_list = ['[All]','ACCOUNTING','CONSULTING']
        visual.select_filter_field_values(field_value_list, Ok_button=True)
       
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[1], time_out)
        x_axis_title=['DEPT']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['SALARY']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['ACCOUNTING', 'CONSULTING']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[1], msg='Step 3.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 3.6')
        expected_tooltip_list=['DEPT:ACCOUNTING', 'SALARY:$283,300.00', 'Filter Chart', 'Exclude from Chart']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 3.7: Verify Tooltip') 
        field_name="DEPT"
        visual.verify_field_in_filterbox(field_name, position, "Step 3.8:")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        title_name="DEPT"
        visual.verify_prompt_title(title_name)
        item_name="ACCOUNTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 3.9')
        item_name="CONSULTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 3.10')
        
        """
        Step 04: In the Filter Prompt, select value PROGRAMMING & DVLPMT.
        """
        item_name="PROGRAMMING & DVLPMT"
        visual.select_single_item_from_show_prompt_table(item_name)
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[2], time_out)
        x_axis_title=['DEPT']
        visual.verify_x_axis_title(x_axis_title, msg='Step 4.1')
        y_axis_title=['SALARY']
        visual.verify_y_axis_title(y_axis_title, msg='Step 4.2')
#         expected_xaxis_label=['ACCOUNTING','CONSULTING','PROGRAMMING &#x26; DVLPMT']

        expected_xaxis_label=['ACCOUNTING','CONSULTING','PROGRAMMING & DVLPMT']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 4.3')
        expected_yaxis_label=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 4.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[2], msg='Step 4.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 4.6')
        expected_tooltip_list=['DEPT:ACCOUNTING', 'SALARY:$283,300.00', 'Filter Chart', 'Exclude from Chart']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 4.7: Verify Tooltip') 
        field_name="DEPT"
        visual.verify_field_in_filterbox(field_name, position, "Step 4.8:")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        title_name="DEPT"
        visual.verify_prompt_title(title_name)
        item_name="ACCOUNTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 4.9')
        item_name="CONSULTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 4.10')
        item_name="PROGRAMMING & DVLPMT"
#         item_name='PROGRAMMING &#x26; DVLPMT'
        visual.verify_item_checked_status_in_show_prompt_table(item_name, msg='Step 4.11')
        
        """
        Step 05: Click Run and verify the output.
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, group_label, time_out)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers[2], time_out)
        x_axis_title=['DEPT']
        visual.verify_x_axis_title(x_axis_title, msg='Step 5.1')
        y_axis_title=['SALARY']
        visual.verify_y_axis_title(y_axis_title, msg='Step 5.2')
#         expected_xaxis_label=['ACCOUNTING','CONSULTING','PROGRAMMING &#x26; DVLPMT']
        expected_xaxis_label=['ACCOUNTING','CONSULTING','PROGRAMMING & DVLPMT']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, risers[2], msg='Step 5.5')
        riser_css="[class*='riser!s0!g0!mbar!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, msg='Step 5.6')
        expected_tooltip_list=['DEPT:ACCOUNTING', 'SALARY:$283,300.00', 'Filter Chart', 'Exclude from Chart']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 5.7: Verify Tooltip') 
        prompt_css="#LOBJPrompt_11"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="DEPT"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        item_name="ACCOUNTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 5.8')
        item_name="CONSULTING"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 5.9')
        item_name="PROGRAMMING & DVLPMT"
#         item_name='PROGRAMMING &#x26; DVLPMT'
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 5.10')
        visual.take_run_window_snapshot(Test_Case_ID, '05')
        
        """
        Step 06: Launch the IA API to logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()