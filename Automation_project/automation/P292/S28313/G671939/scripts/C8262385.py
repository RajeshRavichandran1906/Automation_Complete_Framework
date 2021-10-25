'''
Created on Jul 18, 2019

@author: Aftab

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262385
TestCase Name = SET HIDENULLACRS=ON, AHTML and HTML
'''
import unittest
from common.wftools.report import Report
from common.wftools.active_report import Active_Report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C8262385_TestClass(BaseTestCase):

    def test_C8262385(self):
        
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

        '''
        Step 1 : Run the fex using below API link
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S28313/G671908/html_hidenullacrs_on.fex
        '''
        report_obj.run_fex_using_api_url(folder_name=folder_path, fex_name='ahtml_hidenullacrs_on',mrid='mrid', mrpass='mrpass',run_table_css='table[class="arGrid"] > tbody > tr',no_of_element=2)
        report_obj.wait_for_visible_text('#ITableData0', 'Region')
        
        '''
        Step 1.00 : The "Espresso" column is missing in the AHTML report.
        '''       
        active_obj.verify_page_summary('0', '6of6records,Page1of1', 'Step 01.00: Verify page summary')
        #active_obj.create_active_report_dataset('C8262385_Ds01.xlsx')
        active_obj.verify_active_report_dataset('C8262385_Ds01.xlsx', msg='Step 01.01 : verify report data', table_css='#ITableData0')
        
        '''
        Step 2 : Logout:
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
        
        '''
        Step 3 : Run the corresponding HTML report html_hidenullacrs_off.fex.
        '''
        report_obj.run_fex_using_api_url(folder_name=folder_path, fex_name='html_hidenullacrs_on',mrid='mrid', mrpass='mrpass',run_table_css='table[cellpadding="1"]>tbody>tr')
        report_obj.wait_for_visible_text('table[cellpadding="1"]', 'Region')
        
        '''
        Step 3.00 : The "Espresso" column is also missing in the HTML report.
        '''        
        #report_obj.create_html_report_dataset('C8262385_Ds02.xlsx','table[cellpadding="1"]')
        report_obj.verify_html_report_dataset('C8262385_Ds02.xlsx',"Step 03.01 : verify report data",'table[cellpadding="1"]')
         
        '''
        Step 4 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()