'''
Created on May'31, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109010
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2109010_TestClass(BaseTestCase):
    
    def test_C2109010(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109010'
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid02', 'mrpass02')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P141/S8357', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Click "Change" > "Heatmap"
        """
        ribbonobj.change_chart_type("heatmap")
        
        """
        Step 03: Add "Product,Subategory" to Horizontal axis
        """
        metaobj.datatree_field_click("Product,Subcategory",1,1,"Add To Query","Horizontal Axis")
        
        """
        Step 04:Add "Sale,Month" to Vertical axis
        """
        time.sleep(2)
        metaobj.datatree_field_click("Sale,Month",1,1,"Add To Query","Vertical Axis")
        
        """
        Step 05: Verify label values
        """
        time.sleep(15)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory",'Step 03: Verify X title Product Subcategory')
        xtitle=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 text[class='xaxisOrdinal-title']")
        utillobj.asequal(xtitle[1].text,'Sale Month',"Step 03: Verify X Title Sale Month")
        
        """
        Step 06: Add "Revenue" to Color bucket
        """
        time.sleep(3)
        metaobj.datatree_field_click("Revenue",1,1,"Add To Query","Color")
        
        """
        Step 07: Hover over a value(charger, sale month 12) > Filter Chart
        """
        time.sleep(5)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s11!g3!mbar", 'Filter Chart')
 
        """
        Step 08: verify query added to filter pane
        """
        time.sleep(15)
        metaobj.verify_filter_pane_field("PRODUCT_SUBCATEG and TIME_MTH", 1, "Step 08: verify query added to filter pane")
        x_val_list=['Charger']
        y_val_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 08c: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "persian_red", "Step 08d(i): Verify first bar color")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory",'Step 08: Verify X title Product Subcategory')
        xtitle=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 text[class='xaxisOrdinal-title']")
        utillobj.asequal(xtitle[1].text,'Sale Month',"Step 08: Verify X Title Sale Month")
        
        """
        Step 09: verify charger subcategory is filtered
        """
        time.sleep(10)
        a=['Revenue:$413,036.96', 'Sale Month:12', 'Product Subcategory:Charger', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 09.2: verify charger subcategory is filtered")
 
        """
        Step 10:Click "Run" in the toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 11: Verify output
        """
        elem1=(By.CSS_SELECTOR, '[class*="riser!s0!g0!mbar"]')
        resultobj._validate_page(elem1)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 11.1: verify charger subcategory is filtered")
        x_val_list=['Charger']
        y_val_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 11c: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "persian_red", "Step 11d(i): Verify first bar color")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory",'Step 11: Verify X title Product Subcategory')
        xtitle=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 text[class='xaxisOrdinal-title']")
        utillobj.asequal(xtitle[1].text,'Sale Month',"Step 11: Verify X Title Sale Month")
        
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']"),'C2109010_Actual_step11', image_type='actual')
        time.sleep(5)
        
        """
        Step 12: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 13: Click "Save" in the toolbar > Type C2109010 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)

if __name__ == '__main__':
    unittest.main()