'''
Created on Dec 26, 2016

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2035233
Verify Horizontal Stacked Line is working properly
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

class C2035233_TestClass(BaseTestCase):

    def test_C2035233(self):
        
        Test_Case_ID = "C2035233"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2035233.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "Line" > "Horizontal Stacked Line" > "OK".
        """
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('line', 'horizontal_stacked_line', 9, ok_btn_click=True)
        
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
        Step05: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step06: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5) 
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")   
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step07: Click "IA" > "Save"
        Step08: Close the IA window
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """ Step09: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2035233.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step10: Verify the following chart is displayed."""
        #Screenshot        
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step10_'+browser.lower()+'.png', "Step 10: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
        Step11: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()

