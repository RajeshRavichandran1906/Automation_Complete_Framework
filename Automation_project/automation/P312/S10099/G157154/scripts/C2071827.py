'''
Created on March 02, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2071827
TestCase Name = Visualization Bubble Chart filter:TypeError:Object not support action
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2071827_TestClass(BaseTestCase):

    def test_C2071827(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        Test_Case_ID = 'C2071827'
        run_fex = 'C2071827_Repro.fex'
        maintable_css='#MAINTABLE_wbody2_f'
        sleep_time = 3
        risers_num = [7,1]
        time_out = 200
        num = 1
        color = "royal_blue"
        
        """
        Step 01: Run the attached C2071827.Repro.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10099&BIP_item=C2071827_Repro.fex
        """
        visual.run_visualization_using_api(run_fex)
        parent_css="#MAINTABLE_wbody2 circle[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers_num[0], time_out)
        x_axis_title=['CNT Product Category']
        visual.verify_x_axis_title(x_axis_title, parent_css=maintable_css, msg='Step 1.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, parent_css=maintable_css, msg='Step 1.2')
        expected_xaxis_label=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        visual.verify_x_axis_label(expected_xaxis_label, parent_css=maintable_css, msg='Step 1.3')
        expected_yaxis_label=['0', '30M', '60M', '90M', '120M', '150M']
        visual.verify_y_axis_label(expected_yaxis_label,  parent_css=maintable_css, msg='Step 1.4')
        parent_css="#MAINTABLE_wbody2_f circle"
        visual.verify_number_of_risers(parent_css, num, risers_num[0], msg='Step 1.5')
        riser_css="[class*='riser!s0!g0!mmarker!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, parent_css=maintable_css, msg='Step 1.6')
        expected_tooltip_list=['CNT Product Category:153171', 'Revenue:$73,319,094.18', 'CNT Product Category:153171', 'Product Category:Camcorder', 'Filter Chart', 'Exclude from Chart']
        riser_css="riser!s1!g0!mmarker!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 1.7: Verify Tooltip', parent_css='MAINTABLE_wbody2')
        expected_legend_list=['Product Category','Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'CNT Product Category', '375.2K', '205.3K', '35.4K']
        visual.verify_legends(expected_legend_list, parent_css=maintable_css, msg='Step 1.8')
        prompt_css="#LOBJPrompt_12"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="Sale,Quarter"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        item_name="1"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 1.9')
        item_name="2"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 1.10')
        
        """
        Step 02: Hover any bubble Click Filter chart (ex. Camcorder)
        """
        time.sleep(sleep_time)
        riser_css='riser!s1!g0!mmarker!'
        menu_path='Filter Chart'
        visual.select_tooltip(riser_css, menu_path, parent_css='MAINTABLE_wbody2')
        
        """
        Step 03: Verify the following chart displayed without any error 
        """
        parent_css="#MAINTABLE_wbody2 circle[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, risers_num[1], time_out)
        x_axis_title=['CNT Product Category']
        visual.verify_x_axis_title(x_axis_title, parent_css=maintable_css, msg='Step 3.1')
        y_axis_title=['Revenue']
        visual.verify_y_axis_title(y_axis_title, parent_css=maintable_css, msg='Step 3.2')
        expected_xaxis_label=['0', '40K', '80K', '120K', '160K', '200K']
        visual.verify_x_axis_label(expected_xaxis_label, parent_css=maintable_css, msg='Step 3.3')
        expected_yaxis_label=['0', '20M', '40M', '60M', '80M', '100M']
        visual.verify_y_axis_label(expected_yaxis_label,  parent_css=maintable_css, msg='Step 3.4')
        parent_css="#MAINTABLE_wbody2_f circle"
        visual.verify_number_of_risers(parent_css, num, risers_num[1], msg='Step 3.5')
        riser_css="[class*='riser!s0!g0!mmarker!']"
        visual.verify_chart_color_using_get_css_property(riser_css, color, parent_css=maintable_css, msg='Step 3.6')
        expected_tooltip_list=['CNT Product Category:153171', 'Revenue:$73,319,094.18', 'CNT Product Category:153171', 'Product Category:Camcorder', 'Remove Filter']
        riser_css="riser!s0!g0!mmarker!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 3.7: Verify Tooltip', parent_css='MAINTABLE_wbody2')
        expected_legend_list=['CNT Product Category', '153,171']
        visual.verify_legends(expected_legend_list, parent_css=maintable_css, msg='Step 3.8')
        prompt_css="#LOBJPrompt_12"
        visual.wait_for_number_of_element(prompt_css, num, time_out)
        title_name="Sale,Quarter"
        visual.verify_prompt_title(title_name, parent_prompt_css=prompt_css)
        item_name="1"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 3.9')
        item_name="2"
        visual.verify_item_checked_status_in_show_prompt_table(item_name, parent_prompt_css=prompt_css, msg='Step 3.10')
        visual.take_run_window_snapshot(Test_Case_ID, '03')
        
        """
        Step 04: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()