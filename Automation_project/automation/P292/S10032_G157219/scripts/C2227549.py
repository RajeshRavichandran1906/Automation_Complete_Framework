'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227549
TestCase Name = Verify create, save and restore HOLD file
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227549_TestClass(BaseTestCase):

    def test_C2227549(self):
        
        Test_Case_ID = "C2227549"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)

        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """    2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)
        
        
        """    3. verify the following report is displayed    """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03: Verify column titles")
        time.sleep(4)
        
        """    4. Select "Home" > "File" button    """
        ribbonobj.select_ribbon_item("Home", "File")
        
        """    5. Save with Default file name "File1"    """
        """    6. File type as Binary(*.ftm)    """
        """    7. Click Save    """
        utillobj.ibfs_save_as("File1", "Binary (*.ftm)")
        
        """    8. Notice "Create Report" button at the bottom of report    """
        btn_css='#createFromHoldButton #createFromHoldMenuBtn'
        bol=driver.find_element_by_css_selector(btn_css).is_displayed()
        utillobj.asequal(True, bol, "Step 08: Verify 'Create Report' button at the bottom of report ")
        
        """    9. Click on the Create Report to create hold report    """
        ia_resultobj.create_hold_type("Create Report")
        
        """    10. Double click "COUNTRY", "CAR", "DEALER_COST".    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        
        """    11. Verify the Query pane and the following report is displayed.    """
        metaobj.verify_query_pane_field("Sum", "DEALER_COST", 1, "Step 11a: ")
        metaobj.verify_query_pane_field("By", "COUNTRY", 1, "Step 11b: ")
        metaobj.verify_query_pane_field("By", "CAR", 2, "Step 11c: ")
        
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 11d: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_2", 10, 3, "C2227549_Ds01.xlsx", "Step 11e: verify data set")
        time.sleep(4)
        
        
        """    12. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(2)
        
        """    13. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227549_Ds02.xlsx", "Step 13a: verify data set")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    14. Click "IA" > "Save".    """
        """    15. Enter Title = "C2227549".    """
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
        elem1=(By.CSS_SELECTOR, "#TableChart_2")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    19. Verify Canvas    """
        coln_list = ['COUNTRY', 'CAR' ,'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 19a: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_2", 10, 3, "C2227549_Ds01.xlsx", "Step 19b: verify data set")
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
