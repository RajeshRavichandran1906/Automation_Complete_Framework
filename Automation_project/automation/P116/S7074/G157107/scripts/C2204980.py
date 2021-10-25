'''
Created on Jul 18, 2017
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_chart_rollup
from common.lib import utillity


class C2204980_TestClass(BaseTestCase):

    def test_C2204980(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204980'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
        Step 01: Execute 90416.fex from repro
        """
        utillobj.active_run_fex_api_login("90416.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","CAR", "Step 01a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST", "Step 01b: Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO','AUDI', 'BMW', 'DATSUN', 'JAGUAR','JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 01d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g3!mbar!", 'cerulean_blue', 'Step 01e: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g4!mbar!", ['DEALER_COST, JAGUAR: 18,621'],"Step 01f: Verify Chart tooltip")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by CAR', 'Step 01g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 01h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
        Step 02: Change the calculation from sum to max.
        """
        rollobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Max', 7)
        time.sleep(10)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0","CAR", "Step 02a: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0","DEALER_COST", "Step 02b: Verify Y-Axis Title")
        expected_xval_list=['ALFA ROMEO','AUDI', 'BMW', 'DATSUN', 'JAGUAR','JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02c: ')
        result_obj.verify_number_of_riser('MAINTABLE_wbody0', 1, 10, 'Step 02d: Verify number of risers')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g7!mbar!", 'cerulean_blue', 'Step 02e: Verify bar Color')
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0',"riser!s0!g2!mbar!", ['DEALER_COST, BMW: 49,500'],"Step 02f: Verify Chart tooltip")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST by CAR', 'Step 02g: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Column','Pie','Line','Scatter','Advanced Chart','Original Chart'],"Step 02h: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02i: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Max'],"Step 02j: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
    
    
    