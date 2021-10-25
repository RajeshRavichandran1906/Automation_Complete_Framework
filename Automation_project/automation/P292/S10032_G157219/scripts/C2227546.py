'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227546
TestCase Name = Verify Auto Link Targets with multiple drill downs
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227546_TestClass(BaseTestCase):

    def test_C2227546(self):
        #Test_Case_ID = "C2227546"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Reopen fex AUTOLINK_SOURCE01 using IA API:    """
        utillobj.infoassist_api_edit("AUTOLINK_SOURCE01", "report", "S7385")
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """    2. Select Format Tab > Verify "Enable Auto Linking" is enabled.    """
        ribbonobj.switch_ia_tab("Format")
        time.sleep(3)
        oVerify="tool-bar-button-checked" in driver.find_element_by_id("FormatEnableAutoLink").get_attribute("class")
        utillobj.asequal(True, oVerify, "Step 02a: Verify 'Enable Auto Linking' is enabled")
        
        """    3. Click field "MODEL", click "Drill Down" on the Ribbon    """
        metaobj.querytree_field_click("MODEL", 1)
        time.sleep(15)
        #driver.find_element_by_css_selector("#FieldDrillDown img").click()
        dd_btn=driver.find_element_by_css_selector("#FieldDrillDown img")
        utillobj.default_left_click(object_locator=dd_btn)
        time.sleep(10)
        
        """    4. Click "Browse", select "AUTOLINK_TARGET01", click "Open"    """
        """    5. Remove default name in the "Description" area -> Type "Drill down to Report"    """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name="AUTOLINK_TARGET01",set_description="Drill down to Report")
        
        """    6. Click "Create a new drill down" icon    """
        new_btn=driver.find_element_by_css_selector("#drillDownNew img")
        utillobj.default_left_click(object_locator=new_btn)
        time.sleep(3)
        
        """    7. Click "Web Page" option, click URL input box.    """
        """    8. Type http://www.ibi.com    """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com")
        
        """    9. Click "Create a new drill down" icon    """
        new_btn=driver.find_element_by_css_selector("#drillDownNew")
        utillobj.default_left_click(object_locator=new_btn)
        time.sleep(3)
        
        """    10. Click "Web Page" option, click URL input box    """
        """    11. Type http://www.google.com    """
        """    12. Click OK    """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.google.com", click_ok='yes')
        
        """    13. Verify the hyperlink is applied on Live preview    """
        ia_resultobj.verify_autolink("TableChart_1","2000 4 DOOR BERLINA",18,"Step 13a: Verify Auto Drill applied in 2000 4 DOOR BERLINA") 
 
        """    14. Click "Save" > verify save message > click OK    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("AUTOLINK_SOURCE01_a")
        time.sleep(5)
        
        """    15. Click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        time.sleep(8)
        utillobj.switch_to_frame(pause=1)
        time.sleep(3) 
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227546_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227546_Ds01.xlsx", "Step 15a: verify data set")
        
        """    16. Click value "2000 GT VELOCE", verify menu for multi-drill and auto link targets    """
        iarun.verify_autolink_tooltip_values("table[summary='Summary']", 3, 2, ['Drill down to Report', 'Drill Down 2', 'Drill Down 3', 'Auto Links'], "Step 16a: Verify menu for Multi-drill and Autolink targets",browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7)
        
        """    17. Hover over Auto Links -> select the auto link target "AUTOLINK_TARGET01" -> verify output    """
        #iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 3,2, "Auto Links->AUTOLINK_TARGET01", "Step 17a: verify ONLY 'AUTOLINK_TARGET01' fex is listed", browser_height=80, x_offset=x_fr, y_offset=y_fr-7)
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 3,2, "Auto Links->AUTOLINK_TARGET01", "Step 17a: verify ONLY 'AUTOLINK_TARGET01' fex is listed", browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 3,2, "Auto Links->AUTOLINK_TARGET01")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227546_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227546_Ds02.xlsx", "Step 17b: verify Output")
        
        """    18. Close output window for selected "AUTOLINK_TARGET01" target    """
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(pause=1)
        time.sleep(3) 
        
        """    19. Click value "2002 2 DOOR" in the initial output window    """
        """    20. Select "Drill down to Report" -> verify output    """
        #iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Drill down to Report", "Step 17a: Click value '2002 2 DOOR'", browser_height=80, x_offset=x_fr, y_offset=y_fr-7)
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 6,2, "Drill down to Report", "Step 17a: Click value '2002 2 DOOR'", browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,2, "Drill down to Report")
        utillobj.switch_to_default_content(pause=1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        expected_plist=['Close Filter Panel', 'Reset filter values', 'Save current values', 'Run with filter values']
        plist=[]
        prompt=driver.find_elements_by_css_selector("#promptPanel div>a")
        for i in range(len(prompt)):
            plist.append(prompt[i].get_attribute("title"))
        utillobj.asequal(plist, expected_plist, "step 20a: Verify autoprompt navigation buttons")
        arprompt=driver.find_element_by_css_selector("#promptPanel > div > div > div[class^='autop-amper'] > div > div").get_attribute("title")
        utillobj.asin("CAR", arprompt, "Step 20b: verify the field name")
                
        """    21. Close the output window for the selected drill Report    """
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        utillobj.switch_to_frame(pause=1)
        time.sleep(3) 
        
        """    22. Click value "2000 GT VELOCE" -> select "Drill Down3"    """
        #iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 3,2, "Drill Down 3", "Step 22a: Click value '2002 2 DOOR'", browser_height=80, x_offset=x_fr, y_offset=y_fr-7)
        #iarun.select_report_autolink_tooltip_menu("table[summary= 'Summary']", 3,2, "Drill Down 3", "Step 22a: Click value '2002 2 DOOR'", browser_height=80, x_offset=x_fr+10, y_offset=y_fr-7, x_offset_menu=x_fr+5, y_offset_menu=y_fr-7)
        iarun.select_report_autolink_tooltip_menu_pyautogui("table[summary= 'Summary']", 6,2, "Drill Down 3")
        time.sleep(5)
        
        """    23. Verify google page is displayed - https://www.google.com/    """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        owebpage=driver.title
        utillobj.asequal("Google", owebpage, "Step 23a: Verify Google page isdisplayed")
        
        """    24. Close the web page, close the output window    """
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        
        """    25. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
    
