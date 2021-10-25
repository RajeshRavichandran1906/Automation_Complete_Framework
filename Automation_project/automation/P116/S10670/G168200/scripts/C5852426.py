'''Created on 14-June-2018

@author: Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10670
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5852426
TestCase Name = AHTML: StreamGraph basic procedure creation.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_resultarea, ia_resultarea, active_miscelaneous

class C5852426_TestClass(BaseTestCase):

    def test_C5852426(self):
        """
        TESTCASE VARIABLES
        """
        fex_name = 'StreamBasic.fex'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        step1="""
            Step 01 : Sign in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Restore the saved StremBaisc.fex using below API
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP116_S10670%252FG168200%252F&BIP_item=StreamBasic.fex
        """
        utillobj.active_run_fex_api_login(fex_name, "S10670", 'mrid','mrpass')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0 text[class^='xaxis'][class$='title']", 'CAR', result_obj.home_page_long_timesleep)
        utillobj.capture_screenshot('01.00', step1)
        
        step3="""
            Step 03 : Verify the StreamGraph Basic Chart is generated
        """
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 1.1: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval_list=[]
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 01.02: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 01.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 01.04: Verify Color')
        
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR', 'Step 01.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 01.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 01.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 01.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.capture_screenshot('03.00', step3, expected_image_verify=True)
        
        step4="""
            Step 04 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.capture_screenshot('04.00', step4)
        

if __name__ == "__main__":
    unittest.main()