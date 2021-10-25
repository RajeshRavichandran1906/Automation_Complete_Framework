'''
Created date 20.12.2016 

@author: Nasir

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050027
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7086
'''

import unittest,time, pyautogui
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon, visualization_metadata
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2050027_TestClass(BaseTestCase):
    
    def test_C2050027(self):
        
        Test_Case_ID = "C2050027"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Select "Format" > "Chart Types" > "Other"."""
        """Step 03: Select "Special" > "Vertical Box plot Chart" > "OK"."""
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('special', 'vertical_boxplot', 4, ok_btn_click=True)
        
        """Step 04. Drag and drop "MSRP" over "Upper quartile"."""
        metaobj.drag_drop_data_tree_items_to_query_tree("MSRP", 1, "Upper quartile", 0)
        time.sleep(4)
        
        """Step 05. Drag and drop "Revenue Per,Sq. Ft." over "Median"."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Revenue Per,Sq. Ft.", 1, "Median", 0)
        time.sleep(4)
        
        """Step 06. Drag and drop "Gross Profit" over "Lower quartile"."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Gross Profit", 1, "Lower quartile", 0)
        time.sleep(4)
        
        """Step 07. Drag and drop "Cost of Goods" over "Lower Limit"."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Cost of Goods", 1, "Lower limit", 0)
        time.sleep(4)
        
        """Step 08: Verify the following chart is displayed."""
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
        """Step 09: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 10: Verify the following chart is displayed."""     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
 
        
        """Step 11: Click "IA" > "Save"."""
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID + "_" + browser)
        time.sleep(5)
        
        """Step 12: Close the IA window.""" 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 13: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 14: Verify the following chart is displayed."""
        """Step 15: Close IA."""
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        