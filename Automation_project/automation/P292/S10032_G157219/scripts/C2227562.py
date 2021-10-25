'''
Created on 17-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227562
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227562_TestClass(BaseTestCase):

    def test_C2227562(self):
        
        Test_Case_ID = "C2227562"
        driver = self.driver
        driver.implicitly_wait(20)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
                
        """
        1. Launch the IA API with CAROLAP, Report mode:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAROLAP&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('report','ibisamp/CAROLAP','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "DEALER_COST".
        """
        time.sleep(4) 
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4) 
        
        """
        Step 03: Expand COUNTRY Dimension -> double-click "COUNTRY".
        """
        time.sleep(4) 
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4) 
        
        """
        Step 04: Select "Format" > "Auto Drill" button.
        """
        ribbonobj.select_ribbon_item('Format', 'Auto_Drill') 
        
        """
        Step 05: Click "Run"
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        
        """
        Step 06: Verify Auto Drill links displayed for COUNTRY
        """
        utillobj.switch_to_frame(pause=1)
        '''WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe"]')))
        time.sleep(3)'''
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        #utillobj.switch_to_frame(pause=2, frame_css='iframe[src]')
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","ENGLAND",2,1,5,"Step 06: Verify Auto Drill applied in value ENGLAND")
        time.sleep(2)        
        
        """
        Step 07: Click value "ENGLAND"
        Step 08: Verify auto drill menu is displayed with option "Drill Down to CAR"
        """
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",2,1,['Drill down to CAR'], "Step 07: Verify the Auto Drill menu for ENGLAND")
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",2,1,['Drill down to CAR'], "Step 07: Verify the Auto Drill menu for ENGLAND",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        time.sleep(2)
        
        """
        Step 09: Select "Drill Down to CAR", Verify Report
        """        
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",2,1,['Drill down to CAR'], "Step 07: Verify the Auto Drill menu for ENGLAND",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",2,1, 'Drill down to CAR', "Step 07: Verify the Auto Drill menu for ENGLAND")
        time.sleep(5)
        iarun.verify_autolink("table[summary='Summary']","JAGUAR",4,1,4,"Step 09.2: Verify Auto Drill applied in value JAGUAR")
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227562_Ds01.xlsx", "Step 09.3: verify Auto Drill, drill down data set")
        
        """
        Step 10: Click "JAGUAR", Verify menu
        """        
        time.sleep(2)
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,['Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL'], "Step 10: Verify the Auto Drill menu for JAGUAR")
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,['Restore Original', 'Drill up to COUNTRY', 'Drill down to MODEL'], "Step 10: Verify the Auto Drill menu for JAGUAR",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        time.sleep(2)
        
        """
        Step 11: Select "Drill Down to MODEL", Verify Report
        """
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to MODEL', "Step 11.1: Select the Auto Drill menu, Drill down to MODEL",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to MODEL', "Step 11.1: Select the Auto Drill menu, Drill down to MODEL")
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","V12XKE AUTO",4,1,4,"Step 11.2: Verify Auto Drill applied in value V12XKE AUTO")
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227562_Ds02.xlsx", "Step 11.3: verify Auto Drill, drill down data set")
        
        """
        Step 12: Click "V12XKE AUTO", Verify menu
        """
        time.sleep(3)
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,['Restore Original', 'Drill up to CAR'], "Step 12: Verify the Auto Drill menu for V12XKE AUTO",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,['Restore Original', 'Drill up to CAR'], "Step 12: Verify the Auto Drill menu for V12XKE AUTO")
        time.sleep(2)
        
        """
        Step 13: Select "Drill Up to CAR", Verify Report
        """
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill up to CAR', "Step 13.1: Select the Auto Drill menu, Drill up to CAR")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill up to CAR', "Step 13.1: Select the Auto Drill menu, Drill up to CAR",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","JAGUAR",4,1,4,"Step 13.2: Verify Auto Drill applied in value JAGUAR")
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227562_Ds03.xlsx", "Step 13.3: verify Auto Drill, drill down data set")
        
        """
        Step 14: Click "TRIUMPH" > Select "Restore Original"
        """
        time.sleep(2)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",6,1,'Restore Original', "Step 14: Select the Auto Drill menu, Restore Original")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",6,1,'Restore Original', "Step 14: Select the Auto Drill menu, Restore Original",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        time.sleep(3)
        
        """
        Step 15: Verify the following Report
        """
        iarun.verify_autolink("table[summary='Summary']","ENGLAND",2,1,5,"Step 15.1: Verify Auto Drill applied in value ENGLAND")
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227562_Ds04.xlsx", "Step 15.2: verify Auto Drill, drill down data set")
        utillobj.switch_to_default_content(pause=1)
        """
        Step 16: Click "IA" > "Save As" > Enter Title = "C2227562" > Click "Save".
        """
        #driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)        
        
        """
        Step 17: Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 18: Reopen fex using IA API:
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step 19: Select "Format" > verify "Auto Drill" button is selected
        """
        ribbonobj.switch_ia_tab('Format')
        selected=self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute("class")
        utillobj.asin("tool-bar-button-checked",selected,"Step 19: Verify Auto Drill Button is selected")
        
        """
        Step 20: Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        

if __name__ == "__main__":
    unittest.main()
        
        
        
        
                  
    