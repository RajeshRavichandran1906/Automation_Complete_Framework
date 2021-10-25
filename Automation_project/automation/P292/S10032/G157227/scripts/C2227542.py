'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227542
TestCase Name = Verify converting joined Report with Filter to Chart mode
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.wftools import visualization
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.report import Report
from common.lib.core_utility import CoreUtillityMethods

class C2227542_TestClass(BaseTestCase):

    def test_C2227542(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = "C2227542"
        
        """ TESTCASE OBJECTS """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        visual_obj = visualization.Visualization(driver)
        report = Report(self.driver)
        core_utility = CoreUtillityMethods(self.driver)
        
        """ Testcase css"""
        qwery_css = "#queryBoxColumn"
        cancel_css = "#dlgWhere_btnCancel"
        
        """    1. Launch the IA API with EMPDATA, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P292/S10032_infoassist_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > OPEN > "OK".    """
        ia_ribbonobj.create_join("ibisamp", "training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03.01: Verify join created successfully")
        ok_button  = driver.find_element_by_css_selector("#dlgJoin_btnOK")
        core_utility.left_click(ok_button)
        time.sleep(5)
         
        """    4. Double click "LASTNAME", "LOCATION", "EXPENSES".    """
        report.double_click_on_datetree_item("LASTNAME", 1)
        report.wait_for_visible_text(qwery_css, "LASTNAME")
        
        metaobj.datatree_field_click("Dimensions->LOCATION", 2, 1)
        report.wait_for_visible_text(qwery_css, "LOCATION")
        
        report.double_click_on_datetree_item("EXPENSES", 1)
        report.wait_for_visible_text(qwery_css, "EXPENSES")
        
        """    5 . verify the following report is displayed    """
        coln_list = ["LASTNAME", "LOCATION", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 05.01: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2227542_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 30,3,'C2227542_Ds01.xlsx',"Step 05.02: Verify report data set")
        time.sleep(8)
        
        """    6. Drag "EXPENSES" TO Filter pane.    """
        visual_obj.drag_and_drop_from_data_tree_to_filter('EXPENSES', 1)
        report.wait_for_visible_text(cancel_css, "Cancel")
        
        """    7. Double click "Equal To".    """
        """    8. Select "Greater than" option.    """
        equal_to_obj = utillobj.validate_and_get_webdriver_object("#dlgWhereWhereTree > div.bi-tree-view-body-content > table > tbody > tr:nth-child(2) > td > span > span > span:nth-child(2)", "Equal to css")
        core_utility.python_doubble_click(equal_to_obj)
        time.sleep(5)
        
        arrow_button_obj = utillobj.validate_and_get_webdriver_object("div[id*='InlineControlOperator'] div[class='bi-component combo-box-arrow']", "Arrow button css")
        core_utility.python_left_click(arrow_button_obj)
        report.wait_for_visible_text("#wndWhereOperatorPopup_list", "Equal to")
        
        greater_than_obj = utillobj.validate_and_get_webdriver_object("#wndWhereOperatorPopup_list div[id*='BiListItem']:nth-child(3)", "Greater than")
        core_utility.python_doubble_click(greater_than_obj)
        time.sleep(5)
        
        """    9. Double click <Value>.    """
        value_obj = utillobj.validate_and_get_webdriver_object("div[id*='InlineControlValue']", "Value button css")
        core_utility.python_doubble_click(value_obj)
        report.wait_for_visible_text("#wndWhereValuePopup_btnCancel", "Cancel")
        
        
        """    10. Enter Value = "3000".    """
        element = driver.find_element_by_css_selector("#dlgWhereValue #id_wv_text_value")
        core_utility.left_click(element)
        time.sleep(5)
        driver.find_element_by_css_selector("#dlgWhereValue #id_wv_text_value").send_keys("3000")
        time.sleep(5)
        
        """    11. Click "OK" (2x).    """
        parent_css="#wndWhereValuePopup_btnOK"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90)
        ok_btn=driver.find_element_by_css_selector("#wndWhereValuePopup_btnOK")
        core_utility.left_click(ok_btn)
        time.sleep(5)
        ia_ribbonobj.close_filter_dialog(btn='Ok')
        time.sleep(5)
        
        """    12. Verify report displays LASTNAME > 3000 in "Live Preview".    """
        coln_list = ["LASTNAME", "LOCATION", "EXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 12.01: Verify column titles")
        time.sleep(4)
        #ia_resultobj.create_report_data_set('TableChart_1', 10,3,'C2227542_Ds02.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 10,3,'C2227542_Ds02.xlsx',"Step 12.02: Verify report data set")
        
        """    13. Verify "Filter" pane has the following expression.    """
        metaobj.verify_filter_pane_field('EXPENSES Greater than 3000', 1, "Step 13.01: Verify the filter pane")
        
        """    14. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        
        """    15. Verify report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227542_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227542_Ds03.xlsx", "Step 15.01: verify data set")
        
        """    16. Dismiss Run output window.    """
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    17. Select "Home" > "Chart".    """
        ribbonobj.select_ribbon_item('Home', 'Chart')
        parent_css="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    18. Verify chart is displayed in "Live Preview".    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 18.01: Verify the total number of risers displayed on preview Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 18.02: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 18.03: Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 18.04: Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 18.05: Verify Y-Axis Title")
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        parent_css="rect[class*='riser!s0!g1!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    20. Verify chart is displayed.    """
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 10, 'Step 20.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 20.02: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mbar!", "bar_blue1", "Step 20.03: Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 20.04: Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 20.05: Verify Y-Axis Title")
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
        utillobj.ibfs_save_as(Test_Case_ID+'_1')
        time.sleep(5)
        
        """    24. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    25. Reopen Chart fex using IA API:     """
        parent_css="input[id=SignonUserName]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032_infoassist_1')
        time.sleep(10)
        parent_css="#TableChart_1 rect[class^='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(10)
        
        """    26. Verify "Live Preview".    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 10, 'Step 26.01: Verify the total number of risers displayed on preview Chart')
        expected_xval_list=['ADAMS : NJ', 'ADDAMS : MI', 'ANDERSON : WA', 'CONTI : MA', 'ELLNER : IA', 'GOTLIEB : MO', 'MEDINA : NJ', 'SO : MA', 'WHITE : CA', 'WHITE : IA']
        expected_yval_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 26.02: ')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 26.03: Verify first bar color")
        xaxis_value="LASTNAME : LOCATION"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 26.04: Verify X-Axis Title")
        yaxis_value="EXPENSES"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 26.05: Verify Y-Axis Title")
        
        """    27. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()