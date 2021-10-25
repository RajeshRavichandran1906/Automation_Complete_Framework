'''
Created on 21-DEC-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2047833
TestCase Name = Verify Ring Pie is working properly (82xx)
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2047833_TestClass(BaseTestCase):

    def test_C2047833(self):
        
        Test_Case_ID = "C2047833"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 1. Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
               http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047833.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "[id^='LayoutChartObjectDrawLayer']")
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        
        """ 2. Select "Format" > "Chart Types" > "Other".        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        
        
        """ 3. Select "Pie" > "Ring Pie" > "OK".                """
        ia_ribbobj.select_other_chart_type('pie', 'ring_pie', 4, ok_btn_click=True)
        
        
        """ 4. Verify the following chart is displayed.         """
        browser=utillobj.parseinitfile('browser')
        '''Screenshot''' 
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        
        """ 5. Click "Run".            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """ 6. Verify the following chart is displayed.         """
        '''Screenshot'''   
        time.sleep(5)     
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_'+browser+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        
        """ 7. Click "IA" > "Save".        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        
        """ 8. Close the IA window.        """
        utillobj.infoassist_api_logout()
        
        
        """ 9. Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
               http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047833.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "[id^='LayoutChartObjectDrawLayer']")
        resultobj._validate_page(elem1)
        time.sleep(3)
        
        
        """ 10. Verify the following chart is displayed.        """
        '''Screenshot'''
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step10_'+browser.lower()+'.png', "Step 10: verify chart")
#         ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
#         utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """ 11. Close IA.        """
        time.sleep(2)
        
        

if __name__ == '__main__':
    unittest.main()