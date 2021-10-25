'''
Created on Sep 28, 2018

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419803
Testcase Name : Verify to check Advanced Chart tool for Area- 'Sales by Region Dashboard - Pie chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.lib import utillity

class C6419803_TestClass(BaseTestCase):

    def test_C6419803(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 70
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_0"
        RINGPIE_EXPECTED_LABEL=['Revenue']
        RINGPIE_EXPECTED_LEGENDLIST=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        RINGPIE_RISER_CSS1="[class='riser!s4!g0!mwedge!']"
        RINGPIE_RISER_CSS2="[class='riser!s0!g0!mwedge!']"
        RINGPIE_RISER_CSS3="[class='riser!s3!g0!mwedge!']"
        TOTAL_RISERS="[class*='riser!s']"
        CHART_TITLE='Sales by Product Category'
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" path[class^='riser!']"
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        RINGPIE_LABEL_CSS="#"+PARENT_CSS+" [class^='totalLabel']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 02 : Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
        RINGPIE_EXPECTED_TOTALLABEL1=['70.1M']
        
        """Verify output"""
        chart_obj.verify_legends_in_run_window(RINGPIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS1, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS2, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RINGPIE_RISER_CSS3, 'pale_yellow', parent_css="#"+PARENT_CSS, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_LABEL, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, RINGPIE_EXPECTED_TOTALLABEL1, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 03:07: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 03:08:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        
        """
        Step 03 : Go to the Pie chart "Sales by Product Category"
        Step 04 : Click "Advanced Chart" icon
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        
        """
        Step 05 : Click "Advanced Chart" icon > Area > OK
        """
        wall1_window_css="wall1"
        active_chart_obj.select_advance_chart(wall1_window_css, "area")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_RISER_CSS1="riser!s0!g0!marea!"
        BAR_EXPECTED_LEGENDLIST=['Product Category', 'Revenue']
        BAR_EXPECTED_XAXIS_TITLE=['Product Category']
        BAR_EXPECTED_YAXIS_TITLE=['Revenue']
        BAR_EXPECTED_XAXIS_LABELLIST=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Produc...']
        BAR_EXPECTED_YAXIS_LABELLIST1=['0', '4M', '8M', '12M', '16M', '20M', '24M']
        
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 1, "Step 05:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 05:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 05:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 05:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 05:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 05:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 1, msg="Step 05:10 :")
        
        """
        Step 06 : Click "Advanced Chart" icon > Stacked Area > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "stackedarea")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 06:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 06:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 1, "Step 06:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 06:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 06:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 06:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 06:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST1, parent_css="#"+PARENT_CSS, msg="Step 06:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 1, msg="Step 06:10 :")
        
        """
        Step 07 : Click "Advanced Chart" icon > Percent Area > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        active_chart_obj.select_advance_chart(wall1_window_css, "percentarea")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        BAR_EXPECTED_YAXIS_LABELLIST2=['0%', '20%', '40%', '60%', '80%', '100%']
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:01 : Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 07:02 :")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='"+BAR_RISER_CSS1+"']", 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 07:03 : Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 1, "Step 07:04 : Verify number of segments in bar chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_legends_in_run_window(BAR_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 07:05 : Verify legends")
        chart_obj.verify_x_axis_title_in_run_window(BAR_EXPECTED_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 07:06 :")
        chart_obj.verify_y_axis_title_in_run_window(BAR_EXPECTED_YAXIS_TITLE, parent_css="#"+PARENT_CSS, msg="Step 07:07 :")
        chart_obj.verify_x_axis_label_in_run_window(BAR_EXPECTED_XAXIS_LABELLIST, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5, msg="Step 07:08 :")
        chart_obj.verify_y_axis_label_in_run_window(BAR_EXPECTED_YAXIS_LABELLIST2, parent_css="#"+PARENT_CSS, msg="Step 07:09 :")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 1, 1, msg="Step 07:10 :")
        
        """
        Step 08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()