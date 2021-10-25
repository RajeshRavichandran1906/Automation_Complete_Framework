'''
Created on 21-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227514
TestCase Name = Verify single-select Dynamic Filter using Define from master
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227514_TestClass(BaseTestCase):

    def test_C2227514(self):
        
        Test_Case_ID = "C2227514"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with EMDPATA, Report mode:
        """
        utillobj.infoassist_api_login('report','ibisamp/EMPDATA','P137/S7385', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """
        2. Double click "LASTNAME", "AREA", "SALARY".
        """
        time.sleep(4)
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("AREA", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(4)
        
        """
        3. Verify the following report is displayed.
        """
        coln_list = ['LASTNAME', 'AREA', 'SALARY']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 41,3,'C2227514_Ds01.xlsx',"Step 03: Verify report data set")        
        
        """
        4. Drag "AREA" to Filter pane.
        """      
        metaobj.drag_drop_data_tree_items_to_filter("AREA", 1)   
        time.sleep(1)

        """
        5. Double-click <Value>, Select Type = "Parameter".
        6. Select "Dynamic" radio button.
        7. Select "Area" field
        8. Click "OK" (2x).
        """
        ia_ribbonobj.create_parameter_filter_condition('Dynamic', ['AREA'])
        
        """
        9. Verify the following is displayed in the "Filter" pane.
        """
        metaobj.verify_filter_pane_field('AREA Equal to Dynamic Parameter (Name: AREA, Field: AREA in EMPDATA)', 1, "Step 09: Verify the filter pane")
        
        """
        10. Click "Run".
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        11. Verify the following autoprompt (AREA = CENTRAL) is displayed.
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.verify_default_amper_value('AREA','CENTRAL',"Step 11: Verify Defualt amper value CENTRAL in run window")
        
        """
        12. Select "CORPORATE" from "AREA" (dropdown).
        """
        time.sleep(2)
        iarun.select_amper_value('AREA', ['CORPORATE'],False)
        time.sleep(4)
        
        """
        13. Click "Run" in the Output window.
        """
        iarun.select_amper_menu('Run')
        
        """
        14. Verify Output window displayed the appropriate "CORPORATE" data.
        """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227514_Ds02.xlsx", "Step 14: verify data set")
        
        """
        15. Click "IA" > "Save" > "C2227514" > click Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        16. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        17. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227514.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit('C2227514', 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """
        18. Verify Filter pane
        """
        metaobj.verify_filter_pane_field('AREA Equal to Dynamic Parameter (Name: AREA, Field: AREA in ibisamp/EMPDATA)', 1, "Step 18: Verify the filter pane")
        
        """
        19. Logout
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()
        