'''
Created on Oct 19, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203782
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata,active_miscelaneous,visualization_resultarea
from common.lib import utillity
import unittest,time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class C2203782_TestClass(BaseTestCase):

    def test_C2203782(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        Test_Case_ID = 'C2203782'
        
        """
        Step 01: Create a AHTML report eg:Country,Car and Sales fields using CAR master file.
        """
        utillobj.infoassist_api_login('report', 'ibisamp/car', 'P116/S7072', 'mrid', 'mrpass')
        
        parent_css="#TableChart_1 [align='justify']"
        result_obj.wait_for_property(parent_css, 1)
        
        metadataobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('CAR', 2, 1)
        time.sleep(4)
        metadataobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        """
        Step 02: Select format as Active Report.
        """
        ribbonobj.change_output_format_type('active_report', location='Home')
        time.sleep(10)
        
        """
        Step 03: In AHTML Report,click on any cell value, select 'Comment' option. C2203782_1
        """
        
        ribbonobj.select_tool_menu_item('menu_run')
        iframe_loc = driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr = iframe_loc.location['x']
        y_fr = (iframe_loc.location['y']) - 7
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it
            ((By.CSS_SELECTOR, '[id^=ReportIframe-]')))   
        miscellaneousobj.select_field_menu_items('ITableData0', 0, 0, 'Comments', x_offset=x_fr, y_offset=y_fr, browser_height=80)
        parent_css="td.arWindowBarTitle"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(5)
        """
        Step 04: Give any word/sentence and give 'OK'.
        """
        self.driver.find_element_by_css_selector('[name="note"]').send_keys('Text Message')
        self.driver.find_element_by_css_selector('[class="arPromptButton"]').click()
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203782_Ds01.xlsx','Step 04: Verify data set')
        
        """
        Step 05: Now select Restore original from any heading.
        """
        time.sleep(2)
        miscellaneousobj.select_menu_items('ITableData0', 0, 'Restore Original', x_offset=x_fr, y_offset=y_fr, browser_height=80)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203782_Ds02.xlsx','Step 05: Verify data set')
                
        """
        Step 06: Now again click on any cell and select 'Comment' option again
        """
        miscellaneousobj.select_field_menu_items('ITableData0', 0, 0, 'Comments', x_offset=x_fr, y_offset=y_fr, browser_height=80)
        
        """
        Step 07: Verfity that report gets executed without any error in IE browser.
        """
        self.driver.find_element_by_css_selector('[onclick="closewin(1)"]').click()
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203782_Ds02.xlsx','Step 07: Verify data set')
        
        self.driver.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()