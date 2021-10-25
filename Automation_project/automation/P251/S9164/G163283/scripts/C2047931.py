'''
Created on Dec 20, 2016

@author: Magesh

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2047931
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Verify XY Scatter is working properly.

'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2047931_TestClass(BaseTestCase):
    
    def test_C2047931(self):
        
        Test_Case_ID = "C2047931"
        
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047931.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Verify the following chart is displayed."""
        
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step02', image_type='actual')  
        time.sleep(3)
        
        """Step 03: Double click "Revenue" and "Sale,Month"."""
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Sale,Month', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(8)
        
        """Step 04: Drag and drop "Product,Category" over "Legend (Series)"."""
        metaobj.drag_and_drop_query_items("Product,Category", "Legend (Series)")
        time.sleep(4)
         
        """Step 05: Verify the following chart is displayed."""
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step05', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """Step 06: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 07: Verify the following chart is displayed."""
        
        browser=utillobj.parseinitfile('browser')  
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step7_"+ browser +".png" , "Step7 verification")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step07_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot  
        
        
        """Step 08: Click "IA" > "Save"."""

        """Step 09: Close the IA window.""" 
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 10: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047931.fex&tool=chart"""
        
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 11: Verify the following chart is displayed."""
        
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """
        Step12: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)
        
if __name__=='__main__':
    unittest.main()