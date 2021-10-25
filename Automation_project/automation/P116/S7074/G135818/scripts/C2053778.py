'''
Created on Jan 08, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053778
TestCase Name = Verify move to bottom icon moves pagination to the bottom
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.active_report import Active_Report

class C2053778_TestClass(BaseTestCase):

    def test_C2053778(self):
        
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        active_report = Active_Report(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        MEDIUM_WAIT_TIME = 40
        folder_name="P116/S7074"
        fex_name="AR-RP-001"
        
        """
        Step 01: Execute the AR-RP-001.fex
        """
        active_chart.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', wait_time=MEDIUM_WAIT_TIME)
        active_report.wait_for_visible_text("#ITableData0 tr:nth-child(2) td:nth-child(2)", "C141")
        active_report.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """
        Step 01.a: Select State > Chart > Pie > Category
        """
        active_report.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(5)
        
        """
        Step 02: Click New icon (dropdown) > New
        """
        active_chart.create_new_item('wall1', 'New')
        time.sleep(5)
        active_chart.move_active_popup_window(2, "900", "100")
        
        """
        Verify another chart window is opened.
        Verify title as 'State By Category' is displayed.
        The look and feel of new chart is the same as first chart window. 
        """
        active_chart.verify_x_axis_label_in_run_window(['State'], parent_css='#wall1', xyz_axis_label_css="text[class^='pieLabel!g0!mpieLabel!']",  msg='Step 03.1')
        active_chart.verify_number_of_risers_in_run_window("path[class*='mwedge']", 1, 3, parent_css='#wall1', msg='Step 03.2: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#wall1', msg='Step 03.3')
        active_chart.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css='#wall1', msg='Step 03.4')
        active_chart.verify_chart_title('State by Category', msg='Step 03.5', parent_css='#wall1')
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Count'], msg='Step 03.6', parent_css='#wall1')
        
        active_chart.verify_x_axis_label_in_run_window(['State'], parent_css='#wall2', xyz_axis_label_css="text[class^='pieLabel!g0!mpieLabel!']",  msg='Step 03.7')
        active_chart.verify_number_of_risers_in_run_window("path[class*='mwedge']", 1, 3, parent_css='#wall2', msg='Step 03.8: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mwedge!']", 'cerulean_blue', parent_css='#wall2', msg='Step 03.9')
        active_chart.verify_legends_in_run_window(['Coffee', 'Food', 'Gifts'], parent_css='#wall2', msg='Step 03.10')
        active_chart.verify_chart_title('State by Category', msg='Step 03.11', parent_css='#wall2')
        active_chart.verify_active_chart_toolbar(['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Count'], msg='Step 03.12', parent_css='#wall2')
        
if __name__ == '__main__':
    unittest.main()