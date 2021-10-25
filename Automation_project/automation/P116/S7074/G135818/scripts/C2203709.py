'''
Created on Oct 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203709
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,active_miscelaneous,ia_resultarea
from common.lib import utillity
import unittest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class C2203709_TestClass(BaseTestCase):

    def test_C2203709(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultareaobj = ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID = 'C2203709'
        """
        Step 01: Create an report using InfoAssist with CAR master file.
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7074', 'mrid', 'mrpass')
          
        """
        Step 02: Add fields Car,Country and Sales
        """
        metadataobj.datatree_field_click('CAR', 2, 1)
        metadataobj.datatree_field_click('COUNTRY', 2, 1)
        metadataobj.datatree_field_click('SALES', 2, 1)
  
        """
        Step 03: Change the default format to active report from the format dropdown.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
  
        """
        Step 04: Right click on Car and Country field from Query pane select Hide. Verify Sales column is displayed.
        """
        metadataobj.querytree_field_click('CAR', 1, 1,'Visibility')
        self.driver.find_element_by_xpath("//td[contains(text(),'Hide')]").click()
        time.sleep(5)
        metadataobj.querytree_field_click('COUNTRY', 1, 1,'Visibility')
        val = self.driver.find_elements_by_xpath("//td[contains(text(),'Hide')]")
        val[1].click()
        time.sleep(4)
        resultareaobj.verify_report_data_set('TableChart_1', 10, 1, 'C2203709_Ds01.xlsx','Step 04: Verify Sales column is displayed.')
          
        """
        Step 05: Select Dropdown from Sales->Chart->Pie->Group By and verify NOPRINT fields are not available from the option.
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.switch_to_frame(pause=3)
        
        expected_menu_list = ['Group By (X)','SALES']
        miscelaneousobj.verify_menu_items('ITableData0', 2, 'Chart->Pie', expected_menu_list, 'Step 05: verify NOPRINT fields are not available from the option')
        
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()