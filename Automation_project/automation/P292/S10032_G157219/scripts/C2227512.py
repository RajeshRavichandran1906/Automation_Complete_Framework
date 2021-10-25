'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227512
TestCase Name = Verify request with a Define field 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, define_compute, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227512_TestClass(BaseTestCase):

    def test_C2227512(self):
        
        Test_Case_ID = "C2227512"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
         
        """    2. Double click "CAR"    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)        
        
        """    3. Select Data Tab > Click Define    """
        defcomp.invoke_define_compute_dialog('define')
        
        """    4. Enter Field = "DEFSALES".    """
        """    5. Double click "Sales" > "OK".    """
        defcomp.enter_define_compute_parameter("DEFSALES", 'D12.2', 'SALES', 1)
        defcomp.close_define_compute_dialog('ok')
        
        """    6. Scroll down on Data pane and verify that "DEFSALES" has been added to "Measures".    """
        metaobj.verify_data_pane_field("Measures/Properties", "DEFSALES", 15, "Step 6a: ")
        
        """    7. Double click "DEFSALES".    """
        metaobj.datatree_field_click("DEFSALES", 2, 1)
        time.sleep(4)

        """    8. Verify "DEFSALES" field is displayed in "Live Preview".   """
        coln_list = ['CAR', 'DEFSALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08: Verify column titles")
        time.sleep(4)
        
        """    9. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    10. Verify the report is displayed.    """
        """    11. Close the output window    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227512_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227512_Ds01.xlsx", "Step 11a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    12. Click "IA" > "Save" > C2227512 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    13. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    14. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    15. Verify Canvas    """
        coln_list = ['CAR', 'DEFSALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 15: Verify column titles")
        time.sleep(4)
        
        """    16. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


       
        
