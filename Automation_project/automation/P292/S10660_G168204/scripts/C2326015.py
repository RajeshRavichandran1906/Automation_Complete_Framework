'''
Created on Nov 1, 2017

@author: BM13368
Testcase_Name : Support for Curved Corners on chart elements (Risers, Frame, ...)
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2326015
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity


class C2326015_TestClass(BaseTestCase):

    def test_C2326015(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2326015a.FEX'
        Test_Case_ID1 = 'C2326015b.FEX'
        
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01 : Sign to WebFocus using the below link.
            http://machine:port/ibi_apps
            Step 02 : Execute the attached Fex - C2326015a using the below API Url
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2326015a.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID, "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Verification : Expected to see as below
        """
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 01:01: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step 01:02: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 01:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 01:04: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g4!mbar!", "pale_green", "Step 01:05: Verify first bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['RETAIL_COST', 'DEALER_COST'], 'Step 01.06 : Verify chart legends')
        time.sleep(2)
        
        """
            Verify tooltip information
        """
        expected_tooltip_list=['COUNTRY:ENGLAND', 'RETAIL_COST:45,319']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 01:06 Hover over bar and verify tooltip info")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step02', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        """
            Step 03 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 04 : Sign to WebFocus using the below link.
            http://machine:port/ibi_apps
            Step 05 : Execute the attached Fex - C2326015b using the below API Url
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2326015b.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1, "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Verification : Expected to see as below
        """
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 05:01: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step 05:02: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar", "bar_blue", "Step 05:04: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g4!mbar!", "pale_green", "Step 05:05: Verify second bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['RETAIL_COST', 'DEALER_COST'], 'Step 05.06 : Verify chart legends')
        """
            Verify tooltip information 
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 05:07 Hover over bar and verify tooltip info")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID + '_Actual_step05', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        """
            Step 06 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
                              
    if __name__ == "__main__":
        unittest.main()
        
        
        
        
        
        
        
        
        
        

