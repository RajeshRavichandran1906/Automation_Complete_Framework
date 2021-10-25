'''Created by June 29 2019

@author: Aftab

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2241291
Suite : Bar Chart Verify NOPRINT for Matrix - Rows is working properly (HTML5)
'''

import unittest
import time
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.lib.global_variables import Global_variables
from common.pages.visualization_resultarea import Visualization_Resultarea

class C2241291_TestClass(BaseTestCase):

    def test_C2241291(self):
        
        ''' Test case objects '''
        utils = UtillityMethods(self.driver)
        core_util = CoreUtillityMethods(self.driver)
        chart_obj = Chart(self.driver)
        g_var = Global_variables()
        viz_rslt = Visualization_Resultarea(self.driver)
        
        ''' Test case variables'''
        total_riser_css = "#pfjTableChart_1 .risers rect"
        riser_css = 'riser!s0!g3!mbar!r3!c0!'
        fexname = '{0}_Base'.format(g_var.current_test_case)
        
        """
        Step 1: Edit C2241291_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159425%2FC2241291_Base.fex
        """
        chart_obj.edit_fex_using_api_url(None, fex_name=fexname)
        utils.synchronize_with_number_of_element(total_riser_css, 10, chart_obj.home_page_long_timesleep)
        
        """
        Step 2: Verify the following chart is displayed.
        """
        chart_obj.verify_y_axis_title_in_preview(['SALES', 'SALES', 'SALES', 'SALES', 'SALES'], msg='Step 2')
        chart_obj.verify_y_axis_label_in_preview(['0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K'], msg='Step 2.1')
        chart_obj.verify_x_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg='Step 2.2')
        viz_rslt.verify_number_of_riser(total_riser_css.split(' ')[0][1:], 1, 10, 'Step 2.3: Verify chart riser.', custome_css=' '+total_riser_css[17:])
        chart_obj.verify_chart_color(total_riser_css.split(' ')[0][1:], riser_css, 'bar_blue', 'Step 2.1: Verify chart color.')
        
        """
        Step 3: Click "Run".
        """
        chart_obj.run_report_from_toptoolbar()
        core_util.switch_to_frame()
        utils.synchronize_with_number_of_element(total_riser_css.replace('pfjTableChart_1', 'jschart_HOLD_0'), 14, chart_obj.home_page_long_timesleep)
        
        """
        Step 4: Verify the following chart is displayed.
        """
        chart_obj.verify_y_axis_title_in_run_window(['SALES', 'SALES', 'SALES', 'SALES', 'SALES'], msg='Step 4')
        chart_obj.verify_y_axis_label_in_run_window(['0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K', '0', '20K', '40K', '60K', '80K', '100K'], msg='Step 4.1')
        chart_obj.verify_x_axis_label_in_run_window(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], msg='Step 4.2')
        viz_rslt.verify_number_of_riser(total_riser_css.replace('pfjTableChart_1', 'jschart_HOLD_0').split(' ')[0][1:], 1, 14, 'Step 4.3: Verify chart riser.', custome_css=' '+total_riser_css[17:])
        chart_obj.verify_chart_color(total_riser_css.replace('pfjTableChart_1', 'jschart_HOLD_0').split(' ')[0][1:], riser_css, 'bar_blue', 'Step 2.14.4: Verify chart color.')
        
        """
        Step 5: Hover over any riser.
        """
        """
        Step 6: Verify "COUNTRY" is not displayed.
        """
        chart_obj.verify_tooltip_in_run_window(riser_css, ['CAR:DATSUN', 'SALES:43000'], 'Step 6: Verify "COUNTRY" is not displayed in tooltip.')
        
        """
        Step 7: Logout using API
                http://domain:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(3)        
 
if __name__ == '__main__':
    unittest.main()