'''
Created on Oct 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203745
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata, visualization_resultarea, ia_ribbon
from common.lib import utillity
import unittest,time
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class C2203745_TestClass(BaseTestCase):

    def test_C2203745(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        Test_Case_ID = 'C2203745'
        
        """
        Step 01: Create a report with IA, use car file
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7072', 'mrid', 'mrpass')
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        utillobj._validate_page(elem)
        
        
        """
        Step 02: Add fiels car, sales
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        elem=(By.CSS_SELECTOR,'#TableChart_1')
        utillobj._validate_page(elem)
        coln_list = ['CAR', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02: Verify Canvas column titles")
        
        """
        Step 03: Select Format tab, select Active Report format
        """
        
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 04: Select Active Report Options under Features group to open dlg and Click 'Advanced' in this dialog.
        Step 05: Check 'Expiration' checkbox and enter '160101' under Date input box
        Step 06: Enter 'test1' under password input box, say ok
        """
        time.sleep(7)
        ribbonobj.select_ribbon_item('Format', 'Active_Report_Options')
        time.sleep(7)
        ia_ribbonobj.active_report_options('Advanced', advanced_expiration=True, advanced_expirationDateTxtFld='160101', advanced_password='test1', btnOk=True)

        """
        Step 07: Verify password is prompted when executing report.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(3)
        
        """
        Step 08: Verify password is prompted when executing report.
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))        
        elem1=(By.CSS_SELECTOR,'#wall1')
        utillobj._validate_page(elem1)
        time.sleep(7)
        password_window = self.driver.find_element_by_css_selector('[class="arWindowBarTitle"] ').is_displayed()
        utillobj.asequal(password_window,True,'Step 07: Verify password is prompted when executing report')
        time.sleep(2)
        
        """
        Step 09: Saved the Test case with test case name='C2203745'.
        """
        self.driver.switch_to_default_content()
        time.sleep(9)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
        