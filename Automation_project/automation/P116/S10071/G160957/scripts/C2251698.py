'''
Created on Jan19, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251698
TestCase Name = Document using Radio Button Filter with ARDATA_COLUMN multi-fields (ACT-287).
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_run
from common.lib import utillity


class C2251698_TestClass(BaseTestCase):

    def test_C2251698(self):
        Test_Case_ID = 'C2251698'
        """
        Step01: Execute the attached repro - act-287-radiobutton.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        utillobj.active_run_fex_api_login('act-287-radiobuttom.fex','S10071_4','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
        """
        Expect to see the following Document with a report and a two-field Radio Button Filter.
        Verify that the Radio Buttons display entries for all of the data on the report.
        """
        def verify(r1,r1_sum,r1_col,radiolist,radio_defau,step):
            #1st Report
            active_misobj.verify_page_summary(r1,r1_sum,step+'.1a: Verify the Report Heading of 1st Report')
            active_misobj.verify_column_heading('ITableData'+str(r1), r1_col, step+'.1b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx', step+'.1c: Verify data.')
            #Radio Button
            msg=step+".2: Verify Radio button"
            ia_runobj.verify_active_dashboard_prompts('radio',"#PROMPT_1_cs",radiolist, msg, default_selected_check=radio_defau)
            
        r1_col=['COUNTRY','CAR','RETAIL_COST','DEALER_COST']
        radiolist=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN']
        radio_defau='[All]'
        verify(0,'10of10records,Page1of1',r1_col,radiolist,radio_defau,"Step01")
        
        """
        Step02: Click the England,Triumph radio button.
        Expect to see only data for England,Triumph.
        """
        ia_runobj.select_active_dashboard_prompts('radio','#PROMPT_1_cs',['ENGLAND,TRIUMPH'])
        r1_col=['COUNTRY','CAR','RETAIL_COST','DEALER_COST']
        radiolist=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN']
        radio_defau='[All]'#'ENGLAND,TRIUMPH'
        verify(0,'1of10records,Page1of1',r1_col,radiolist,radio_defau,"Step02")
        
        """
        Step03: Click the England,Jaguar radio button.
        Expect to see only data for England,Triumph.Radio buttons allow one selection at a time.
        """
        ia_runobj.select_active_dashboard_prompts('radio','#PROMPT_1_cs',['ENGLAND,JAGUAR'])
        r1_col=['COUNTRY','CAR','RETAIL_COST','DEALER_COST']
        radiolist=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN']
        radio_defau='[All]'#'ENGLAND,JAGUAR'
        verify(0,'1of10records,Page1of1',r1_col,radiolist,radio_defau,"Step03")
        
        """
        Step04 :Click the All radio button.
        Expect to see all rows redisplayed.
        """
        ia_runobj.select_active_dashboard_prompts('radio','#PROMPT_1_cs',['[All]'])
        r1_col=['COUNTRY','CAR','RETAIL_COST','DEALER_COST']
        radiolist=['[All]', 'ENGLAND,JAGUAR', 'ENGLAND,JENSEN']
        radio_defau='[All]'
        verify(0,'10of10records,Page1of1',r1_col,radiolist,radio_defau,"Step04")
        
        
if __name__ == '__main__':
    unittest.main()


