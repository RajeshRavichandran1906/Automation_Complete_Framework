'''
Created on Jun 13, 2019

@author: Varun/Prasanth
Testcase Name : Auto Drill with Reporting Objects - Chart component
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279919

'''

import unittest
from common.wftools import chart
from common.lib import global_variables
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase

class C7279919_TestClass(BaseTestCase):
    
    def test_C7279919(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        global_var_obj=global_variables.Global_variables()
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        case_id=global_var_obj.current_test_case
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch MyReport (Chart mode) using the below API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/RO-Chart.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(None, fex_name="RO-Chart")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        utils.wait_for_page_loads(chart_obj.home_page_long_timesleep, pause_time=5) #firefox its required
        
        """
        STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
        self.driver.set_page_load_timeout(chart_obj.chart_long_timesleep)
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """
        STEP 3: Click Run in toolbar
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame("iframe")
        chart_obj.wait_for_visible_text(".chart", "Store Business Region : Product Category" )
        
        """
        STEP 3.01 Expected: Check the following Output.
        """
        if global_var_obj.browser_name in ["chrome", "cr"]:
            expected_x_axis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Product...']
        else:
            expected_x_axis_label_list = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, msg="Step 03.01")
        
        expected_y_axis_label_list=['0', '40M', '80M', '120M', '160M', '200M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, msg="Step 03.02")
        
        expected_col_label_list=['Store Business Region : Product Category', 'EMEA', 'North America', 'Oceania', 'South America']
        chart_obj.verify_column_label_in_run_window(expected_col_label_list, "#jschart_HOLD_0", msg="Step 03.03")
        
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 03.04")
        
        expected_legend_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 03.05")
        
        expected_segment_number=139
        chart_obj.verify_number_of_chart_segment("jschart_HOLD_0", expected_segment_number, msg="Step 03.06 : Verify_number_of_chart_segments")
        
        """
        STEP 4: Hover over Top bar(2016) in "Stereo Systems" under "North America" > Hover over "Drill down to" and Click "Store Business Sub Region".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s5!g4!mbar!r0!c1!", 'Drill down to->Store Business Sub Region')
        chart_obj.wait_for_visible_text("#jschart_HOLD_0 foreignObject", visble_element_text="North America")
        
        """
        STEP 5: Hover over "Stereo Systems" under "West" > Hover over "Drill down to" and Click "Sale Year/Quarter".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s0!g0!mbar!r0!c7!", 'Drill down to->Sale Year/Quarter')
        chart_obj.wait_for_visible_text("#jschart_HOLD_0 foreignObject", visble_element_text="2016")
        
        """
        STEP 6: Hover over "Top bar" > Hover over "Drill down to" and Click "Product Subcategory".
        """
        chart_obj.select_autodrill_chart_tooltip_menu("riser!s3!g0!mbar!r0!c0!", 'Drill down to->Product Subcategory')
        chart_obj.wait_for_visible_text("#jschart_HOLD_0 foreignObject", visble_element_text="Stereo Systems")
        
        """
        STEP 6.01 Expected: Check the Breadcrumb and following Output.
        """
        expected_breadcrumb=['Home->NorthAmerica', 'Home->2016', 'Home->StereoSystems']
        chart_obj.verify_chart_autodrill_breadcrumb_text(expected_breadcrumb, step_num="06.01")
        expected_x_axis_label_list=['Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, msg="Step 06.02")
        
        expected_y_axis_label_list=['0', '1M', '2M', '3M', '4M', '5M', '6M']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, msg="Step 06.03")
        
        expected_col_label_list=['Store Business Sub Region : Product Subcategory', 'West']
        chart_obj.verify_column_label_in_run_window(expected_col_label_list, "#jschart_HOLD_0", msg="Step 06.04")
        
        expected_y_axis_title_list=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 06.05")
        
        expected_legend_list=['Sale Year/Quarter', '2016 Q4']
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 06.06")
        
        expected_segment_number=4
        chart_obj.verify_number_of_chart_segment("jschart_HOLD_0", expected_segment_number, msg="Step 06.07 : Verify_number_of_chart_segments")
        
        """
        STEP 7: Click "IA" menu and Click "Save As" option.
        """
        """
        STEP 8: Enter "C7279919" in Tittle textbox and Click "Save" button.
        """
        chart_obj.switch_to_default_content()
        chart_obj.save_as_from_application_menu_item(case_id,group_id)
        
        """
        STEP 9: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        STEP 10:Reopen the saved fex using API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279871.fex&tool=Report
        """
        chart_obj.edit_fex_using_api_url(folder_name=folder_path, fex_name=case_id)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        utils.wait_for_page_loads(chart_obj.home_page_long_timesleep) #firefox its required
        
        """
        STEP 11:Click "Format" tab
        """
        self.driver.set_page_load_timeout(chart_obj.chart_long_timesleep)
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        
        """
        STEP 11.01 Expected : Check "Auto Drill" button is active.
        """
        chart_obj.verify_ribbon_item_selected("format_auto_drill", "11.01")
        
        """
        STEP 12: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()
        