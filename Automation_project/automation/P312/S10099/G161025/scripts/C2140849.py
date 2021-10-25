'''
Created on June29, 2016
@author: Kiruthika - Sindhuja

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140849
TestCase Name : IA-4610:Vis: Unable to Lasso and Filter options on a Grid in Preview if 6 fields with long values
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2140849_TestClass(BaseTestCase):

    def test_C2140849(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140849'
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/Customer_Data&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
#         utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8404', 'mrid04', 'mrpass04')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        time.sleep(10)
        
        """
        Step 02: Change to grid
        """        
        ribbonobj.change_chart_type('grid')
        
        """
        Step 03: Double Click on Revenue, Sale Year.
        """        
        time.sleep(5)
        metaobj.datatree_field_click('Sale,Year', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue',2,1)
        time.sleep(15)
        
        """
        Step 04: Verify grid title values
        """       
        time.sleep(15)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 1)
        lit =['Sale Year', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1',lit, 'Step 04.1: Verify field titles')
        
        """
        Step 05: Verify grid data values.
        """
        time.sleep(3)
        row_val=['2011', '$48,965,069.21']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val,'Step 05: verify grid 1st row value')
        
        """
        Step 06: Add Sale Quarter, Sale Month, Customer Business Region, Customer Business Sub Region, Customer Country to Rows.
        """        
        metaobj.datatree_field_click('Sale,Quarter', 2, 1)
        time.sleep(5)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 2)
        metaobj.datatree_field_click('Sale,Month', 2, 1)
        time.sleep(15)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 3)
        metaobj.datatree_field_click('Customer,Business,Region', 2, 1)
        time.sleep(10)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 4)
        metaobj.datatree_field_click('Customer,Business,Sub Region', 2, 1)
        time.sleep(12)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 5)
        metaobj.datatree_field_click('Customer,Country', 2, 1)
        
        time.sleep(20)
        
        """
        Step 07: verify query pane
        """
        time.sleep(10)
        metaobj.verify_query_pane_field('Rows', 'Sale,Year',1, "Step 07a: Verify query pane")
        metaobj.verify_query_pane_field('Rows', 'Sale,Quarter',2, "Step 07b: Verify query pane")
        metaobj.verify_query_pane_field('Rows', 'Sale,Month',3, "Step 07c: Verify query pane")
        metaobj.verify_query_pane_field('Rows', 'Customer,Business,Region',4, "Step 07d: Verify query pane")
        metaobj.verify_query_pane_field('Rows', 'Customer,Business,Sub Region',5, "Step 07e: Verify query pane")
        
        """
        Step 08: Verify first and last 3 row values.
        """        
        time.sleep(15)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 6)
        row_val2=['2011', '1', '1', 'EMEA', 'Europe', 'Czech Republic', '$168.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val2,'Step 08: verify grid 1st row value')

        """
        Step 09:  Add Customer Business Region to Filter and choose Equal to North America & South America
        """        
        time.sleep(5)
        metaobj.datatree_field_click('Customer,Business,Region',1,1,'Filter')
        time.sleep(8)        
        l = ["[All]","North America", "South America" ]
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        
        """
        Step 10: Verify query added to filter pane
        """        
        time.sleep(15)        
        metaobj.verify_filter_pane_field('Customer,Business,Region',1, "Step 10: Verify query added to filter")
        
        """
        Step 11: Verify values in filter prompt.
        """        
        time.sleep(15)
        propertyobj.select_or_verify_show_prompt_item(1, "North America", verify=True, verify_type= True, msg ="Step 11.b: Verify North America in filter prompt")
        
        """
        Step 12: Lasso on Revenue values($531,506.67, $251,976.25, $1,133.44 and $735.98) and select Filter Chart.
        """
        resultobj.create_lasso("MAINTABLE_wbody1", "rect","s0!g0!mcellFill!r0!c0", target_tag = "rect",target_riser="s0!g0!mcellFill!r3!c0")
        miscelanousobj.select_active_lasso_menu("Filter Chart")
        
        """
        Step 13: Verify filtered grid values 
        """        
        time.sleep(18)       
        row_val2=['2011', '1', '1', 'North America', 'Canada', 'Canada', '$531,506.67']
        time.sleep(10)
        WebDriverWait(self.driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, ".rowTitle text")) == 6)
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val2,'Step 13: verify grid 1st row value')
        
        """
        Step 14: Click Run in the toolbar
        """        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        
        """
        Step 15: Verify output
        """        
        time.sleep(25)
        elem1=(By.CSS_SELECTOR, "#MAINTABLE_wbody1 g.rowLabels > text")
        resultobj._validate_page(elem1)
        time.sleep(10)
        row_val2=['2011', '1', '1', 'North America', 'Canada', 'Canada', '$531,506.67']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1',row_val2,'Step 15: verify grid 1st row value')
                
        """
        Step 16: Close the output window.
        """    
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 17: Click "Save" in the toolbar > Type C2140687 > Click "Save" in the Save As dialog
        """        
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(8)        
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
#        