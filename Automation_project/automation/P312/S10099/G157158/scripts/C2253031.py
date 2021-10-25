'''
Created on Feb 26, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253031
Test_Case Name : Vis: Multiple Drill and Show Data on 2 By fields at runtime loses showdata values
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253031_TestClass(BaseTestCase):

    def test_C2253031(self):
        
        Test_Case_ID = "C2253031"
        metadata_browser_query_variables__css = "#iaMetaDataBrowser td"  
        metadata_browser_css = "#iaMetaDataBrowser"    
        changed_bar_text_css="[class*='bi-component dv-caption'] div"    
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        short_wait_time_in_sec = 60
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        toolbar_run="#topToolBar #runButton img"
        
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,riser_color_css,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser, tooltip, msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        visual.wait_for_visible_text(metadata_browser_query_variables__css, 'Filters and Variables', short_wait_time_in_sec)
        
        """
        Step02: Double click "Revenue" and "Sale,Year".
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text(yaxis_title_css, "Revenue", 45)
        visual.double_click_on_datetree_item('Sale,Year', 1)
        visual.wait_for_visible_text(xaxis_title_css, "SaleYear", 45)
        
        """
        Step03: Verify labels and riser values
        """
        no_of_riser=6
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['Sale Year']
        y_title=['Revenue']
        expected_xaxis_labels=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yaxis_labels=['0', '100M', '200M', '300M', '400M', '500M']
        year2016_riser="riser!s0!g5!mbar"
        year2016_tooltip=['Sale Year:2016', 'Revenue:$452,307,832.95', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        step_num='03'
        verify_bar_chart(x_title, y_title, expected_xaxis_labels, expected_yaxis_labels, year2016_riser, year2016_riser, no_of_riser, year2016_tooltip, step_num)        
        
        """
        Step04: Add "Customer Business Region" to Horizontal axis.
        Step05: Verify query pane
        """
        visual.wait_for_number_of_element(metadata_browser_css, 1, short_wait_time_in_sec)
        visual.drag_field_from_data_tree_to_query_pane("Customer,Business,Region", 1, "Sale,Year", 1)
        visual.verify_field_listed_under_querytree('Horizontal Axis', "Customer,Business,Region", 2, "Step05.1: Verify Customer Business Region added to Horizontal Axis")
        visual.verify_field_listed_under_querytree('Horizontal Axis', "Sale,Year", 1, "Step05.2: Verify Sale Year added to Horizontal Axis")
        
        """
        Step06: Verify 2015:EMEA bar riser tooltip
        """
        no_of_riser=23
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        EMEA2015_riser_css="riser!s0!g15!mbar"       
        EMEA2015_tooltip=['Sale Year:2015', 'Customer Business Region:EMEA', 'Revenue:$140,440,022.62', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip(EMEA2015_riser_css,EMEA2015_tooltip,msg='Step06: Verify 2015:EMEA bar riser tooltip')
        
        """
        Step07: Click Run in the toolbar
        Step08: Hover over "EMEA:2012" and choose > Drilldown > Sale Quarter.
        """
        visual.wait_for_number_of_element(toolbar_run, 1, short_wait_time_in_sec)
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        q12013_riser_css="riser!s0!g3!mbar"
        visual.select_tooltip(q12013_riser_css, "Drill down to->Sale Quarter", move_to_tooltip=True)
        
        """
        Step09: Verify Chart.
        Step10: Hover on first bar and verify tooltip
        """
        no_of_riser=4
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['Sale Quarter : Customer Business Region']
        y_title=['Revenue']
        expected_xaxis_labels=['1 : EMEA', '2 : EMEA', '3 : EMEA', '4 : EMEA']
        expected_yaxis_labels=['0', '3M', '6M', '9M', '12M', '15M']
        EMEA1_riser="riser!s0!g0!mbar"
        EMEA1_tooltip=['Sale Quarter:1', 'Customer Business Region:EMEA', 'Revenue:$9,122,881.25', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Sale Year', 'Drill down to']
        step_num='10'
        verify_bar_chart(x_title, y_title, expected_xaxis_labels, expected_yaxis_labels, EMEA1_riser, EMEA1_riser, no_of_riser, EMEA1_tooltip, step_num)        
        
        """
        Step11: Click on Show Data from the run menu option.
        Step12: Verify it shows Sale Quarter correctly.
        Step13: Change that to Chart using Run menu option.
        """
        visual.select_bottom_right_run_menu_options('show_report_css')
        show_data_sale_quarter="#MAINTABLE_2 span"
        visual.wait_for_visible_text(show_data_sale_quarter, "SaleQuarter", long_wait_time_in_sec)
#         visual.create_visualization_tabular_report(Test_Case_ID+'_DS_01.xlsx')
        visual.verify_visualization_tabular_report(Test_Case_ID+'_DS_01.xlsx', msg='Step 12.1: Verify Data')
        visual.select_bottom_right_run_menu_options('show_report_css', toggle_button_click='no')
        
        """
        Step14: Hover over any bar(4:EMEA) and click > DrillUp > Sale Year.
        Step15: Verify label values
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        EMEA4_riser_css="riser!s0!g3!mbar"
        visual.select_tooltip(EMEA4_riser_css, "Drill up to Sale Year", move_to_tooltip=True)
        no_of_riser=23
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        
        """
        Step16: Click on Show Data from Run menu option.
        Step17: Verify show data display Sale Year data values
        """
        visual.select_bottom_right_run_menu_options('show_report_css')
        show_data_sale_quarter="#MAINTABLE_3 span"
        visual.wait_for_visible_text(show_data_sale_quarter, "SaleYear", long_wait_time_in_sec)
#         visual.create_visualization_tabular_report(Test_Case_ID+'_DS_02.xlsx', table_css="#MAINTABLE_wbody3 .arPivot table > tbody > tr")
        visual.verify_visualization_tabular_report(Test_Case_ID+'_DS_02.xlsx', table_css="#MAINTABLE_wbody3 .arPivot table > tbody > tr", msg='Step 17: Verify Data')
        
        visual.take_run_window_snapshot(Test_Case_ID, '17')
        visual.switch_to_previous_window()
                 
        """
        Step18: Close the output window
        Step19: Click "Save" in the toolbar > Type C2253017 > Click "Save" in the Save As dialog
        Step20: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
