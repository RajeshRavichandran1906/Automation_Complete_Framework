'''
Created on January 4, 2019

@author: KK14897

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5831045
TestCase Name = AHTML: Export to XML (Excel) does not respect Scientific Notation format (ACT-1412)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart
from common.pages import active_miscelaneous
from common.lib import utillity, core_utility

class C5831045_TestClass(BaseTestCase):
    
    def test_C5831045(self):
        
        ac_obj=active_chart.Active_Chart(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        '''
        Step 1 : Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2 : Execute the attached fex using API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/S18035&BIP_item=ACT-1412.fex
        '''
        ac_obj.run_fex_using_api_url(folder_path, "ACT-1412", mrid='mrid', mrpass='mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'SALES_D12.5E', 'SALES_D16.2C', 'SALES_E16', 'SALES_E16.2', 'SALES_F16.2C','SALES_F16.2CE','SALES_P16.2C']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report ACT-1412.fex')
        
        '''
        Step 3 : From report click any field drop down and select Export->XML(Excel)format
        '''
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        utillobj.save_file_from_browser('C5831045_Actual')
        
        
        '''
        Step 4 : Verify the exported excel sheet displaying its scientific notations properly.
        '''
        utillobj.verify_xml_xls('C5831045_Actual.xls', 'C5831045_Expected.xls', 'Step 2. Verify file contents')
        
        '''
        Step 5 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        ac_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()