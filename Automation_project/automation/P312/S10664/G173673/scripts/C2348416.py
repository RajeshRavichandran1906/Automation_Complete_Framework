'''
Created on Jan 10, 2018

@author: Nasir
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2348416_TestClass(BaseTestCase):

    def test_C2348416(self):
        
        oVisualization=Visualization(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        oVisualization.invoke_visualization_using_api('baseapp/wf_retail_lite')
                
        """    2. Right click "Gross Profit" > Create Bins    """
        oVisualization.right_click_on_datetree_item("Gross Profit", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Review - Create bin window's title is "Create Bins - WF_RETAIL.WF_RETAIL_SALES.GROSS_PROFIT_US"    """
        """    4. Click Cancel    """
        expected_bin_title="Create Bins - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US"
        oVisualization.verify_bins_dialog(bin_dialog_title=expected_bin_title, btn_click='cancel', msg="Step 03a")
        
        """    5. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()