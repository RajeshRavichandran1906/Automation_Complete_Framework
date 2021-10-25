'''
Created on Sep 27, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107423&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case Description : IA-4652:Vis: Grid: Adding many fields and filter doesn't render scroll bar and output freezes
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.pages import metadata, visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity

class C2107423_TestClass(BaseTestCase):  
    def test_C2107423(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107423'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propobj=visualization_properties.Visualization_Properties(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        print("Issue in Firefox browser: Adding many fields to Grid browser becomes unresponsive: Known Product Failure - IA-5727")
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
 
        """
        Step 02: Change to Grid.
        """
        ribbonobj.change_chart_type("grid")
        
        """
        Step 03: Double Click Revenue, assert new in run_data, "New in Grid not matched"Sale Year, Sale Quarter, Sale Month, Customer Business Region, Customer Business
        Sub region, Customer Country, Product Category.
        """
        time.sleep(5)
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        metaobj.datatree_field_click("Revenue",2,1)
        time.sleep(5)
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year",2,1)
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Quarter",2,1)
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Month",2,1)
        time.sleep(5)
        metadataobj.collapse_data_field_section('Transaction Date, Simple->Sales_Related')
        time.sleep(5)
        metaobj.datatree_field_click("Customer,Business,Region",2,1)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 4)
        metaobj.datatree_field_click("Customer,Business,Sub Region",2,1)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 5)
        metaobj.datatree_field_click("Customer,Country",2,1)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 6)
        metaobj.datatree_field_click("Product,Category",2,1)
        time.sleep(10)
        """
        Step 04: Verify field titles added to canvas
        """
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            time.sleep(50)
        WebDriverWait(self.driver, 300).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 7)
        parent_css1=".rowTitle text"
        resultobj.wait_for_property(parent_css1, 7)
        time.sleep(10)
        parent_css1=".colHeader text"
        resultobj.wait_for_property(parent_css1, 1)
        list_ele =['Sale Year', 'Sale Quarter', 'Sale Month', 'Customer Business Region', 'Customer Business Sub Region', 'Customer Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',list_ele, 'Step 04.1: Verify field titles')
        row_val=['2011', '1', '1', 'EMEA', 'Europe', 'Czech Republic', 'Accessories', '$168.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 04.2: verify grid 1st row value')
 
        """
        Step 05: Add Customer Business Region to Filter Equal to EMEA, click Ok.
        """
        time.sleep(10)
        metaobj.drag_drop_data_tree_items_to_filter('Customer,Business,Region', 0)
#         metaobj.datatree_field_click('Customer,Business,Region',1,1,'Filter')
        time.sleep(5)
        l=['[All]','EMEA']
        metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['GridItems',l])
        time.sleep(8)
        """
        Step 06: Verify query added to filter pane
        """
        metaobj.verify_filter_pane_field("Customer,Business,Region", 1, 'Step 06: Verify query added to filter pane')
        """
        Step 07: Verify value in filter prompt is EMEA
        """
        time.sleep(40)
        propobj.select_or_verify_show_prompt_item(1, 'EMEA', True,verify_type=True,msg="Step 07: Verify value in filter prompt is EMEA")        
        """
        Step 08: Verify first 2 row values and last two row values.
        """
        time.sleep(8)
        list_val=['Sale Year', 'Sale Quarter', 'Sale Month', 'Customer Business Region', 'Customer Business Sub Region', 'Customer Country', 'Product Category', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',list_val, 'Step 08.1: Verify field titles')
        time.sleep(20)
        row1=['2011', '1', '1', 'EMEA', 'Europe', 'Czech Republic', 'Accessories', '$168.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row1,'Step 08.2: verify grid 1st row value')
 
        """
        Step 09: Click "Save" in the toolbar > Type C2107423 > Click "Save" in the Save As dialog
        """
        time.sleep(4)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
            
if __name__ == '__main__':
    unittest.main()       