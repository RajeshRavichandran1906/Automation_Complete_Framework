'''
Created on Dec 5, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=168358&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2314001
TestCase Name = Bucketized Vertical Dual-Axis Clustered Bar Chart Filter/Exclude tests.
'''

import unittest,time 
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart, active_chart, visualization



class C2314001_TestClass(BaseTestCase):

    def test_C2314001(self):
        
        "-------------------------------------------------------------------CLASS OBJECTS--------------------------------------------------------------------------"
        driver = self.driver #Driver reference object created
        chart_obj = chart.Chart(driver)
        visual_obj=visualization.Visualization(driver)
        utillobj = utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 60
        FEX_NAME='Vertical_Cluster_Bar'
        FOLDER_NAME='P292_S10660/G168358'
        chart_title='DEALER_COST, LENGTH by CAR'
        x_axis_title=['CAR']
        y_axis_title=['DEALER_COST']
        y2_axis_title=['LENGTH']
        expected_legend_list=['DEALER_COST','LENGTH']
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        PREVIEW_PARENT_CSS="TableChart_1"
        RUN_PARENT_CSS="MAINTABLE_0_f"
        TOOLBAR_PARENT_CSS="MAINTABLE_wmenu0"
        CHART_SEGMENT_CSS="riser!s0!g0!mbar"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """ 
        Step 01: Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 02: Expand folder P292_S10660_G168358
        Execute the following URL:  
        Open FEX:http://machine:port/{alias/run.bip?BIP_REQUEST_TYPE=BIP_RUNBIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10660_G168358%252F&BIP_item=Vertical_Cluster_Bar.fex
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        chart_obj.edit_fex_using_api_url(FOLDER_NAME, 'chart', FEX_NAME, mrid='mrid', mrpass='mrpass')
        
        """
        Expect to see the following Active Streamgraph.
        """
        parent_css="#TableChart_1 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 02.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+PREVIEW_PARENT_CSS, msg="Step 02.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+PREVIEW_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 02.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 02.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 02.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+PREVIEW_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 02.6')
        chart_obj.verify_chart_color(PREVIEW_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 02.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS, 20, 'Step 02.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+PREVIEW_PARENT_CSS, msg='Step 02.9: ')
        
        """
        Step 03: Click the Run button.
        Expect to see the following Vertical Dual-Axis Clustered Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        time.sleep(5)
        chart_obj.switch_to_frame()
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 03.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 03.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 03.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 03.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 03.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 03.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 03.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 20, 'Step 03.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 03.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 03.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 3.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 3.12: Filter Button Removed')
        
        """
        Step 04: Hover over the first blue bar for Alfa Romeo.
        Select Exclude from Chart.
        Expect to see the following Bar Chart, with Alfa Romeo removed.
        """
        time.sleep(5)  
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s0!g0!mbar!", 'Exclude from Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 18, 20)
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 04.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 04.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 04.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 04.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 04.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 18, 'Step 04.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 04.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.12: Filter Button Visible')
        
        """
        Step 05: Hover over the blue bar for BMW. 
        Select Exclude from Chart.
        Expect to see the following Bar Chart, with Alfa Romeo & BMW removed.
        """
        time.sleep(5)
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s0!g1!mbar!", 'Exclude from Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 16, 20)
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 05.1")
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 05.2")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300','350', '400', '450']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 05.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 05.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 05.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 16, 'Step 05.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 05.12: Filter Button Visible')
        
        """
        Step 06: Hover over the blue bar for Audi.
        Select Remove Filter.
        Expect to see the original Bar Chart with Alfa Romeo and BMW restored.
        """
        time.sleep(5)
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s0!g0!mbar!", 'Remove Filter')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 20, 20)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 06.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 06.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 06.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 06.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 06.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 20, 'Step 06.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 06.12: Filter Button Removed')
        
        """
        Step 07:Left-click and draw a box around the bars for Alfa Romeo and Audi.
        Select Exclude from Chart.
        Expect to see the following Bar chart with both Alfa Romeo and Audi bars removed.
        """
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f [class='riser!s0!g0!mbar!']", 1, 20)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s1!g1!ay2!mbar!")
        visual_obj.create_lasso(source_element, target_element, source_xoffset=0, target_xoffset=10, source_element_location='middle_left')
        visual_obj.select_lasso_tooltip('Exclude from Chart')
#         source_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g0!mbar!']")
#         target_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s1!g1!ay2!mbar!']")
#         visual_obj.create_lasso(source_elem, target_elem, source_element_location='middle_left', target_element_location='bottom_right')
#         time.sleep(3)
#         chart_obj.select_lasso_filter(select_item='Exclude from Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 16, 20)
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 07.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 07.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 07.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 07.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 07.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 07.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 07.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 16, 'Step 07.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 07.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 07.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 07.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        
        """
        Step 08:Hover over the blue bar for BMW
        Select Remove Filter.
        Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        time.sleep(5)
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s0!g0!mbar!", 'Remove Filter')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 20, 20)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 08.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 08.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 08.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 08.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 08.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 20, 'Step 08.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 08.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 08.12: Filter Button Removed')
        
        """
        Step 09:Left-click and draw a box around the bars for Peugeot, Toyota & Triumph.
        Select Filter Chart.
        Expect to see the following Bar Chart with bars for Peugeot, Toyota & Triumph only.
        """
        time.sleep(5)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g7!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s1!g9!ay2!mbar!']")
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, target_xoffset=10, source_element_location='middle_left')
        visual_obj.select_lasso_tooltip('Filter Chart')
        
#         source_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g7!mbar!']")
#         target_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s1!g9!ay2!mbar!']")
#         visual_obj.create_lasso(source_elem, target_elem, source_element_location='middle_left', target_element_location='middle_right')
#         time.sleep(3)
#         chart_obj.select_lasso_filter(select_item='Filter Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 6, 20)
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 09.1")
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 09.2")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 09.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 09.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 09.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 6, 'Step 09.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 09.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.12: Filter Button Visible')

        """
        Step 10:Hover over the blue bar for Toyota.
        Click Filter Chart.
        Expect to see the following Bar Chart with bars for only Toyota.
        """
        time.sleep(5)
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s0!g1!mbar!", 'Filter Chart')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 2, 20)
        expected_xval_list=['TOYOTA']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 10.1")
        expected_yval1_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 10.2")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 10.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 10.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 10.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 2, 'Step 10.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 10.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 10.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.12: Filter Button Visible')
        
        """
        Step 11:Hover over the green bar for Toyota.
        Select Remove Filter.
        Expect to see only the Remove Filter selection.
        Expect to see the original Bar Chart with Alfa Romeo and Audi restored.
        """
        time.sleep(5)
        chart_obj.select_default_tooltip_menu_in_run_window("MAINTABLE_0_f","riser!s1!g0!ay2!mbar!", 'Remove Filter')
        utillobj.wait_for_page_loads(10)
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0_f svg g.risers >g>rect[class^='riser']", 20, 20)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 11.1")
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval1_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 11.2")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        chart_obj.verify_y_axis_label_in_run_window(expected_yval2_list, parent_css="#"+RUN_PARENT_CSS, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 11.3")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.4')
        chart_obj.verify_y_axis_title_in_run_window(y_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.5')
        chart_obj.verify_y_axis_title_in_run_window(y2_axis_title, parent_css="#"+RUN_PARENT_CSS, x_or_y_axis_title_css="text[class='y2axis-title']", msg='Step 11.6')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 11.7: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 20, 'Step 11.8: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.9')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 11.10: Verify Bar chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 11.11", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.12: Filter Button Removed')
        utillobj.switch_to_default_content(pause=3)
         
        """
        Step 12:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()