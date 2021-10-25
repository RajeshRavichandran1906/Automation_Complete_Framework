'''
Created on Oct 7, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203756
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,active_miscelaneous
from common.lib import utillity
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class C2203756_TestClass(BaseTestCase):

    def test_C2203756(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        Test_Case_ID = 'C2203756'
        
        """
        Step 01: Launch IA to develop a report
        Step 02: Choose CAR as master file, and select output format as Active report
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7072', 'mrid', 'mrpass')
        time.sleep(4)
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 03: Load COUNTRY, CAR, MODEL to get a report
        """
        metadataobj.datatree_field_click('COUNTRY', 2, 1)
        metadataobj.datatree_field_click('CAR', 2, 1)
        metadataobj.datatree_field_click('MODEL', 2, 1)
        
        """
        STep 04: Select 'Report > Theme' from 'Home' tab.
        STep 05: Open ENTeal_Light2.sty, then Run the report
        """
        time.sleep(8)
        ribbonobj.select_theme('Legacy Templates', 'ENTeal_Light2.sty')
        ribbonobj.select_tool_menu_item( 'menu_run')
        time.sleep(3)
        
        """
        Step 06: Verify the column title gets merged in white color, and it is visible properly in run time.
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        columns = ['COUNTRY','CAR','MODEL']
        miscellaneousobj.verify_column_heading('ITableData0',columns , 'Step 06.1: Verify column title')
        utillobj.verify_data_set('ITableData0', 'I0r','C2203756_Ds01.xlsx','Step 06.2: Verify data')
        
        
        self.driver.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()        
        
               
        
        
        