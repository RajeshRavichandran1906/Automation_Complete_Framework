'''
Created on Jan19, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251697
TestCase Name = Document using Combo Box Filter with ARDATA_COLUMN multi-fields (ACT-287).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_run
from common.lib import utillity


class C2251697_TestClass(BaseTestCase):

    def test_C2251697(self):
        Test_Case_ID = 'C2251697'
        """
        Step01: Execute the attached repro - act-287-combobox.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        utillobj.active_run_fex_api_login('act-287-combobox.fex','S10071_4','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
        """
        Expect to see the following Document with a report and a two-field Combo Box Filter.
        Verify that the Combo Box only displays the All entry initially.
        """
        def verify(r1,r1_sum,r1_col,drop,step):
            #1st Report
            active_misobj.verify_page_summary(r1,r1_sum,step+'.1a: Verify the Report Heading of 1st Report')
            active_misobj.verify_column_heading('ITableData'+str(r1), r1_col, step+'.1b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx', step+'.1c: Verify data.')
            #Combo Box Filter
            utillobj.verify_dropdown_value("#combobox_dsPROMPT_1",expected_default_selected_value=drop, default_selection_msg=step+".2: Verify FILTER IS SHOWING ALL")
            
        r1_col=['COUNTRY','CAR','BODYTYPE','LENGTH','WIDTH']
        drop="[All]"
        verify(0,'13of13records,Page1of1',r1_col,drop,"Step01")
        
        """
        Step02: Click the drop down control on the Combo Box,then select Italy,Coupe.
        Expect to see only the data for Italy,Coupe.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1","visible_text",'ITALY,COUPE')
        r1_col=['COUNTRY','CAR','BODYTYPE','LENGTH','WIDTH']
        drop="ITALY,COUPE"
        verify(0,'2of13records,Page1of1',r1_col,drop,"Step02")
        
        """
        Step03: Click the drop down control on the Combo Box, then select Italy,Roadster.
        Expect to see only the data for Italy,Roadster.
        Verify that Italy,Coupe is not displayed, as Combo Box only supports one selection.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1","visible_text",'ITALY,ROADSTER')
        r1_col=['COUNTRY','CAR','BODYTYPE','LENGTH','WIDTH']
        drop="ITALY,ROADSTER"
        verify(0,'1of13records,Page1of1',r1_col,drop,"Step03")
        
        """
        Step04: Click the drop down control on the Combo Box,then select the All entry.
        Expect to see all data displayed.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1","visible_text",'[All]')
        r1_col=['COUNTRY','CAR','BODYTYPE','LENGTH','WIDTH']
        drop="[All]"
        verify(0,'13of13records,Page1of1',r1_col,drop,"Step04")
        
        
if __name__ == '__main__':
    unittest.main()


