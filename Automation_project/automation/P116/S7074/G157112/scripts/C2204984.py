'''
Created on Jul 7, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204984
TestCase Name = AHTML/CHART:Sort Ascending/Descending not respected-134135
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2204984_TestClass(BaseTestCase):

    def test_C2204984(self):
        """
        TESTCASE VARIABLES
        """
        driver = self.driver
         
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Launch Info assist to develop a chart using the CAR file.
        Select Active Report as the output format.
        """
        utillobj.infoassist_api_login('Chart','ibisamp/car','P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        utillobj.synchronize_with_number_of_element(parent_css, 11, 65)
        
        ribbonobj.change_output_format_type('active_report')
        
        
        """
        Add Country, Seats.
        """
        time.sleep(4)
        metadataobj.datatree_field_click("COUNTRY",2,1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 25)
        
        metadataobj.datatree_field_click("SEATS", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 20)
        
        xaxis_value="COUNTRY"
        yaxis_value="SEATS"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 01:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        expected_yval_list=['0', '5', '10', '15', '20', '25', '30', '35', '40']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 1: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 5, 'Step 2: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 01: Verify bar color")
        
        """
        Step 02: In Query window, and select 'Z to A' (Descending) sort icon in FIELD tab.
        """
        time.sleep(2)
        metadataobj.querytree_field_click("SEATS",1,1,"Sort","Sort","Descending")
        time.sleep(4)
        
        """
        Step 03: Verify that bars in chart are arranged in Descending SEATS order, by hovering over the Bars.
        """
        parent_css="#TableChart_1 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 45)
        
        xaxis_value="COUNTRY"
        yaxis_value="SEATS"
        result_obj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['W GERMANY','ENGLAND','ITALY','JAPAN','FRANCE']
        expected_yval_list=['0', '5', '10', '15', '20', '25', '30', '35', '40']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3: Verify XY labels')
        result_obj.verify_number_of_riser('TableChart_1', 1, 5, 'Step 03: Verify number of risers')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03: Verify bar color")
        
        """
        Step 04: Run the chart and verify the charts are arranged in Descending SEATS order.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        
        parent_css="#MAINTABLE_wbody0 rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 5, 45)
        
        xaxis_value="COUNTRY"
        yaxis_value="SEATS"
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 04:a(i) Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['W GERMANY','ENGLAND','ITALY','JAPAN','FRANCE']
        expected_yval_list=['0', '5', '10', '15', '20', '25', '30', '35', '40']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 04: Verify XY labels')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 5, 'Step 04: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 04: Verify bar color")
        time.sleep(5)
        expected_tooltip_list=['COUNTRY:W GERMANY', 'SEATS:34', 'Filter Chart', 'Exclude from Chart']
        result_obj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', expected_tooltip_list, 'Step 04: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SEATS by COUNTRY', 'Step 04: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2204984_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()