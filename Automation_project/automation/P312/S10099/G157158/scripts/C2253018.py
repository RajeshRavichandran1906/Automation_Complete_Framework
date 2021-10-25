'''
Created on Feb 14, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253018
TestCase Name = IA-4048: Visualization, drilldown in Preview creates wrong filter
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253018_TestClass(BaseTestCase):

    def test_C2253018(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253018'
        visual = visualization.Visualization(self.driver)
        sleep_time=4
        position=1
        chart_type='bar'
        riser=[20,315,8]
        time_out=300
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
         
        """
        Step 02: Change > Bar (side by side)
        """
        visual.change_chart_type(chart_type)
        parent_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        visual.wait_for_number_of_element(parent_css, riser[2])
         
        """
        Step 03: Double click Shipment Unit(s) and Sale,Year/Quarter
        """
        field_name='Shipment Unit(s)'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, time_out)
        field_name="Sale,Year/Quarter"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[0], time_out)
         
        """
        Step 04: Verify label values
        """
        x_axis_title=['Sale Year/Quarter']
        visual.verify_x_axis_title(x_axis_title, msg='Step 4.1')
        y_axis_title=['Shipment Unit(s)']
        visual.verify_y_axis_title(y_axis_title, msg='Step 4.2')
        expected_xaxis_label=['2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 4.3')
        expected_yaxis_label=['0', '30K', '60K', '90K', '120K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 4.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, riser[0], msg='Step 4.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 4.6')
         
        """
        Step 05: Verify first and last 3 bar values
        """
        expected_tooltip_list=['Sale Year/Quarter:2012 Q1', 'Shipment Unit(s):3,017', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 5.1: Verify Tooltip') 
        expected_tooltip_list=['Sale Year/Quarter:2016 Q4', 'Shipment Unit(s):115,716', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        visual.verify_tooltip('riser!s0!g19!mbar!', expected_tooltip_list,'Step 5.2: Verify Tooltip') 
         
        """
        Step 06: Drag Product,Category to Color bucket
        """
        visual.drag_field_from_data_tree_to_query_pane("Product,Category", position, "Color")
        parent_css="#queryTreeWindow table tr:nth-child(12) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Product,Category', time_out=time_out)
         
        """
        Step 07: Drag Days,Delayed to Size bucket
        """
        time.sleep(sleep_time)
        visual.drag_field_from_data_tree_to_query_pane("Days,Delayed", position, "Size")
        parent_css="#queryTreeWindow table tr:nth-child(14) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Days,Delayed', time_out=time_out)
         
        """
        Step 08: Verify query pane
        """
        visual.verify_field_listed_under_querytree( 'Vertical Axis', 'Shipment Unit(s)', position, "Step 08.1:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Sale,Year/Quarter', position, "Step 08.2:")
        visual.verify_field_listed_under_querytree('Marker', 'Product,Category', position+position, "Step 08.3:")
        visual.verify_field_listed_under_querytree('Size', 'Days,Delayed', position, "Step 08.4:")
         
        """
        Step 09: Verify first and last 2 bar tooltip values
        """
        expected_tooltip_list=['Sale Year/Quarter:2016 Q4', 'Shipment Unit(s):35,934', 'Days Delayed:19,333', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip('riser!s4!g19!mbar!', expected_tooltip_list,'Step 09.1: Verify Tooltip') 
                   
        """
        Step 10: Right click Days,Delayed > More > Aggregation > Maximum
        """
        visual.right_click_on_field_under_query_tree('Days,Delayed', position, context_menu_path='More->Aggregation Functions->Maximum')
         
        """
        Step 11: Verify query pane (Days,Delayed changed to MAX Days Delayed)
        """
        parent_css="#queryTreeWindow table tr:nth-child(14) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='MAX.Days,Delayed', time_out=time_out)
        visual.verify_field_listed_under_querytree('Size', 'MAX.Days,Delayed', position, "Step 11:")
         
        """
        Step 12: Hover over a bar belonging to category "Stereo Systems" (tallest bar)
        Step 13: Verify tooltip
        """
        expected_tooltip_list=['Sale Year/Quarter:2016 Q4', 'Shipment Unit(s):35,934', 'MAX Days Delayed:8', 'Product Category:Stereo Systems', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip('riser!s4!g19!mbar!', expected_tooltip_list,'Step 13: Verify Tooltip') 
         
        """
        Step 14: Select "Drill Down" on Product,SubCategory
        """
        visual.select_tooltip('riser!s4!g16!mbar!', "Drill down to->Product Subcategory")
        
        """
        Step 15: Verify (Product Category) query is added to filter pane
        """
        parent_css="#qbFilterBox table>tbody>tr>td img"
        visual.wait_for_number_of_element(parent_css, position, time_out)
        visual.verify_field_in_filterbox('PRODUCT_CATEGORY and TIME_DATE_QTR_COMPONENT', position, "Step 15:")
        
        """
        Step 16: Verify legend title
        """
        parent_css="#MAINTABLE_wbody1 .legend text[class='legend-title']"
        visual.wait_for_number_of_element(parent_css, position, time_out)
        visual.verify_x_axis_title(['Sale Year/Quarter'], msg='Step 16.1')
        visual.verify_y_axis_title(['Shipment Unit(s)'], msg='Step 16.2')
        expected_xaxis_label=['2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 16.3')
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 16.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, riser[1], msg='Step 16.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g16!mbar!']", "bar_blue", msg='Step 16.6')
        expected_legend_list=['Product Subcategory', 'Blu Ray', 'Charger', 'DVD Players', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_legends(expected_legend_list, msg='Step 16.7')
        
        """
        Step 17: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 18: Verify output (hover on all bar values and verify tooltip)
        """
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Sale Year/Quarter', time_out=time_out)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[1], time_out)
        visual.verify_x_axis_title(['Sale Year/Quarter'], msg='Step 18.1')
        visual.verify_y_axis_title(['Shipment Unit(s)'], msg='Step 18.2')
        expected_xaxis_label=['2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 18.3')
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 18.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, riser[1], msg='Step 18.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g16!mbar!']", "bar_blue", msg='Step 18.6')
        expected_legend_list=['Product Subcategory', 'Blu Ray', 'Charger', 'DVD Players', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_legends(expected_legend_list, msg='Step 18.7')
        expected_tooltip_list=['Sale Year/Quarter:2016 Q4', 'Shipment Unit(s):21,951', 'MAX Days Delayed:8', 'Product Subcategory:Blu Ray', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to']
        visual.verify_tooltip('riser!s0!g19!mbar!', expected_tooltip_list,'Step 18.8: Verify Tooltip')
        visual.take_run_window_snapshot(Test_Case_ID, '18')
        
        """
        Step 19: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 20: Click "Save" in the toolbar > Type C2141218 > Click "Save" in the Save As dialog
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[1])
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
        Step 21: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()