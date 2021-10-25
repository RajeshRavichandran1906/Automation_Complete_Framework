'''
Created on 26-DEC-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2035238
'''
import unittest
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2035238_TestClass(BaseTestCase):

    def test_C2035238(self):
        
        Test_Case_ID = "C2035238"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        chart_dialog = "[id*='SelectChartTypeDlg']"
        canvas_css = "[id*='TableChart']"
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2035238.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Select "Format" > "Chart Types" > "Other"."""
        """Step 03: Select "Line" > "Horizontal Dual-Axis Stacked Line" > "OK"."""
        ribbonobj.select_ribbon_item('Format', 'Other')
        utillobj.synchronize_until_element_is_visible(chart_dialog, resultobj.home_page_medium_timesleep)
        ia_ribbobj.select_other_chart_type('line', 'horizontal_dual_axis_stacked_line', 11, ok_btn_click=True) 
        utillobj.synchronize_until_element_disappear(chart_dialog, resultobj.home_page_medium_timesleep)
        
        """Step 04: Verify the following chart is displayed."""
        utillobj.synchronize_until_element_is_visible(canvas_css, resultobj.home_page_medium_timesleep)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step04_'+browser.lower()+'.png', "Step 04: verify chart")
        
        """Step 05: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_until_element_disappear(canvas_css, resultobj.home_page_medium_timesleep)
        
        """Step 06: Verify the following chart is displayed."""  
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step06_'+browser.lower()+'.png', "Step 06: verify chart")  
        
        """Step 07: Click "IA" > "Save"."""
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_" + browser)
        
        """Step 08: Close the IA window.""" 
        utillobj.infoassist_api_logout()
        
        """Step 09: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2035238.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 10: Verify the following chart is displayed."""
        """Step 11: Close IA."""
        utillobj.verify_picture_using_sikuli(Test_Case_ID+'_step10_'+browser.lower()+'.png', "Step 10: verify chart")
        
        
if __name__ == '__main__':
    unittest.main()