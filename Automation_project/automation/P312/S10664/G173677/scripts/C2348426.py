'''
Created on Jan 04, 2018

@author: Nasir
'''
import unittest
from common.lib import utillity
from common.pages import ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2348426_TestClass(BaseTestCase):

    def test_C2348426(self):
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult= ia_resultarea.IA_Resultarea(self.driver)
        Edit_Test_Case_ID = 'C2348422'
        
        """    1. Restore the saved fex (edit the domain, port and alias of the URL - do not use the URL as is): - http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348422.fex    """
        utillobj.infoassist_api_edit(Edit_Test_Case_ID,'idis','S10664_binning_1', mrid='mrid', mrpass='mrpass')
        element_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        """    2. Click View Source icon     """
        """    3. Verify bin is showing as define     """
        """    4. Close focexec window    """
        expected_syntax_list=["DEFINE FILE new_retail/wf_retail_lite", "REVENUE_US_BIN_1/D20.2M=FLOOR ( WF_RETAIL_LITE.WF_RETAIL_SALES.REVENUE_US/100 ) * 100 ;", "END"]
        iaresult.verify_fexcode_syntax(expected_syntax_list,'Step 04a: Verify bin is showing as define')
        
        """    5. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()