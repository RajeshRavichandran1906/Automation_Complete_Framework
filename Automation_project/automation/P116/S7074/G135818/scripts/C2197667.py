'''
Created on Oct 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197667
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata, ia_ribbon
from common.lib import utillity
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class C2197667_TestClass(BaseTestCase):

    def test_C2197667(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID = 'C2197667'
        """
        Step 01: Create a Chart using IA with ggsales.mas as AHTML output
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 02: Add fields Category, Dollar Sales, Budget Units and Unit Sales
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        metadataobj.datatree_field_click('Budget Units', 2, 1)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        
        """
        Step 03: Select Format >Chart Types> Others>Select chart 3D Bars 'Standard'
        """
        '''browser=utillobj.parseinitfile('browser')
        
        FormatTab=self.driver.find_element_by_css_selector('[id="FormatTab_tabButton"]')
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(FormatTab, 0, -7,leftClick=True)
        else :
            FormatTab.click()
        time.sleep(3)
        
        otherchart=self.driver.find_element_by_css_selector('[id="FormatOtherChart"]')
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(otherchart, 0, -7,leftClick=True)
        else :
            otherchart.click()
        time.sleep(3)
        
        chartgroup=self.driver.find_element_by_css_selector('[id="ChartTypeGroup_ThreeD"]')
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(chartgroup, 0, -7,leftClick=True)
        else :
            chartgroup.click()
        time.sleep(10)
        
        rightpane=self.driver.find_element_by_xpath('//div[@id="RightPane_ThreeD"]/div/div[2]/div[1]')
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(rightpane, 0, -7,leftClick=True)
        else :
            rightpane.click()
        time.sleep(5)
        ok=self.driver.find_element_by_css_selector('[id="selectChartOkBtn"]')
        if browser=='Firefox' :
            utillobj.click_type_using_pyautogui(ok, 0, -7,leftClick=True)
        else :
            ok.click()'''
        
        time.sleep(4)
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(2)
        ia_ribbonobj.select_other_chart_type('threed', 'threed_bars', 1, ok_btn_click=True)
        time.sleep(1)
       
       
        """
        Step 04: Execute the Chart. Verify that is displays Standard 3D Chart.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))  
        
        element = self.driver.find_element_by_css_selector("#orgdivouter0")
        utillobj.take_screenshot(element, 'C2197667_Base_Step04', image_type='actual_images')
        
        self.driver.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()