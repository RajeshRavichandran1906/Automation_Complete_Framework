'''
Created on Nov 21, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334642
TestCase Name = AHTML: Bucketized Dual Axis charts do not display both Measure labels.(ACT-1197)

'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous

class C2334642_TestClass(BaseTestCase):

    def test_C2334642(self):
    
        """
            Class Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        Step 01:Execute the attached repro - act-1197.fex.This will create an initial Bar Chart.
        Expect to see the following Dual-axis Vertical Bar Chart with separate axis for each Measure field.
        """
        utillobj.active_run_fex_api_login("act-1197.fex", "S7074", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 svg g [class='xaxisOrdinal-title']", "CAR", 65)
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","SALES, DEALER_COST by COUNTRY, CAR", "Step 01.01: Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 01.02: Verify XY labels")
        expected_yval2_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 01.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue", "Step 01.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s4!g0!ay2!mbar!", "brick_red", "Step 01.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 01.07: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "SALES", "Step 01.08: Verify yaxis title")
        
        legend=['SALES:ENGLAND', 'DEALER_COST:ENGLAND', 'SALES:FRANCE', 'DEALER_COST:FRANCE', 'SALES:ITALY', 'DEALER_COST:ITALY', 'SALES:JAPAN', 'DEALER_COST:JAPAN', 'SALES:W GERMANY', 'DEALER_COST:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 01.09: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 01.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        Step 02:Hover over the left bar for Alfa Romeo.
            Expect to see the following Tooltip information for Sales value of 30200. This corresponds to the left-side axis.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'SALES:30200', 'COUNTRY:ITALY', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s4!g0!ay2!mbar!", expected_tooltip_list, "Step 02.01: Verify bar value")
        time.sleep(3)
        
        """
        Step 03:Hover over the right bar for Alfa Romeo.
            Expect to see the following Tooltip information for Dealer_Cost value of 16,235. This corresponds to the right-side axis.
        """
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'COUNTRY:ITALY', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g0!ay2!mbar!", expected_tooltip_list, "Step 03.01: Verify bar value")
        
if __name__ == '__main__':
    unittest.main() 