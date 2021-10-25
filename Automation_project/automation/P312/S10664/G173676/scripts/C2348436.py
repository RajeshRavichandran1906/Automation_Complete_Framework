'''
Created on Jan 02, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.pages import visualization_metadata
from common.lib.basetestcase import BaseTestCase

class C2348436_TestClass(BaseTestCase):

    def test_C2348436(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    2. Right click on "Revenue" in data pane > Create Bins...    """
        metaobj.datatree_field_click("Revenue",1,1, "Create Bins...")
        time.sleep(2)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    3.Highlight default bin value 10 and hit delete key    """
        """    4. Type dash(-) in bin width input    """
        text_box = utillobj.validate_and_get_webdriver_object("#qbBinWidthTextField", 'TextField')
        utillobj.set_text_to_textbox_using_keybord('-', text_box_elem=text_box)
        time.sleep(5)
        metaobj.verify_bin(verify_bin_width='', msg='Step 04.01')
        
        """    5. Click Cancel    """
        core_utillobj.left_click(utillobj.validate_and_get_webdriver_object("#qbBinsCancelBtn", 'CancelBtn'))
               
        """    6. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        time.sleep(2)
        
if __name__ == "__main__":
    unittest.main()