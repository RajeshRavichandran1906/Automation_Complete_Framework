'''
Created on September 11, 2018

@author: Varun

lnxtestrail.ibi.com/testrail/index.php?/cases/view/6725921
TestCase Name = Data pane Measure field context menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C6725921_TestClass(BaseTestCase):

    def test_C6725921(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C6725921'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_meta = metadata.MetaData(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:

        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2F
        """
        visual.invoke_visualization_using_api("baseapp/wf_retail_lite")
        
        """
        Step 02: Expand "Sales" in the Data pane > right-click "Cost of Goods" > verify menu
        """
        metaobj.datatree_field_click('Cost of Goods',1, 1)
#         visual.wait_for_visible_text('#queryBoxColumn', 'Cost of Goods')
        utillobj.select_or_verify_bipop_menu('Add To Query', verify='true', expected_popup_list=['Sum', 'Create Bins...', 'Add To Query', 'Filter'], msg='Step 02.00:')
        
        """
        Step 03: Select "Add to Query > Rows"
        """
        new_meta.collapse_data_field_section("Measure Groups")
        time.sleep(4)
        metaobj.datatree_field_click('Cost of Goods',1, 1, 'Add To Query', 'Rows')
        time.sleep(4)
         
        """
        Step 04: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 369)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 369)
        time.sleep(5)
        expected_label= ['$16.00', '$23.00', '$32.00', '$34.00', '$36.00']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 04.00:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "lochmara", "Step 04.01: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 369, 'Step 04.02: Verify number of risers displayed')
        time.sleep(2)
        expected_tooltip=['Cost of Goods:$16.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r0!c0!",expected_tooltip, "Step 04.03: verify the default tooltip values")       
        time.sleep(5)
         
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
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 369)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 369)
        time.sleep(5)
        expected_label= ['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 06.00:")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0!", "Vermilion", "Step 06.01 Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 369, 'Step 06.02: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '1.6M', '3.3M', '4.9M', '6.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 06.03: Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Cost of Goods:$16.00', 'Gross Profit:$306,512.43', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r0!c0!",expected_tooltip, "Step 06.04: verify the default tooltip values")       
        time.sleep(5)
         
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
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 369)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2583)
        time.sleep(5)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.00: Verify X-Axis Title")
        expected_label= ['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 08.01")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.02: X and Y axis Scales Values has changed or NOT')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0!", "lochmara", "Step 08.03 Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 2583, 'Step 08.04: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '0.8M', '1.7M', '2.5M', '3.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 08.05: Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Cost of Goods:$16.00', 'Product Category:Accessories', 'Gross Profit:$306,512.43', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r0!c0!",expected_tooltip, "Step 08.06: verify the default tooltip values")       
        time.sleep(5)
         
        """
        Step 09: Click Save in the toolbar
        Step 10: Save as "2319017" > Click Save
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
        Step 12: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 13: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar!r0!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 369)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2583)
        time.sleep(5)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 13.00: Verify X-Axis Title")
        expected_label= ['$16.00', '$23.00', '$32.00', '$34.00', '$36.00', '$42.00']
        resultobj.verify_visualization_row_column_header_labels('MAINTABLE_wbody1','Rows','Cost of Goods',expected_label, "Step 13.01:")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13.02: X and Y axis Scales Values has changed or NOT')
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0!", "lochmara", "Step 13.03: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 2583, 'Step 13.04: Verify number of risers displayed')
        time.sleep(2)
        legend=['Gross Profit', '0M', '0.8M', '1.7M', '2.5M', '3.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 13.05: Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Cost of Goods:$16.00', 'Product Category:Accessories', 'Gross Profit:$306,512.43', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r0!c0!",expected_tooltip, "Step 13.06: verify the default tooltip values")
        time.sleep(2)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()