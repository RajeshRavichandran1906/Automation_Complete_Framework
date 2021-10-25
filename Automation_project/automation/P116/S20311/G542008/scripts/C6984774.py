"""-------------------------------------------------------------------------------------------
Created on November 16, 2018
@author: vpriya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984774
Test Case Title =  Verify Curved Line Chart via Advance chart tool bar
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart

class C6984774_TestClass(BaseTestCase):

    def test_6984774(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        
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
            STEP 04 : Add fields as follows: Category under Columns; Product under Horizontal axis; Unit Sales, Dollar Sales under Vertical axis.
        """
        active_chart.drag_field_from_data_tree_to_query_pane('Category', 1, 'Columns')
        active_chart.wait_for_visible_text("text[class='colHeader-label!']", 'Category', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class='colHeader-label!']", 'Category : Product', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Unit Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Unit Sales', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Dollar Sales', 1)
        active_chart.wait_for_visible_text("text[class='legend-labels!s1!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
            STEP 05 : Right click Horizontal Axis and check 'Suppress Empty Group'
            STEP 05.1 : Expect to see the following Preview pane with Suppress Empty Group checked.
        """
        active_chart.verify_query_field_checked_context_menu('Horizontal Axis', 1, ['Suppress Empty Group'], 'Step 05.01 : Verify Suppress Empty Group checked')
        active_chart.verify_column_label_in_preview(['Category : Product', 'Coffee'], msg='Step 05.02')
        active_chart.verify_x_axis_label_in_preview(['Capuccino', 'Espresso'], msg='Step 05.03')
        active_chart.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'], msg='Step 05.04')
        active_chart.verify_legends_in_preview(['Unit Sales', 'Dollar Sales'], msg='Step 05.05')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 4, msg='Step 05.06 : Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!r0!c0!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 05.07')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g0!mbar!r0!c0!']", 'pale_green', parent_css='#pfjTableChart_1', msg='Step 05.08')
        
        """
            STEP 06 : Click the Run button.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s1!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
            STEP 06.1 : Expect to see the following bucketized bar chart.
        """
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 06.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 06.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 06.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 06.04')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 20, msg='Step 06.05 : Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 06.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbodyMain0', msg='Step 06.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 06.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 06.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
            STEP 07 : Select Advance Chart icon from the tool bar.Scroll down to the Line charts.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 07.01 : Verify Advanced Chart menu')
        
        """
            STEP 08 : Select Straight Line Chart and click OK..
        """
        active_chart.select_advance_chart('wall1', 'curvedline', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='line']", 6, MEDIUM_WAIT_TIME)
        
        """
            STEP 08.01 : Expect to see the bar chart converted into a Curved Line Chart.
        """
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 08.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 08.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 08.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 08.04')
        active_chart.verify_number_of_risers_in_run_window('path', 1, 6, msg='Step 08.05 : Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 08.06', attribute='stroke')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mline!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbodyMain0', msg='Step 08.07', attribute='stroke')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 08.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 08.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 08.10 ', parent_css='#MAINTABLE_wmenu0')
        
if __name__ == '__main__':
    unittest.main()          