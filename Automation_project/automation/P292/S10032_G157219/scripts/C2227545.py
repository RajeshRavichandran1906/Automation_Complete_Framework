'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227545
TestCase Name = Verify available Auto Link Targets on two different columns
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227545_TestClass(BaseTestCase):

    def test_C2227545(self):
        
        Test_Case_ID = "C2227545"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """    2. Double click "CAR", "RETAIL_COST".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)
        coln_list = ['CAR', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02a: Verify column titles")
        time.sleep(4)
        
        """    3. Drag and drop "CAR" to Filter Pane    """
        metaobj.datatree_field_click("CAR", 1, 1, 'Filter')
        time.sleep(4)
        
        """    4. Double-click <Value>, select Type "Parameter", click ok, ok    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        metaobj.verify_filter_pane_field('CAR Equal to Simple Parameter (Name: CAR)', 1, "Step 04a")
        
        """    5. Select Format Tab -> Click "Auto Link Target"    """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
        
        """    6. Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_TARGET02", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("AUTOLINK_TARGET02")
        time.sleep(5)
        
        """    7. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    8. Launch the IA API with WF_RETAIL_LITE, Chart mode:    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    9. Double click "CAR","MODEL","SALES"    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("MODEL", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        
        """    10. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        
        """    11. Click "IA" > "Save" > Enter "Title:" = "C2227545", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    12. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        time.sleep(4)
        
        """    13. Verify output with hyperlinks on both "CAR", "MODEL".    """
        utillobj.switch_to_frame(pause=1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)     
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227545_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds01.xlsx", "Step 13a: verify data set")
        iarun.verify_autolink("table[summary='Summary']","ALFA ROMEO",2,1,10,"Step 13a: Verify Auto Drill applied in CAR")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 4 DOOR BERLINA", 2,2,18,"Step 13b: Verify Auto Drill applied in MODEL")
        
        """    14. Click value "2002 2 DOOR", verify ONLY "AUTOLINK_TARGET01" fex is listed    """
        """    15. Hover over and select "AUTOLINK_TARGET01" -> Verify output    """
        #iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01", "Step 14a: verify ONLY 'AUTOLINK_TARGET01' fex is listed",browser_height=80, x_offset=x_fr, y_offset=y_fr-7, browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",6,2,'Auto Links->AUTOLINK_TARGET01', "Step 14a:", x_offset_menu=20, y_offset_menu=7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01", "Step 14a: verify 'AUTOLINK_TARGET01' fex is listed")
        utillobj.switch_to_default_content()
        #driver.switch_to.default_content()
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227545_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds02.xlsx", "Step 15a: verify Output")
        
        """    16. Close output window    """
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(pause=1)
        time.sleep(3) 
        
        """    17. Click value "BMW" in the initial output window, verify ONLY "AUTOLINK_TARGET02" is listed    """
        """    18. Hover over and select "AUTOLINK_TARGET02" -> Verify output    """
        #iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 6,1, "Auto Links->AUTOLINK_TARGET02", "Step 17a: verify ONLY 'AUTOLINK_TARGET02' fex is listed",browser_height=80, x_offset=x_fr, y_offset=y_fr-7, , browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",6,2,'Auto Links->AUTOLINK_TARGET01', "Step 17a:", x_offset_menu=20, y_offset_menu=7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,1, "Auto Links->AUTOLINK_TARGET02")
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 6,1, "Auto Links->AUTOLINK_TARGET02", "Step 17a: verify ONLY 'AUTOLINK_TARGET02' fex is listed")
        utillobj.switch_to_default_content()
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227545_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227545_Ds03.xlsx", "Step 18a: verify Output")
        
        """    19. Close output window    """
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        #utillobj.infoassist_api_logout()
        #time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
    
