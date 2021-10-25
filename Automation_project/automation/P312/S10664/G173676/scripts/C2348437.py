'''
Created on Jan 03, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.pages import visualization_metadata, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2348437_TestClass(BaseTestCase):


    def test_C2348437(self):
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        Test_Case_ID = 'C2348437'
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    2. Right click on "Gross Profit" in data pane > Create Bins...    """
        metaobj.datatree_field_click("Gross Profit",1,1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    3. Click OK in Create bin dialog     """
        metaobj.create_bin("GROSS_PROFIT_US_BIN_1", ok_btn=True)
        
        """    4. Right click "GROS_PROFIT_US_BIN_1" bin > Edit Bins...    """
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'GROSS_PROFIT_US_BIN_1', 190)
        metaobj.datatree_field_click("Dimensions->GROSS_PROFIT_US_BIN_1", 1, 1, "Edit Bins...")
        
        """    5. Click Format button    """
        """    6. Change format to integer    """
        """    7. Click OK    """
        """    8. Change bin width to 10.55    """
        """    9. Click OK in bin dialog    """
        metaobj.create_bin("GROSS_PROFIT_US_BIN_1", bin_format_btn=True, field_type='Integer',ok_btn=True, bin_width='10.55')
        
        """    10. Right click GROSS_PROFIT_US_BIN_1 > Edit Bin    """
        utillobj.synchronize_with_visble_text("[id^='QbMetaDataTree']", 'GROSS_PROFIT_US_BIN_1', 190)
        metaobj.datatree_field_click("Dimensions->GROSS_PROFIT_US_BIN_1", 1, 1, "Edit Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        metaobj.verify_bin(verify_bin_width='10.55', verify_bin_format_edit='I5', msg='Step 10')
        
        """    11. Click Cancel in edit bins dialog    """
        core_utillobj.left_click(utillobj.validate_and_get_webdriver_object("#qbBinsCancelBtn", 'CancelBtn'))
        
        """    12. Click Save in the toolbar > Save as "C2348437" > Click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
               
        """    13. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()