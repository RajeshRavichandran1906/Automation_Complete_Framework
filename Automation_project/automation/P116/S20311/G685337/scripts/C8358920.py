'''
Created on January 25, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8358920
TestCase Name = ACT-1617 Filter selection window are not displaying its values fully
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.base import BasePage

class C8358920_TestClass(BaseTestCase):

    def test_C8358920(self):
        
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
        test_case_id = 'C8358920'
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
        group = core_util_obj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
        filter_values = ['2002/12/31 11:59:59PM', '2007/08/08 12:13:14PM', '2011/03/30 10:23:24PM', '2013/10/04 1:02:03AM']
        
        """
        Test case css
        """
        filter_css = "#wall1 .arFilter"
        page_load_css = '#ITableData0 tr:nth-child(3) td:nth-child(1) tt'
        
        """ 
        Step 1: Log in to WebFOCUS
        http://machine:port/{alias}
        Step 2: Execute ACT-1652.fex from below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S20311/G685337&BIP_item=153599.fex.fex
        An Active Report appears with data from the GGORDER database. The rightmost column has the heading "DATETIME HYYMDSA".
        There are 4 distinct data values in this column:
        2002/12/31 11:59:59PM
        2007/08/08 12:13:14PM
        2011/03/30 10:23:24PM
        2013/10/04 1:02:03AM
        """
        active_report_obj.run_active_report_using_api('153599.fex', column_css=page_load_css, synchronize_visible_element_text='Order', repository_path=folder_path)
        active_report_obj.verify_active_report_dataset( test_case_id +'_step1.xlsx', "Step 1: Verify the data in dataset", table_css="#ITableData0",starting_rownum=1)
        
        """
        Step 3: In the heading of the rightmost column, click on the down arrow, then on Filter, then on Not Equal.
        A Filter Selection window opens.
        """
        active_report_obj.select_menu_items("ITableData0", '7', 'Filter', 'Not equal')
        util_obj.synchronize_with_number_of_element(filter_css, 1 , base_obj.report_short_timesleep)
        util_obj.verify_object_visible(filter_css, True, 'Step 3: Verify filter dialog is open')
        
        """
        Step 4: Move the Filter Selection window so that the report output is more clearly visible.
        In the Filter Selection window, click on the down arrow to the right of the second input box.
        """
        active_report_obj.move_active_popup(1, '300', '50')
        active_report_obj.verify_filter_values(1, filter_values, 'Step 4: Verify filter selection')
        
        """
        Step 5: In the Filter Selection window, click on the top value, 2002/12/31 11:59:59PM.
        Click on Filter.
        The report no longer shows data for DATETIME = 2002/12/31 11:59:59PM.
        """
        active_report_obj.create_filter(1, 'Not equal', value1='2002/12/31 11:59:59PM')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_active_report_dataset( test_case_id +'_step5.xlsx', "Step 5: Verify the data in dataset", table_css="#ITableData0",starting_rownum=1)
        
        """
        Step 6: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()