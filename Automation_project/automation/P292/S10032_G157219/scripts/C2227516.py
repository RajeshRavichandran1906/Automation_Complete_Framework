'''
Created on 24-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227516
TestCase Name = Verify multi-select Dynamic Filter
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

class C2227516_TestClass(BaseTestCase):

    def test_C2227516(self):
        
        Test_Case_ID = "C2227516"
        driver = self.driver
        driver.implicitly_wait(20)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
#         iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with CAR, Report mode:
        """
        utillobj.infoassist_api_login('report','ibisamp/CAR','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        2. Drag/drop COUNTRY field to Filter Pane.
        """        
        metaobj.datatree_field_click("COUNTRY", 1, 1,'Filter')
        time.sleep(1)

        """
        3. Double-click <Value>, Select Type = "Parameter".
        4. Select "Dynamic" radio button.
        5. Check off "Select multiple values at runtime"
        6. Click "OK" (2x).
        """
        ia_ribbonobj.create_parameter_filter_condition('Dynamic', ['COUNTRY'],ParamMultiple=True)
        
        """
        7. Verify filter is created.
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Multiselect Dynamic Parameter (Name: COUNTRY, Field: COUNTRY in CAR)', 1, "Step 07: Verify the filter pane")
       
        """
        8. Add fields "COUNTRY", "SALES".
        """
        time.sleep(2)
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        coln_list = ['COUNTRY', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2,'C2227516_Ds01.xlsx',"Step 08: Verify report data set")        
        
        """
        09. Click "Run".
        """ 
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        10. Click the "All Values" dropdown menu > check off "ENGLAND" and "ITALY"
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_default_amper_value('COUNTRY','All Values',"Step 10: Verify Defualt amper value All Values in run window")
        
        iarun.select_amper_value('COUNTRY', ['ENGLAND','ITALY'],False)
        
        """
        11. Click "Run" in the AutoPrompt window
        """        
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        12. Verify it generated the following output.
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(4)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227516_Ds02.xlsx", "Step 12: verify data set")
        
        """
        13. Click "IA" > Save > "C2227516" > click Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        14. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
        15. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227516.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit('C2227516', 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """
        16. Verify Filter
        """
        metaobj.verify_filter_pane_field('COUNTRY Equal to Multiselect Dynamic Parameter (Name: COUNTRY, Field: COUNTRY in ibisamp/CAR)', 1, "Step 16: Verify the filter pane")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2,'C2227516_Ds03.xlsx',"Step 16: Verify report data set")        
          
        """
        17. Logout:
        """
        utillobj.infoassist_api_logout()
         
if __name__ == '__main__':
    unittest.main()