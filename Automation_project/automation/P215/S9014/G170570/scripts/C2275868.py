'''
Created on Dec 17, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275868&group_by=cases:section_id&group_id=170570&group_order=asc
Testcase Name : Verify to Interaction with 'Sales by Region Dashboard - Report'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.wftools import active_report
from common.lib import utillity
from common.lib import core_utility
import time


class C2275868_TestClass(BaseTestCase):

    def test_C2275868(self):

        driver = self.driver
        Testcase_ID = 'C2275868'
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        utillobj=utillity.UtillityMethods(driver)
        core_util_obj=core_utility.CoreUtillityMethods(driver)
        active_report_obj=active_report.Active_Report(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        MEDIUM_WAIT= 25
        USER_NAME='mrbasid'
        PASSWORD= 'mrbaspass'
        FEX_NAME='Sales_by_Region_Dashboard_Active'
        FOLDER_NAME='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PARENT_CSS="wall1"
        RINGPIE_LABEL_CSS="#MAINTABLE_0 [class^='totalLabel']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 1:Sign to Webfocus using rsbas (basic user)
        http://machine:port/ibi_apps
        Step 2:Run the Document using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """
        chart_obj.run_fex_using_api_url(FOLDER_NAME, FEX_NAME, mrid=USER_NAME, mrpass=PASSWORD, run_chart_css=RINGPIE_LABEL_CSS, no_of_element=1)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds01.xlsx', 'Step 2:Verify active report',table_css="#ITableData2")
 
        """
        Step 3:Go to the Report "% Change and Gross Profit % by Product"
        Step 4:Click on Model dropdown > Select Chart > Column > Product Category
        """
        
        active_report_obj.select_menu_items('ITableData2', 1, 'Model')
        first_menu_css="#dt2_1_0 table tbody #t2_1_0_5"
        utillobj.synchronize_until_element_is_visible(first_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(first_menu_css, 'Model column chart menu')
        core_util_obj.left_click(elem1)
        second_menu_css="table tbody #set2_1_0_5_2i_t"
        utillobj.synchronize_until_element_is_visible(second_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(second_menu_css, 'Model column chart menu')
        core_util_obj.move_to_element(elem1,'bottom_left',mouse_move_duration=0.05)
        #core_util_obj.left_click(elem1,'bottom_left')
        time.sleep(5)
        third_child_menu_css="div[id='dt2_1_0_5_2'] table tbody #set2_1_0_5_2_4i_t"
        
# #         utillobj.synchronize_until_element_is_visible(third_child_menu_css, MEDIUM_WAIT)
#         parent_object=utillobj.validate_and_get_webdriver_object("div[id='dt2_1_0_5_2']", 'Model column chart menu')
        elem1=utillobj.validate_and_get_webdriver_object(third_child_menu_css, 'Model column chart menu')
        core_util_obj.left_click(elem1)
        active_report_obj.wait_for_visible_text("#wbody1_ft div", 'Model by Product Category', time_out=MEDIUM_WAIT)
 
        """
        Step 5:Verify the following Chart is displayed
        """
        CHART_TITLE='Sales by Product Category'
        LINECHART_X_AXIS_LABEL=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        LINECHART_Y_AXIS_LABEL=['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        ACTIVE_CHART_TOOLBAR_LIST=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Count']
        chart_obj.verify_x_axis_label_in_run_window(LINECHART_X_AXIS_LABEL, parent_css="#"+PARENT_CSS, xyz_axis_label_length=5,msg="Step 05:03: ")
        chart_obj.verify_y_axis_label_in_run_window(LINECHART_Y_AXIS_LABEL, parent_css="#"+PARENT_CSS, msg="Step 05:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g3!mbar!']", "bar_blue", parent_css="#"+PARENT_CSS, msg="Step 05:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(PARENT_CSS, 7, "Step 05:06:")
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_CHART_TOOLBAR_LIST, msg="Step 05:07: ", parent_css="#"+PARENT_CSS)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', CHART_TITLE, msg="Step 05:09: Verify Ringpie chart title")

        """
        Step 6:Close the Chart window
        """
        active_chart_obj.close_active_chart_popup_dialog('1')
 
        """
        Step 7:Click 'Model' dropdown > Select "Roll Up" > Product Category
        Verify the following output
        """
        active_report_obj.select_menu_items('ITableData2', 1, 'Model')
        
        first_menu_css="#dt2_1_0 table tbody #t2_1_0_6"
        utillobj.synchronize_until_element_is_visible(first_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(first_menu_css, 'Model column chart menu')
        core_util_obj.left_click(elem1,mouse_move_duration=0.05)
        time.sleep(0.75)
        second_menu_css="table tbody #set2_1_0_6_4i_t"
        utillobj.synchronize_until_element_is_visible(second_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(second_menu_css, 'Model column chart menu')
        core_util_obj.left_click(elem1,mouse_move_duration=0.05)
        time.sleep(0.75)
        title_css="[id^='THEAD_'] div tt div"
        active_report_obj.wait_for_visible_text(title_css, 'Model by Product Category', time_out=MEDIUM_WAIT)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds02.xlsx','Step 7:Verify report data',table_css="#ITableData4")

        """
        Step 8:Close the Roll up window
        """
        active_chart_obj.close_active_chart_popup_dialog('1')
 
        """
        Step 9:Click on Sales(TY) dropdown > Select 'Sort Ascending'
        Verify the Report gets sorted in ascending order
        """
        active_report_obj.select_menu_items('ITableData2', 4, 'Sales(TY)')
        first_menu_css="table tbody #set2_4_0_0i_t"
        utillobj.synchronize_until_element_is_visible(first_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(first_menu_css, 'Sales(TY) column chart menu')
        core_util_obj.left_click(elem1)
        time.sleep(1)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds03.xlsx', 'Step 9:Verify report data',table_css="#ITableData2")

        """
        Step 10:Click "Gross Profit" dropdown > Unselect Visualize
        """
        active_report_obj.select_menu_items('ITableData2', 7, 'Gross Profit %')
        first_menu_css="table tbody #set2_7_0_8i_t"
        utillobj.synchronize_until_element_is_visible(first_menu_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(first_menu_css, 'Gross profit column report menu')
        core_util_obj.left_click(elem1)
        time.sleep(0.75)
        active_report_obj.wait_for_visible_text('#ITableData2 tr:nth-child(3) td:nth-child(4)', '$0', time_out=MEDIUM_WAIT)

        """
        Step 11:Verify the Data bars are removed
        """
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds04.xlsx', 'Step 11:Verify report data',  table_css="#ITableData2")

        """
        Step 12:Click 'Variance' dropdown > Select Restore Original
        Verify it restored back to original value
        Verify the first row value of report output
        """
        active_report_obj.select_menu_items('ITableData2', 5, 'Variance')
        restore_css="table tbody #set2_5_0_22i_t"
        utillobj.synchronize_until_element_is_visible(restore_css, MEDIUM_WAIT)
        elem1=utillobj.validate_and_get_webdriver_object(restore_css, 'Restore Original')
        core_util_obj.left_click(elem1)
        active_report_obj.wait_for_visible_text("#ITableData2 tr:nth-child(3) td:nth-child(5)", '$118,193', time_out=MEDIUM_WAIT)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds01.xlsx', 'Step 12:Verify report data',table_css="#ITableData2")
        
        """
        Step 13:Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        active_report_obj.wait_for_visible_text("#ITableData2 tr:nth-child(3) td:nth-child(5)", '$118,193', time_out=MEDIUM_WAIT)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_Ds01.xlsx', 'Step 13:Verify report data', table_css="#ITableData2")
        
        """
        Step 14:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()