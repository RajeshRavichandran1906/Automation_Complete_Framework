'''
Created on Dec 24, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320609
Test Case Title =  AHTML:Converting chart into Funnel chart 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart
from common.lib import utillity

class C8320609_TestClass(BaseTestCase):

    def test_C8320609(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
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
        active_chart.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chart.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        
        """
        STEP 03 : Change output format to Active Reports
        """
        active_chart.change_output_format_type('active_report')
        active_chart.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        STEP 04 : Add fields as follows:
        Region to Columns.
        Product under Horizontal axis.
        Unit Sales under Vertical axis.
        """
        active_chart.drag_field_from_data_tree_to_query_pane('Region', 1, 'Columns')
        active_chart.wait_for_visible_text("text[class='colHeader-label!']", 'Region', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class='colHeader-label!']", 'Region : Product', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Unit Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        """
        STEP 05 : Run the chart and close the window
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 39, MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Verify the chart is displayed properly
        """
        active_chart.verify_column_label_in_run_window(['Region', 'Midwest', 'Northeast', 'Southeast', 'West'], msg='Step 05.01')
        active_chart.verify_x_axis_label_in_run_window(['Biscotti', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], msg='Step 05.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '40K', '80K', '120K', '160K', '200K', '240K', '280K'], msg='Step 05.03')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 39, msg='Step 05.4 : Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 05.5')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product', 'Product'], msg='Step 05.6')
        active_chart.verify_chart_title('Unit Sales BY Region, Product', msg='Step 05.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.8', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 06 : From the Format tab, select Other option and select Funnel Chart from Special tab and Click Ok
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chart.select_other_chart_type('special', 'funnel', 6)
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 2, MEDIUM_WAIT_TIME)
        
        """
        STEP 06.1 : Verify the Column items are dropped 
        """
        utillobj.verify_element_text('#pfjTableChart_1 text[transform]','Unit Sales', msg='Step 06.1: Verify x-axis title')
        active_chart.verify_legends_in_preview(['Product', 'Capuccino', 'Espresso'], msg='Step 06.2')
        active_chart.verify_number_of_risers('#TableChart_1 path', 2, 1, msg='Step 06.3: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mriser!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 06.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mriser!']", 'pale_green', parent_css='#pfjTableChart_1', msg='Step 06.5')
        
        """
        STEP 07 : Run the chart
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='riser!']", 10, MEDIUM_WAIT_TIME)
        
        """
        STEP 07.1 : Verify the Funnel Chart is displayed properly
        """
        utillobj.verify_element_text('#MAINTABLE_wbody0_f text[transform]','Unit Sales', msg='Step 07.1: Verify x-axis title')
        active_chart.verify_number_of_risers_in_run_window('path', 10, 1, msg='Step 07.2: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mriser!']", 'bar_blue', parent_css='#MAINTABLE_wbody0_f', msg='Step 07.3')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mriser!']", 'pale_green', parent_css='#MAINTABLE_wbody0_f', msg='Step 07.4')
        active_chart.verify_legends_in_run_window(['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], msg='Step 07.5')
        active_chart.verify_chart_title('Unit Sales BY Product', msg='Step 07.6', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 07.7', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 08 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()