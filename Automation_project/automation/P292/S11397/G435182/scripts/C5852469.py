'''
Created on Jul 12, 2018

@author: vishnu priya.
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity
from common.wftools import chart

class C5852469_TestClass(BaseTestCase):
    
    def test_C5852469(self):
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        chart_obj = chart.Chart(self.driver)
        
        '''Step 01 : Execute the attached Fex - C5852469_base.fex using the below API Url
        http://domain.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%252FG435182%252F&BIP_item=C5852469_base.fex '''
        chart_obj.run_fex_using_api_url("P292_S11397/G435182", 'C5852469_base', "mrid", "mrpass")
        time.sleep(6)
        
        """
        Verification : Expected to see as below
        
        """
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 01:01: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 01:02: Verify the total number of risers displayed on Chart')
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K',]
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 01:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 01:04: Verify first bar color")
        title_riser=driver.find_element_by_css_selector("g rect[shape-rendering='auto']")
        utillobj.verify_chart_color("jschart_HOLD_0",None,'red',"Step 01:05:verify title bar colour",attribute_type="fill",custom_css="g rect[shape-rendering='auto']")
        utillobj.verify_chart_color("jschart_HOLD_0",None,'blue',"Step 01:06:verify title border colour",attribute_type="stroke",custom_css="g rect[shape-rendering='auto']")
        rad_x=title_riser.get_attribute("rx")
        acx_rad='10'
        utillobj.asequal(acx_rad,rad_x,"step 01:07 verify radius of the curve in x axis")
        rad_y=title_riser.get_attribute("ry")
        acy_rad='25%'
        acy_rad1=str(acy_rad)
        utillobj.asequal(acy_rad1,rad_y,"step 01:07 verify radius of the curve in y axis")
        
        """
            Step 03 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
    if __name__ == "__main__":
        unittest.main()