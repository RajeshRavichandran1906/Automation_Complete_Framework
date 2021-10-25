'''
Created on May 08, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197662
'''

import unittest,time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.pages import visualization_ribbon,visualization_metadata,visualization_resultarea, active_chart_rollup

class C2197662_TestClass(BaseTestCase):

    def test_C2197662(self):
        
        """
            Class Objects
        """
        act_obj = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        chart_rollup_obj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """ Step 1: Invoke IA chart using CAR master file and select Active report as output format
        """
        utillobj.infoassist_api_login('chart','ibisamp/car','P116/S7074', 'mrid', 'mrpass')
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        result_obj._validate_page(elem1)
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(5)
        
        """ Step 2: Add CAR and Sales field.
                    Verify that the query pane is added with CAR on X-axis and Sales in measure and expect to see the following BAR chart in live preview
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='CAR', with_regular_exprestion=True)
        metadataobj.datatree_field_click('SALES', 2, 1)
        parent_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN',  'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 02.01: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 10, 'Step 02.02: Verify riser')
        
        """ Step 3: Run the report
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(1)
        parent_css="#resultArea [id^=ReportIframe-]"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        act_obj.switch_to_frame(parent_css)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN',  'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.01: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 03.02: Verify riser')
        
        
        """ Step 4: Using the Advanced Chart Tool, select Scatter(XY Plot)
                    Expect to see the following Scatter Plot.
        """
        chart_rollup_obj.click_chart_menu_bar_items('MAINTABLE_0', 1)
        parent_css="#wall1 [class='arWindowBarTitle']"
        result_obj.wait_for_property(parent_css, 1, string_value='Chart/RollupTool', with_regular_exprestion=True)
        chart_rollup_obj.select_advance_chart('wall1', 'scatter(xy_plot)')
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN',  'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04.01: ')
        result_obj.verify_number_of_circle('MAINTABLE_wbody0', 10, 11, 'Step 04.02: Verify riser')
        time.sleep(2)        

if __name__ == "__main__":
    unittest.main() 