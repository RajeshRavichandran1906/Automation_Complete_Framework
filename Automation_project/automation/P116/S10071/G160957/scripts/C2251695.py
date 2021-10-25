'''
Created on Jan 23, 2018

@author: Robert

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251695
TestCase Name = Document using Check Box Filter with ARDATA_COLUMN multi-fields (ACT-287).
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251695_TestClass(BaseTestCase):

    def test_C2251695(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """    1. Execute the attached repro - act-287-checkbox.fex    """
            
        utillobj.active_run_fex_api_login('act-287-checkbox.fex', 'S10071_3', 'mrid', 'mrpass')
             
        resultobj.wait_for_property("#ITableData0",1,30)
         
        time.sleep(3)
         
        """    1.1. Expect to see the following Document with a report and a two-field Check Box Filter.    """
        """    1.2. Verify that for each Check Box entry, there is data on the report.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "MODEL", "DEALER_COST", "SALES"]
        
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251695_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251695_Ds01.xlsx', 'Step 1.2c: Verify data.')
        exp_list=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN', 'ENGLAND,TRIUMPH', 'FRANCE,PEUGEOT', 'ITALY,ALFA ROMEO', 'ITALY,MASERATI', 'JAPAN,DATSUN', 'JAPAN,TOYOTA', 'W GERMANY,AUDI', 'W GERMANY,BMW']
        sel_list='[All]'
        iarun.verify_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', exp_list, 'Step 1.2d Verify checkbox contents', default_selected_check=sel_list)
        
        """    2. Click both boxes for Italy.    """
        """    2.1. Expect to see both boxes checked and only Italy data displayed.    """
        
        sel_list=['ITALY,ALFA ROMEO', 'ITALY,MASERATI']       
        iarun.select_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', sel_list, scroll_down_times=0)
        time.sleep(10)
        #iarun.verify_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', exp_list, 'Step 2.1a Verify default selected check', default_selected_check='ITALY,ALFA ROMEO')
        #iarun.verify_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', exp_list, 'Step 2.1a Verify default selected check', default_selected_check='ITALY,MASERATI')
        
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251695_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251695_Ds02.xlsx', 'Step 2.1b: Verify data after filtering.')
        
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '4of18records,Page1of1', 'Step 2.1c: Verify the Report Heading')
        
        """    3. Click England,Jaguar box.    """
        """    3.1. Expect to see both boxes checked for Italy plus the data for England,Jaguar.    """
        
        sel_list=['ENGLAND,JAGUAR']       
        iarun.select_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', sel_list, scroll_down_times=0)
        time.sleep(10)
        #iarun.verify_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', exp_list, 'Step 3.1a Verify default selected', default_selected_check='ENGLAND,JAGUAR')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251695_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251695_Ds03.xlsx', 'Step 3.1b: Verify data after filtering.')
        miscelanousobj.verify_page_summary(0, '6of18records,Page1of1', 'Step 2.1c: Verify the Report Heading')
        
        """    4. Click the [All] option.    """
        """    4.1. Expect to see all 13 rows re-appear.    """
        sel_list=['[All]']       
        iarun.select_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', sel_list, scroll_down_times=0)
        time.sleep(10)
        #iarun.verify_active_dashboard_prompts('checkbox', '#checkbox_dOBJECT3', exp_list, 'Step 4.1a Verify default selected check', default_selected_check='[All]')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251695_Ds01.xlsx', 'Step 4.1b: Verify data after filtering.')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 4.1c: Verify the Report Heading')
        

        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()
        