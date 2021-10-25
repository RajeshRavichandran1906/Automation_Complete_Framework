'''
Created on Aug 16, 2019

@author: osdamtx

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262387
TestCase Name = HIDENULLACRS ON, WEBVIEWER (CACHE) ON, CACHELINES = 400
'''
import unittest
from common.wftools.report import Report
from common.wftools.active_report import Active_Report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C8262387_TestClass(BaseTestCase):

    def test_C8262387(self):
        
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
        case_id = 'C8262387'
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        
        '''
        step 1 : Run the below fex using API link
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671939/act_1563_cache_on_with_cachelines_400.fex
        '''
        report_obj.run_fex_using_api_url(folder_name=folder_path, fex_name='act_1563_cache_on_with_cachelines_400',mrid='mrid', mrpass='mrpass',run_table_css='table[class="arGrid"] > tbody > tr')
        report_obj.wait_for_visible_text('#ITableData0', 'Product Name')
        
        '''
        step 01.01 : The report indicates "159 of 159 records, Page 1 of 4".
        The leftmost column headings contain the text Audio Technica, AudioVox D1788PN, AudioVox VE727, BOSE 10 Speaker Black, BOSE 10 Speaker White, and BOSE 16 Speaker White.
        The columns for Audio Technica and AudioVox VE727 are present, even though the single entries in them do not appear until pages 4 and 3.
        Most of the table entries indicate "missing".
        '''
        active_obj.verify_page_summary('0', '159of159records,Page1of4', 'Step 01.01: Verify page summary')
#         active_obj.create_active_report_dataset(DATA_SET_NAME1)
        active_obj.verify_active_report_dataset(DATA_SET_NAME1, msg='Step 01.02 : Verify report data', table_css='#ITableData0')

        '''
        Step 2: Close the output window.
        step 3 : Logout:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
        
    if __name__ == '__main__':
        unittest.main()
        
        
        
        