'''
Created on December 27, 2018

@author: AA14564

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10564&group_by=cases:section_id&group_id=164143&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5901785
TestCase Name = Verify default extensions show in chart picker
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report 
from common.lib.core_utility import CoreUtillityMethods

class C5901785_TestClass(BaseTestCase):

    def test_C5901785(self):
        
        """
        TESTCASE Object's
        """
        active_rpt_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        page_load_css = '#ITableData0 tr:nth-child(1) td:nth-child(1)'
        case_id = 'C5901785'
        
        """
        Step 1: Sign in to WebFOCUS as a basic user
                    http://machine:port/{alias}
        """
        """
        Step 2: Expand folder P95_S18043/G439418
                Execute the following URL:
                http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P95_S18043/G439418/ACT-1364.fex&tool=Report
        """
        active_rpt_obj.run_active_report_using_api('act-1364.fex', column_css=page_load_css, synchronize_visible_element_text='EMP_ID', repository_path=folder_path)
        active_rpt_obj.verify_page_summary('0', '12of12records,Page1of1', 'Step 2: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'.xlsx', 'Step 2.1: Verify the data.', table_css="#ITableData0")
        
        """
        Step 3: Click on the "DATE A6YMD" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 2, 'Filter', 'Equals')
        
        """
        Step 4: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '82/11/01', '82/12/01', '83/01/01', '83/03/01', '83/05/01', '84/09/01'], 'Step 4: Verify page summary.')
        
        """
        Step 5: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 6: Click on the "DATE I6YMD" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 6, 'Filter', 'Equals')
        
        """
        Step 7: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '82/11/01', '82/12/01', '83/01/01', '83/03/01', '83/05/01', '84/09/01'], 'Step 7: Verify page summary.')
        
        """
        Step 8: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 9: Click on the "DATE A6" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 7, 'Filter', 'Equals')
        
        """
        Step 10: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '821101', '821201', '830101', '830301', '830501', '840901'], 'Step 10: Verify page summary.')
        
        """
        Step 11: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 12: Click on the "DATE MDY" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 9, 'Filter', 'Equals')
        
        """
        Step 13: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '11/01/82', '12/01/82', '01/01/83', '03/01/83', '05/01/83', '09/01/84'], 'Step 13: Verify page summary.')
        
        """
        Step 14: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 15: Click on the "DATE YYMD" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 10, 'Filter', 'Equals')
        
        """
        Step 16: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '1982/11/01', '1982/12/01', '1983/01/01', '1983/03/01', '1983/05/01', '1984/09/01'], 'Step 16: Verify page summary.')
        
        """
        Step 17: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 18: Click on the "DATE JUL" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 11, 'Filter', 'Equals')
        
        """
        Step 19: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '82/305', '82/335', '83/001', '83/060', '83/121', '84/245'], 'Step 19: Verify page summary.')
        
        """
        Step 20: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 21: Click on the "DATE I6" column > Select Filter > Equals
        """
        active_rpt_obj.select_menu_items('ITableData0', 5, 'Filter', 'Equals')
        
        """
        Step 22: Click on the values dropdown arrow > Verify values area displayed
        """
        active_rpt_obj.verify_filter_values(1, ['[BLANK]', '821101', '821201', '830101', '830301', '830501', '840901'], 'Step 22: Verify page summary.')
        
        """
        Step 23: Close the 'Filter Selection' dialog
        """
        active_rpt_obj.close_filter_dialog()
        
        """
        Step 24: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()