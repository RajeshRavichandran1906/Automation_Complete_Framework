"""
Created on Jun 20, 2016
@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110387
TestCase Name : IA-4552:Vis: Exclude From Chart in Bubble map with Color is not working in Preview
"""

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2110387_TestClass(BaseTestCase):

    def test_C2110387(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110387'
        """
        Step 01: http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Change to bubble map.
        """
        time.sleep(6)
        ribbonobj.change_chart_type('bubble_map')
        
        """
        Step 03: Double click Customer Country and Revenue.
        """
        time.sleep(10)
        metaobj.datatree_field_click('Customer,Country', 2,1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(10)
        
        """
        Step 04: verify query pane
    
        """
        metaobj.verify_query_pane_field("Layer","Customer,Country",1,"Step 04: verify Customer,Country added to query pane")
        metaobj.verify_query_pane_field("Size","Revenue",1,"Step 04: verify Customer,Country added to query pane")
        
        """
        Step 05: Add Sale Year to Color.
        """
        metaobj.datatree_field_click("Sale,Year", 1, 1,'Add To Query','Color')
        time.sleep(5)
        
        """
        Step 06: Verify legend values
        """
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 10)
        
        legend_values=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016', 'Revenue', '167.8M','83.9M']
        resultobj.verify_riser_legends('MAINTABLE_wbody1', legend_values, "Step 06: Verify legend values")
        
        """
        Step 07: Verify query pane to check field added to color bucket column
        """
        metaobj.verify_query_pane_field("Color BY", "Sale,Year",1,"Step 07: verify Sale Year added to color bucket column")
        
        """
        Step 08: Select 2011 United States and click Exclude from Chart.
        """
        elem1=(By.CSS_SELECTOR, "circle[class*='riser!s0!g17']")
        resultobj._validate_page(elem1)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g17!m", "Exclude from Chart")
        time.sleep(10)
        
        """
        Step 09: verify query added to filter pane
        """
        utillobj._validate_page((By.CSS_SELECTOR,"#qbFilterBox table>tbody>tr>td>img"))
        metaobj.verify_filter_pane_field("COUNTRY_NAME and TIME_YEAR",1,"Step 09: verify query added to filter pane")
        time.sleep(2)
        
        
        """
        Step 10: Verify 2011 united states value is removed
        """
        #applicable only after Exclude from chart
        parent_css1="circle[class*='riser!s0']"
        utillobj.synchronize_with_number_of_element(parent_css1, 32, 30)
        
        excluded=driver.find_elements_by_css_selector('[class*="s0!g17"]')
        utillobj.asequal(len(excluded),0,"Step 10: Verify 2012 united states value is removed")
        
        """
        Step 11: Click Run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        
        elem1=(By.CSS_SELECTOR, '[class*="riser!s"]')
        resultobj._validate_page(elem1)
        
        """
        Step 12: Verify output
        """ 
        excluded=driver.find_elements_by_css_selector('[class*="s0!g17"]')
        utillobj.asequal(len(excluded),0,"Step 12: Verify 2011 united states value is removed")  
        
        time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        
        """
        Step 13: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 14: Click "Save" in the toolbar > Type C2110387 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main()