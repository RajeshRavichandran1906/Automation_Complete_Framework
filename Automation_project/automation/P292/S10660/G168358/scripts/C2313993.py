'''
Created on Dec 04, 2018

@author: vpriya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=168358&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313993
TestCase Name = Bucketized Mekko chart Basic chart Filtering/Exclusions..
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart, active_chart,visualization
from common.lib import global_variables

class C2313993_TestClass(BaseTestCase):

    def test_C2313993(self):
        
        "-------------------------------------------------------------------CLASS OBJECTS--------------------------------------------------------------------------"
        driver = self.driver #Driver reference object created
        chart_obj = chart.Chart(driver)
        visual_obj=visualization.Visualization(driver)
        utillobj = utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        glob_var=global_variables.Global_variables()
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        MEDIUM_WAIT= 60
        FEX_NAME='MekkoBasic'
        FOLDER_NAME='P292_S10660/G168358'
        chart_title='DEALER_COST, RETAIL_COST by CAR'
        x_axis_title=['CAR']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        ACTIVE_TOOLBAR_LIST1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        RUN_PARENT_CSS="MAINTABLE_0_f"
        TOOLBAR_PARENT_CSS="MAINTABLE_wmenu0"
        CHART_SEGMENT_CSS="riser!s0!g2!mbar!"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        step1="""        
        Step 01: Sign in to WebFOCUS
        http://machine:port/{alias}
        Step 02: Expand folder P292_S10660_G168358
        Execute the following URL:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10660_G168358%252FBIP_item=StremBasic.fex
        """
        chart_obj.edit_fex_using_api_url(FOLDER_NAME, 'chart', FEX_NAME, mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(20)
        parent_css="#pfjTableChart_1 g.chartPanel"
        chart_obj.wait_for_number_of_element(parent_css, 1, 240)
        
        """
        expect to see the following Active Mekko chart, sorted in Descending Measure order..
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T', 'D']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 02.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 02.02: ')
        chart_obj.verify_chart_color(RUN_PARENT_CSS, CHART_SEGMENT_CSS, 'bar_blue1', 'Step 02.03: Verify Color')
        chart_obj.verify_number_of_chart_segment(RUN_PARENT_CSS, 20, 'Step 02.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 02.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 02.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 02.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('01.00', step1)
        
        step3="""
        Step 03: Hover over the lower area(blue) for Alfa Romeo.
        Expect to see the following Tooltip information
        Step 04: Select the Exclude from Chart option.
        Expect to see the following Active Mekko, with Alfa Romeo excluded.
        """
        chart_obj.switch_to_frame()
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235  (45.35%)', 'Filter Chart', 'Exclude from Chart']
        chart_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_tooltip_list, msg="Step 03.01: Verify tooltip", parent_css="#MAINTABLE_0_f")
        chart_obj.select_tooltip_in_run_window("riser!s0!g0!mbar!", 'Exclude from Chart', parent_css='#MAINTABLE_0_f')
    
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 9, MEDIUM_WAIT)
        if glob_var.browser_name=="firefox":
            expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'JENSEN', 'AUDI', 'PEU...', 'TR...', 'T...', 'D...']
        else:
            expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T...', 'D']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 04.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g1!mbar!', 'bar_blue1', 'Step 04.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 18, 'Step 04.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 04.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 04.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 04.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.08: Filter Button Visible')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('03.00', step3)
        
        step5="""
        Step 05: Hover over the upper area(light green) for BMW.
        Select the Exclude from Chart option.
        Expect to see the following Active mekko chart, with Alfa Romeo and BMW excluded.
        """
        chart_obj.switch_to_frame()
        chart_obj.select_tooltip_in_run_window("riser!s1!g1!mbar!", 'Exclude from Chart', parent_css='#MAINTABLE_0_f')
        time.sleep(10)
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 8, MEDIUM_WAIT)
        if glob_var.browser_name=="firefox":
            expected_xval_list=['MASERATI', 'JAGUAR', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOY...', 'DA...']
        else:
            expected_xval_list=['MASERATI', 'JAGUAR', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUM...', 'TO...', 'DA...']
        
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 05.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g1!mbar!', 'bar_blue1', 'Step 05.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 16, 'Step 05.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 05.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 05.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 05.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 05.08: Filter Button Visible')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('04.00', step5)
        
        step6="""
        Step 06: Hover over the lower area(blue) for Audi and click the Remove Filter option.
        Expect to see the Filter removed and all CARs restored.
        """
        chart_obj.switch_to_frame()
        chart_obj.select_tooltip_in_run_window("riser!s0!g0!mbar!", 'Remove Filter', parent_css='#MAINTABLE_0_f')
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T', 'D']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 06.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 06.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 20, 'Step 06.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 06.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 06.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 06.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 06.08: Filter Button Removed')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('06.00', step6)
        
        step7="""
        Step 07:Left click and draw a box that touches BMW and Maserati..
        Expect to see the following box around BMW and Maserati..
        """
        chart_obj.switch_to_frame()
        source_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g2!mbar!']")
        target_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g6!mbar!']")
        visual_obj.create_lasso(source_elem, target_elem, source_element_location='middle', target_element_location='bottom_right')
        utillobj.capture_screenshot('07.00', step7)
        
        step8="""
        Step 08: Select the Exclude from Chart option.
        Expect to see both BMW and Maserati removed.
        """
        chart_obj.select_lasso_filter(select_item='Exclude from Chart')
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        time.sleep(5)
        expected_xval_list=['JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PEUGEOT', 'TRIUMPH', 'TOY...', 'DAT...']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 08.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 08.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 16, 'Step 08.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 08.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 08.06: Verify chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 08.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 08.08: Filter Button Visible')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('08.00', step8)
        
        step9="""
        Step 09: Hover over the lower area(blue) for JAGUAR and select the Remove Filter option..
        Expect to see the Filter removed and all CARs restored..
        """
        chart_obj.switch_to_frame()
        chart_obj.select_tooltip_in_run_window("riser!s0!g0!mbar!", 'Remove Filter', parent_css='#MAINTABLE_0_f')
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T', 'D']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 09.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 09.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 20, 'Step 09.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 09.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 09.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 09.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 09.08: Filter Button Removed')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('09.00', step9)
        
        step10="""
        Step 10: Left click and draw a box that touches Triumph, Toyota & Datsun.
        Select the Filter Chart option.
        Expect to see only data for Triumph, Toyota & Datsun.
        """
        chart_obj.switch_to_frame()
        source_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g9!mbar!")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g3!mbar!']")
        visual_obj.create_lasso(source_element, target_element, source_xoffset=0, target_xoffset=10, source_element_location='middle_left')
        visual_obj.select_lasso_tooltip('Filter Chart')
        
#         source_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g9!mbar!']")
#         target_elem=driver.find_element_by_css_selector("#MAINTABLE_0_f [class='riser!s0!g3!mbar!']")
#         visual_obj.create_lasso(source_elem, target_elem)
#         chart_obj.select_lasso_filter(select_item='Filter Chart')
        
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 3, MEDIUM_WAIT)
        expected_xval_list=['TRIUMPH', 'TOYOTA', 'DATSUN']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 10.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 10.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 6, 'Step 10.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 10.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 10.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 10.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 10.08: Filter Button Visible')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('10.00', step10)
        
        step11="""
        Step 11: Hover over the lower area(blue) for Peugeot and select the Remove Filter option.
        Expect to see all CARs restored.
        """
        chart_obj.switch_to_frame()
        chart_obj.select_tooltip_in_run_window("riser!s0!g2!mbar!", 'Remove Filter', parent_css='#MAINTABLE_0_f')
        parent_css="#MAINTABLE_0_f svg > g text[class^='xaxis'][class*='labels']"
        chart_obj.wait_for_number_of_element(parent_css, 10, MEDIUM_WAIT)
        expected_xval_list=['BMW', 'MASERATI', 'JAGUAR', 'ALFA ROMEO', 'JENSEN', 'AUDI', 'PE...', 'TR...', 'T', 'D']
        chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css="#"+RUN_PARENT_CSS, msg="Step 11.01: ")
        chart_obj.verify_x_axis_title_in_run_window(x_axis_title, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.02: ')
        chart_obj.verify_chart_color('MAINTABLE_0_f', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 11.03: Verify Color')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_0_f', 20, 'Step 11.04: Verify Number of riser', custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_PARENT_CSS, msg='Step 11.05: ')
        active_chart_obj.verify_chart_title(chart_title, msg="Step 11.06: Verify Line chart title", parent_css="#"+RUN_PARENT_CSS)
        active_chart_obj.verify_active_chart_toolbar(ACTIVE_TOOLBAR_LIST1, msg="Step 11.07: ", parent_css="#"+TOOLBAR_PARENT_CSS)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.08: Filter Button Removed')
        chart_obj.switch_to_default_content()
        utillobj.capture_screenshot('11.00', step11)
        
        """
        Step 12: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()       