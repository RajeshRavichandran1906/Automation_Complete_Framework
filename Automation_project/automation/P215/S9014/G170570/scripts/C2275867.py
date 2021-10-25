'''
Created on Oct 18, 2018

@author: BM13368
Testcase Name : Verify Run and Interaction with 'Sales by Region Dashboard - Line chart'
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275867&group_by=cases:section_id&group_id=170570&group_order=asc
'''
import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.pages import active_chart_rollup
from common.wftools import visualization
from common.lib import utillity


class C2275867_TestClass(BaseTestCase):

    def test_C2275867(self):
        
        driver = self.driver
       
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        active_chart_rollup_obj=active_chart_rollup.Active_Chart_Rollup(driver)
        visual_obj=visualization.Visualization(driver)
        utillobj=utillity.UtillityMethods(driver)

        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        MEDIUM_WAIT= 95
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="MAINTABLE_1"
        
        RINGPIE_LABEL_CSS="#MAINTABLE_0 [class^='totalLabel']"
        CHART_SEGMENT_CSS="#"+PARENT_CSS+" .chartPanel [tdgtitle]"
        RISER_CSS1='marker!s1!g6!mmarker!'
        
        LINECHART_X_AXIS_LABEL=['1', '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']
        LINECHART_Y_AXIS_LABEL=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        
        LINECHART_XAXIS_TITLE=['Sale Month']
        LINECHART_EXPECTED_LEGENDS=['Sales (TY)', 'Sales (LY)']
        CHART_TITLE='Sales by Product Category'
        
        ACTIVE_CHART_TOOLBAR_LIST=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 1 : Expected Result
        Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 2 :Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
         
        """ 
        Step 3 :Go to Line chart "Sales by Month(TY vs LY)"
        Step 4:Hover over on point 7 > Click Exclude from chart
        """
        chart_obj.select_tooltip_in_run_window(RISER_CSS1, 'Exclude from Chart', parent_css="#"+PARENT_CSS, yoffset=6, use_marker_enable=True, move_to_tooltip=True)
         
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 04:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 04:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 04:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL, parent_css="#"+PARENT_CSS, msg="Step 04:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 04:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 24, "Step 04:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 04:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 04:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 04:09: Verify Ringpie chart title") 
         
        """
        Step 5:Hover over on point 4 > Click Filter chart
        """
        RISER_CSS1='marker!s1!g3!mmarker!'
        chart_obj.select_tooltip_in_run_window(RISER_CSS1, 'Filter Chart', parent_css="#"+PARENT_CSS, yoffset=6, use_marker_enable=True, move_to_tooltip=True)
        LINECHART_X_AXIS_LABEL=['4']
        LINECHART_Y_AXIS_LABEL=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
         
        """
        Verify the Output
        """
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 05:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 05:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 05:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL, parent_css="#"+PARENT_CSS, msg="Step 05:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 05:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 4, "Step 05:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 05:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 05:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:09: Verify Ringpie chart title")
         
        """
        Step 6:Click "Remove filter" icon
        """
        active_chart_rollup_obj.click_chart_menu_bar_items(PARENT_CSS, 4)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
         
         
        """
        Verify the filter is removed
        """
        LINECHART_X_AXIS_LABEL1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        LINECHART_Y_AXIS_LABEL1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 06:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 06:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 06:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL1, parent_css="#"+PARENT_CSS, msg="Step 06:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 06:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 06:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 06:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 06:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 06:09: Verify Ringpie chart title")
        
        """
        Step 7:Lasso 14 Points > Click Filter Chart
        """
        RISER_CSS1="#"+PARENT_CSS+" [class='marker!s0!g9!mmarker!']"
        source_obj=utillobj.validate_and_get_webdriver_object(RISER_CSS1, 'Line chart source object')
        coord=utillobj.enable_marker_using_javascript(source_obj, 'middle')
        sx=coord['x']+10
        time.sleep(2)
        sy=coord['y']-5
        time.sleep(2)
        RISER_CSS2="#"+PARENT_CSS+" [class='marker!s1!g3!mmarker!']"
        target_obj=utillobj.validate_and_get_webdriver_object(RISER_CSS2, 'Line chart target object')
        coord=utillobj.enable_marker_using_javascript(target_obj, 'middle')
        tx=coord['x']+5
        ty=coord['y']+5
        time.sleep(2)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        visual_obj.select_lasso_tooltip('Filter Chart')
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 16, MEDIUM_WAIT) 
         
        """
        Step 8:Verify the Output
        """
        LINECHART_X_AXIS_LABEL1=['4', '5', '6', '7', '8', '9', '10']
        LINECHART_Y_AXIS_LABEL1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 08:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 08:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 08:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL1, parent_css="#"+PARENT_CSS, msg="Step 08:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 08:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 16, "Step 08:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 08:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 08:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 08:09: Verify Ringpie chart title")
         
        """
        Step 9:Click "Restore Original" from first menu icon
        """
        active_chart_obj.create_new_item(PARENT_CSS, 'Restore Original', index=1)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
         
        """
        Verify restored back to original
        """
        LINECHART_X_AXIS_LABEL1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        LINECHART_Y_AXIS_LABEL1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 09:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 09:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 09:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL1, parent_css="#"+PARENT_CSS, msg="Step 09:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 09:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 09:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 09:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 09:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 09:09: Verify Ringpie chart title")
         
        """
        Step 10:Lasso 8 points > Click Exclude from chart
        """
        RISER_CSS1="#"+PARENT_CSS+" [class='marker!s0!g5!mmarker!']"
        source_obj=utillobj.validate_and_get_webdriver_object(RISER_CSS1, 'Line chart source object')
        coord=utillobj.enable_marker_using_javascript(source_obj, 'middle')
        sx=coord['x']+10
        time.sleep(2)
        sy=coord['y']-5
        time.sleep(2)
        RISER_CSS2="#"+PARENT_CSS+" [class='marker!s1!g2!mmarker!']"
        target_obj=utillobj.validate_and_get_webdriver_object(RISER_CSS2, 'Line chart target object')
        coord=utillobj.enable_marker_using_javascript(target_obj, 'middle')
        tx=coord['x']+5
        ty=coord['y']+5
        time.sleep(2)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 18, MEDIUM_WAIT)
         
        """
        Step 11:Verify the Output
        """
        LINECHART_X_AXIS_LABEL1=['1', '2', '7', '8', '9', '10', '11', '12']
        LINECHART_Y_AXIS_LABEL1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 11:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 11:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 11:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL1, parent_css="#"+PARENT_CSS, msg="Step 11:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 11:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 18, "Step 11:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 11:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 11:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 11:09: Verify Ringpie chart title")
         
        """
        Step 12:Hover over any point on Line chart > Click "Remove Filter"
        """
        chart_obj.select_tooltip_in_run_window('marker!s0!g2!mmarker!', 'Remove Filter', parent_css="#"+PARENT_CSS, yoffset=6, use_marker_enable=True, move_to_tooltip=True)
        chart_obj.wait_for_number_of_element(CHART_SEGMENT_CSS, 26, MEDIUM_WAIT)
          
        """ 
        Step 13:Verify restored back to original
        """
        LINECHART_X_AXIS_LABEL1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        LINECHART_Y_AXIS_LABEL1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 13:01: ')
        chart_obj.verify_legends_in_run_window(LINECHART_EXPECTED_LEGENDS, parent_css="#"+PARENT_CSS, msg='Step 13:02: ')
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL1, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 13:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL1, parent_css="#"+PARENT_CSS, msg="Step 13:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue", parent_css="#"+PARENT_CSS, attribute='stroke', msg="Step 13:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 26, "Step 13:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 13:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_x_axis_title_in_run_window(LINECHART_XAXIS_TITLE, parent_css="#"+PARENT_CSS, msg='Step 13:08: ')
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 13:09: Verify Ringpie chart title")
        
        """
        Step 14:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()