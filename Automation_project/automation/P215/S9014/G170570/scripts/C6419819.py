'''
Created on Oct 23, 2018

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419819
Testcase Name : Verify to check Advanced Chart tool for Line - 'Sales by Region Dashboard - Line chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart

class C6419819_TestClass(BaseTestCase):

    def test_C6419819(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 70
        SHORT_WAIT=25
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        chart_title='Sales by Month (TY vs LY)'
        x_axis_title=['Sale Month']
        expected_legend_list=['Sales (TY)', 'Sales (LY)']
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_1"
        WALL1_WINDOW_CSS="wall1"
        WALL1_BAR_CSS="#"+WALL1_WINDOW_CSS+" #chticon_1_1_bar1"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_markers="circle[class^='marker']"
        linechart_no_of_riser_css="#"+PARENT_CSS+" "+linechart_no_of_risers
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """Step 1 :Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 2 :Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex"""
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=CHART_SEGMENT_CSS, no_of_element=26)
        
        """
        Step 3: Go to Line chart "Sales by Month(TY vs LY)"
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        """
        Step 04 : Click "Advanced Chart" icon > Line > OK
        """
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "line", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
       
        """
        Verify the Output 
        """
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 04:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 04:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 04:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 04:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 04:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 04:6: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 04:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 04:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 5: Click "Advanced Chart" icon > Curved > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "curvedline", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 05:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 05:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 05:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 05:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 05:6: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 05:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 6: Click "Advanced Chart" icon > Straight > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "strightline", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 06:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 06:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 06:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 06:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 06:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 06:6: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 06:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 7:Click "Advanced Chart" icon > Curved+ Markers > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "curvedplusmarkers", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 07:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 07:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 07:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 07:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 07:5: Verify line color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='marker!s0!g0!mmarker!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 07:6: Verify marker color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 07:7: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:8: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 07:9: ")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 07:10: Verify number of marker segments in line chart", custom_css=linechart_no_of_markers)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 07.11: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 8:Click "Advanced Chart" icon > Straight + Markers > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "strightplusmarkers", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """Verify the Output"""
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 08:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 08:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 08:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 08:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 08:5: Verify line color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='marker!s0!g0!mmarker!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 08:6: Verify marker color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 08:7: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:8: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 08:9: ")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 08:10: Verify number of marker segments in line chart", custom_css=linechart_no_of_markers)
        active_chart_obj.verify_chart_title(chart_title, msg="Step 08.11: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 09:Click "Advanced Chart" icon > Step > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "stepline", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 09:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 09:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 09:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 09:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 09:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 09:6: Verify number of segments in line chart")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 09:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 09.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 10:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()