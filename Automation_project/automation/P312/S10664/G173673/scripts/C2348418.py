'''
Created on Jan 10, 2018
@author: Nasir
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.pages.core_metadata import CoreMetaData

class C2348418_TestClass(BaseTestCase):

    def test_C2348418(self):
        Test_Case_ID = 'C2348418'
        oVisualization=Visualization(self.driver)
        metadataobj = CoreMetaData(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        oVisualization.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """    2. Right click Product>Model>Attributes> Price,Dollars > Create Bin    """
        oVisualization.right_click_on_datetree_item("Price,Dollars", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    3. Set bin width '100'    """
        """    4. Click OK    """
        oVisualization.create_bins('PRICE_DOLLARS_BIN_1', bin_width='100')
        
        """    5. Verify the bin is added to under dimensions    """
        metadataobj.collapse_data_field_section('Attributes->Model->Product')
        time.sleep(5)
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'PRICE_DOLLARS_BIN_1', 6, "Step 05a")
        
        """    6. Right click 'Gross profit' (under measures) > Create Bin    """
        oVisualization.right_click_on_datetree_item("Gross Profit", 1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        oVisualization.wait_for_number_of_element(parent_css, 1)
        
        """    7. Set bin width '100'    """
        """    8. Click OK    """
        oVisualization.create_bins('GROSS_PROFIT_US_BIN_1', bin_width='100')
        
        """    9. Verify the bin is added to under dimensions    """
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'GROSS_PROFIT_US_BIN_1', 6, "Step 09a")
        oVisualization.verify_field_listed_under_datatree('Dimensions', 'PRICE_DOLLARS_BIN_1', 7, "Step 09b")
        
        """    10. Double click on created two bins    """
        
        oVisualization.double_click_on_datetree_item('Dimensions->GROSS_PROFIT_US_BIN_1', 1)
        oVisualization.double_click_on_datetree_item('Dimensions->PRICE_DOLLARS_BIN_1', 1)
        
        """    11. Verify fields added to horizontal axis as following    """
        oVisualization.verify_field_listed_under_querytree('Horizontal Axis', 'GROSS_PROFIT_US_BIN_1', 1, "Step 11a: Verify GROSS_PROFIT_US_BIN_1 is visible underneath Horizontal Axis")
        oVisualization.verify_field_listed_under_querytree('Horizontal Axis', 'PRICE_DOLLARS_BIN_1', 2, "Step 12a: Verify PRICE_DOLLARS_BIN_1 is visible underneath Horizontal Axis")
        
        """    12. Click Save in the toolbar > Save as "C2348418" > Click Save    """
        oVisualization.save_as_visualization_from_menubar(Test_Case_ID)
        
        """    13. Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()