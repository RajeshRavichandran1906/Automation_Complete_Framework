"""-------------------------------------------------------------------------------------------
Created on June 28, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/9480182
Test Case Title =  Breadcrumbs - Have two hierarchy sorts from different dimensions - Active format
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.report import Report
from selenium.webdriver import ActionChains
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.active_miscelaneous import Active_Miscelaneous 
from common.lib.global_variables import Global_variables

class C9480182_TestClass(BaseTestCase):

    def test_C9480182(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        utils = UtillityMethods(self.driver)
        active_misce = Active_Miscelaneous(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        CASE_ID = "C9480182"
        FEX_FILE = "IA-Shell"
        DATASET1 = CASE_ID + "_DataSet_01.xlsx"
        DATASET2 = CASE_ID + "_DataSet_02.xlsx"
        DATASET3 = CASE_ID + "_DataSet_03.xlsx"
        DATASET4 = CASE_ID + "_DataSet_04.xlsx"
        ACTIVE_TABLE_ID = "ITableData0"
        ACTIVE_TABLE_CSS = "#" + ACTIVE_TABLE_ID
        
        """
            STEP 01 : Reopen the saved fex using API link:
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G784981/IA-Shell.fex&tool=Report
        """
        report.edit_fex_using_api_url(FEX_FILE)
        utils.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report.home_page_long_timesleep)
        
        """
            STEP 02 : Click on Home tab -> Select "HTML Analytical Document" format from Format drop down (HTML)
        """ 
        self.driver.set_page_load_timeout(100)
        report.select_output_format_from_ribbon("HTML Analytic Document")
        utils.synchronize_with_visble_text("#HomeFormatType", "HTML Analytic Document", report.home_page_short_timesleep)
        
        """
            STEP 03 : Click on Format tab -> Auto Drill button
        """
        report.select_ia_ribbon_item("Format", "auto_drill")
        
        """
            STEP 04 : Click Run
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.switch_to_frame("iframe[src*='contentDrill']")
        
        """
            STEP 04 - Expected : Verify drill down report in active format appears as below. 
        """
        #utils.create_table_data_start_end_rowcolumn(DATASET1, ACTIVE_TABLE_CSS, 0, 18)
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, 'Accessories', report.home_page_long_timesleep)
        msg = "Step 04.01 : Verify drill down report in active format appears as below"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET1, ACTIVE_TABLE_CSS, msg, 0, 18)
        
        """
            STEP 05 : Click on Stereo Systems under North America
            STE 05 : Expected - Verify drill menu appears as below
        """
        msg = "Step 05.01 : Verify drill menu for Stereo Systems under North America"
        expected_value = ['Drill down to Product Subcategory', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_misce.verify_field_menu_items(ACTIVE_TABLE_ID, 11, 1, expected_value, msg)
        
        """
            STEP 06 : Select 'Drill down to Product Subcategory'
        """
        active_misce.select_field_menu_items(ACTIVE_TABLE_ID, 11, 1, "Drill down to Product Subcategory")
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "Home", report.home_page_long_timesleep)
        
        """
            STEP 06 - Expected : Verify Breadcrumb appears at the bottom of the HEADING (if one exists) with name of field you drilled down from.
        """
#         utils.create_table_data_start_end_rowcolumn(DATASET2, ACTIVE_TABLE_CSS)
        msg = "Step 06.01 : Verify Breadcrumb appears at the bottom of the HEADING with name of field you drilled down from"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET2, ACTIVE_TABLE_CSS, msg)
        
        """
            STEP 07 : Click on North America
            STEP 07 - Expected : Verify drill menu appears as below. 
        """
        msg = "Step 07.01 : Verify drill menu for North America"
        expected_value = ['Reset', 'Drill down to Store Business Sub Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_misce.verify_field_menu_items(ACTIVE_TABLE_ID, 0, 0, expected_value, msg)
        
        """
            STEP 08 : Select 'Drill down to Store Business Sub Region'
        """
        active_misce.select_field_menu_items(ACTIVE_TABLE_ID, 0, 0, "Drill down to Store Business Sub Region")
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "North America", report.home_page_long_timesleep)
        
        """
            STEP 08 - Expected - Verify this breadcrumb (North America) should appear above the previous one (Stereo Systems) Since this is a higher level sort .
            Verify that Auto Drill is still selected as below.
        """
#         utils.create_table_data_start_end_rowcolumn(DATASET3, ACTIVE_TABLE_CSS, 0, 18)
        msg = "Step 08.01 : Verify this breadcrumb (North America) should appear above the previous one"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET3, ACTIVE_TABLE_CSS, msg, 0, 18)
        report.switch_to_default_content()
        report.verify_ribbon_item_selected("format_auto_drill", "08.02")
        report.switch_to_frame()
        report.switch_to_frame("iframe[src*='contentDrill']")
        
        """
            STEP 09 : Click on Home Theater Systems under West
            STEP 09 - Expected : Verify drill menu appears as below
            STEP 10 : Select 'Drill down to Model'
        """
        expected_value = ['Reset', 'Go up to Product Category', 'Drill down to Model', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        if Global_variables.browser_name == 'firefox':
            row_elem = self.driver.find_element_by_css_selector("#ITableData0 tr[id*='r31.'] td[id$='C1']")
            self.driver.execute_script("return arguments[0].scrollIntoView();", row_elem)
            ActionChains(self.driver).move_to_element(row_elem).click(row_elem).perform()
            utils.synchronize_with_number_of_element("div[id^='dt0_I0r'][style*='block']", 1, 10)
            menus=self.driver.find_elements_by_css_selector("div[id^='dt0_I0r'][style*='block']")
            x = menus[-1].find_elements_by_css_selector("span[id^='set0_I0r']")
            actual_value=[el.text.strip() for el in x if el.text.strip() != '']
            utils.asequal(expected_value, actual_value, 'Step 09.01: Verify drill menu appears')
            context_ele = self.driver.find_element_by_css_selector('div[id="dt0_I0r31.0C1_x__0"] table>tbody>tr[id="t0_I0r31.0C1_x__0_2"]')
            ActionChains(self.driver).move_to_element(context_ele).click(context_ele).perform()
        else:
            msg = "Step 09.01 : Verify drill menu for Home Theater Systems under West"
            active_misce.verify_field_menu_items(ACTIVE_TABLE_ID, 31, 1, expected_value, msg)
            active_misce.select_field_menu_items(ACTIVE_TABLE_ID, 31, 1, "Drill down to Model")
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "Panasonic", report.home_page_long_timesleep)     
        
        
        """
            STEP 10 - Expected : Verify the breadcrumbs should keep their relative positioning (should not flip positions). Second breadcrumb will show additional level.
        """
#         utils.create_table_data_start_end_rowcolumn(DATASET4, ACTIVE_TABLE_CSS)
        msg = "Step 10.01 : Verify the breadcrumbs should keep their relative positioning and Second breadcrumb will show additional level"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET4, ACTIVE_TABLE_CSS, msg)
        
        """
            STEP 11 : Click IA main menu and select Save As option.
            STEP 12 : Enter "C9480182" and click on save button in save as dialog.
        """
        report.switch_to_default_content()
        report.save_as_from_application_menu_item(CASE_ID)
        report.api_logout()
        
        """
            STEP 13 : Open saved fex using the API:
            http://machine_name:port/alias/ia?item=IBFS:/WFC/Repository/P292_S29835/G784981/C9480182.fex&tool=Report
        """
        report.edit_fex_using_api_url(CASE_ID)
        utils.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report.home_page_long_timesleep)
        
        """
            STEP 14 : Click on Format tab.
        """
        report.switch_ia_ribbon_tab("Format")
        
        """
            STEP 14 - Expected : Verify Auto Drill is still selected as below.
        """
        report.verify_ribbon_item_selected("format_auto_drill", "14.01")
        
        """
            STEP 15 : Logout using API:http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()