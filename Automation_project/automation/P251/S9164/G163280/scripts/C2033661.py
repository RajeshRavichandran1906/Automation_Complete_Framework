'''
Created on Dec 26, 2016

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2033661
Verify Vertical Absolute Line is working properly
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from common.pages.metadata import MetaData

class C2033661_TestClass(BaseTestCase):

    def test_C2033661(self):
        
        Test_Case_ID = "C2033661"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.ibi.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2033661.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "Line" > "Vertical Absolute Line" > "OK".
        """
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('line', 'vertical_absolute_line', 1, ok_btn_click=True)
        
        """
        Step04: Verify the following chart is displayed.
        """
        browser=utillobj.parseinitfile('browser')
        #Screenshot   
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 05: Double click "Revenue", "Cost of Goods", "Discount" and "Product,Category".
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Discount", 2, 1)
        time.sleep(4)
        MetaData.scroll_data_field_table(self,'Product,Category')
        MetaData.double_click_on_data_filed(self,'Product->Product,Category', 1)

        
        """
        Step06: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")     
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step07: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step08: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5)    
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step08_'+browser.lower()+'.png', "Step 08: verify chart")
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step08_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step09: Click "IA" > "Save"
        Step10: Close the IA window
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step11: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        """
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step12: Verify the following chart is displayed. 
        """
        #Screenshot  
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step12_'+browser.lower()+'.png', "Step 12: verify chart")     
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
        Step13: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)

if __name__ == '__main__':
    unittest.main()

