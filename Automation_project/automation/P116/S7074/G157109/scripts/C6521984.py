'''
Created on Jan 10, 2019

@author: Magesh
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/6521984
TestCase_Name : AHTML: Running bucket chart without setting ARGRAPHENGINE hangs (ACT-1572)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart

class C6521984_TestClass(BaseTestCase):

    def test_C6521984(self):
        
        """
        TESTCASE VARIABLES
        """
        active_chart = Active_Chart(self.driver)
        chart_obj = chart.Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        run_parent_css="MAINTABLE_wbody0"
        fex_name="C6521984"
        folder_name='P116_S7074/G157109'
        
        """
        Step 01: Login to WebFOCUS environment using the below link:
        http://machine:port/{alias}
        Step 02: Run C6521984.fex using the below API link:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S7074/G157109&BIP_item=C6521984.fex
        """
        active_chart.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass', run_chart_css="#MAINTABLE_wbody0_f rect[class*='riser!']", no_of_element=5, wait_time=MEDIUM_WAIT_TIME)
        
        """ 
        Step 02.1: Verify the chart is displayed properly
        """ 
        active_chart.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 02.1')
        active_chart.verify_y_axis_title_in_run_window(['SEATS'], msg='Step 02.2')
        active_chart.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg='Step 02.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '5', '10', '15', '20', '25', '30', '35', '40'], msg='Step 02.4')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 5, msg='Step 02.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'red', parent_css='#'+run_parent_css, msg='Step 02.6')
        active_chart.verify_chart_title('SEATS by COUNTRY', msg='Step 02.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 02.8', parent_css='#MAINTABLE_wmenu0')
        chart_obj.verify_number_of_chart_segment(run_parent_css, 2, msg='Step 02.9: Expect to see the x-axis majorGrid Line.', custom_css="path[class*='xaxis'][class*='majorGrid']")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 2, msg='Step 02.10: Expect to see the Y-axis majorGrid Line.', custom_css="path[class*='yaxis'][class*='majorGrid']")
        
        """
        Step 03 : Launch below IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()