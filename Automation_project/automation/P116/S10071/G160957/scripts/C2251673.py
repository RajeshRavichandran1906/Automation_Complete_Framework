'''
Created on Jan 22, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251673
@author: BM13368
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity

class C2251673_TestClass(BaseTestCase):

    def test_C2251673(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251673'
        active_fex_name ='sort_checkbox.fex'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
            Step 01:Execute the attached Document repro - sort_listbox.fex.
            Expect to see the initial 1000 line report for ggorder.
        """
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_3", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        """
            Step 01:Execute the attached Document repro - sort_checkbox.fex
            Expect to see the initial 1000 line report for ggorder.
            Verify that each Check Box displays its values in Descending order.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 01:01: Verify the Report Heading shows 1000of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01:02: Verify the column heading')
         
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 01:03: Verify report data",desired_no_of_rows=20)
        """
            Verify that each List Box displays its values in Descending order.
        """
        check1_values=['[All]', '1000', '999', '998', '997', '996', '995', '994', '993', '992', '991', '990']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_1_cs', check1_values, "Step 01:01:Verify checkbox1 values", default_selected_check='[All]')
          
        check2_values=['[All]', '11:59:59PM', '10:23:24PM', '12:13:14PM', '01:02:03AM']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_2_cs', check2_values, "Step 01:02:Verify checkbox2 values", default_selected_check='[All]')
          
        check3_values=['[All]', '1996/153', '1996/122', '1996/092', '1996/061', '1996/032', '1996/001']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_3_cs', check3_values, "Step 01:03:Verify checkbox3 values", default_selected_check='[All]')
          
        check4_values=['[All]', 'R1250', 'R1248', 'R1244', 'R1200', 'R1109', 'R1100', 'R1088', 'R1044', 'R1041', 'R1040', 'R1020', 'R1019']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_4_cs', check4_values, "Step 01:04:Verify checkbox4 values", default_selected_check='[All]')
          
        check5_values=['[All]', '140.00%', '125.00%', '96.00%', '81.00%', '76.00%', '58.00%', '28.00%', '26.00%', '17.00%', '13.00%']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_5_cs', check5_values, "Step 01:05:Verify checkbox5 values", default_selected_check='[All]')
          
        check6_values=['[All]', '$1,139.00', '$1,124.00', '$1,123.00', '$1,109.00', '$1,108.00', '$1,094.00', '$1,093.00']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_6_cs', check6_values, "Step 01:06:Verify checkbox6 values", default_selected_check='[All]')
        """ 
            Step 02:For the top row left Check Box, which controls Integer field - Order Number, scroll down and select the value 975.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_1_cs', ['975'], scroll_down_times=14)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see a single row for Order Number - 975, as that column contains only unique values.
        """
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', 'Step 02:01: Verify the Report Heading shows 1of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx","Step 02:03: Verify report data")
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_1_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 02:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 02:05: Verify report data",desired_no_of_rows=20)
        """ 
            Step 03:For the middle row left Check Box, which controls Datetime field - HHISA, select value 10:23:24PM.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_2_cs', ['10:23:24PM'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see the report display 5 rows for HHISA - 10:23:24PM.
        """
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', 'Step 03:01: Verify the Report Heading shows 5of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx","Step 03:03: Verify report data")
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_2_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 03:05: Verify report data",desired_no_of_rows=20)
         
        """ 
            Step 04:For the bottom row left Check Box, which controls Date field - ORDER_YYJUL, select value 1996/153.
            Reset the Check Box to the ALL option for the next test.
            Expect to see the report display 100 rows for ORDER_YYJUL - 1996/153.
            Currently, Check Box Filtering is not working for Dashboard filtering of Date fields.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['1996/153'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see the report display 5 rows for HHISA - 10:23:24PM.
        """
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', 'Step 04:01: Verify the Report Heading shows 100of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx","Step 04:03: Verify report data", desired_no_of_rows=20)
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 04:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 04:05: Verify report data",desired_no_of_rows=20)
         
        """ 
            Step 05:For the upper row right Check Box, which controls alphanumeric Store Code field, select value R1244.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_4_cs', ['R1244'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see the report display 75 rows for Store Code - R1244.
        """
        miscelanousobj.verify_page_summary(0, '75of1000records,Page1of2', 'Step 05:01: Verify the Report Heading shows 75of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx","Step 05:03: Verify report data", desired_no_of_rows=20)
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_4_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 05:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 05:05: Verify report data",desired_no_of_rows=20)
        """ 
            Step 06:For the middle row right Check Box, which controls numeric field - DECIMAL6, scroll down and select value 28.00%.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_5_cs', ['28.00%'], scroll_down_times=3)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see the report display 148 rows for DECIMAL6 - 28.00%.
        """
        miscelanousobj.verify_page_summary(0, '148of1000records,Page1of3', 'Step 06:01: Verify the Report Heading shows 75of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx","Step 06:03: Verify report data", desired_no_of_rows=20)
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_5_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 06:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 06:05: Verify report data",desired_no_of_rows=20)
        """    
            Step 07:For the bottom row right Check Box, which controls Packed data field - PACKED7, select value $1,093.00.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_6_cs', ['$1,093.00'], scroll_down_times=3)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
          
        """
            Expect to see the report display 2 rows for PACKED7 - $1,093.00.
        """
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', 'Step 06:01: Verify the Report Heading shows 75of1000records')
        column_list=['Order Number', 'Store Code', 'HHISA', 'ORDER_YYJUL','DECIMAL6', 'PACKED7']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx","Step 06:03: Verify report data")
        """
            Reset the Check Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_6_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 06:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 06:05: Verify report data",desired_no_of_rows=20)
        
if __name__ == "__main__":
    unittest.main()