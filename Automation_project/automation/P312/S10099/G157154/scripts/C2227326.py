'''
Created on Feb 26, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227326
TestCase Name = Run time Reset option works after filter displays no data
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2227326_TestClass(BaseTestCase):

    def test_C2227326(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        driver=self.driver
        Test_Case_ID = 'C2227326'
        restore_fex = 'C2227326_Repro'
        sleep_time=3
        riser=7
        group_label=7
        time_out=200
        num=1
        source_xoffset=-15
        target_xoffset=10
        source_element_location='middle_left'
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?item=IBFS:/WFC/Repository/S10099/C2227326_Repro.fex&tool=idis
        """
        visual.edit_visualization_using_api(restore_fex)

        """
        Step 02: Verify the following chart is displayed.
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser, time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 2.1')
        y_axis_title=['Cost of Goods']
        visual.verify_y_axis_title(y_axis_title, msg='Step 2.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 2.6')
        expected_tooltip_list=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g0!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Click Run and verify the output.
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Verify output
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser, time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['Cost of Goods']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser, msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 3.6')
        expected_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g1!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 3.7: Verify Tooltip') 
        
        """
        Step 04: Select all bars using lasso filter > Exclude from chart
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, group_label, time_out)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g6!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location=source_element_location)
        time.sleep(sleep_time)
        tooltip_value="Exclude from Chart"
        visual.select_lasso_tooltip(tooltip_value)
        
        """
        Step 05: Verify the following chart displayed with "No data to graph"
        """
        parent_css="#MAINTABLE_wbody1 div[style*='text']"
        visual.wait_for_visible_text(parent_css, visble_element_text='NodatatoGraph', time_out=time_out)
        visual.verify_element_visiblty(element_css=parent_css, msg='Step 05')
        
        """ 
        Step 06: Expand menu in the lower right corner to select the Reset option, select the Reset option (second icon) 
        """ 
        parent_css="#MAINTABLE_menuContainer1"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        reset_option="reset"
        visual.select_bottom_right_run_menu_options(reset_option)
        
        """
        Step 07: Verify Reset option will clear all filters to what they were at original execution
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser, time_out)
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 07.1')
        y_axis_title=['Cost of Goods']
        visual.verify_y_axis_title(y_axis_title, msg='Step 07.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 07.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 07.4')
        parent_css="#MAINTABLE_wbody1_f rect"
        visual.verify_number_of_risers(parent_css, num, riser, msg='Step 07.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 07.6')
        expected_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css="riser!s0!g1!mbar!"
        visual.verify_tooltip(riser_css, expected_tooltip_list,'Step 07.7: Verify Tooltip') 
        visual.take_run_window_snapshot(Test_Case_ID, '07')
        time.sleep(1)
        """
        Step 08: Launch the IA API to logout. http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()      