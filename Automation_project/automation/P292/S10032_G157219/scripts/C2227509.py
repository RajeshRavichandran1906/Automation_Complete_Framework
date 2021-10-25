'''
Created on 20-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227509
TestCase Name = Verify Compute based on a joined field 
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

class C2227509_TestClass(BaseTestCase):

    def test_C2227509(self):
        
        Test_Case_ID = "C2227509"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > Open > "OK".    """
        ia_ribbonobj.create_join("training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03a: Verify join link color")
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)
        
        """    4. Double click "LASTNAME", "COURSECODE"    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("COURSECODE", 2, 1)
        time.sleep(4)   
        
        """    5. verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 05a: Verify column titles")
        
        """    6. Select Data Tab > Click Compute    """
        defcomp.invoke_define_compute_dialog('compute')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """    7. Enter Field = "NEWEXPENSES"    """
        """    8. Double click "EXPENSES" > "OK".    """
        defcomp.enter_define_compute_parameter("NEWEXPENSES", 'D12.2', 'EXPENSES', 1)
        defcomp.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """    9. Verify "NEWEXPENSES" field is displayed in "Live Preview".    """
        coln_list = ["LASTNAME", "COURSECODE", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 9a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227509_Ds01.xlsx", "Step 9b: verify preview data")
        #ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2068465_Ds01.xlsx", "Step 9b: verify preview data")   
        
        """    10. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    11. Verify the report is displayed.    """
        """    12. Close the output window    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227509_Ds02.xlsx", "Step 12a: verify data set")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    13. Click "IA" > "Save" > C2227509 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    15. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    16. Verify Canvas    """
        coln_list = ["LASTNAME", "COURSECODE", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227509_Ds01.xlsx", "Step 16b: verify preview data") 
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
