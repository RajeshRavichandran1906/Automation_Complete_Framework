'''
Created on Feb 1, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348959
TestCase Name = Group field moved to Rows
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348959_TestClass(BaseTestCase):

    def test_C2348959(self):
        """
        TESTCASE VARIABLES
        """
        Restore_fex = 'C2348959_Base'
        Test_Case_ID = 'C2348959'
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348959_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(4)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_y_axis_title(['Revenue'], msg='Step 1.1')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 1.2')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 1.3')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 1.4')
        expected_column_label_list=['PRODUCT_CATEGORY_1', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_column_label(expected_column_label_list, msg="Step 1.5:")
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 1.6: Verify Tooltip') 
        time.sleep(5)
        
        """
        Step 02: Drag and drop "PRODUCT_CATEGORY_1" from query pane Matrix Columns to Rows bucket
        """
        visual.drag_field_within_query_pane('PRODUCT_CATEGORY_1', 'Rows')
        time.sleep(6)
        
        """
        Step 03: Verify Group moves with no error to Matrix Columns bucket
        """
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_y_axis_title(['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue'], msg='Step 3.1')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.2')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 3.3')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!r0!c0!']", "bar_blue", msg='Step 3.4')
        expected_row_label_list=['PRODUCT_CATEGORY_1', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_rows_label(expected_row_label_list, msg="Step 03.5:")
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!r0!c0!', expected_tooltip_list,'Step 3.6: Verify Tooltip') 
        time.sleep(5)
        visual.take_preview_snapshot(Test_Case_ID ,'03')
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 04: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()