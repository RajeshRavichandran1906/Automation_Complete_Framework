'''
Created on Dec 26, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986663
Test Case Title =  Verify all Bar options via Advanced chart tool.
'''

import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.active_chart import Active_Chart

class C6986663_TestClass(BaseTestCase):

    def test_C6986663(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
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
        STEP 04 : Add fields as follows:
        Category under Columns.
        Product under Horizontal axis.
        Unit Sales, Dollar Sales under Vertical axis.
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
        STEP 04.1 : Expect to see the following Preview.
        """
        active_chart.verify_column_label_in_preview(['Category : Product', 'Coffee'], msg='Step 04.01')
        active_chart.verify_x_axis_label_in_preview(['Capuccino', 'Espresso'], msg='Step 04.2')
        active_chart.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'], msg='Step 04.3')
        active_chart.verify_legends_in_preview(['Unit Sales', 'Dollar Sales'], msg='Step 04.4')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 4, msg='Step 04.5 : Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!r0!c0!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 04.6')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g0!mbar!r0!c0!']", 'pale_green', parent_css='#pfjTableChart_1', msg='Step 04.7')
        
        """
        STEP 05 : Click the Run button.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s1!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Expect to see the following bucketized bar chart.
        """
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 05.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 05.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 05.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 05.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 05.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 05.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 05.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 05.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 05.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 05.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 06 : Select the Advanced Chart icon from the tool bar.
        Click the Vertical Column option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 06 : Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'column', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 06.01 : Expect to see the bar chart converted into a Vertical Column Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 06.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 06.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 06.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 06.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 06.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 06.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 06.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 06.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 06.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 07 : Again select Advanced Chart icon from the tool bar.
        Select the Stacked Column option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 07: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'stackedcolumn', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 07.01 : Expect to see the bar chart converted into a Stacked Column Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 07.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 07.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '3M', '6M', '9M', '12M', '15M'], msg='Step 07.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 07.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 07.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 07.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 07.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 07.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 07.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 07.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 08 : Again select Advanced Chart icon from the tool bar.
        Select the Percent Column option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 08: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'percentcolumn', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 08.01 : Expect to see the bar chart converted into a Percent Column Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 08.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 08.02')
        active_chart.verify_y_axis_label_in_run_window(['0%', '20%', '40%', '60%', '80%', '100%'], msg='Step 08.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 08.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 05.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 08.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 08.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 08.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 08.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 08.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 09 : Again select Advance Chart icon from the tool bar.
        Select the Column Depth option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 09: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'columndepth', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 40, MEDIUM_WAIT_TIME)
        
        """
        STEP 09.01 : Expect to see the bar chart converted into a Column Depth Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 09.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 09.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 09.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 09.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 40, msg='Step 09.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 09.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 09.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 09.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 09.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 09.10 ', parent_css='#MAINTABLE_wmenu0')
        
        gradient_fill_css="#MAINTABLE_wbody0 rect[fill='url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_100p_20p_204204204_1_95p_136136136_1)']"
        utillobj.verify_object_visible(gradient_fill_css, True, 'Step 09.11 : Verify Column Depth gradient_fill')
        
        """
        STEP 10 : Again select Advance Chart icon from the tool bar.
        Select the Stacked Depth option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 10: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'stackeddepth', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 10.01 : Expect to see the bar chart converted into a Stacked Depth Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 10.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 10.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '3M', '6M', '9M', '12M', '15M'], msg='Step 10.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 10.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 10.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 10.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 10.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 10.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 10.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 10.10 ', parent_css='#MAINTABLE_wmenu0')
        
        gradient_fill_css="#MAINTABLE_wbody0 rect[fill='url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_100p_20p_204204204_1_95p_136136136_1)']"
        utillobj.verify_object_visible(gradient_fill_css, True, 'Step 10.11 : Verify Stacked Depth gradient_fill')
        
        """
        STEP 11 : Again select Advance Chart icon from the tool bar.
        Select the Percent Depth option.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 11: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'percentdepth', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 11.01 : Expect to see the bar chart converted into a Percent Depth Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_column_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 11.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 11.02')
        active_chart.verify_y_axis_label_in_run_window(['0%', '20%', '40%', '60%', '80%', '100%'], msg='Step 11.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 11.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 11.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 11.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 11.07')
        active_chart.verify_x_axis_title_in_run_window(['Product', 'Product', 'Product'], msg='Step 11.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 11.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 11.10 ', parent_css='#MAINTABLE_wmenu0')
        
        gradient_fill_css="#MAINTABLE_wbody0 rect[fill='url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_100p_20p_204204204_1_95p_136136136_1)']"
        utillobj.verify_object_visible(gradient_fill_css, True, 'Step 11.11 : Verify Percent Depth gradient_fill')
        active_chart.switch_to_default_content()
        
        """
        STEP 12 : Close Run window
        From query pane change category from Columns to Rows and click run.
        Now click Chart Rollup tool from Active Chart toolbar.
        Select Horizontal Bar chart and click Ok.
        """
        active_chart.drag_field_within_query_pane('Category', 'Rows')
        active_chart.wait_for_visible_text("#queryTreeColumn tr:nth-child(4)", 'Category', MEDIUM_WAIT_TIME)
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s1!']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 12: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'bar', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 12.01 : Expect to see the bar chart converted into a Horizontal Bar Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_rows_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 12.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 12.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 12.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 12.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 12.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 12.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 12.07')
        active_chart.verify_x_axis_title_in_run_window(['Product'], msg='Step 12.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 12.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 12.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 13 : Again select Advance Chart icon from the tool bar.
        Select the second Horizontal option, Stacked Bar.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 13 : Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'stackedbar', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 13.01 : Expect to see the bar chart converted into a Horizontal stackedbar Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_rows_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 13.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 13.02')
        active_chart.verify_y_axis_label_in_run_window(['0', '3M', '6M', '9M', '12M', '15M'], msg='Step 13.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 13.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 13.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 13.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 13.07')
        active_chart.verify_x_axis_title_in_run_window(['Product'], msg='Step 13.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 13.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 13.10 ', parent_css='#MAINTABLE_wmenu0')
        
        """
        STEP 14 : Again select Advance Chart icon from the tool bar.
        Select the third Horizontal option, Percent Bar.
        Click Ok.
        """
        active_chart.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart.verify_popup_or_dialog_caption_text('#wall1', 'Chart/Rollup Tool', 'Step 14: Verify Advanced Chart menu')
        active_chart.select_advance_chart('wall1', 'percentbar', 0)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser']", 20, MEDIUM_WAIT_TIME)
        
        """
        STEP 14.01 : Expect to see the bar chart converted into a Horizontal percentbar Chart.
        """
        time.sleep(SHORT_TIME/2)
        active_chart.verify_rows_label_in_run_window(['Category', 'Coffee', 'Food', 'Gifts'], msg='Step 14.01')
        active_chart.verify_x_axis_label_in_run_window(['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos'], msg='Step 14.02')
        active_chart.verify_y_axis_label_in_run_window(['0%', '20%', '40%', '60%', '80%', '100%'], msg='Step 14.03')
        active_chart.verify_legends_in_run_window(['Unit Sales', 'Dollar Sales'], msg='Step 14.04')
        active_chart.verify_number_of_risers('#MAINTABLE_wbody0_f rect', 1, 20, msg='Step 14.05: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 14.06')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbody0', msg='Step 14.07')
        active_chart.verify_x_axis_title_in_run_window(['Product'], msg='Step 14.08')
        active_chart.verify_chart_title('Unit Sales, Dollar Sales BY Category, Product', msg='Step 14.09', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 14.10 ', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 15 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()