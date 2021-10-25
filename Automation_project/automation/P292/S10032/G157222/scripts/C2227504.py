'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227504
TestCase Name = Verify simple join, save and restore fex 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2227504_TestClass(BaseTestCase):

    def test_C2227504(self):
        
        Test_Case_ID = "C2227504"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 60)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > "OK".    """
        ia_ribbonobj.create_join("ibisamp", "training")
        
        """    4. Verify the following is displayed in the "Join" window.    """
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 04a: Verify join created successfully")
        
        """    5. Click "OK".    """
        join_btn=driver.find_element_by_css_selector("#dlgJoin_btnOK img")
        utillobj.default_left_click(object_locator=join_btn)
        time.sleep(5)
         
        """    6. Double click "LASTNAME", "COURSECODE", "EXPENSES".    """
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Measures/Properties->EXPENSES", 2, 1)
        time.sleep(4)       
        
        """    7 . verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 07: Verify column titles")
        time.sleep(4)
        
        """    8. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        
        """    9. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227504_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227504_Ds01.xlsx", "Step 9a: verify data set")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    10. Close the output window    """
        """    11. Click "IA" > "Save".    """
        """    12. Enter Title = "C2227504".    """
        """    13. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    15. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        preview = (By.CSS_SELECTOR,'#TableChart_1')
        resultobj._validate_page(preview)
        time.sleep(10)
        
        """    16. Verify Canvas    """
        coln_list = ["LASTNAME", "COURSECODE", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2227504_Ds02.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227504_Ds02.xlsx", "Step 16b: verify data set")
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
