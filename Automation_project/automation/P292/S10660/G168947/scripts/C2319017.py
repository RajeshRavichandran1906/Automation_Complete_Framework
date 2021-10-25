'''
Created on Oct 13, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319017
TestCase Name = Data pane Measure field context menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase

class C2319017_TestClass(BaseTestCase):

    def test_C2319017(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2319017'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_meta = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Expand "Sales" in the Data pane > right-click "Cost of Goods" > verify menu
        """
        
        time.sleep(4)
        metaobj.datatree_field_click('Cost of Goods',1, 1)
        time.sleep(4)
        utillobj.select_or_verify_bipop_menu('Add To Query', verify='true', expected_popup_list=['Sum', 'Create Bins...', 'Add To Query', 'Filter'], msg='Step 02:')
        
        """
        Step 03: Select "Add to Query > Rows"
        """
        new_meta.collapse_data_field_section("Measures")
        time.sleep(4)
        metaobj.datatree_field_click('Cost of Goods',1, 1, 'Add To Query', 'Rows')
        time.sleep(4)
         
        """
        Step 04: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 369)
        time.sleep(5)
        expected_label= ['16', '23', '32', '34', '36', '42', '45']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 04:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "lochmara", "Step 04(i) Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 369, 'Step 04(ii): Verify number of risers displayed')
         
        """
        Step 05: Right-click "Gross Profit" in the Data pane > select "Add to Query > Color"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Gross Profit',1, 1, 'Add To Query', 'Color')
        time.sleep(4)
         
        """
        Step 06: Verify Preview
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 369)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 369)
        time.sleep(5)
        expected_label= ['16', '23', '32', '34', '36', '42', '45']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 06:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "cinnabar", "Step 06.b(i) Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 369, 'Step 06.c: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '1.7M', '3.4M', '5.2M', '6.9M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06:d(ii) Verify Y-Axis Title")
        
         
        """
        Step 07: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
         
        """
        Step 08: Verify Preview
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2583)
        time.sleep(5)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        expected_label= ['16', '23', '32', '34', '36', '42', '45']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 08:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.b: X and Y axis Scales Values has changed or NOT')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0!", "lochmara", "Step 08.c(i) Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 2583, 'Step 08: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '0.9M', '1.8M', '2.6M', '3.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(ii) Verify Y-Axis Title")
         
        """
        Step 09: Click Save in the toolbar
        Step 10: Save as "C2319017" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 12: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2319017.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 13: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2583)
        time.sleep(5)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 13:d(i) Verify X-Axis Title")
        expected_label= ['16', '23', '32', '34', '36', '42', '45']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 13:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13.b: X and Y axis Scales Values has changed or NOT')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0!", "lochmara", "Step 13.c(i) Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 2583, 'Step 13: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '0.9M', '1.8M', '2.6M', '3.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 13:d(ii) Verify Y-Axis Title")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2319017_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)       
        time.sleep(5)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()
