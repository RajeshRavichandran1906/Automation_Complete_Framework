'''
Created date 21.12.2016 

@author: Nasir

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2047843
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7086
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2047843_TestClass(BaseTestCase):
    
    def test_C2047843(self):
        
        Test_Case_ID = "C2047843"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Select "Format" > "Chart Types" > "Other"."""
        """Step 03: Select "Pie" > "Multi Proportional Ring Pie" (groups)> "OK"."""
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('pie', 'pie_multi_ring_proportional', 8, ok_btn_click=True) 
        
        """Step 04: Verify the following chart is displayed."""
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """Step 05: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 06: Verify the following chart is displayed."""
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)  
        
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
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 10: Verify the following chart is displayed."""
        """Step 11: Close IA."""
        time.sleep(3)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step10_'+browser.lower()+'.png', "Step 10: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        