'''
Created on Dec 21, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984775
Test Case Title =  Verify chart filter functionality in Vertical Absolute Area in others tab (under Format menu).
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart, chart

class C6984775_TestClass(BaseTestCase):

    def test_C6984775(self):
       
        """
        CLASS OBJECTS
        """
        active_chartobj = active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        preview_parent_css="TableChart_1"
        
        """
        STEP 01 : Log in to WebFOCUS http://machine:port/{alias}
        STEP 02 : Execute following URL to create Chart 
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS2031%2F
        """
        active_chartobj.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chartobj.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        
        """
        STEP 03 : Change output format to Active Reports
        """
        active_chartobj.change_output_format_type('active_report')
        active_chartobj.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        Step 04 : Select Format > Other>Area
        Select Vertical Absolute Area
        Click OK.
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chartobj.select_other_chart_type('area', 'vertical_absolute_area', 1)
        active_chartobj.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 5, MEDIUM_WAIT_TIME)
        
        """
        STEP 05 : Add fields as follows:
        Region under Columns,
        Dollar Sales and Unit Sales under Vertical Axis
        Product ID under Horizontal Axis
        """
        active_chartobj.drag_field_from_data_tree_to_query_pane('Region', 1, 'Columns')
        active_chartobj.wait_for_visible_text("text[class='colHeader-label!']", 'Region', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Dollar Sales', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(8)", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Unit Sales', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(9)", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        active_chartobj.double_click_on_datetree_item('Product ID', 1)
        active_chartobj.wait_for_visible_text("#queryTreeColumn tr:nth-child(11)", 'Product ID', MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Expect to see the following chart
        """
        active_chartobj.verify_column_label_in_preview(['Region : Product ID', 'Midwest', 'Northeast', 'Southeast', 'West'], msg='Step 05.01')
        active_chartobj.verify_x_axis_label_in_preview(['C141', 'C141', 'C144', 'C141', 'C144', 'C141', 'C144'], msg='Step 05.02')
        active_chartobj.verify_y_axis_label_in_preview(['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M'], msg='Step 05.03')
        active_chartobj.verify_legends_in_preview(['Dollar Sales', 'Unit Sales'], msg='Step 05.04')
        active_chartobj.verify_number_of_risers('#TableChart_1 path', 2, 4, msg='Step 05.05: Verify number of bar risers')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!marea!r0!c1!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 05.06')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!marea!r0!c1!']", 'pale_green', parent_css='#pfjTableChart_1', msg='Step 05.07')
        
        """
        STEP 06 : Click the Run button.
        """
        active_chartobj.run_chart_from_toptoolbar()
        active_chartobj.switch_to_frame()
        active_chartobj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s0!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
        STEP 06.1 : Verify bucketized Vertical Absolute Area output.
        """
        active_chartobj.verify_column_label_in_run_window(['Region', 'Midwest', 'Northeast', 'Southeast', 'West'], msg='Step 06.01')
        x_axis_label_list=['C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...', 'C...', 'C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...', 'G...']
        active_chartobj.verify_x_axis_label_in_run_window(x_axis_label_list,parent_css='#MAINTABLE_wbody0', msg='Step 06.02')
        active_chartobj.verify_y_axis_label_in_run_window(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M'],parent_css='#MAINTABLE_wbody0', msg='Step 06.03')
        active_chartobj.verify_legends_in_run_window(['Dollar Sales', 'Unit Sales'], msg='Step 06.04')
        active_chartobj.verify_number_of_risers('#MAINTABLE_wbody0_f path', 2, 4, msg='Step 05.05: Verify number of bar risers')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!marea!r0!c1!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 06.06')
        active_chartobj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!marea!r0!c1!']", 'pale_green', parent_css='#MAINTABLE_wbodyMain0', msg='Step 06.07')
        active_chartobj.verify_x_axis_title_in_run_window(['Product ID', 'Product ID', 'Product ID', 'Product ID'], msg='Step 06.08')
        active_chartobj.verify_chart_title('Dollar Sales, Unit Sales BY Region, Product ID', msg='Step 06.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chartobj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 07 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()