'''
Created on Oct 22, 2018

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419821
Testcase Name : Verify to check Advanced Chart tool for Area - 'Sales by Region Dashboard - Line Chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.lib import utillity

class C6419821_TestClass(BaseTestCase):

    def test_C6419821(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 70
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
        TOTAL_RISERS="[class*='riser!s']"
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" path[class^='riser!']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+PARENT_CSS+" "+linechart_no_of_risers
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 02 : Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=CHART_SEGMENT_CSS, no_of_element=26)
        
        """Verify output"""
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 02:1: ')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 02:2: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 02:3: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 02:4: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 02:5: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 02:6:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 02:7: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 02:8: ")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 02.9: Verify Line chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 03 : Go to Line chart "Sales by Month(TY vs LY)"
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        
        """
        Step 04 : Click "Advanced Chart" icon > Area > OK
        """
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "area", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_RISER_CSS1="riser!s0!g0!marea!"
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 04:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 04.2 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 2, "Step 04.3: Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 04.4: Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg="Step 04.5:")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 04.6:")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 04.7:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 2, msg="Step 04.8:")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.9: Verify Area chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 05 : Click "Advanced Chart" icon > Stacked Area > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedarea", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05.2 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 2, "Step 05.3: Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 05.4: Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg="Step 05.5:")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 05.6:")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 05.7:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 2, msg="Step 05.8:")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.9: Verify Stacked Area chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 06 : Click "Advanced Chart" icon > Percent Area > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "percentarea", 1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_XAXIS_LABELLIST=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0%', '20%', '40%', '60%', '80%', '100%']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 06.2 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 2, "Step 06.3: Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PARENT_CSS, msg="Step 06.4: Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PARENT_CSS, msg="Step 06.5:")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 06.6:")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 06.7:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 2, msg="Step 06.8:")
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.9: Verify Percent Area chart title", parent_css="#"+PARENT_CSS, title_css="[class^='title']")
        
        """
        Step 07: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()
