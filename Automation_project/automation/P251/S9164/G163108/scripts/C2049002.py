'''
Created date 20.12.2016 

@author: Nasir

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2049002
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7086
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2049002_TestClass(BaseTestCase):
    
    def test_C2049002(self):
        
        Test_Case_ID = "C2049002"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Verify the following chart is displayed."""
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step02', image_type='actual',x=1, y=1, w=-1, h=-1) 
        time.sleep(3)
        
        """Step 03: Double click "Revenue", "Sale,Year"."""
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Sale,Year', 2, 1)
        time.sleep(8)
        
        """Step 04: Verify the following chart is displayed."""        
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """Step 05: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 06: Verify the following chart is displayed."""     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """Step 07: Click "IA" > "Save"."""
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID + "_" + browser)
        time.sleep(5)
        
        """Step 08: Close the IA window.""" 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 09: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 10: Verify the following chart is displayed."""
        """Step 11: Close IA."""
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        