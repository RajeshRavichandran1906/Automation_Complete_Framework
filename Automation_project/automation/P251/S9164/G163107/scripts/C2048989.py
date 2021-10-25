'''
Created date 19.12.2016 

@author: Nasir

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2048989
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7086
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2048989_TestClass(BaseTestCase):
    
    def test_C2048989(self):
        
        Test_Case_ID = "C2048989"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048989.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Select "Format" > "Chart Types" > "Other"."""
        """Step 03: Select "Stock" > "Stock Hi-Lo with Volume" > "OK"."""
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('stock', 'stock_high_low_volume', 2, ok_btn_click=True)
        
        """Step 04: Drag and drop "Sale Unit(s)" over "Volume"."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale Unit(s)", 1, "Volume", 0)
        time.sleep(4)
        
        """Step 05: Verify the following chart is displayed."""
        time.sleep(5)     
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step05', image_type='actual')  
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step5_"+ browser +".png","step5:verification")
        time.sleep(3)
        
        """Step 06: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 07: Verify the following chart is displayed."""     
#         ele=driver.find_element_by_css_selector("#resultArea")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step07_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step7_"+ browser +".png","step7:verification")
        
        
        """Step 08: Click "IA" > "Save"."""
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID + "_" + browser)
        time.sleep(5)
        
        """Step 09: Close the IA window.""" 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 10: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 11: Verify the following chart is displayed."""
        """Step 12: Close IA."""
        time.sleep(3)     
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step12', image_type='actual',x=1, y=1, w=-1, h=-1)  
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step11_"+ browser +".png","step11:verification")
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        