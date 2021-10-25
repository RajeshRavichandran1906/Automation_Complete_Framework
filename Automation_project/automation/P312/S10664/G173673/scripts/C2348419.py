'''
Created on Jan 10, 2018
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.pages.core_metadata import CoreMetaData

class C2348419_TestClass(BaseTestCase):

    def test_C2348419(self):
        Edit_Test_Case_ID='C2348419_Base'
        Test_Case_ID = 'C2348419'
        oVisualization=Visualization(self.driver)
        metadataobj = CoreMetaData(self.driver)
        
        """    1. Reopen the saved "C2348419_Base.fex" from (edit the domain, port and alias of the URL - do not use the URL as is):
                  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_binning_1%2FC2348419_Base.fex    """
        oVisualization.edit_visualization_using_api(Edit_Test_Case_ID)
        parent_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    2. Repeat Create Bin for same "Gross profit" field    """
        oVisualization.right_click_on_datetree_item("Gross Profit", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Verify new bin window opens    """
        expected_bin_title="Create Bins - WF_RETAIL_LITE.WF_RETAIL_SALES.GROSS_PROFIT_US"
        oVisualization.verify_bins_dialog(bin_dialog_title=expected_bin_title, btn_click=None, msg="Step 03a")
        
        """    4. Set bin width '1000'> click OK    """
        oVisualization.create_bins('GROSS_PROFIT_US_BIN_2', bin_width='1000')
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        """    5. Verify the bin is added to under dimensions    """
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'GROSS_PROFIT_US_BIN_1', 6, "Step 05a")
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'GROSS_PROFIT_US_BIN_2', 7, "Step 05b")
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'PRICE_DOLLARS_BIN_1', 8, "Step 05c")
        
        """    6. Click Save in the toolbar > Save as "C2348419" > Click Save    """
        oVisualization.save_as_visualization_from_menubar(Test_Case_ID)
        
        """    7. Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()