'''
Created on Oct 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197664
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea
from common.lib import utillity
import unittest
import time


class C2197664_TestClass(BaseTestCase):

    def test_C2197664(self):
        
                
        """Execute the attached repro - 143495.fex."""
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('143495.fex','S7074','mrid','mrpass')      
        time.sleep(4)   
        active_misobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by SEATS', 'Step 01: Execute the 143495.fex.')

        """
        Step 02: Verify scatter is plotted and exact values.
        """
        expected_xval_list = ['0', '1', '2', '3', '4', '5', '6']
        expected_yval_list = ['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K', '45K', '50K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_0', expected_xval_list, expected_yval_list, 'Step 02: Verify scatter is plotted and exact values')
        active_misobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SALES by SEATS', 'Step 2.1: Verify Chart Title')
        active_misobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options', 'Column','Pie','Line', 'Scatter', 'Advanced Chart', 'Original Chart'],"Step 2.2: Verify Chart toolbar")
        active_misobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 2.3: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        active_misobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Detail'],"Step 2.4: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_xaxis_title('MAINTABLE_0', "SEATS","Step 02.4 : Verify Xaxis title" , custom_css="text[class='xaxisNumeric-title']")
        resultobj.verify_yaxis_title('MAINTABLE_0', "SALES", "Step 02.5 : Verify yaxis title")

if __name__ == "__main__":
    unittest.main()
    