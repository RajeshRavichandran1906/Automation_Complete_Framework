'''
Created on Jan 8, 2019

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6670344
Test Case Title =  Date Period sorting with color (ACT-1442) 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.lib import utillity

class C6670344_TestClass(BaseTestCase):

    def test_C6670344(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 40
        folder_name="P116_S18157/G513460"
        fex_name="ACT-1442"
        
        """
        STEP 01 : Log in to WebFOCUS: http://machine:port/{alias}
        STEP 02 : Execute fex using API below
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S18157/G513460&BIP_item=ACT-1442.fex
        """
        active_chart.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', wait_time=MEDIUM_WAIT_TIME)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 70, MEDIUM_WAIT_TIME)
        
        """
        STEP 03 : Verify the StreamGraph ColorBy Chart is generated
        """
        active_chart.verify_x_axis_title_in_run_window(['d_period_display'], msg='Step 03.1')
        active_chart.verify_x_axis_label_in_run_window(['Nov, 1981', 'Dec, 1981', 'Jan, 1982', 'Feb, 1982', 'Mar, 1982', 'Apr, 1982', 'May, 1982', 'Jun, 1982', 'Jul, 1982', 'Aug, 1982'], msg='Step 03.2')
        active_chart.verify_y_axis_title_in_run_window(['CNT EMP_ID'], msg='Step 03.3')
        active_chart.verify_y_axis_label_in_run_window(['0', '3', '6', '9', '12', '15'], msg='Step 03.4')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 70, msg='Step 03.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 03.6')
        active_chart.verify_legends_in_run_window(['DED_CODE', 'CITY', 'FED', 'FICA', 'HLTH', 'LIFE', 'SAVE', 'STAT'], msg='Step 03.7')
        active_chart.verify_chart_title('CNT EMP_ID by DED_CODE, d_period_display', msg='Step 03.8', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Count'], msg='Step 03.9', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 04 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()