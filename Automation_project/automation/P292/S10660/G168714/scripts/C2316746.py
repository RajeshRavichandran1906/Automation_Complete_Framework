'''
Created on Nov 2, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2316746
TestCase Name = Runtime filter options on bins
'''

import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.wftools.visualization import Visualization

class C2316746_TestClass(BaseTestCase):

    def test_C2316746(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1='C2316746_base'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visual = Visualization(self.driver)
        
        """
            Step 01 : Use API call to run visualization created in previous test case
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2316743.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID_1+'.fex','S10660_visual_2','mrid','mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1", "PRICE_DOLLARS_BIN_1", 180)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRICE_DOLLARS_BIN_1', "Step 01.01 : Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Quantity Sold', "Step 01:02 : Verify Y-Axis Title")
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 01.03 : Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 18, 'Step 01.04 : Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 01.05 : Verify first bar color")
    
        """
            Step 02 : Lasso on first five riser
        """
        source_element = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar']")
        target_element = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g4!mbar")
        visual.create_lasso(source_element, target_element)
        
        """
            Step 03 : Verify no filter options displayed and only points count
        """
        visual.verify_lasso_tooltip(['5 points'], msg='Step 03.01 : Verify no filter options displayed and only 5 points count')
        
        """
            Step 04 : Close run window
        """
        
if __name__ == '__main__':
    unittest.main()