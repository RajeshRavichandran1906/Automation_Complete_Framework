'''
Created on 01-Feb-2017

@author: Aftab
Reautomated by Niranjan on 27-Nov-2017.
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227573
TestCase Name = Verify adding column total and row total to report
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.report import Report


class C2227573_TestClass(BaseTestCase):

    def test_C2227573(self):
        
        Test_Case_ID = "C2227573"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        report= Report(self.driver)
        
        """
            TESTCASE CSS
        """
        qwerty_tree_css = "#queryTreeWindow"
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".            """
        report.double_click_on_datetree_item("COUNTRY", 1)
        report.wait_for_visible_text(qwerty_tree_css, "COUNTRY")
        
        report.double_click_on_datetree_item("CAR", 1)
        report.wait_for_visible_text(qwerty_tree_css, "CAR")
        
        report.double_click_on_datetree_item("DEALER_COST", 1)
        report.wait_for_visible_text(qwerty_tree_css, "DEALER_COST")
        
        report.double_click_on_datetree_item("RETAIL_COST", 1)
        report.wait_for_visible_text(qwerty_tree_css, "RETAIL_COST")
        
        """ 3. Verify the following report is displayed.        """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 3.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 3.2: Verify report dataset in live preview.')
        
        """ 4. Select "Home" > "Report" > "Column Totals" button.        """
        ribbonobj.select_ribbon_item('Home', 'column_totals')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 4.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 11, 4, Test_Case_ID+"_Ds02.xlsx", 'Step 4.2: Verify report dataset after column total.')
        column_total_value_list=['TOTAL', '', '143,794', '173,204']
        msg="Step 4.2: Verify Canvas column total Values."
        ia_resultobj.verify_column_total('TableChart_1', column_total_value_list, msg)        
        
        """ 5. Click on "Row Totals" button.        """
        ribbonobj.select_ribbon_item('Home', 'row_totals')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        
        """ 6. Verify the following report is displayed.            """
        ia_resultobj.verify_report_data_set('TableChart_1', 12, 5, Test_Case_ID+"_Ds03.xlsx", 'Step 6.2: Verify report dataset after row total.')
        
        
        """ 7. Click "Run".            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        
        
        """ 8. Verify the report is displayed.            """
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds04.xlsx", 'Step 8: Verify report dataset after run.')
        
        """ 9. Click "IA" > "Save"            """
        """ 10. Enter Title = "C2227573".     """
        """ 11. Click "Save".                 """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnOK", "Save")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        """ 12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        utillobj.infoassist_api_logout()
        
        
        """ 13. Reopen saved FEX:    
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227573.fex&tool=Report
        """
        uname=(By.CSS_SELECTOR, "input[id='SignonUserName']")
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        
        
        """ 14. Verify successful restore        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 14.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 11, 5, Test_Case_ID+"_Ds03.xlsx", 'Step 14.2: Verify report dataset')
        
        
        """ 15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        time.sleep(2)         
        
        
if __name__ == '__main__':
    unittest.main() 