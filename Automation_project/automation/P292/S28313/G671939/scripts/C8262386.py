'''
Created on Jul 18, 2019

@author: osdamtx

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262386
TestCase Name = HIDENULLACRS ON, WEBVIEWER (CACHE) ON, CACHELINES default
'''
import unittest
from common.wftools.report import Report
from common.wftools.active_report import Active_Report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C8262386_TestClass(BaseTestCase):

    def test_C8262386(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj= Report(self.driver)
        core_utils_obj = CoreUtillityMethods(self.driver)
        active_obj = Active_Report(self.driver)
                
        """
            TESTCASE Variables
        """
        project_id = core_utils_obj.parseinitfile('project_id')
        suite_id = core_utils_obj.parseinitfile('suite_id')
        group_id = core_utils_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        case_id = 'C8262386'
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        DATA_SET_NAME3 = case_id + '_DataSet_03.xlsx'
        DATA_SET_NAME4 = case_id + '_DataSet_04.xlsx'
                
        '''
        step 1 : Run the below fex using API link
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671939/act_1563_cache_on_with_default_cachelines.fex
        '''
        report_obj.run_fex_using_api_url(folder_name=folder_path, fex_name='act_1563_cache_on_with_default_cachelines',mrid='mrid', mrpass='mrpass',run_table_css='table[class="arGrid"] > tbody > tr')
        report_obj.wait_for_visible_text('#ITableData0', 'Product Name')
              
        '''
        step 01.00 : The report indicates "159 of 159 records, Page 1 of 4".
                     The leftmost column headings contain the text AudioVox D1788PN, BOSE 10 Speaker Black, BOSE 10 Speaker White, and BOSE 16 Speaker White.
                     There is no column for Audio Technica and no column for AudioVox VE727.
                     Most of the table entries indicate "missing".
        step 2 : Scroll to the bottom of Page 1 of 4.
                There is a table entry in column 1 for AudioVox D1788PN.
        '''
        active_obj.verify_page_summary('0', '159of159records,Page1of4', 'Step 01.00: Verify page summary')
        #active_obj.create_active_report_dataset(DATA_SET_NAME1)
        active_obj.verify_active_report_dataset(DATA_SET_NAME1, msg='Step 01.01 & 02.00 : Verify report data', table_css='#ITableData0')

        '''
        step 3 : Scroll to the top; move to Page 2 of 4.
                 The same 4 columns are at the left of the report.
        step 4 : Scroll to the bottom of the page.
                 Toward the bottom there are entries for BOSE 10 Speaker Black, BOSE 10 Speaker White, and BOSE 16 Speaker White.
        '''
        active_obj.navigate_page('next_page')
        active_obj.wait_for_visible_text('#ITableData0', 'Product Name')
        active_obj.verify_page_summary('0', '159of159records,Page2of4', 'Step 03.00: Verify page summary')
        #active_obj.create_active_report_dataset(DATA_SET_NAME2)
        active_obj.verify_active_report_dataset(DATA_SET_NAME2, msg='Step 03.01 & 04.00 : Verify report data', table_css='#ITableData0')
        
        '''
        step 5 : Scroll to the top; move to Page 3 to of 4.
                 Columns now appear for Audio Technica and AudioVox VE727.
        step 6 : Scroll down 3 pages.
                 There is an entry for AudioVox VE727.
        '''
        active_obj.navigate_page('next_page')
        active_obj.wait_for_visible_text('#ITableData0', 'Product Name')
        active_obj.verify_page_summary('0', '159of159records,Page3of4', 'Step 05.00: Verify page summary')
        #active_obj.create_active_report_dataset(DATA_SET_NAME3)
        active_obj.verify_active_report_dataset(DATA_SET_NAME3, msg='Step 05.01 & 06.00 : Verify report data', table_css='#ITableData0')
        
        '''
        step 7 : Scroll to the top; move to Page 4 of 4.
                 There is an entry for Audio Technica in the first row.
                 Note that the column for AudioTechnica appeared on Page 3, even though the only entry for Audio Technica is on Page 4.
        '''
        active_obj.navigate_page('next_page')
        active_obj.wait_for_visible_text('#ITableData0', 'Product Name')
        active_obj.verify_page_summary('0', '159of159records,Page4of4', 'Step 07.00: Verify page summary')
        #active_obj.create_active_report_dataset(DATA_SET_NAME4)
        active_obj.verify_active_report_dataset(DATA_SET_NAME4, msg='Step 07.01 : Verify report data', table_css='#ITableData0')          
         
        '''
        step 8 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()