'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227544
TestCase Name = Enable Auto Link and verify available Auto Link Targets from IA and repository tree
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon, wf_mainpage, wf_legacymainpage
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227544_TestClass(BaseTestCase):

    def test_C2227544(self):
        
        #Test_Case_ID = "C2227544"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        mainpage=wf_mainpage.Wf_Mainpage(self.driver)
        legacyobj=wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    2. Double click "CAR","MODEL","DEALER_COST".    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("MODEL", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        coln_list = ["CAR", "MODEL", "DEALER_COST"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02a: Verify column titles")
        time.sleep(4)
         
        """    3. Drag and drop "CAR" to Filter Pane    """
        metaobj.datatree_field_click("CAR", 1, 1, 'Filter')
        time.sleep(4)
         
        """    4. Double-click <Value>, select Type "Parameter", click ok, ok    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
         
        """    5. Drag and drop "MODEL" to Filter Pane    """
        metaobj.datatree_field_click("MODEL", 1, 1, 'Filter')
        time.sleep(4)
         
        """    6. Double-click <Value>, select Type "Parameter", click ok, ok    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple',rownum=3)
        metaobj.verify_filter_pane_field('CAR Equal to Simple Parameter (Name: CAR)', 1, "Step 06a")
        metaobj.verify_filter_pane_field('MODEL Equal to Simple Parameter (Name: MODEL)', 2, "Step 06b")
         
        """    7. Select Format Tab -> Click "Auto Link Target"    """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
         
        """    8. Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_TARGET01", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("AUTOLINK_TARGET01")
        time.sleep(5)
        
        """    9. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    10. Launch the IA API with WF_RETAIL_LITE, Chart mode:    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    11. Double click "CAR","MODEL","SALES"    """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("MODEL", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        
        """    12. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        
        """    13. Click "IA" > "Save" > Enter "Title:" = "AUTOLINK_SOURCE01", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("AUTOLINK_SOURCE01")
        time.sleep(5)
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        '''iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        time.sleep(8)'''
        
        """    15. Verify output with hyperlinks on field "MODEL" ONLY    """
        utillobj.switch_to_frame(pause=1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(5)     
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227544_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds01.xlsx", "Step 15a: verify data set")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 GT VELOCE", 3,2,18,"Step 15")
        
        """    16. Click value "2002 2 DOOR", verify "AUTOLINK_TARGET01" fex is listed    """
        """    17. Hover over and select "AUTOLINK_TARGET01"    """
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",6,2,'Auto Links->AUTOLINK_TARGET01', "Step 17a:", x_offset_menu=20, y_offset_menu=7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01", "Step 17a: verify 'AUTOLINK_TARGET01' fex is listed", browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        time.sleep(10)
        utillobj.switch_to_default_content(pause=1)
        #driver.switch_to.default_content()
        time.sleep(8)
        utillobj.switch_to_window(1)
        #driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
         
        """    18. Verify output.    """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds02.xlsx", "Step 18a: verify Output")
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
          
        """    20. Logon to WF and expand Repository folder > "S7385"    """
        """    21. Highlight "AUTOLINK_SOURCE01" > Right mouse click > "Properties" > Verify "Enable Auto Linking" checkbox is enabled > click "Cancel".    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#bipTreePanel #treeView")
        resultobj._validate_page(elem1)
        time.sleep(15)
        project_id=utillobj.parseinitfile('project_id')
        folder = utillobj.parseinitfile('suite_id')
        legacyobj.select_repository_menu(project_id + "->" + folder + "->" + "AUTOLINK_SOURCE01", "Properties")
        #mainpage.select_repository_menu('P137->S7385->AUTOLINK_SOURCE01', 'Properties')
        mainpage.select_or_verify_properties_flaglist('enable_auto_link',check=True, msg='Step 21a: verify Enable Auto Linking checkbox is enabled')
        #driver.find_element_by_css_selector("#btnCancel img").click()
        cancel_btn=driver.find_element_by_css_selector("#btnCancel img")
        utillobj.default_left_click(object_locator=cancel_btn)
        time.sleep(4)            
        
        """    22. Highlight "AUTOLINK_TARGET01" > Right mouse click > "Properties" > Verify "Auto Link Target" checkbox is enabled > click "Cancel".    """
        legacyobj.select_repository_menu('AUTOLINK_TARGET01', 'Properties')
        legacyobj.select_or_verify_properties_flaglist('auto_link_target',check=True, msg='Step 22a: verify auto_link_target checkbox is enabled')
        cancel_btn=driver.find_element_by_css_selector("#btnCancel img")
        utillobj.default_left_click(object_locator=cancel_btn)
        time.sleep(4)
        
        """    23. Highlight "AUTOLINK_SOURCE01" > Right mouse click > "Run".    """
        legacyobj.select_repository_menu('AUTOLINK_SOURCE01', 'Run')
        time.sleep(4)
        utillobj.switch_to_window(1)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
          
        """    24. Verify output with hyperlinks on field "MODEL" ONLY.    """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds01.xlsx", "Step 24a: verify data set")
        iarun.verify_autolink("table[summary= 'Summary']", "2000 GT VELOCE", 3,2,18,"Step 24")
          
        """    25. Click value "2002 2 DOOR", verify "AUTOLINK_TARGET01" fex is listed    """
        """    26. Hover over and select "AUTOLINK_TARGET01".    """
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01")
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",6,2,'Auto Links->AUTOLINK_TARGET01', "Step 17a:", x_offset_menu=20, y_offset_menu=7)
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Auto Links->AUTOLINK_TARGET01", "Step 26a: verify 'AUTOLINK_TARGET01' fex is listed",browser_height=45, x_offset=10, y_offset=5)
        
        """"s = driver.find_element_by_css_selector("#ui-id-1")
        s.click()
        s2= driver.find_element_by_css_selector("#ui-id-2")
        s2.click()"""
        time.sleep(10)
        utillobj.switch_to_window(2)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(8)
          
        """    27. Verify output.    """
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227544_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227544_Ds03.xlsx", "Step 27a: verify Output")
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(1)
        time.sleep(1)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(4)        
          
        """    28. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
          

        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
