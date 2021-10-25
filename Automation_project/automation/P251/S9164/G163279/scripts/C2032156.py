'''
Created on 12-DEC-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2032156
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from common.pages.metadata import MetaData

class C2032156_TestClass(BaseTestCase):

    def test_C2032156(self):
        
        Test_Case_ID = "C2032156"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
#         ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
#         ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
#         ia_runobj = ia_run.IA_Run(self.driver)
#         ia_styobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.ibi.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2032156.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Verify the following chart is displayed.
        """
        time.sleep(5)        
        browser=utillobj.parseinitfile('browser')
        time.sleep(5)     
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step2_"+ browser +".png" , "Step2 verification")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step02', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step03: Double click "Revenue", "Cost of Goods", "Discount" and "Product,Category".
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Discount', 2, 1)
        time.sleep(4)
        MetaData.scroll_data_field_table(self,'Product,Category')
        MetaData.double_click_on_data_filed(self,'Product->Product,Category', 1)
        
        """
        Step04: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5)     
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step4_"+ browser + ".png" , "Step4 verification ")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step05: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step06: Verify PDF downloads. Open the PDF.
        Step07: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5)     
#         ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step7_"+browser +".png" , "Step7 verification")
        
#         utillobj.take_screenshot(ele,Test_Case_ID+'_'+browser+'_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step08: Click "IA" > "Save"
        Step09: Close the window
        Step10: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        Step11: Verify the following chart is displayed.        
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        #Screenshot        
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step4_" + browser + ".png" , "Step11 verification")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
        Step12: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)


        
if __name__ == '__main__':
    unittest.main()