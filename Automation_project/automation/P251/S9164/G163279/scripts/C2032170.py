'''
Created on 19-DEC-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2032170
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2032170_TestClass(BaseTestCase):

    
    def test_C2032170(self):
        
        Test_Case_ID = "C2032170"
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
        """
        Step 01: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        http://domain.ibi.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2032170.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "Error Bar" > "OK".
        """
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('bar', 'error_bar', 5, ok_btn_click=True)
        
        """
        Step04: Drag and drop "Discount" over "Errorbar Low".
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Discount', 1, 'Errorbar Low',0)
        
        """
        Step05: Drag and drop "Cost of Goods" over Errorbar High".
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods', 1, 'Errorbar High',0)
        
        """
        Step06: Verify the following chart is displayed.
        """
        browser=utillobj.parseinitfile('browser')
        #Screenshot   
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step07: Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step08: Verify PDF downloads. Open the PDF.
        Step09: Verify the following chart is displayed.
        """
        #Screenshot   
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step9_"+ browser +".png" , "Step9 verification")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step09'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        """
        Step10: Click "IA" > "Save"
        Step11: Close the window
        Step12: Launch the IA API with chart in edit mode (edit domain, port and alias portions of URL, do not use link as is):
        Step13: Verify the following chart is displayed.        
        """
        time.sleep(1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940',mrid='mrid',mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        #Screenshot        
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        
        """
        Step14: Close IA.
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(1)


if __name__ == '__main__':
    unittest.main()