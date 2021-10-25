'''
Created on 17-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227562
'''
import unittest, time
from common.lib import utillity, core_utility 
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon, ia_run, metadata

class C2227562_TestClass(BaseTestCase):

    def test_C2227562(self):
        
        Test_Case_ID = "C2227562"
        
        driver = self.driver
        iarun=ia_run.IA_Run(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
              
        """
        1. Launch the IA API with CAROLAP, Report mode:
        http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAROLAP&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('report','ibisamp/carolap','P137/S7385', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02: Double click "DEALER_COST".
        """
        time.sleep(4) 
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4) 
        
        """
        Step 03: Expand COUNTRY Dimension -> double-click "COUNTRY".
        """
        metadataobj.double_click_on_data_filed('COUNTRY->COUNTRY->COUNTRY', 3)
        time.sleep(10) 
        
        """
        Step 04: Select "Format" > "Auto Drill" button.
        """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(2)
        ribbon_item=driver.find_element_by_css_selector("#FormatAutoDrill img")
        utillobj.default_left_click(object_locator=ribbon_item)
        
        """
        Step 05: Click "Run"
        """
        app_css = "#applicationButton img"
        utillobj.synchronize_with_number_of_element(app_css, 1, 30)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        core_utils.switch_to_frame()
      
        """
        Step 06: Verify Auto Drill links displayed for COUNTRY
        """
        time.sleep(3)
        core_utils.switch_to_frame(frame_css='iframe[src]')
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
        time.sleep(10)
        
        """
        Step 11: Select "Drill Down to MODEL", Verify Report
        """
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to MODEL', "Step 11.1: Select the Auto Drill menu, Drill down to MODEL",browser_height=80, x_offset=x_fr, y_offset=y_fr-8)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to MODEL', "Step 11.1: Select the Auto Drill menu, Drill down to MODEL")
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","V12XKE AUTO",4,1,4,"Step 11.2: Verify Auto Drill applied in value V12XKE AUTO")
        time.sleep(10)
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
        time.sleep(10)
        
        """
        Step 15: Verify the following Report
        """
        iarun.verify_autolink("table[summary='Summary']","ENGLAND",2,1,5,"Step 15.1: Verify Auto Drill applied in value ENGLAND")
        time.sleep(10)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227562_Ds04.xlsx", "Step 15.2: verify Auto Drill, drill down data set")
        utillobj.switch_to_default_content(pause=1)
        
        """
        Step 16: Click "IA" > "Save As" > Enter Title = "C2227562" > Click "Save".
        """
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
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 19: Select "Format" > verify "Auto Drill" button is selected
        """
        ribbonobj.switch_ia_tab('Format')
        selected=self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute("class")
        utillobj.asin("tool-bar-button-checked",selected,"Step 19: Verify Auto Drill Button is selected")
        
        """
        Step 20: Logout:
        """
       
if __name__ == "__main__":
    unittest.main()