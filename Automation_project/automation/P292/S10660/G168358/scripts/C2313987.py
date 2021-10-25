'''
Created on Dec 04, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=168358&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313987
TestCase Name = Bucketized StreamGraph Basic chart Filtering/Exclusions.
'''

import time
import unittest

from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart, active_chart
from common.wftools.visualization import Visualization


class C2313987_TestClass(BaseTestCase):

    def test_C2313987(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        visual = Visualization(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 60
        FEX_NAME='StreamBasic'
        FOLDER_NAME='P292_S10660/G168358'
        chart_title='DEALER_COST, RETAIL_COST BY CAR'
        x_axis_title=['CAR']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        RUN_PARENT_CSS="MAINTABLE_wbody0"
        TOOLBAR_PARENT_CSS="MAINTABLE_wmenu0"
        CHART_SEGMENT_CSS="riser!s0!g0!marea"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """        
        Step 01: Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 02: Expand folder P292_S10660_G168358
        Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10660_G168358%252FBIP_item=StremBasic.fex
        """
        chart_obj.edit_fex_using_api_url(FOLDER_NAME, 'chart', FEX_NAME, mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        chart_obj.wait_for_number_of_element(parent_css, 1, MEDIUM_WAIT)
        
        """
        Expect to see the following Active Streamgraph.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 02:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 02:2: ')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 02.3: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 2, 'Step 02.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 02.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 02.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 02:7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        
        """
        Step 03: Hover over the lower area(blue) for Alfa Romeo.
        Expect to see the following Tooltip information
        Step 04: Select the Exclude from Chart option.
        Expect to see the following Active Streamgraph, with Alfa Romeo excluded.
        """
        chart_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        core_utils.python_move_to_element(chart_ele, element_location='middle_left')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        chart_obj.select_or_verify_marker_tooltip_in_run_window('marker!s0!g0!mmarker!', select_tooltip="Exclude from Chart", verify_tooltip_list=expected_tooltip_list, msg='Step 03.01 : Verify marker tooltip values and select exclude from chart', parent_css='#MAINTABLE_wbody0')

        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 9, MEDIUM_WAIT)
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 04:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 04:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 04.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 04.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 04:7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.8: Filter Button Visible')
    
        """
        Step 05: Hover over the upper area(light green) for BMW.
        Select the Exclude from Chart option.
        Expect to see the following Active Streamgraph, with Alfa Romeo and BMW excluded.
        """
        chart_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        core_utils.python_move_to_element(chart_ele, element_location='middle_left')
        chart_obj.select_or_verify_marker_tooltip_in_run_window('marker!s1!g1!mmarker!', select_tooltip="Exclude from Chart", msg='Step 5 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        time.sleep(10)
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 8, MEDIUM_WAIT)
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 05:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 05:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 05.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05:7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 05.8: Filter Button Visible')
        
        """
        Step 06: Hover over the lower area(blue) for Audi and click the Remove Filter option.
        Expect to see the Filter removed and all CARs restored.
        """
        chart_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        core_utils.python_move_to_element(chart_ele, element_location='middle_left')
        chart_obj.select_or_verify_marker_tooltip_in_run_window('marker!s0!g0!mmarker!', select_tooltip="Remove Filter", msg='Step 6 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 06:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 06:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 06.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 06.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06:7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 06.8: Filter Button Removed')
    
        """
        Step 07: Left click and draw a box that touches Alfa Romeo and Audi.
        Expect to see the following box around Alfa Romeo and Audi.
        """
        source_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g0!mmarker!']")
        target_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g1!mmarker!']")
        visual.create_marker_lasso(source_elem, target_elem, source_xoffset=-40, source_yoffset=40, target_xoffset=10, target_yoffset=-50)
        
        """
        Step 08: Select the Exclude from Chart option.
        Expect to see both Alfa Romeo and Audi removed.
        """
        visual.select_lasso_tooltip('Exclude from Chart')
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        
        chart_obj.wait_for_number_of_element(parent_css, 8, MEDIUM_WAIT)
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 08:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 08:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 08.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 08.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 08.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08:7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 08.8: Filter Button Visible')
        
        """
        Step 09: Hover over the lower area(blue) for BMW and select the Remove Filter option.
        Expect to see the Filter removed and all CARs restored.
        """
        chart_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        core_utils.python_move_to_element(chart_ele, element_location='middle_left')
        chart_obj.select_or_verify_marker_tooltip_in_run_window('marker!s0!g0!mmarker!', select_tooltip="Remove Filter", msg='Step 9 : Verify marker tooltip', parent_css='#MAINTABLE_wbody0')
        
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 09:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 09:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 09.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 09.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09.7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 09.8: Filter Button Removed')
        
        """
        Step 10: Left click and draw a box that touches Peugeot, Toyota and Triumph.
        Select the Filter Chart option.
        Expect to see only data for Peugeot, Toyota & Triumph.
        """
        source_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g7!mmarker!']")
        target_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g9!mmarker!']")  
        visual.create_marker_lasso(source_elem, target_elem, source_xoffset=-5, source_yoffset=50, target_xoffset=30, target_yoffset=-50)
        visual.select_lasso_tooltip('Filter Chart')
        time.sleep(10)
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 3, MEDIUM_WAIT)
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 10:1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 10:2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 10.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 10.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 10.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 10.7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.8: Filter Button Visible')
        
        """
        Step 11: Hover over the lower area(blue) for Peugeot and select the Remove Filter option.
        Expect to see all CARs restored.
        """
        chart_ele=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        core_utils.python_move_to_element(chart_ele, element_location='middle_left')
        chart_obj.select_or_verify_marker_tooltip_in_run_window('marker!s0!g0!mmarker!', select_tooltip="Remove Filter", msg='Step 11: Verify marker tooltip')
        parent_css="#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 11.1: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.2: ')
        chart_obj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 11.3: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 11.4: Verify Number of riser', custom_css="path[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.5: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 11.6: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 11.7: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.8: Filter Button Removed')
        
        """
        Step 12: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
      
if __name__ == '__main__':
    unittest.main()       