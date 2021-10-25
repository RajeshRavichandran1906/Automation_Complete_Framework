'''
Created on August 8, 2018

@author: vishnu_priya.
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart

class C8262014_TestClass(BaseTestCase):
    
    def test_C8262014(self):
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        chart_obj = chart.Chart(self.driver)
        project_id=core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id = core_utill_obj.parseinitfile('group_id')
        folder_name = project_id+'_'+suite_id+'/'+group_id
        
        
        '''Step 01 : Execute the attached Fex - C8262014_base.fex using the below API Url
        http://domain.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%252FG435182%252F&BIP_item=C5852469_base.fex '''
        
        chart_obj.run_fex_using_api_url(folder_name, 'C8262014_base', "mrid", "mrpass")
        time.sleep(6)
        
        """
        Step 2: Verify below in the chart window,
        Chart title displayed in top with background color, border with corner radius
        Background color is red
        Border color blue
        Curved corner radius
        
        """
        resultobj.verify_xaxis_title("jschart_HOLD_0", 'COUNTRY', "Step 02:01: Verify -xAxis Title")
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 02:02: Verify the total number of risers displayed on Chart')
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K',]
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 02:03: X and Y axis labels')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue", "Step 02:04: Verify first bar color")
        title_riser=driver.find_element_by_css_selector("g rect[shape-rendering='auto']")
        utillobj.verify_chart_color("jschart_HOLD_0",None,'red',"Step 02:05: Verify title bar colour",attribute_type="fill",custom_css="g rect[shape-rendering='auto']")
        utillobj.verify_chart_color("jschart_HOLD_0",None,'blue',"Step 02:06: Verify title border colour",attribute_type="stroke",custom_css="g rect[shape-rendering='auto']")
        rad_x=title_riser.get_attribute("rx")
        acx_rad='10'
        utillobj.asequal(acx_rad,rad_x,"Step 02:07: Verify radius of the curve in x axis")
        rad_y=title_riser.get_attribute("ry")
        acy_rad='25%'
        acy_rad1=str(acy_rad)
        utillobj.asequal(acy_rad1,rad_y,"Step 02:08: Verify radius of the curve in y axis")
        
        """
            Step 03 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
    if __name__ == "__main__":
        unittest.main()