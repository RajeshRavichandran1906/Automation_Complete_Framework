'''
Created on MAY 11,2017 

@author: pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Testcase = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227205
TestCase Name = AHTML Chart displays single line X axis label;JSCHART works (ACT-207)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest,time
from common.pages import visualization_resultarea, active_miscelaneous


class C2227205_TestClass(BaseTestCase):

    def test_C2227205(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        """ 
        Step 1:In Text Editor, create a new report fex; copy the attached repro_simple.fex.
        Run the report.      
        """
        utillobj.active_run_fex_api_login("repro_simple.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        """ 
        Step 2: Verify the run report 
        """
        yaxis_value ="RETAIL_COST"
        result_obj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 2:a(i) Verify -yAxis Title")
        expected_xval_list=['01/2014', 'ENGLAND', '03/2014', 'FRANCE', '03/2014', 'ITALY', '02/2014', 'JAPAN', '03/2014', 'W GERMANY', '01/2014', '02/2014', '03/2014', 'Average', '01/2014', '02/2014', '03/2014', 'Best Class']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        result_obj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 2:b:Verify XY labels")
        result_obj.verify_number_of_riser("jschart_HOLD_0", 1, 11, 'Step 2:c: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "portage", "Step 2:d: Verify first bar color")
        result_obj.verify_data_labels('jschart_HOLD_0', ['45,319', '5,610', '51,065', '6,478', '64,732', '11,330', '3,239', '10,117', '17,850', '3,339', '31,500'], "step 2.e:Verify data labels", custom_css=".chartPanel .groupPanel .datalabels g text[class^='dataLabels']")
       
        utillobj.infoassist_api_logout()
        """ 
        Step 3:Execute the attached - repro_AHTML
        """
        utillobj.active_run_fex_api_login("repro_AHTML.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", ':', "Step 3:a(i) Verify -yAxis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'RETAIL_COST', "Step 3.a(ii) Verify -yAxis Title")
        expected_xval_list=['ENGLAND/01/2014', 'FRANCE/03/2014', 'ITALY/03/2014', 'JAPAN/02/2014', 'W GERMANY/03/2014', 'Average/01/2014', 'Average/02/2014', 'Average/03/2014', 'Best Class/01/2014', 'Best Class/02/2014', 'Best Class/03/2014']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        result_obj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval_list, "Step 3.b:Verify XY labels")
        result_obj.verify_number_of_riser("MAINTABLE_wbody0", 1, 11, 'Step 3.c: Verify the total number of risers displayed on preview')
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "cerulean_blue_1", "Step 3.d: Verify first bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 3.e: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 3.f: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 3.g: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['RETAIL_COST, W GERMANY/03/2014: 64,732']
        miscelaneous_obj.verify_active_chart_tooltip("MAINTABLE_wbody0", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 3.h: Verify bar value")
        result_obj.verify_data_labels('MAINTABLE_wbody0', ['45,319', '5,610', '51,065', '6,478', '64,732', '11,330', '3,239', '10,117', '17,850', '3,339', '31,500'], "step 3.i:Verify data labels", custom_css=".chartPanel .groupPanel .datalabels g text[class^='dataLabels']")
       
if __name__ == "__main__":
    unittest.main()  
