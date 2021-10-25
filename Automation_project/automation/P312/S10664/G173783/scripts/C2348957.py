'''
Created on Feb 5, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348957
TestCase Name = Group field moved to Color
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348957_TestClass(BaseTestCase):

    def test_C2348957(self):
        """
        TESTCASE VARIABLES
        """
        Restore_fex = 'C2348957_Base'
        Test_Case_ID = 'C2348957'
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348957_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 1.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 1.2')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 1.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 1.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 1.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 1.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 1.7:")
        time.sleep(5)  
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 1.8: Verify Tooltip') 
        
        """
        Step 02: Drag and drop "PRODUCT_CATEGORY_1" from query pane horizontal axis to Color bucket
        """
        visual.drag_field_within_query_pane('PRODUCT_CATEGORY_1', 'Color')
        time.sleep(6)
        
        """
        Step 03: Verify Group moves with no error to Color bucket.
        Preview updated to one riser with stacked colors and "PRODUCT_CATEGORY_1" value name show in legend
        """
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_y_axis_title(['Revenue'], msg='Step 3.1')
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.2')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 3.3')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s3!g0!mbar!']", "pale_yellow", msg='Step 3.4')
        visual.verify_field_listed_under_querytree('Color BY', 'PRODUCT_CATEGORY_1', 1, "Step 3.5:")
        expected_legend_list=['PRODUCT_CATEGORY_1', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_legends(expected_legend_list, msg='Step 3.6')
        time.sleep(5)   
        expected_tooltip_list=['Revenue:$284,074,040.77', 'PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 3.7: Verify Tooltip') 
        time.sleep(5)
        
        """
        Step 04: Drag group from Color bucket back to Horizontal Axis
        """
        visual.drag_field_within_query_pane('PRODUCT_CATEGORY_1', 'Horizontal Axis')
        time.sleep(10)
        
        """
        Step 05: Verify Group moves with no error and preview restores to previous
        """
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 5.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 5.2')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 5.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 5.7:")
        time.sleep(5)  
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 5.8: Verify Tooltip') 
        time.sleep(5)
        visual.take_preview_snapshot(Test_Case_ID ,'05')
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 06: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()