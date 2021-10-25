'''
Created on 30-DEC-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2033657
'''
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
import unittest

class C2033657_TestClass(BaseTestCase):
    
    def test_C2033657(self):
        
        Test_Case_ID = "C2033657"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        
        chart_dialog = "[id*='SelectChartTypeDlg']"
        canvas_css = "[id*='TableChart']"
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2033657.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "Horizontal Waterfall Chart" > "OK".
        """
        ribbonobj.select_ribbon_item('Format', 'Other')
        utillobj.synchronize_until_element_is_visible(chart_dialog, resultobj.home_page_medium_timesleep)
        ia_ribbobj.select_other_chart_type('bar', 'horizontal_waterfall_charts', 22, ok_btn_click=True)
        utillobj.synchronize_until_element_disappear(chart_dialog, resultobj.home_page_medium_timesleep)
        
        """
        Step04: Double click "Revenue".
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        utillobj.synchronize_until_element_is_visible(canvas_css, resultobj.home_page_medium_timesleep)
        
        """
        Step05: Verify the following chart is displayed.
        """
        browser=utillobj.parseinitfile('browser')
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step5_"+ browser +".png" , "Step5 verification")
        
        """
        Step06: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_until_element_disappear(canvas_css, resultobj.home_page_medium_timesleep)
        
        """
        Step07: Verify the following chart is displayed.
        """
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step7_"+ browser +".png" , "Step7 verification")
        
        """
        Step08: Click "IA" > "Save"
        Step09: Close the window
        Step10: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        Step11: Verify the following chart is displayed.        
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step5_"+ browser +".png" , "Step11 verification")
        
        """
        Step12: Close IA.
        """
        
if __name__ == '__main__':
    unittest.main()