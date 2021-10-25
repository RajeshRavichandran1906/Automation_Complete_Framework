'''
Created on June6, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108845&group_by=cases:section_id&group_id=146864&group_order=asc
TestCase Name : A-4393:Can't Lasso Filter at design time for bar or stacked bar visualization
'''
import unittest
import time,re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2108845_TestClass(BaseTestCase):
    
    def test_C2108845(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108845'        
        """
        Step 01: Launch API (Folder - S8357 and Master - wf_retail_lite) and login as "autodevuser03"
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid02', 'mrpass02')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Change to line chart
        """
        ribbonobj.change_chart_type('line')
        
        """
        Step 03: Add Revenue to vertical and Sale,Year/Month to horizontal axis
        """
        metaobj.datatree_field_click('Revenue',2,1)
        time.sleep(5)
        metaobj.datatree_field_click('Sale,Year/Month',2,1)
        time.sleep(4)
        
        """
        Step 04: Verify x and y axis label values.
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year/Month",'Step 03: Verify X title Sale Year/Month')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue",'Step 03: Verify Y title Revenue')
        
        """
        Step 05: Verify first and last 3
        """
        ribbonobj.select_ribbon_item('Series', 'Marker',opt='Circle')
        elem1=(By.CSS_SELECTOR, "[class*='marker!s0!g0!mmarker']")
        resultobj._validate_page(elem1)
     
        a=['Sale Year/Month:2011/01', 'Revenue:$3,874,651.96', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Quarter', 'Drill down to Sale Day']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','marker!s0!g0!mmarker',a,"Step 05: Verify tooltip values")
         
        """
        Step 06: Lasso 2012/11 to 2013/10 values and select filter chart
        """
        elem1=(By.CSS_SELECTOR, "[class*='marker!s0!g22!mmarker']")
        resultobj._validate_page(elem1)
        resultobj.create_lasso("MAINTABLE_wbody1",'circle', 'marker!s0!g22!mmarker', target_tag='circle', target_riser='marker!s0!g33!mmarker')
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(6)
         
        """
        Step 07: Verify query added to filter pane.
        """
        parent_css="#qbFilterWindow #qbFilterBox img"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 12)
        metaobj.verify_filter_pane_field("Sale,Year/Month",1,"Step 07: Verify query added to filter pane.")
         
        """
        Step 08: Verify output in preview
        """
         
        time.sleep(5)
        a =['Sale Year/Month:2012/11', 'Revenue:$5,788,867.16', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Quarter', 'Drill down to Sale Day']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','marker!s0!g0!mmarker', a,"Step 08: Verify first point tooltip value in Preview")
         
        """
        Step 09: Click "Run" in the toolbar.
        """
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        utillobj.switch_to_window(1)            #to switch to run window
        time.sleep(15)
        
        """
        Step 10: Verify output
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-labels']"
        resultobj.wait_for_property(parent_css, 12)
        
        a=['Sale Year/Month:2012/11', 'Revenue:$5,788,867.16', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year/Quarter', 'Drill down to Sale Day']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','marker!s0!g0!mmarker',a,"Step 10: Verify first point tooltip value in Preview")
        time.sleep(25)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108845_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step 11: Close the output window
        """
        self.driver.close()
        time.sleep(7)
        utillobj.switch_to_window(0)        # switch back to main window
        time.sleep(9)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
          
        """
        Step 12: Click "Save" in the toolbar > Type C2108845 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)
        



if __name__ == '__main__':
    unittest.main()

