'''
Created on Dec 21, 2016

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2047675
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Verify Pie is working properly.

'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2047675_TestClass(BaseTestCase):
    
    def test_C2047675(self):
        
        Test_Case_ID = "C2047675"
        
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047675.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        utillobj.wait_for_page_loads(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Verify the following chart is displayed."""
        #Screenshot   
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step02_'+browser.lower()+'.png', "Step 02: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """Step 03: Double click "Revenue" and "Product,Category"."""
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product->Product,Category', 2, 1)
        time.sleep(8)
         
        """Step 04: Verify the following chart is displayed."""
        
        time.sleep(3)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """Step 05: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 06: Verify the following chart is displayed."""
        
        browser=utillobj.parseinitfile('browser')  
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot  
        
        
        """Step 07: Click "IA" > "Save"."""
        """Step 08: Close the IA window.""" 
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 09: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047675.fex&tool=chart"""
        
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 10: Verify the following chart is displayed."""
        
        time.sleep(3)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step10_'+browser.lower()+'.png', "Step 10: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """
        Step11: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)
        
if __name__=='__main__':
    unittest.main()
