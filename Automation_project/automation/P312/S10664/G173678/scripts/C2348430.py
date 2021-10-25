'''
Created on Jan 04, 2018

@author: Nasir
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_metadata
from common.lib.basetestcase import BaseTestCase

class C2348430_TestClass(BaseTestCase):


    def test_C2348430(self):
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        Edit_Test_Case_ID = 'C2348430_Base'
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        """    1. Restore the C2348430_Base.fex using API(edit the domain, port and alias of the URL - do not use the URL as is):
                  http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_binning_1%2FC2348430_Base.fex   """
        utillobj.infoassist_api_edit(Edit_Test_Case_ID,'idis','S10664_binning_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1,expire_time=100)
        
        """    2. Click on "REVENUE_US_BIN_1" bin in query pane     """
        metaobj.querytree_field_click('REVENUE_US_BIN_1', 1)
        time.sleep(3)
        
        """    3. Verify format section in the Field ribbon     """
        utillobj.verify_object_visible("#FieldFormatType[disabled]", True, "Step 03a: Verify Format Type Combobox Disabled")
        utillobj.verify_object_visible("#FieldFormatCurrency[disabled]", True, "Step 03b: Verify Change Currency Options Disabled")
        utillobj.verify_object_visible("#FieldFormatPercent[disabled]", True, "Step 03c: Verify Percent icon Disabled")
        utillobj.verify_object_visible("#FieldFormatComma[disabled]", True, "Step 03d: Verify Comma icon Disabled")
        utillobj.verify_object_visible("#FieldFormatDecimalLenUp[disabled]", True, "Step 03e: Verify Increase Decimal Places Icon Disabled")
        utillobj.verify_object_visible("#FieldFormatDecimalLenDown[disabled]", True, "Step 03f: Verify Decrease Decimal Places Icon Disabled")
        ele=driver.find_element_by_css_selector("#FieldFormatCluster")
        utillobj.take_screenshot(ele,'C2348430_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    4. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()