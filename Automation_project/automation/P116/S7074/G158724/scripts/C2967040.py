'''
Created on Jan 9, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2967040
Test Case Title =  Verify Vertical Histogram in others tab under Format menu.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart

class C2967040_TestClass(BaseTestCase):

    def test_C2967040(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        preview_parent_css="TableChart_1"
        
        """
        STEP 01 : Log in to WebFOCUS http://machine:port/{alias}
        STEP 02 : Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S7074%2FG158724%2F
        """
        active_chart.invoke_ia_chart_tool_using_api('ibisamp/ggsales')
        
        """
        Expect to see the following Live Preview pane, with the default Vertical Column Bar Chart on the canvas
        """
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 02.01')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 02.02')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 02.03')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 02.04: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+preview_parent_css, msg='Step 02.05')
        
        """
        STEP 03 : Change output format to Active Reports
        """
        active_chart.change_output_format_type('active_report')
        active_chart.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        STEP 04 :Add fields Category and Unit Sales
        """
        active_chart.double_click_on_datetree_item('Category', 1)
        active_chart.wait_for_visible_text("text[class='xaxisOrdinal-title']", 'Category', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Unit Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        """
        STEP 04.1 : Expect to see the following Preview.
        """
        active_chart.verify_x_axis_label_in_preview(['Coffee'], msg='Step 04.01')
        active_chart.verify_y_axis_label_in_preview(['0', '100K', '200K', '300K', '400K', '500K', '600K'], msg='Step 04.2')
        active_chart.verify_x_axis_title_in_preview(['Category'], msg='Step 04.3')
        active_chart.verify_y_axis_title_in_preview(['Unit Sales'], msg='Step 04.4')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 1, msg='Step 04.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+preview_parent_css, msg='Step 04.6')
        
        """
        Step 05 : Select Format > Other
        Step 06 : From Select a chart pop up choose 'Vertical Histogram Bar'
        Step 07 : Click OK
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chart.select_other_chart_type('bar', 'vertical_histogram', 6)
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" rect[class*='riser!']", 162, MEDIUM_WAIT_TIME)
        
        """
        STEP 07.1 : Expect to see the following Preview.
        """
        active_chart.verify_x_axis_title_in_preview(['UNITS_BIN_1'], msg='Step 07.1')
        active_chart.verify_y_axis_title_in_preview(['CNT Unit Sales'], msg='Step 07.2')
        active_chart.verify_x_axis_label_in_preview(['100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200', '210', '220'], msg='Step 07.3')
        active_chart.verify_y_axis_label_in_preview(['0', '4', '8', '12', '16'], msg='Step 07.4')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 162, msg='Step 07.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#'+preview_parent_css, msg='Step 07.6')
        
        """
        STEP 08 : Click Run and verify output.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 179, MEDIUM_WAIT_TIME)
        
        """
        STEP 08.1 : Verify output.
        """
        active_chart.verify_x_axis_title_in_run_window(['UNITS_BIN_1'], msg='Step 08.1')
        active_chart.verify_y_axis_title_in_run_window(['CNT Unit Sales'], msg='Step 08.2')
        active_chart.verify_x_axis_label_in_run_window(['60', '70', '80', '90', '100', '110', '120', '130', '140', '150', '160', '170', '180'], msg='Step 08.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '10', '20', '30', '40', '50'], msg='Step 08.4')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 179, msg='Step 08.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 08.6')
        active_chart.verify_chart_title('CNT Unit Sales BY UNITS_BIN_1', msg='Step 08.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Count'], msg='Step 08.8', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 09 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()