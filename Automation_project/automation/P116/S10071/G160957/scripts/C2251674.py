'''
Created on Jan 22, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251674
@author: Praveen Ramkumar
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity

class C2251674_TestClass(BaseTestCase):

    def test_C2251674(self):
        
        """ TESTCASE VARIABLES """
        
        Test_Case_ID = 'C2251674'
        active_fex_name ='sort_radiobutton.fex'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """
            Step 01:Execute the attached Document repro - sort_radiobutton.fex.
            Expect to see the initial 1000 line report for ggorder.
            Verify that each Radio Button box displays its values in Descending order.
        """
        
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_3", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 [class='arGrid']", 1, 65)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 01:01:verify_page_summary 1000of1000records,Page1of18')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        list1_values=['[All]', '1000', '999', '998', '997', '996', '995', '994', '993', '992', '991', '990', '989']
        ia_runobj.verify_active_dashboard_prompts('radio', '#PROMPT_1_cs', list1_values, "Step 01:04:Verify radiobox1 values")
        list2_values=['[All]', '2013', '2002']
        ia_runobj.verify_active_dashboard_prompts('radio', '#PROMPT_3_cs', list2_values, "Step 01:05:Verify radiobox2 values")
                
        """
            Step 02:For the top row left Radio Button, which controls Integer field - Order Number, scroll down to the bottom of the list and select the value 2.
            Reset the Radio Button to the ALL option for the next test..
            Expect to see a single row for Order Number - 2, as that column contains only unique values.
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_1_cs', ['2'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', 'Step 02:01:verify_page_summary 1of1000records,Page1of1')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_1_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 02:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 03:For the middle row left Radio Button, which controls Date field - ORDER_WRMTRDYY, select value Saturday, June 1 1996.
            Reset the Radio Button to the ALL option for the next test.Expect to see the report display 100 rows for ORDER_WRMTRDYY - Saturday, June 1 1996.
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_2_cs', ['Saturday, June  1 1996'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
#         miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', 'Step 03:01:verify_page_summary 100of1000records,Page1of2')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds03.xlsx")
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_2_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 04:For the bottom row left Radio Button, which controls Datetime field - HYY, select value 2013.
            Reset the Radio Button to the ALL option for the next test.Expect to see the report display 10 rows for HYY - 2013.        
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_3_cs', ['2013'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', 'Step 04:01:verify_page_summary 10of1000records,Page1of1')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds04.xlsx")
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_3_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 04:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 05:For the upper row right Radio Button, which controls alphanumeric Store Code field, select value R1250.
            Reset the Radio Button to the ALL option for the next test.Expect to see the report display 75 rows for Store Code - R1250.
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_4_cs', ['R1250'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '75of1000records,Page1of2', 'Step 05:01:verify_page_summary 75of1000records,Page1of2')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds05.xlsx")
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_4_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 05:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 06:For the middle row right Radio Button, which controls numeric field - DECIMAL5, scroll down and select value 26.00 CR.
            Reset the Radio Button to the ALL option for the next test.Expect to see the report display 134 rows for DECIMAL5 - 26.00 CR.
        """
                        
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_5_cs', ['26.00 CR'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '134of1000records,Page1of3', 'Step 06:01:verify_page_summary 134of1000records,Page1of3')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06.02: Verify the column heading')

#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds06.xlsx")
        
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_5_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 06:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
        """
            Step 07:For the bottom row right Radio Button, which controls Packed data field - PACKED3, scroll to the bottom and select value $000,013.00.
            Reset the Radio Button to the ALL option for the next test.Expect to see the report display 84 rows for PACKED3 - $000,013.00.        
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_6_cs', ['$000,013.00'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', 'Step 07:01:verify_page_summary 84of1000records,Page1of2')
        column_list=['Order Number', 'ORDER_WRMTRDYY', 'HYY', 'Store Code', 'DECIMAL5', 'PACKED3']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07.02: Verify the column heading')
#         utillobj.create_table_data('ITableData0', Test_Case_ID+"_Ds07.xlsx")
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds07.xlsx")

        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_6_cs', ['[All]'])
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 07:03:verify_page_summary 1000of1000records,Page1of18')
        utillobj.verify_table_data('ITableData0', Test_Case_ID+"_Ds01.xlsx")
        
                
if __name__ == "__main__":
    unittest.main()