'''
Created on Nov 6, 2017

@author: BM13368
Testcase_Name : Add percent to data label 
Testcase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2336636&group_by=cases:section_id&group_id=171547&group_order=asc
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity

class C2336636_TestClass(BaseTestCase):

    def test_C2336636(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2336636.fex'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01 : Use API call to run 2336636.fex (replace domain/port/alias):
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10660&BIP_item=C2336636.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID, "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Verification : Expected to see as below
        """
        parent_css="#jschart_HOLD_0 .chartPanel text[class^='pieLabel!g']"
        resultobj.wait_for_property(parent_css, 1)
        expected_label_list=['SALES']
        resultobj.verify_riser_pie_labels_and_legends("jschart_HOLD_0", expected_label_list,"Step 01:01: Verify pie chart labels") 
        resultobj.verify_number_of_pie_segments("jschart_HOLD_0", 1, 6, 'Step 01:02: Verify the total number of pie chart segment')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mwedge!", "bilbao", "Step 01:03: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "portage", "Step 01:04: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mwedge!", "mint_green", "Step 01:05: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mwedge!", "violet", "Step 01:06: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mwedge!", "canary", "Step 01:07: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g0!mwedge!", "light_sky_blue", "Step 01:08: Verify first bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'TOYOTA'], 'Step 01.09 : Verify chart legends')
        expected_datalabel=['$30,200.00(14.49%)', '$7,800.00(3.74%)', '$80,390.00(38.57%)', '$43,000.00(20.63%)', '$12,000.00(5.76%)', '$35,030.00(16.81%)']
        resultobj.verify_data_labels("jschart_HOLD_0", expected_datalabel, "Step 01:10: Verify the data lables in the pie chart", custom_css="svg > g.chartPanel text[class*='mdataLabels']")
        time.sleep(2)
        
        """
            Verify tooltip information
        """
        expected_tooltip_list=['TOYOTA:35,030 (16.81%)']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s5!g0!mwedge!", expected_tooltip_list, "Step 01:11 Hover over pie chart and verify tooltip info")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step02', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        """
            Step 02 : Close output window.
        """
        """
            Step 03 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
    if __name__ == "__main__":
        unittest.main()

        
        


