'''
Created on January 17, 2019

@author: Varun
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227199
TestCase Name = Subtotals not updated in Active compound Report w/ filters
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage
from common.wftools import report

class C2227199_TestClass(BaseTestCase):

    def test_C2227199(self):
        
        """
        TESTCASE Object's
        """
        report_obj = report.Report(self.driver)
        base_obj = BasePage(self.driver)
        util_obj = UtillityMethods(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
#         group = core_util_obj.parseinitfile('group_id')
        folder_path = "{0}/{1}".format(project, suite)
        
        """
        Test case css
        """
        filter_css = "#wall1 .arFilter"
        page_load_css = '#ITableData0 tr:nth-child(1) td:nth-child(1)'
        
        """ 
        Step 1: Execute the attached repro that demonstrates the default behavior for Subtotals/Filtering.
        act-205-subtotal-off.fex
        """
        active_report_obj.run_active_report_using_api('act-205-subtotal-off.fex', column_css=page_load_css, synchronize_visible_element_text='COUNTRY', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step1.xlsx', "Step 1.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 1.2: Verify Page summary')
         
        """
        Step 2: From the drop down for Country, select Filter, then Not Equal and select the value for England.
        Expect to see the report and Filter selection.
        """
        active_report_obj.select_menu_items("ITableData0", 0, 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Not equal', value1="ENGLAND")
         
        """
        Step 3: Click the Filter button.
        """
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step3.xlsx', "Step 3.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '7of10records,Page1of1', 'Step 3.2: Verify Page summary')
        report_obj.api_logout()
         
        """
        Step 4: Execute the attached repro that demonstrates the default behavior for Subtotals/Filtering.
        act-205-subtotal-on.fex
        Expect to see the following Active report with subtotals for each Country.
        """
        active_report_obj.run_active_report_using_api('act-205-subtotal-on.fex', column_css=page_load_css, synchronize_visible_element_text='COUNTRY', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step4.xlsx', "Step 4.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 4.2: Verify Page summary')
         
        """
        Step 5: From the drop down for Country, select Filter, then Not Equal and select the value for England.
        Expect to see the report and Filter selection.
        """
        active_report_obj.select_menu_items("ITableData0", 0, 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Not equal', value1="ENGLAND")
         
        """
        Step 6: Click the Filter button.
        Expect to see the Filtered report, with England removed.
        Also notice that the remaining Countries have their subtotals intact.
        """
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step6.xlsx', "Step 6.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '7of10records,Page1of1', 'Step 6.2: Verify Page summary')
        report_obj.api_logout()
         
        """
        Step 7: Execute the attached repro that demonstrates the default behavior for Subtotals/Filtering.
        act-205-subtot-off-operators.fex
        Expect to see the following Active report with subtotals for each Country.
        """
        active_report_obj.run_active_report_using_api('act-205-subtot-off-operators.fex', column_css=page_load_css, synchronize_visible_element_text='COUNTRY', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step7.xlsx', "Step 7.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 7.2: Verify Page summary')
         
        """
        Step 8: From the drop down for Country, select Filter, then Not Equal and select the value for W Germany.
        Expect to see the report and Filter selection.
        """
        active_report_obj.select_menu_items("ITableData0", 0, 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Not equal', value1="W GERMANY")
         
        """
        Step 9: Click the Filter button.
        Expect to see the Filtered report, with England removed.
        Also notice that all Subtotals have been removed.
        This is the default behavior for Filtering.
        """
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step9.xlsx', "Step 9.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '8of10records,Page1of1', 'Step 9.2: Verify Page summary')
        report_obj.api_logout()
        
        """
        Step 10: Execute the attached repro that demonstrates the default behavior for Subtotals/Filtering.
        act-205-subtot-on-operators.fex
        """
        active_report_obj.run_active_report_using_api('act-205-subtot-on-operators.fex', column_css=page_load_css, synchronize_visible_element_text='COUNTRY', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step10.xlsx', "Step 10.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 10.2: Verify Page summary')
        
        """
        Step 11: From the drop down for Country, select Filter, then Not Equal and select the value for W Germany.
        Expect to see the report and Filter selection.
        """
        active_report_obj.select_menu_items("ITableData0", 0, 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Not equal', value1="W GERMANY")
        
        """
        Step 12: Click the Filter button.
        Expect to see the Filtered report, with W Germany removed.
        The new Maximum Total for Sales should be the value of 43000 for Japan, since W Germany and its 80390 was filtered out.
        Also notice that the remaining Countries have their subtotals intact.
        """
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step12.xlsx', "Step 12.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '8of10records,Page1of1', 'Step 12.2: Verify Page summary')
        
        """
        Step 13: Close the Filter panel.
        Expect to see the following Active report with subtotals for each Country again.
        """
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step10.xlsx', "Step 13.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '10of10records,Page1of1', 'Step 13.2: Verify Page summary')
        
        """
        Step 14: From the drop down for Total of all Country Dcost, select Filter, then Not Equal and select the value for 4,292, on the Triumph row.
        This value is associated with the row for Jensen, for England.
        Expect to see the report and Filter selection.
        """
        active_report_obj.select_menu_items("ITableData0", 5, 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        active_report_obj.create_filter(1, 'Not equal', value1="4,292")
        
        """
        Step 15: Click the Filter button.
        Expect to see the Filtered report, with value for 4,292 on the Triumph line removed.
        The new lowest vale for England is now 14,940 on the Jensen row.
        England remains but now with only 2 Cars and an adjusted Country Subtotal minimum value of 14,940.
        Also notice that the remaining Countries have their subtotals intact.
        """
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset('C2227199_dataset_step15.xlsx', "Step 15.1: Verify the data in dataset", table_css="#ITableData0")
        active_report_obj.verify_page_summary(0, '9of10records,Page1of1', 'Step 15.2: Verify Page summary')
        
if __name__ == '__main__':
    unittest.main()