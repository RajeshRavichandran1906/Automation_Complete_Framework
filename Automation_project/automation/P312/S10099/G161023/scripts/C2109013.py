'''
Created on May'31, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109013
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity


class C2109013_TestClass(BaseTestCase):

    def test_C2109013(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109013'
        """
            Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(20)
            
        """
        Step 02: Change to Grid
        """
        ribbonobj.change_chart_type("grid")
        time.sleep(10)
              
        """
        Step 03: Double click Sale,Year (YYMDy), Product,Category, Quantity Sold
        """
        metaobj.datatree_field_click("Sale,Year", 1, 2,'Add To Query', 'Rows')
        time.sleep(10)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click("Quantity,Sold", 2, 1)
        time.sleep(15)
            
        """
        Step 04: Verify first and last 3 row values.
        """
        resultobj.verify_grid_column_heading("MAINTABLE_wbody1", ['Sale Year', 'Product Category', 'Quantity Sold'], "Step 04: Verify column titles")
        time.sleep(4)
        row1=["2011","Accessories","20,152"]
        resultobj.verify_grid_row_val("MAINTABLE_wbody1", row1, "Step 04: Verify report row value")
            
        """
        Step 05: Verify query pane dialog
        """
        metaobj.verify_query_pane_field("Rows", "Sale,Year", 1, "Step 05a: Verify Query Pane")
        metaobj.verify_query_pane_field("Rows", "Product,Category", 2, "Step 05b: Verify Query pane")
        metaobj.verify_query_pane_field("Measure", "Quantity,Sold", 1, "Step 05c: Verify Query pane")        
    
        """
        Step 06: Add 'Store,Business,Region', 'Product,Category', 'Product,Subcategory' to filter with defaults (All, equal, show prompt).
        """
        metaobj.datatree_field_click("Store,Business,Region", 1, 1,"Filter")
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(5)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(5)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        metaobj.datatree_field_click("Product,Subcategory", 1, 1,"Filter")
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(5)
        metaobj.create_visualization_filters('alpha')
        time.sleep(15)
            
        """
        Step 07: Verify 3 queries added to filter pane.
        """
        metaobj.verify_filter_pane_field("Store,Business,Region", 1, "Step 07: Verify Store,Business,Region added to filter pane")
        metaobj.verify_filter_pane_field("Product,Category", 2, "Step 07: Verify Product,Category added to filter pane")
        metaobj.verify_filter_pane_field("Product,Subcategory", 3, "Step 07: Verify Product,Subcategory added to filter pane")
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=True, msg='Step 07a: verify the ALL is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(2,'[All]', True, verify_type=True, msg='Step 07b: verify the ALL is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(3,'[All]', True, verify_type=True, msg='Step 07c: verify the ALL is checked under Show prompt')
        time.sleep(5)
                   
        """
        Step 08: Click run in toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        chart_type_css="rect[class*='riser!s0!g0!mcellFill!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=True, msg='Step 08a: verify the ALL is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(2,'[All]', True, verify_type=True, msg='Step 08b: verify the ALL is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(3,'[All]', True, verify_type=True, msg='Step 08c: verify the ALL is checked under Show prompt')
            
        """
        Step 09: Verify value for 2011/Accessories = 20,152
        """
        expected_tooltip=['Sale Year:2011', 'Product Category:Accessories', 'Quantity Sold:20,152']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step 09: verify the default tooltip values")
            
        """
        Step 10: Check EMEA in Store,Business,Region filter prompts
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1,'EMEA', False, verify_type=True, msg='Step 10a: Check EMEA in Store,Business,Region filter prompts')
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=False, msg='Step 10b: verify the ALL is unchecked in Store,Business,Region filter prompts')
            #propertyobj.change_filter_prompt_checkBoxValue("1","1","runtime")
            
        """
        Step 11: Verify value for 2011/Accessories = 13,435.
        """
        time.sleep(8)
        c=['Sale Year:2011', 'Product Category:Accessories', 'Quantity Sold:13,435']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mcellFill!r0!c0!",c, "Step 11a: Verify value for 2011/Accessories = 13,435")
        
        """
        Step 12: Check Accessories in Product,Category filter prompt
        """
        propertyobj.select_or_verify_show_prompt_item(2,'Accessories', False, verify_type=False, msg='Step 10a: Check Accessories in Product,Category filter prompt')
        time.sleep(8)
        propertyobj.select_or_verify_show_prompt_item(2,'[All]', True, verify_type=False, msg='Step 10b: verify the ALL is unchecked in Product,Category filter prompt')
            
        """
        Step 13: Verify value for 2011/Accessories = 13,435.
        """
        time.sleep(7)
        d=['Sale Year:2011', 'Product Category:Accessories', 'Quantity Sold:13,435']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mcellFill!r0!c0!",d, "Step 13a: Verify value for 2011/Accessories = 13,435")
            
        """
        Step 14: Verify output.
        """
        time.sleep(4)
        row1=["2011","Accessories","13,435"]
        resultobj.verify_grid_row_val("MAINTABLE_wbody1", row1, "Step 14: Verify report row value")
            
        """
        Step 15: Close the output window
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
            
        """
        Step 16: Click "Save" in the toolbar > Type C2109013 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()