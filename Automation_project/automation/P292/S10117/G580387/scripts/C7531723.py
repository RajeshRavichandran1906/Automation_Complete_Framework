"""-------------------------------------------------------------------------------------------
Created on June 27, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/7531723
Test Case Title =  Breadcrumbs - Have two hierarchy sorts from different dimensions - Active format
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.pages.active_miscelaneous import Active_Miscelaneous 

class C7531723_TestClass(BaseTestCase):

    def test_C7531723(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        active_misce = Active_Miscelaneous(self.driver)
        utils = UtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        CASE_ID = "C7531723"
        FEX_FILE = "IA-Shell"
        DATASET1 = CASE_ID + "_DataSet_01.xlsx"
        DATASET2 = CASE_ID + "_DataSet_02.xlsx"
        DATASET3 = CASE_ID + "_DataSet_03.xlsx"
        DATASET4 = CASE_ID + "_DataSet_04.xlsx"
        ACTIVE_TABLE_ID = "ITableData0"
        ACTIVE_TABLE_CSS = "#" + ACTIVE_TABLE_ID
        
        """
            STEP 01 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """
        report.edit_fex_using_api_url(FEX_FILE)
        utils.synchronize_with_visble_text("#TableChart_1", "Sale,Year", 120)
        
        """
            STEP 02 : Click on Home tab -> Select Active Report format from Format drop down (HTML)
        """ 
        report.select_output_format_from_ribbon("Active Report")
        utils.synchronize_with_visble_text("#HomeFormatType", "Active Report", 10)
        
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
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "Home", 120)
        
        """
            STEP 06 - Expected : Verify Breadcrumb appears at the bottom of the HEADING (if one exists) with name of field you drilled down from.
        """
        #utils.create_table_data_start_end_rowcolumn(DATASET2, ACTIVE_TABLE_CSS)
        msg = "Step 06.01 : Verify Breadcrumb appears at the bottom of the HEADING with name of field you drilled down from"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET2, ACTIVE_TABLE_CSS, msg)
        
        """
            STEP 07 : Click on North America
            STEP 07 - Expected : Verify drill menu appears as below. 
        """
        msg = "Step 07.01 : Verify drill menu for North America"
        expected_value = ['Restore Original', 'Drill down to Store Business Sub Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_misce.verify_field_menu_items(ACTIVE_TABLE_ID, 0, 0, expected_value, msg)
        
        """
            STEP 08 : Select 'Drill down to Store Business Sub Region'
        """
        active_misce.select_field_menu_items(ACTIVE_TABLE_ID, 0, 0, "Drill down to Store Business Sub Region")
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "North America", 120)
        
        """
            STEP 08 - Expected - Verify this breadcrumb (North America) should appear above the previous one (Stereo Systems) Since this is a higher level sort .
            Verify that Auto Drill is still selected as below.
        """
        #utils.create_table_data_start_end_rowcolumn(DATASET3, ACTIVE_TABLE_CSS, 0, 18)
        msg = "Step 08.01 : Verify this breadcrumb (North America) should appear above the previous one"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET3, ACTIVE_TABLE_CSS, msg, 0, 18)
        report.switch_to_default_content()
        report.verify_ribbon_item_selected("format_auto_drill", "08.02")
        report.switch_to_frame()
        report.switch_to_frame("iframe[src*='contentDrill']")
        
        """
            STEP 09 : Click on Home Theater Systems under West
            STEP 09 - Expected : Verify drill menu appears as below
        """
        msg = "Step 09.01 : Verify drill menu for Home Theater Systems under West"
        expected_value = ['Restore Original', 'Drill up to Product Category', 'Drill down to Model', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_misce.verify_field_menu_items(ACTIVE_TABLE_ID, 31, 1, expected_value, msg)
        
        """
            STEP 10 : Select 'Drill down to Model'
        """
        active_misce.select_field_menu_items(ACTIVE_TABLE_ID, 31, 1, "Drill down to Model")
        utils.synchronize_with_visble_text(ACTIVE_TABLE_CSS, "Panasonic", 120)
        
        """
            STEP 10 - Expected : Verify the breadcrumbs should keep their relative positioning (should not flip positions). Second breadcrumb will show additional level.
        """
        #utils.create_table_data_start_end_rowcolumn(DATASET4, ACTIVE_TABLE_CSS)
        msg = "Step 08.01 : erify the breadcrumbs should keep their relative positioning and Second breadcrumb will show additional level"
        utils.verify_table_data_using_start_end_rowcolumn(DATASET4, ACTIVE_TABLE_CSS, msg)
        
        """
            STEP 11 : Click IA main menu and select Save As option.
            STEP 12 : Enter C7531723 and click on save button in save as dialog
        """
        report.switch_to_default_content()
        report.save_as_from_application_menu_item(CASE_ID)
        report.api_logout()
        
        """
            STEP 13 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7531723.fex&tool=Report
        """
        report.edit_fex_using_api_url(CASE_ID)
        utils.synchronize_with_visble_text("#TableChart_1", "Sale,Year", 120)
        
        """
            STEP 14 : Click on Format tab.
        """
        report.switch_ia_ribbon_tab("Format")
        
        """
            STEP 14 - Expected : Verify Auto Drill is still selected as below.
        """
        report.verify_ribbon_item_selected("format_auto_drill", "08.02")
        
        """
            STEP 15 : Logout using API:http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()