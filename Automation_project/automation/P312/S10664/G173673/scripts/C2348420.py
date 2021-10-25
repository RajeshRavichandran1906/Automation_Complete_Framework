'''
Created on Jan 10, 2018
@author: Nasir
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2348420_TestClass(BaseTestCase):

    def test_C2348420(self):
        Edit_Test_Case_ID='C2348420_Base'
        oVisualization=Visualization(self.driver)
        
        """    1. Restore the saved "C2348420_Base.fex" from (edit the domain, port and alias of the URL - do not use the URL as is):
                  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_binning_1%2FC2348420_Base.fex    """
        oVisualization.edit_visualization_using_api(Edit_Test_Case_ID)
        parent_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    2. Repeat Create Bin for same "Gross profit" field    """
        oVisualization.right_click_on_datetree_item("Gross Profit", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Verify the field name in edit bin window    """
        """    4. Click Cancel    """
        expected_bin_title="Create Bins - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US"
        oVisualization.verify_bins_dialog(bin_dialog_title=expected_bin_title,name_textbox_value='GROSS_PROFIT_US_BIN_3', btn_click='cancel', msg="Step 03a")

            
        """    5. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()