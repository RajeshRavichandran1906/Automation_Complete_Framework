'''
Created on June 21, 2016

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404 
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109128
'''
__author__ = "Gobinath Thiyagarajan"
__copyright__ = "IBI"

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity  

class C2140680_TestClass(BaseTestCase):
    def test_C2140680(self):
        #Test Variables 
        Test_Case_ID = 'C2140680'
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        '''Step 01: Launch the IA API 
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''
        
        driver = self.driver #Driver reference object created    
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        '''Step 02: Double click "Revenue" and "Product,Category"'''
        
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(10)  
        
        '''Step 03: Verify label values '''
        sync_css="#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, sync_css)
        resultobj._validate_page(elem1)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        time.sleep(6)
        
        '''  Step 04: Verify  bar riser values '''
        
        tooltip_val=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",tooltip_val,"Step 04: Verify  bar riser values ")
         
        '''Step 05:Add "Customer,Business,Region" to Horizontal axis. '''
        
        metaobj.datatree_field_click('Customer,Business,Region', 1, 1,'Add To Query', 'Horizontal Axis') 
        parent_css="#MAINTABLE_wbody1 text[class^='xaxis'][class$='title']"
        expected_obj="Product Category : Customer Business Region"
        utillobj.synchronize_with_visble_text(parent_css, expected_obj, 45)
#         timeout=0
#         while True:
#             temp_obj = self.driver.find_element_by_css_selector(parent_css).text
#             if len(temp_obj) == expected_obj:
#                 break
#             timeout+=1
#             if timeout == 250:
#                 break
#             time.sleep(1)
        
        '''Step 06: Verify Query pane'''
        _step06 = 'Step 06: Verify Query pane'
        
        metaobj.verify_query_pane_field('Vertical Axis','Revenue',1, _step06 )
        
        '''Step 07: Verify labels  '''
        
        lab_val = ["Product Category : Customer Business Region", "Revenue"]
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", lab_val[0], "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", lab_val[1], "Step 07:d(ii) Verify Y-Axis Title")
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1) 
        time.sleep(5)  
        tooltip_val=['Product Category:Accessories', 'Customer Business Region:EMEA', 'Revenue:$68,812,972.66', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar',tooltip_val,"Step 07: Verify output value")
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1) 
        time.sleep(5)                            
        
        '''Step 08: Hover over on EMEA:Accessories and click Exclude from Chart '''
        
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g0!mbar', 'Exclude from Chart')
        resultobj.wait_for_property("#MAINTABLE_wbody1 [class^='riser!s0!']", 27)
        expected_xval_list=['Accessories : North America', 'Accessories : Oceania', 'Accessories : South America']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        time.sleep(10)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08b(i): Verify bar color")
        
        
        '''Step 09:  Verify Query added to filter pane'''
        time.sleep(8)
        metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and BUSINESS_REGION',1, 'Step 09:  Verify Query added to filter pane')
         
        '''Step 10:  Verify Accessories value excluded '''
        
        _step10 = 'Step 10:  Verify Accessories value excluded'
        xaxis_value = "Accessories : EMEA"
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, _step10+": X Label") 
        
        '''Step 11: Hover over on EMEA:Camcorder and click Exclude from Chart. '''
        time.sleep(6)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g3!mbar', 'Exclude from Chart')
        time.sleep(25)
        resultobj.wait_for_property("#MAINTABLE_wbody1 [class^='riser!s0!']", 26)
        
        '''  Step 12.Verify Camcorder value excluded '''
        
        _step12 = 'Step 12.Verify Camcorder value excluded '
        xaxis_value = "Camcorder:EMEA"
        time.sleep(8)
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, _step12+": X Label")
        
        expected_xval_list=['Accessories : Oceania']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12b(i): Verify bar color")
        
        '''Step 13:Click Run in the toolbar'''
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(30)
#        
#         s= driver.window_handles
#         #to switch to run window
#         driver.switch_to.window(s[-1])
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
       
        '''Step 14 : Verify output'''
        
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(10)
        tooltip_val=['Product Category:Accessories', 'Customer Business Region:North America', 'Revenue:$54,160,885.45', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar',tooltip_val,"Step 14: Verify output value")
        
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, "Step 14: X Label")
        
        expected_xval_list=['Accessories : North America', 'Accessories : Oceania', 'Accessories : South America', 'Camcorder : North America']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14b(i): Verify bar color")
        
        time.sleep(20)
        
        utillobj.take_screenshot(driver.find_element_by_css_selector(" #orgdiv0"),'C2140680_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        '''Step 15: Close the output window.'''
        
        self.driver.close()
#         window_before = driver.window_handles[0]  # switch back to main window
#         driver.switch_to.window(window_before)
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        '''Step 16: Click "Save" in the toolbar > Type C2140680 > Click "Save" in the Save As dialog '''
        
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        

if __name__ == '__main__':
    unittest.main()

