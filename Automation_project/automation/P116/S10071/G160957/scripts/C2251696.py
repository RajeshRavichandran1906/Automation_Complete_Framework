'''
Created on Feb 08, 2018

@author: Praveen Ramkumar

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251696
TestCase Name = Document using List Box Filter with ARDATA_COLUMN multi-fields (ACT-287).
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251696_TestClass(BaseTestCase):

    def test_C2251696(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        
        """   Step: 1.Execute the attached repro - act-287-listbox.fex    """
            
        utillobj.active_run_fex_api_login('act-287-listbox.fex', 'S10071_3', 'mrid', 'mrpass')             
        resultobj.wait_for_property("#ITableData0",1,30)         
        time.sleep(3)
        
         
        """    1.1. Expect to see the following Document with a report and a two-field Check Box Filter.    """
        """    1.2. Verify that for each Check Box entry, there is data on the report.    """
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 1.2a: Verify the Report Heading')
        column_list=["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 1.2b: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251696_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251696_Ds01.xlsx', 'Step 1.2c: Verify data.')
        
        exp_list=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN', 'ENGLAND,TRIUMPH', 'FRANCE,PEUGEOT', 'ITALY,ALFA ROMEO', 'ITALY,MASERATI', 'JAPAN,DATSUN', 'JAPAN,TOYOTA', 'W GERMANY,AUDI', 'W GERMANY,BMW']
        iarun.verify_active_dashboard_prompts('listbox', '#PROMPT_1_cs', exp_list, 'Step 1.2d Verify listbox contents')
        
        """   Step 2:Click the two List Box entries for Germany.
                Expect to see only the data for both W Germany/Audi and 
                W Germany/BMW.   
        """
        
        sel_list=['W GERMANY,AUDI', 'W GERMANY,BMW']       
        iarun.select_active_dashboard_prompts('listbox', '#PROMPT_1_cs', sel_list)
        time.sleep(10)
        
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251696_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251696_Ds02.xlsx', 'Step 2.1b: Verify data after filtering.')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of18records,Page1of1', 'Step 2.1c: Verify the Report Heading')
        
        """   Step 3:Click the List Box entry for France.Expect to see the data for both W Germany/Audi and 
                W Germany/BMW plus the row for France,Peugeot.   
        """
        
        sel_list=['FRANCE,PEUGEOT']       
        iarun.select_active_dashboard_prompts('listbox', '#PROMPT_1_cs', sel_list)
        time.sleep(10)
        
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251696_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251696_Ds03.xlsx', 'Step 3.1: Verify data after filtering.')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '8of18records,Page1of1', 'Step 3.2: Verify the Report Heading')
        
        """   Step 4:Click the List Box entry for All.Expect to see all previous selection s cleared and all data displayed.   
        """
        
        sel_list=['[All]']
        iarun.select_active_dashboard_prompts('listbox', '#PROMPT_1_cs', sel_list)
        time.sleep(10)
        
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2251696_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251696_Ds04.xlsx', 'Step 4.1: Verify data after filtering.')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 4.2: Verify the Report Heading')
        
if __name__=='__main__' :
    unittest.main()    
    