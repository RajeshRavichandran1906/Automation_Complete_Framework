'''
Created on Oct 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203752
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,visualization_resultarea
from common.lib import utillity
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class C2203752_TestClass(BaseTestCase):

    def test_C2203752(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        Test_Case_ID = 'C2203752'
        
        """
        Step 01: Launch InfoAssist to develop a Report
        Step 02: Select 'GGSALES' as master file
        """
        utillobj.infoassist_api_login('report', 'ibisamp/ggsales', 'P116/S7072', 'mrid', 'mrpass')
        parent_css="#TableChart_1 [align='justify']"
        result_obj.wait_for_property(parent_css, 1)
        
        """
        Step 03: Add Category, Product as 'BY' fields and Unit sales, Dollar Sales as MEASURE(SUM) fields
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('Product', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        time.sleep(4)
        
        """
        Step 04: From Home tab, select Active Report output format
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 05: From Format tab, expand features group and select 'Active Report options'
        """
        format_tab=self.driver.find_element_by_css_selector('[id="FormatTab_tabButton"]')
        utillobj.default_left_click(object_locator=format_tab)
        time.sleep(5)
        
        report_Style=self.driver.find_element_by_css_selector('[id="FormatActiveReportStyling"]')
        utillobj.default_left_click(object_locator=report_Style)
        time.sleep(5)

        """
        STep 06: Switch to 'ADVANCED' tab and enter '123' in password text box and click apply and give ok.
        """
        report_Style_advance=self.driver.find_element_by_css_selector('[id="activeReportStyleAdvanced"]')
        utillobj.default_left_click(object_locator=report_Style_advance)
        time.sleep(3)
        self.driver.find_element_by_css_selector('[id="securityPasswordFld"]').send_keys('123')
        time.sleep(3)
        self.driver.find_element_by_css_selector('[id="activeReportOptionsApplyBtn"]').click()
        time.sleep(3)
        self.driver.find_element_by_css_selector('[id="activeReportOptionsOkBtn"]').click()
        
        """
        Step 07: Run the report.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        
        """
        Step 08: Report should prompts for password window give 123 as password.
        """
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))  
        
        time.sleep(10)
        self.driver.find_element_by_css_selector('[name="promptform"] input').send_keys('123')
        self.driver.find_element_by_css_selector('[class="arPromptButton"]').click()
        
        """
        Step 09: Now report has to be viewed successfully.
        """
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        time.sleep(1)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203752_Ds01.xlsx','Step 09: Now report has to be viewed successfully')
    
        self.driver.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()