'''
Created on Jan 03, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.pages import visualization_metadata
from common.lib.basetestcase import BaseTestCase

class C2348439_TestClass(BaseTestCase):


    def test_C2348439(self):
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    2. Right click 'Cost of Goods' > Create Bins...    """
        metaobj.datatree_field_click("Cost of Goods",1,1, "Create Bins...")
        time.sleep(2)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    3. Enter '2000.5' for bin width    """
        """    4. Click Format button and changed to Packed    """
        """    5. Click 'OK'(2x)    """
        metaobj.create_bin("COGS_US_BIN_1", bin_format_btn=True, field_type='Packed',ok_btn=True, bin_width='2000.5')
        
        """    6. Right click bin field > Edit Bin    """
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'COGS_US_BIN_1', 190)
        metaobj.datatree_field_click("Dimensions->COGS_US_BIN_1", 1, 1, "Edit Bins...")
        
        """    7. Verify Value 2000.5 shows in bin width    """
        metaobj.verify_bin(verify_bin_width='2000.5', verify_bin_format_edit='P12.2', msg='Step 07.01')
        
        """    8. Click Cancel    """
        core_utillobj.left_click(utillobj.validate_and_get_webdriver_object("#qbBinsCancelBtn", 'CancelBtn'))
               
        """    9. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()