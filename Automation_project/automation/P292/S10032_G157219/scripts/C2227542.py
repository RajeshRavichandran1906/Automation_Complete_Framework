'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227542
TestCase Name = Verify converting joined Report with Filter to Chart mode
'''
import unittest, pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227542_TestClass(BaseTestCase):

    def test_C2227542(self):
        
        Test_Case_ID = "C2227542"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch the IA API with EMPDATA, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > OPEN > "OK".    """
        ia_ribbonobj.create_join("training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03a: Verify join created successfully")
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(5)
         
        """    4. Double click "LASTNAME", "LOCATION", "EXPENSES".    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("LOCATION", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(4)       
        
        """    5 . verify the following report is displayed    """
        coln_list = ["LASTNAME", "LOCATION", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 05a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2227542_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 30,3,'C2227542_Ds01.xlsx',"Step 05b: Verify report data set")
        
        """    6. Drag "EXPENSES" TO Filter pane.    """
        metaobj.datatree_field_click("EXPENSES", 1, 1, 'Filter')
        
        """    7. Double click "Equal To".    """
        """    8. Select "Greater than" option.    """
        ia_ribbonobj.select_condition_in_filter_dialog(2, "Greater than")
        
        """    9. Double click <Value>.    """
        condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class*='selected']>span>span")
        condition_elem[len(condition_elem)-1].click()
        browser=utillobj.parseinitfile('browser')
        browser_height=75
        if browser=='Firefox':
            x_fr=condition_elem[len(condition_elem)-1].location["x"]
            y_fr=condition_elem[len(condition_elem)-1].location["y"]
            pyautogui.moveTo(x_fr+20,y_fr+browser_height)
            time.sleep(2)
            pyautogui.doubleClick(x_fr+20,y_fr+browser_height,button='left')
        else:
            action1 = ActionChains(self.driver)
            action1.double_click(condition_elem[len(condition_elem)-1]).perform()
            del action1
        
        """    10. Enter Value = "3000".    """
        driver.find_element_by_css_selector("#dlgWhereValue #id_wv_text_value").click()
        time.sleep(5)
        driver.find_element_by_css_selector("#dlgWhereValue #id_wv_text_value").send_keys("3000")
        time.sleep(5)
        
        """    11. Click "OK" (2x).    """
        ok_btn=driver.find_element_by_css_selector("#wndWhereValuePopup_btnOK")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(5)
        ia_ribbonobj.close_filter_dialog(btn='Ok')
        time.sleep(5)
        
        """    12. Verify report displays LASTNAME > 3000 in "Live Preview".    """
        coln_list = ["LASTNAME", "LOCATION", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 11a: Verify column titles")
        time.sleep(4)
        #ia_resultobj.create_report_data_set('TableChart_1', 10,3,'C2227542_Ds02.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10,3,'C2227542_Ds02.xlsx',"Step 11b: Verify report data set")
        
        """    13. Verify "Filter" pane has the following expression.    """
        metaobj.verify_filter_pane_field('EXPENSES Greater than 3000', 1, "Step 12: Verify the filter pane")
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        
        """    15. Verify report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227542_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227542_Ds03.xlsx", "Step 15a: verify data set")
        
        """    16. Dismiss Run output window.    """
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    17. Select "Home" > "Chart".    """
        ribbonobj.select_ribbon_item('Home', 'Chart')
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    18. Verify chart is displayed in "Live Preview".    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 18a: Verify the total number of risers displayed on preview Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 18b: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 18c(i): Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 18d(i): Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 18d(ii): Verify Y-Axis Title")
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        time.sleep(10)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227542_Actual_step19', image_type='actual',x=1, y=1, w=-1, h=-1)
        iframe=driver.find_element_by_css_selector("[id^=ReportIframe-]")
        x_fr=iframe.location["x"]
        y_fr=iframe.location["y"]
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    20. Verify chart is displayed.    """
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step 20a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 20b: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue1", "Step 20c(i): Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 20d(i): Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 20d(ii): Verify Y-Axis Title")
        expected_tooltip=['LASTNAME:ELLNER', 'LOCATION:IA', 'EXPENSES:3,350.00']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g4!mbar",expected_tooltip, "Step 20e: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-8)
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    21. Save Chart: Click "IA" > "Save" > "C2227542" > Click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    22. Click "IA" > "Close"    """
        ribbonobj.select_tool_menu_item('menu_close')
         
        """    23. Save Report: Click "IA" > "Save As" > "C2227542_1" > Click Save    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID + '_1')
        time.sleep(5)
        
        """    24. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    25. Reopen Chart fex using IA API:     """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S7385')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    26. Verify "Live Preview".    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 26a: Verify the total number of risers displayed on preview Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 26b: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 26c(i): Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 26d(i): Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 26d(ii): Verify Y-Axis Title")
        
        """    27. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
