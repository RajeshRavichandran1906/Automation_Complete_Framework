'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227511
TestCase Name = Verify Define based on a joined field 
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

class C2227511_TestClass(BaseTestCase):

    def test_C2227511(self):
        
        Test_Case_ID = "C2227511"
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
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
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
        
        """    6. Select Data Tab > Click Define    """
        defcomp.invoke_define_compute_dialog('define')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """    7. Type ID for Field name, I9 for Format, double-click "ID Vendor"    """
        defcomp.enter_define_compute_parameter("JOINDEFEXPENSES", 'D12.2', 'EXPENSES', 1)
        
        """    8. Click OK to create define field    """
        defcomp.close_define_compute_dialog('ok')
        
        """    9. Double click "JOINDEFEXPENSES"    """
        metaobj.datatree_field_click("JOINDEFEXPENSES", 2, 1)
        time.sleep(4)
        
        """    10. verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 10a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227511_Ds01.xlsx", "Step 10b: verify preview data")  
        
        """    11. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    12. Verify the report is displayed.    """
        """    13. Close the output window    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227511_Ds02.xlsx", "Step 13a: verify data set")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    14. Click "IA" > "Save" > C2227511 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    16. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    17. Verify Canvas    """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 17a: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227511_Ds01.xlsx", "Step 17b: verify preview data") 
        
        """    18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
