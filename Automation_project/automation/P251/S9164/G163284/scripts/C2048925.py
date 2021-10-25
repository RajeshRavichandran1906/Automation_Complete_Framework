'''
Created date 14.12.2016 

@author: Gobizen

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2048428
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Verify 3D Honeycomb Surface is working properly.

'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators


class C2048925_TestClass(BaseTestCase):
    
    def test_C2048925(self):
        
        Test_Case_ID = "C2048925"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048925.fex&tool=chart"""
        
        utillobj.infoassist_api_edit('C2048925', 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Select "Format" > "Chart Types" > "Other """
        
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step01', image_type='actual')  
        time.sleep(3)
        
        """Step 03: Select "3D" > " 3D Honeycomb Surface" > "OK". """
        
        ribbonobj.select_ribbon_item('Format', 'Other')
        time.sleep(4)
        ia_ribbobj.select_other_chart_type('threed', 'threed_honeycomb_surface', 15, ok_btn_click=True )
        
        
         
        """Step 04: Verify the following chart is displayed."""
        
        time.sleep(7)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step02', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """Step 05: Click "Run"."""
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """Step 06: Verify the following chart is displayed."""
        
        browser=utillobj.parseinitfile('browser')  
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step6_"+ browser +".png" , "Step6 verification",tolerance=0.95)
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step03_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot  
        
        
        """Step 07: Click "IA" > "Save"."""

        """Step 08: Close the IA window.""" 
        
        """Step 09: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(''+Test_Case_ID+'_'+browser+'')
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        
        utillobj.infoassist_api_edit(''+Test_Case_ID+'_'+browser+'', 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 10: Verify the following chart is displayed."""
        
        """Step 11: Close IA."""
        
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        