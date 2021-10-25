'''
Created on Jan 02, 2018

@author: Nasir
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata
from common.lib.basetestcase import BaseTestCase

class C2348431_TestClass(BaseTestCase):

    def test_C2348431(self):
        
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    2. Right click on "Revenue" in data pane > Create Bins...    """
        metaobj.datatree_field_click("Revenue",1,1, "Create Bins...")
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 190)
        
        """    3. Verify default bin width value    """
        metaobj.verify_bin(verify_bin_width='10', msg='Step 03.01')
        
        """    4. Click Cancel    """
        oCancel_btn=driver.find_element_by_css_selector("#qbBinsCancelBtn")
        utillobj.click_type_using_pyautogui(oCancel_btn, leftClick=True)
               
        """    5. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()