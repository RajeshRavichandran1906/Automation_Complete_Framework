'''
Created on Jan19, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251703
TestCase Name = AHTML: Document with Radio Button performs very slowly on volume file. (ACT-529).
'''
import unittest,time,datetime
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_run
from common.lib import utillity


class C2251703_TestClass(BaseTestCase):

    def test_C2251703(self):
        Test_Case_ID = 'C2251703'
        """
        Step 01: Execute the attached repro act-529.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        utillobj.active_run_fex_api_login('act-529.fex','S10071_4','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
        """
        Expect to see the following Document, containing a 2500 row report and three Filter controls,
         all tied to the report.
        The Combo Box, Radio Button and Check Box filters should all select a record near 
        the bottom of the report and return to All records in virtually the same time.
        """
        def verify(r1,r1_sum,r1_col,radio,radio_defau,drop,check,check_defau,step):
            #1st Report
            active_misobj.verify_page_summary(r1,r1_sum,step+".1a: Verify the Report Heading of 1st Report")
            active_misobj.verify_column_heading('ITableData'+str(r1), r1_col, step+'.1b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r1), Test_Case_ID+'_Ds'+step+'.1.xlsx', step+'.1c: Verify data.')
            #Combo Box Filter
            utillobj.verify_dropdown_value("#combobox_dsPROMPT_3",expected_default_selected_value=drop ,default_selection_msg=step+".2: Verify Dropdown IS SHOWING")
            #Check Box
            ia_runobj.verify_active_dashboard_prompts("check_box","#PROMPT_2_cs",check, step+".3: Verify check box IS SHOWING",default_selected_check=check_defau)
            
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='[All]'
        drop='[All]'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        verify(0,'2500of2500records,Page1of44',r1_col,radio,radio_defau,drop,check,check_defau,"Step01")
        #RadioButton
        ia_runobj.verify_active_dashboard_prompts("radio","#PROMPT_1_cs",radio, "Step01.4: Verify Radio button", default_selected_check=radio_defau)
            
        """
        Step02: From the Combo Box, click the drop down and use the scroll bar to go to the bottom of the list.
        Select the last record, the value doesn't matter. 
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_3","visible_text",'Buochs')
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='[All]'
        drop='Buochs'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        verify(0,'1of2500records,Page1of1',r1_col,radio,radio_defau,drop,check,check_defau,"Step02")
        #RadioButton
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#PROMPT_1_cs",['[All]'], "Step02.4: Verify Radio button")
        
        """
        Step03: Use the scroll bar to return to the top of the Combo Box list and select All.
        Expect to see the full report listed again, with 2500 records.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_3","visible_text",'[All]')
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='[All]'
        drop='[All]'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        element_css="table[id='IWindowBody0'] .arGridBar table>tbody>tr>td[align='left'] table tr td:nth-child(2)"
        utillobj.synchronize_with_visble_text(element_css, "2500of2500records,Page1of44", 20)
        verify(0,'2500of2500records,Page1of44',r1_col,radio,radio_defau,drop,check,check_defau,"Step03")
        #RadioButton
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#PROMPT_1_cs",['[All]'], "Step03.4: Verify Radio button")
         
        """
        Step04: From the Radio Button, use the scroll bar to go to the bottom of the list. 
        Select the last value, which should be the same as the value used in the Combo Box.
        The Radio Button filter should select a record at the bottom of the report as quickly as the Combo Box selection.
        """
        ia_runobj.select_active_dashboard_prompts('radio',"#PROMPT_1_cs",['Buochs'])
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='Buochs'
        drop='[All]'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        verify(0,'1of2500records,Page1of1',r1_col,radio,radio_defau,drop,check,check_defau,"Step04")
        #RadioButton
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#PROMPT_1_cs",['Buochs'], "Step04.4: Verify Radio button")
         
        """
        Step05: Use the scroll bar to return o the top of the Radio Button list and select All.
        Expect to see the full report listed again, with 2500 records.
        """
        ia_runobj.select_active_dashboard_prompts('radio',"#PROMPT_1_cs",['[All]'])
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='[All]'
        drop='[All]'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        verify(0,'2500of2500records,Page1of44',r1_col,radio,radio_defau,drop,check,check_defau,"Step05")
        #RadioButton
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#PROMPT_1_cs",['[All]'], "Step05.4: Verify Radio button")
         
        """
        Step06: From the Check Box, use the scroll bar to go to the bottom of the list.
        Select the last value, which should be the same as the value used in the Combo Box and Radio Box steps.
        The Check Box filter should select a record at the bottom of the report as quickly as the Radio Button selection.
        """
        ia_runobj.select_active_dashboard_prompts('check',"#PROMPT_2_cs",['Buochs'])
        r1_col=['Customer City','Revenue']
        radio=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        radio_defau='[All]'
        drop='[All]'
        check=['[All]', "'S Gravenvoeren", "'S-Gravenhage"]
        check_defau='[All]'
        verify(0,'1of2500records,Page1of1',r1_col,radio,radio_defau,drop,check,check_defau,"Step06")
        #Check box
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("check","#PROMPT_2_cs",['Buochs'], "Step06.4: Verify Check box")
        #RadioButton
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#PROMPT_1_cs",['[All]'], "Step06.5: Verify Radio button")
         
        
if __name__ == '__main__':
    unittest.main()


