'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227505
TestCase Name = Verify Where-based join, save and restore fex
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227505_TestClass(BaseTestCase):

    def test_C2227505(self):
        
        Test_Case_ID = "C2227505"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > "OK".    """
        ia_ribbonobj.create_join("training")
        time.sleep(8)
        '''    Workaround::: clicking add file not working, Hence closing the join dailog anf reopening it '''
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(8)
        
        """    4. Click "Add New" > LOCATOR.MAS > "OK".    """
        ia_ribbonobj.create_join("locator")
        #ia_ribbonobj.create_join("locator", new_join=False)
        
        """    5. Verify the following is displayed in the "Join" window.    """
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 05a: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 05b: verify Join link color 'red' for second join")
        
        """    6. Click "Filter" button.    """
        ia_ribbonobj.select_join_menu_buttons("filter")
        
        """    7. Verify filter is EMPDATA.PIN = LOCATOR.PIN.     """
        ia_ribbonobj.verify_join_filter_Condition("EMPDATA.EMPDATA.PIN Equal to LOCATOR.LOCATOR.PIN", "Step 07a: Verify filter condition")
        
        """    8. Click "OK" (2x).     """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        ia_ribbonobj.select_join_menu_buttons("ok")
         
        """    9. Double click "LASTNAME", "BUS_PHONE", "EXPENSES".    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("BUS_PHONE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(4)       
        
        """    10 . verify the following report is displayed    """
        coln_list = ["LASTNAME", "BUS_PHONE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 10: Verify column titles")
        time.sleep(4)
        
        """    11. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        time.sleep(8)
        
        """    12. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227505_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227505_Ds01.xlsx", "Step 12a: verify data set")
        time.sleep(3)
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    13. Close the output window    """
        """    14. Click "IA" > "Save".    """
        """    15. Enter Title = "C2068465".    """
        """    16. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    18. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    19. Verify Canvas    """
        coln_list = ["LASTNAME", "BUS_PHONE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 19a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2227505_Ds02.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227505_Ds02.xlsx", "Step 19b: verify data set")
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
