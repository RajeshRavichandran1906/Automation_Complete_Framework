'''
Created on 17-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227513
TestCase Name = Verify Filter expression, retrieving Values for a Measure field
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227513_TestClass(BaseTestCase):

    def test_C2227513(self):
        
        Test_Case_ID = "C2227513"
        driver = self.driver
        driver.implicitly_wait(20)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with CAR, Report mode::
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        2. Double click "COUNTRY", "SALES" 
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4) 
        
        """
        3. Drag SALES to Filter Pane
        """        
        metaobj.datatree_field_click("SALES", 1, 1,'Filter')
        time.sleep(1)

        """
        4. Double click <Value> > "Get Values" (dropdown) > "All".
        5. Double click "13000".
        6. Verify "13000" moved over to the "Multiple Values" side.
        7. Click "OK" (2x).
        """
        ia_ribbonobj.create_constant_filter_condition('All',['13000'])
        
        """
        8. Verify the following report is displayed.
        """
        coln_list = ['COUNTRY', 'SALES', '']
        resultobj.verify_report_titles_on_preview(3, 2, "TableChart_1", coln_list, "Step 08a: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 1,2,'C2227513_Ds01.xlsx',"Step 08: Verify report data set")
        
        """
        9. Click "Run".
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        10. Verify report is displayed.
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "[id^='ReportIframe-']")))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227513_Ds02.xlsx", "Step 10: verify data set")

        """
        11. Click "IA" > "Save" > "C2227513" > click Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        12. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        13. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227513.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit('C2227513', 'document', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        14. Verify Preview
        """
        coln_list = ['COUNTRY', 'SALES', '']
        resultobj.verify_report_titles_on_preview(3, 2, "TableChart_1", coln_list, "Step 14a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 1,2,'C2227513_Ds01.xlsx',"Step 14: Verify preview data set by reopening fex")
        
        """
        15. Logout
        """
        utillobj.infoassist_api_logout()
        
        
if __name__ == '__main__':
    unittest.main()
        