'''
Created on Dec 28, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852500
Test Case Title =  AHTML: Restore Horizontal Dual-Axis Stacked Line Chart via API 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.lib import utillity

class C5852500_TestClass(BaseTestCase):

    def test_C5852500(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 40
        folder_name="P116_S10670/G168276"
        fex_name="Horizontal_Dual_Axis_Stacked_Line"
        
        """
        STEP 01 : Sign in to WebFOCUS: http://machine:port/{alias}
        STEP 02 : Restore the saved Horizontal Dual Axis Stacked Line.fex using below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP116_S10670%252FG168276%252F&BIP_item=Horizontal_Dual_Axis_Stacked_Line.fex
        """
        active_chart.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', wait_time=MEDIUM_WAIT_TIME)
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='riser!']", 4, MEDIUM_WAIT_TIME)
        
        """
        STEP 03 : Verify the Horizontal Dual Axis Stacked Line Chart is generated.
        """
        active_chart.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg='Step 03.1')
        active_chart.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K'], msg='Step 03.2')
        active_chart.verify_y_axis_label_in_run_window(['0', '400', '800', '1,200', '1,600'], xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg='Step 03.3')
        active_chart.verify_number_of_risers_in_run_window('path', 1, 4, msg='Step 03.4: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', attribute='stroke', msg='Step 03.5')
        active_chart.verify_x_axis_title_in_run_window(['CAR'], msg='Step 03.6')
        active_chart.verify_legends_in_run_window(['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT'], msg='Step 03.9')
        active_chart.verify_chart_title('DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', msg='Step 03.10', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 03.11', parent_css='#MAINTABLE_wmenu0')
        
        """
        Step 04 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()