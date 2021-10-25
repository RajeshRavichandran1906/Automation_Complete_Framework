'''
Created on Jun 28, 2019

@author: Aftab
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2276145
TestCase Name : Portal: ToolTip info of TreeMap shown incomplete
'''

import unittest
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase

class C2276145_TestClass(BaseTestCase):

    def test_C2276145(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
    
        """
        1 : Run C2276145_Base.fex .
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159435&BIP_item=C2276145_Base.fex
        """
        chart_obj.run_fex_using_api_url('P251_S9164/G159435','C2276145_Base', mrid='mrid', mrpass='mrpass')

        """
        2 : Reduce the size of the window.
        """
        chart_obj.set_browser_window_size()

        """
        3 : Hover over on any filed and verify the toolip showing all fields with out any cut-off.
        """
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 41, msg="step 3.01")
        chart_obj.verify_active_chart_tooltip('jschart_HOLD_0', 'riser!sStereo Systems-_-DMP-692!g0!mnode', ['Stereo Systems > DMP-692', 'Cost of Goods: 2.6M', 'Discount: 233K'], "Step:3.01 Verify tooltips")
        """
        4 : Logout using API
            http://domain:port/alias/service/wf_security_logout.jsp   
        """
        chart_obj.api_logout()

if __name__ == '__main__':
    unittest.main()