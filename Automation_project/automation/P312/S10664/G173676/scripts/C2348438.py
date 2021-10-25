'''
Created on Jan 03, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.pages import metadata, visualization_metadata
from common.lib.basetestcase import BaseTestCase

class C2348438_TestClass(BaseTestCase):


    def test_C2348438(self):
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    2. Right click 'Cost of Goods' > Create Bins...    """
        metaobj.datatree_field_click("Cost of Goods",1,1, "Create Bins...")
        time.sleep(2)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        """    3. Enter '5000.5 ' for bin width    """
        """    4. Click 'OK'    """
        metaobj.create_bin("COGS_US_BIN_1", bin_width='5000.5')
        
        """    5. Verify bin created without any error and added under dimensions    """
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'COGS_US_BIN_1', 190)
        metaobj.verify_data_pane_field('Dimensions', 'COGS_US_BIN_1', 6, "Step 05a: Verify bin created without any error and added under dimensions")
        
        """    6. Right click on 'COG_US_BIN_1'    """
        """    7. Click "Edit bins"    """
        metaobj.datatree_field_click('Dimensions->COGS_US_BIN_1', 1, 1, "Edit Bins...")
        
        """    8. Verify bin width '5000.5' preserved    """
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        metaobj.verify_bin(verify_bin_width='5000.5', msg='Step 08')
        
        """    9. Click Cancel    """
        core_utillobj.left_click(utillobj.validate_and_get_webdriver_object("#qbBinsCancelBtn", 'CancelBtn'))
               
        """    10. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()