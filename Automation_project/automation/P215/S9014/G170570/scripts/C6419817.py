'''
Created on Oct 22, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6419817&group_by=cases:section_id&group_order=asc&group_id=170570
Testcase Name : Verify to check Advanced Chart tool for Pie - 'Sales by Region Dashboard - Line Chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart

class C6419817_TestClass(BaseTestCase):

    def test_C6419817(self):
        
        driver = self.driver
       
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)

        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        MEDIUM_WAIT= 95
        SHORT_WAIT=20
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_1"
        
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        PIE_EXPECTED_LABEL=['Sales (TY)', 'Sales (LY)']
        
        CHART_TITLE='Sales by Product Category'
        
        WALL1_WINDOW_CSS="wall1"
        WALL1_BAR_CSS="#"+WALL1_WINDOW_CSS+" .arToolColumnBorder"
        
        PIE_RISER_CSS1="[class='riser!s0!g0!mwedge!']"
        PIE_RISER_CSS2="[class='riser!s4!g1!mwedge!']"
        TOTAL_RISERS="[class*='riser!s']"
        
        RINGPIE_LABEL_CSS="#MAINTABLE_0 [class^='totalLabel']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 1:Sign to Webfocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 2:Run the Document using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
         
        """
        Step 3:Go to Line chart "Sales by Month(TY vs LY)"
        Step 4:Click "Advanced Chart" icon > Pie > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "piebevel", index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        NO_OF_RISERS_WITHTAGNAME="#"+PARENT_CSS+" [class*='riser']"
        PIE_EXPECTED_LEGENDLIST=['1', '2', '3', '6', '7', '8', '9', '10', '11', '12']
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 05:01:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS1, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05:02: Verify color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 05:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(PIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!']", msg='Step 05:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 4, "Step 05:07: Verify number of pie slicers")
        
        """
        Step 5:Click "Advanced Chart" icon > Pie with Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "piewithdepth", index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 124, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 05:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS1, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 05:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 114, "Step 05:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(PIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!']", msg='Step 05:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 16, "Step 05:07: Verify number of pie with depth")
        
        """
        Step 6:Click "Advanced Chart" icon > Donut (Cylinder) > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "dountcylinder", index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 48, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        PIE_EXPECTED_TOTALLABEL1=['37.5M', '32.6M']
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 06:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS1, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 06:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 52, "Step 06:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(PIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!']", msg='Step 06:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 06:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 7, "Step 06:07: Verify number of donut cylinder")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, PIE_EXPECTED_TOTALLABEL1, "Step 06:08: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True)
        
        """
        Step 7:Click "Advanced Chart" icon > Donut with Depth > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "dountwithDepth", index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 148, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 07:01: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS1, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 07:02:")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 140, "Step 07:03: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_pie_label_in_single_group_in_run_window(PIE_EXPECTED_LABEL, parent_css="#"+PARENT_CSS, label_css="text[class^='pieLabel!']", msg='Step 07:04:')
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07:05: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 07:06:")
        chart_obj.verify_number_of_risers(NO_OF_RISERS_WITHTAGNAME, 7, 20, "Step 07:07: Verify number of donut cylinder")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, PIE_EXPECTED_TOTALLABEL1, "Step 07:08: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True)
        
        """
        Step 8:Click "Advanced Chart" icon > Donut > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "donutbevel", index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 24, MEDIUM_WAIT)
        
        """
        Verify the Output
        """
        chart_obj.verify_legends_in_run_window(PIE_EXPECTED_LEGENDLIST, parent_css="#"+PARENT_CSS, msg="Step 08:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS1, 'bar_blue', parent_css="#"+PARENT_CSS, msg="Step 08:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(PIE_RISER_CSS2, 'brick_red', parent_css="#"+PARENT_CSS, msg="Step 08:03: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(PARENT_CSS, PIE_EXPECTED_LABEL, "Step 08:04: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 08:06: Verify number of pie segments in the chart", custom_css=TOTAL_RISERS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 08:07:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:08: Verify active chart toolbar", parent_css="#"+PARENT_CSS)
        
        """
        Step 9:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()