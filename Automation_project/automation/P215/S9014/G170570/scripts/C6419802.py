'''
Created on Oct 17, 2018

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6419802
Testcase Name : Verify to check Advanced Chart tool for Line - 'Sales by Region Dashboard - Pie chart'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart

class C6419802_TestClass(BaseTestCase):

    def test_C6419802(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        MEDIUM_WAIT= 70
        SHORT_WAIT=25
        
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Sales_by_Region_Dashboard_Active'
        folder_name='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_0"
        WALL1_WINDOW_CSS="wall1"
        WALL1_BAR_CSS="#"+WALL1_WINDOW_CSS+" #chticon_1_0_bar1"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        
        linechart_x_axis_label1=['Accessor...', 'Camcorder', 'Computers', 'Media Pl...', 'Stereo S...', 'Televisions', 'Video Pr...']
        linechart_y_axis_label1=['0', '4M', '8M', '12M', '16M', '20M', '24M']
        
        ringpie_chart_title='Sales by Product Category'
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        treemap_parent_css="MAINTABLE_3"
        
        no_of_risers="rect[class^='riser']"
        treemap_no_of_riser_css="#"+treemap_parent_css+" "+no_of_risers
        
        linechart_x_axis_title=['Product Category']
        linechart_y_axis_title=['Revenue']
        linechart_expected_legend_list=['Product Category', 'Revenue']
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """Step 1 :Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 2 :Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex"""
        
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=treemap_no_of_riser_css, no_of_element=31)
        
        """Step 3:Go to the Pie chart "Sales by Product Category
        Step 4:Click "Advanced Chart" icon
        Step 5:Click "Advanced Chart" icon > Line > OK"""
        
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "line")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
       
        """
            Verify linechart 
        """
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 05:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 05:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 05:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 05:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 05:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 05:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 05:09: Verify Ringpie chart title")
        
        """
           Step 6:Click "Advanced Chart" icon > Curved > OK
        
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "curvedline")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
        
        """
            Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 06:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 06:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 06:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 06:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 06:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 06:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 06:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 06:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 06:09: Verify Ringpie chart title")
        
        """
            Step 7:Click "Advanced Chart" icon > Straight > OK
        """
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "strightline")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
            
        
        """Verify the Output"""
        
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 07:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 07:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 07:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 07:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 07:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 07:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 07:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 07:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 07:09: Verify Ringpie chart title")
        
        """
            Step 8:Click "Advanced Chart" icon > Curved+ Markers > OK
        """
        
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "strightline")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
            
        
        """Verify the Output"""
        
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 08:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 08:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 08:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 08:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 08:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 08:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 08:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 08:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 08:09: Verify Ringpie chart title")
        
        """
            Step 9:Click "Advanced Chart" icon > Straight + Markers > OK
        """
        
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "strightplusmarkers")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
            
        
        """Verify the Output"""
        
        marker_css="#MAINTABLE_wbody0_f [class='markers'] circle[class*='marker']"
        
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 09:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 09:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 09:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 09:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 09:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 09:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 09:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 09:08: ')
        chart_obj.verify_number_of_circles_in_run_window(0, 8, "Step 09:09:", marker_css)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 09:10: Verify Ringpie chart title")
        
        
        """Step 10:Click "Advanced Chart" icon > Step > OK"""
        
        active_chart_obj.click_chart_menu_bar_items(PARENT_CSS, 1)
        chart_obj.wait_for_number_of_element(WALL1_BAR_CSS, 1, SHORT_WAIT)
        
        active_chart_obj.select_advance_chart(WALL1_WINDOW_CSS, "stepline")
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 8, MEDIUM_WAIT)
        
        
        """Verify the Output"""
        
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+PARENT_CSS, msg='Step 10:01: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+PARENT_CSS, msg='Step 10:02: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 10:03: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+PARENT_CSS, msg="Step 10:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 10:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 8, "Step 10:06:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 10:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_y_axis_title_in_run_window(linechart_y_axis_title, parent_css="#"+PARENT_CSS, msg='Step 10:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 10:09: Verify Ringpie chart title")
        
        """Step 11:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp"""





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()