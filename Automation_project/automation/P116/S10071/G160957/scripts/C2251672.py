'''
Created on Jan 21, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251672
@author: BM13368
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity

class C2251672_TestClass(BaseTestCase):

    def test_C2251672(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251672'
        active_fex_name ='sort_listbox.fex'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
            Step 01:Execute the attached Document repro - sort_listbox.fex.
            Expect to see the initial 1000 line report for ggorder.
        """
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_3", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 01:01: Verify the Report Heading shows 1000of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01:02: Verify the column heading')
         
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 01:03: Verify report data",desired_no_of_rows=20)
        """
            Verify that each List Box displays its values in Descending order.
        """
        list1_values=['[All]', '1000', '999', '998', '997', '996', '995', '994', '993', '992', '991', '990', '989']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_1_cs', list1_values, "Step 01:01:Verify listbox1 values")
        
        list2_values=['[All]', 'JUNE  1, 1996', 'MAY  1, 1996', 'APRIL  1, 1996', 'MARCH  1, 1996', 'FEBRUARY  1, 1996', 'JANUARY  1, 1996']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_2_cs', list2_values, "Step 01:02:Verify listbox2 values")
          
        list3_values=['[All]', '04 Oct 13', '14 Jul 13', '04 Apr 13', '01 Jan 13']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_3_cs', list3_values, "Step 01:03:Verify listbox3 values")
           
        list4_values=['[All]', 'R1250', 'R1248', 'R1244', 'R1200', 'R1109', 'R1100', 'R1088', 'R1044', 'R1041', 'R1040', 'R1020', 'R1019']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_4_cs', list4_values, "Step 01:04:Verify listbox4 values")
           
        list5_values=['[All]', '$0,000,140.00', '$0,000,125.00', '$0,000,096.00', '$0,000,081.00', '$0,000,076.00', '$0,000,058.00']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_5_cs', list5_values, "Step 01:05:Verify listbox5 values")
           
        list6_values=['[All]', '(13.00)', '(17.00)', '(26.00)', '(28.00)', '(58.00)', '(76.00)', '(81.00)', '(96.00)', '(125.00)', '(140.00)']
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_6_cs', list6_values, "Step 01:06:Verify listbox6 values")
        """   
            Step 02:For the top row left List Box, which controls Integer field - Order Number, select the value 999.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_1_cs', ['999'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
          
        """
            Expect to see a single row for Order Number - 999, as that column contains only unique values.
        """
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', 'Step 02:01: Verify the Report Heading shows 1of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx","Step 02:03: Verify report data")
        """
            Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_1_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 02:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 02:05: Verify report data",desired_no_of_rows=20)
        """ 
            Step 03:For the middle row left List Box, which controls Date field - ORDER_MTRDYY, select value APRIL 1, 1996
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['APRIL 1, 1996'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        """
            Expect to see the report display 180 rows for ORDER_MTRDYY - APRIL 1, 1996.
        """
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', 'Step 03:01: Verify the Report Heading shows 180of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx","Step 03:03: Verify report data")
        """
            Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 03:05: Verify report data",desired_no_of_rows=20)
           
        """ 
            Step 04:For the bottom row left List Box, which controls Datetime field - HDMTY, select value 04 Oct 13.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_3_cs', ['04 Oct 13'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        """
            Expect to see the report display 10 rows for HDTMY - 04 Oct 13.
        """
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', 'Step 04:01: Verify the Report Heading shows 10of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx","Step 04:03: Verify report data")
        """
            Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_3_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 04:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 04:05: Verify report data",desired_no_of_rows=20)
        """ 
            Step 05:For the upper row right List Box, which controls alphanumeric Store Code field, scroll to the bottom of the List Box values and select R1020.
               
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_4_cs', ['R1020'], scroll_down_times=4)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        """
            Expect to see the report display 90 rows for Store Code - R1020.
        """
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', 'Step 05:01: Verify the Report Heading shows 10of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx","Step 05:03: Verify report data")
        """
            Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_4_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 05:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 05:05: Verify report data",desired_no_of_rows=20)
#          
        """    
            Step 06:For the middle row right List Box, which controls numeric field - DECIMAL2, select value $0,000,140.00
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_5_cs', ['$0,000,140.00'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        """
            Expect to see the report display 67 rows for DECIMAL2 - $0,000,140.00.
        """
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', 'Step 06:01: Verify the Report Heading shows 10of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx","Step 06:03: Verify report data", desired_no_of_rows=20)
        """
           Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_5_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 06:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 06:05: Verify report data",desired_no_of_rows=20)
        """    
            Step 07:For the bottom row right List Box, which controls Packed data field - PACKED4, select value (17.00).
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_6_cs', ['(17.00)'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        """
            Expect to see the report display 99 rows for PACKED4 - (17.00).
        """
        miscelanousobj.verify_page_summary(0, '99of1000records,Page1of2', 'Step 07:01: Verify the Report Heading shows 10of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_MTRDYY', 'HDMTY','DECIMAL2', 'PACKED4']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx",desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx","Step 07:03: Verify report data",desired_no_of_rows=20)
        """
            Reset the List Box to the ALL option for the next test.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_6_cs', ['[All]'])
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
           
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 07:04: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 07:05: Verify report data",desired_no_of_rows=20)

if __name__ == "__main__":
    unittest.main()