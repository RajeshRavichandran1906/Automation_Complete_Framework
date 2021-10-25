'''
Created on Jun 29, 2019

@author: Aftab
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2276122
TestCase Name : HTML5:No tooltip after series from Line chart changed to BAR
'''

import unittest
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase

class C2276122_TestClass(BaseTestCase):

    def test_C2276122(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
    
        """
        1 : Run C2276122_Base.fex .
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159435&BIP_item=C2276145_Base.fex
        """
        chart_obj.run_fex_using_api_url('P251_S9164/G159425','C2276122_Base', mrid='mrid', mrpass='mrpass')
 
        """
        2 : Hover over Bar chart.
        3 : Verify it display the tooltip.
        """
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 9, msg="step 2.01")
        chart_obj.verify_x_axis_label_in_run_window(['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY'] ,'#jschart_HOLD_0',msg='Step 2.02')
        chart_obj.verify_y_axis_label_in_run_window(["0", "20K", "40K", "60K", "80K", "100K"],'#jschart_HOLD_0', msg="step 2.03") 
        chart_obj.verify_x_axis_title_in_run_window(["COUNTRY"],'#jschart_HOLD_0', msg="step 2.04")
        chart_obj.verify_y_axis_title_in_run_window(["SALES"], '#jschart_HOLD_0',msg="step 2.05")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", "cerulean_blue",'#jschart_HOLD_0', msg="step 2.06")
        
        chart_obj.verify_active_chart_tooltip('jschart_HOLD_0', 'riser!s0!g0!mbar!', ['SALES, ENGLAND: 12,000'], "Step:3.01 Verify tooltips")
        
        """
        4 : Logout using API
            http://domain:port/alias/service/wf_security_logout.jsp   
        """
        chart_obj.api_logout()

if __name__ == '__main__':
    unittest.main()