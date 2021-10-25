'''
Created on Nov 2, 2017

@author: BM13368
Testcase_Name : Verify binding values in sort field to Colors
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2334455&group_by=cases:section_id&group_id=171261&group_order=asc 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity

class C2334455_TestClass(BaseTestCase):


    def test_C2334455(self):
        """
            Testcase Variables
        """
        Test_Case_ID = 'C2334455a.fex'
        Test_Case_ID1 = 'C2334455b.fex'
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
            Step 01 : Sign to WebFocus using the below link.
            http://machine:port/ibi_apps
            Step 02 : Execute the attached Fex - C2334455a using the below API Url
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2334455a.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID, "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Verification : Expected to see as below
        """
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 02:01: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 9, 'Step 02:02: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '1', '2', '3', '4', '5', '6', '7', '8']
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 02:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "rosy_brown", "Step 02:04: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "yellow", "Step 02:05: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mbar!", "cyan", "Step 02:06: Verify first bar second color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['SEATS', '2', '4', '5'], 'Step 02.07 : Verify first bar third color')
        time.sleep(2)
        """
            Verification : Verify tooltip in the bar chart
        """
        expected_tooltip_list=['COUNTRY:ITALY', 'CNT MODEL:3', 'SEATS:2']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 02:08 Hover over bar and verify tooltip info")
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
            Step 05 : Execute the attached Fex - C2334455b using the below API Url
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S10660&BIP_item=C2334455b.FEX
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1, "S10660_chart_2", 'mrid', 'mrpass')
        time.sleep(6)
        """
            Verification : Expected to see as below
        """
        parent_css="#jschart_HOLD_0 text[class^='xaxis'][class$='title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_yaxis_title("jschart_HOLD_0", 'CNT Full Name', "Step 05:01: Verify -xAxis Title")
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'Customer Business Region', "Step 05:02: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 8, 'Step 05:03: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=[]
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05:04: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 05:05: Verify first bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g0!mbar!", "purple", "Step 05:06: Verify first bar color")
        resultobj.verify_riser_legends('jschart_HOLD_0',['Gender', 'F', 'M'], 'Step 05.07 : Verify first bar third color')
        time.sleep(2)
        """
            Verification : Verify tooltip in the bar chart
        """
        expected_tooltip_list=['Customer Business Region:EMEA', 'CNT Full Name:111608', 'Gender:M']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 05:08 Hover over bar and verify tooltip info")
        obj1=driver.find_element_by_css_selector("#jschart_HOLD_0")
        time.sleep(1)
        utillobj.take_screenshot(obj1,Test_Case_ID1 + '_Actual_step05', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(1)
        """
            Step 06 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()