'''
Created on December 27, 2018

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5901788
TestCase Name = Verify AHTML Report with Legacy Dates - retrieve filter values and apply filter
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage

class C5901788_TestClass(BaseTestCase):

    def test_C5901788(self):
        
        """
        TESTCASE Object's
        """
        base_obj = BasePage(self.driver)
        util_obj = UtillityMethods(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
        group = core_util_obj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
        
        """
        Test case css
        """
        filter_css = "#wall1 .arFilter"
        page_load_css = '#ITableData0 tr:nth-child(1) td:nth-child(1)'
        
        """ 
        Step 1: Sign in to WebFOCUS as a basic user
        http://machine:port/{alias}
        Step 2: Expand folder P95_S18043/G439418
        Execute the following URL:
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P95_S18043/G439418/ACT-1364b.fex&tool=Report
        """
        active_report_obj.run_active_report_using_api('act-1364b.fex', column_css=page_load_css, synchronize_visible_element_text='EMP_ID', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset('C5901788.xlsx', "Step 1.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '12of12records,Page1of1', 'Step 1.2: Verify Page summary')
        
        """
        Step 3: Click on the "A8" column > Select Filter > Equals
        """
        active_report_obj.select_menu_items("ITableData0", 3, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        
        """
        Step 4: Click on the values dropdown arrow > Verify values area displayed
        """
        active_report_obj.verify_filter_values(1, ['[BLANK]', '821101', '821201', '830101', '830301', '830501', '840901'], 'Step 4: Verify filter selection')
        
        """
        Step 5: Select value "83/03/01" > Click on "Filter"
        """
        active_report_obj.create_filter(1, 'Equals', value1="830301")
        active_report_obj.filter_button_click('Filter')
        
        """
        Step 6: Verify selection is applied
        """
        active_report_obj.verify_active_report_dataset('C5901788_1.xlsx', "Step 6.1: Verify the filtered data in dataset", table_css="#ITableData0")
        
        """
        Step 7: Close the 'Filter Selection' dialog
        """
        active_report_obj.close_filter_dialog()
        
        """
        Step 8: Click on the "DATE A6M|D|Y" column > Select Filter > Equals
        """
        active_report_obj.select_menu_items("ITableData0", 8, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        
        """
        Step 9: Click on the values dropdown arrow > Verify values area displayed
        """
        active_report_obj.verify_filter_values(1, ['[BLANK]', '110182', '120182', '010183', '030183', '050183', '090184'], 'Step 9.1: Verify filter values')
        
        """
        Step 10: Close the 'Filter Selection' dialog
        """
        active_report_obj.close_filter_dialog()
        
        """
        Step 11: Click on the "DATEYYMD" column > Select Filter > Equals
        """
        active_report_obj.select_menu_items("ITableData0", 10, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        
        """
        Step 12: Click on the values dropdown arrow > Verify values area displayed
        """
        active_report_obj.verify_filter_values(1, ['[BLANK]', '1982/11/01', '1982/12/01', '1983/01/01', '1983/03/01', '1983/05/01', '1984/09/01'], 'Step 12.1: Verify filter values')
        
        """
        Step 13: Close the 'Filter Selection' dialog
        """
        active_report_obj.close_filter_dialog()
        
        """
        Step 14: Click on the "DATE JUL" column > Select Filter > Equals
        """
        active_report_obj.select_menu_items("ITableData0", 11, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        
        """
        Step 15: Click on the values dropdown arrow > Verify values area displayed
        """
        active_report_obj.verify_filter_values(1, ['[BLANK]', '82/305', '82/335', '83/001', '83/060', '83/121', '84/245'], 'Step 15.1: Verify filter values')
        
        """
        Step 16: Close the 'Filter Selection' dialog
        """
        active_report_obj.close_filter_dialog()
        
        """
        Step 17: Click on the "DATE MDY" column > Select Filter > Equals
        """
        active_report_obj.select_menu_items("ITableData0", 9, 'Filter', 'Equals')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        
        """
        Step 18: Click on the values dropdown arrow > Verify values area displayed
        """
        active_report_obj.verify_filter_values(1, ['[BLANK]', '11/01/82', '12/01/82', '01/01/83', '03/01/83', '05/01/83', '09/01/84'], 'Step 18.1: Verify filter values')
        
        """
        Step 19: Select value "12/01/82" > Click on "Filter" button
        """
        active_report_obj.create_filter(1, 'Equals', value1="12/01/82")
        active_report_obj.filter_button_click('Filter')
        
        """
        Step 20: Verify selection is applied
        """
        active_report_obj.verify_active_report_dataset('C5901788_2.xlsx', "Step 20.1: Verify the filtered data in dataset", table_css="#ITableData0")
        
        """
        Step 21: Close the 'Filter Selection' dialog
        """
        active_report_obj.close_filter_dialog()
        
        """
        Step 22: Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()