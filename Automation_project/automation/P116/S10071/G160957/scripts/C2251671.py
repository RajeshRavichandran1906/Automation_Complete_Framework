'''
Created on Jan 18, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251671
@author: BM13368
'''
import unittest, time
from common.lib import utillity
from common.pages import active_miscelaneous
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import Select

class C2251671_TestClass(BaseTestCase):

    def test_C2251671(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251671'
        active_fex_name ='sort_dropdown.fex'
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01:Execute the attached Document repro - sort_dropdown.fex.
            Expect to see the initial 1000 line report for ggorder.
        """
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_3", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 01:01: Verify the Report Heading shows 1000of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 01:03: Verify report data",desired_no_of_rows=20)
        """ 
            Step 02:For the top row left Drop Down Box, which controls Integer field - Order Number, first click the arrow to verify that the values are in Descending order.
        """ 
        expected_value='[All]'
        value_list=['[All]', '1000','999','998','997','996','995','994','993', '992']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", value_list=value_list, msg="Step 02:01:Verify the dropdown values are in descending order", expected_default_selected_value=expected_value, default_selection_msg="Step 02:02Verify default selected value shows All in the first dropdown")
            
        """
            Now select value 990 from the list
            Expect to see a single row for Order Number - 990, as that column contains only unique values..
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1", "visible_text", "990")
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', 'Step 02:03: Verify the Report Heading shows 1000of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx","Step 02:05: Verify report data") 
            
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1", "visible_text", '[All]')
        time.sleep(5)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='[All]', default_selection_msg="Step 02:06Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 02:06: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 02:07: Verify report data",desired_no_of_rows=20)
        """ 
            Step 03:For the middle row left Drop Down Box, which controls Alphanumeric field - Store Code, first click the arrow to verify that the values are in Descending order.
        """
        expected_value='[All]'
        value_list=['[All]', 'R1250', 'R1248', 'R1244', 'R1200', 'R1109', 'R1100', 'R1088', 'R1044', 'R1041', 'R1040', 'R1020', 'R1019']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_3", value_list=value_list, msg="Step 03:01:Verify the dropdown values are in descending order", expected_default_selected_value=expected_value, default_selection_msg="Step 03:02:Verify default selected value shows All in the first dropdown")
        """
            Now select value R1088 from the list.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_3", "visible_text", 'R1088')
        time.sleep(5)
        """
            Expect to see the report display 90 rows for Store Code - R1088.
        """
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', 'Step 03:03: Verify the Report Heading shows 90of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx","Step 03:05: Verify report data",desired_no_of_rows=20)
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_3", "visible_text", '[All]')
        time.sleep(5)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_3", expected_default_selected_value='[All]', default_selection_msg="Step 03:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03:07: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 03:08: Verify report data",desired_no_of_rows=20)
        time.sleep(2)
        """ 
            Step 04:For the bottom row left Drop Down Box, which controls Date field - ORDER_YYMD, first click the arrow to verify that the values are in Descending order.
        """
        expected_value='[All]'
        value_list=['[All]', '19960601', '19960501', '19960401', '19960301', '19960201', '19960101']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_5", value_list=value_list, msg="Step 04:01:Verify the dropdown values are in descending order", expected_default_selected_value=expected_value, default_selection_msg="Step 04:02:Verify default selected value shows All in the first dropdown")
        """
            Now select value 19960601 from the list.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_5", "visible_text", '19960601')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        """
            Expect to see the report display 100 rows for ORDER_YYMD - 19960601.
        """
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', 'Step 04:03: Verify the Report Heading shows 90of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx","Step 04:05: Verify report data",desired_no_of_rows=20)
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_5", "visible_text", '[All]')
        time.sleep(5)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_5", expected_default_selected_value='[All]', default_selection_msg="Step 04:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 04:07: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 04:08: Verify report data",desired_no_of_rows=20)
        time.sleep(2)
          
        """
            Step 05:For the upper row right Drop Down Box, which controls Datetime field - HYYMDSA, first click the arrow to verify that the values are in Descending order.
        """
        expected_value='[All]'
        value_list=['[All]', '2013/10/04 1:02:03AM', '2011/03/30 10:23:24PM', '2007/08/08 12:13:14PM', '2002/12/31 11:59:59PM']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_2", expected_default_selected_value=expected_value, default_selection_msg="Step 05.01:Verify default selected value shows All in the first dropdown")
        select_obj=Select(self.driver.find_element_by_css_selector("#combobox_dsPROMPT_2"))
        list_options = select_obj.options
        options = [x.text for x in list_options]
        utillobj.asequal(value_list, options, "Step 05.02:Verify the dropdown values are in descending order")
            
        """
            Now select value 2007/08/08 12:13:14PM from the list.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_2", "visible_text", '2007/08/08 12:13:14PM')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        """
            Expect to see the report display 5 rows for HYYMDSA - 2007/08/08 12:13:14PM.
        """
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', 'Step 05:03: Verify the Report Heading shows 90of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx","Step 05:05: Verify report data")
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_2", "visible_text", '[All]')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_2", expected_default_selected_value='[All]', default_selection_msg="Step 05:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 05:07: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 05:08: Verify report data",desired_no_of_rows=20)
        time.sleep(2)
        """ 
            Step 06:For the middle row right Drop Down Box, which controls numeric field - DECIMAL, first click the arrow to verify that the values are in Descending order.
        """
        expected_value='[All]'
        value_list=['[All]', '140.00', '125.00', '96.00', '81.00', '76.00', '58.00', '28.00', '26.00', '17.00', '13.00']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_4", value_list=value_list, msg="Step 06:01:Verify the dropdown values are in descending order", expected_default_selected_value=expected_value, default_selection_msg="Step 06:02:Verify default selected value shows All in the first dropdown")
        """
            Now select value 26.00 from the list.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_4", "visible_text", '26.00')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        """
            Expect to see the report display 134 rows for DECIMAL - 26.00.
        """
        miscelanousobj.verify_page_summary(0, '134of1000records,Page1of3', 'Step 06:03: Verify the Report Heading shows 90of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx","Step 06:05: Verify report data")
        time.sleep(2)
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_4", "visible_text", '[All]')
        time.sleep(5)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_4", expected_default_selected_value='[All]', default_selection_msg="Step 06:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 06:07: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 06:08: Verify report data",desired_no_of_rows=20)
        time.sleep(2)
        """
            Step 07:For the bottom row right Drop Down Box, which controls Packed data field - PACKED7, first click the arrow to verify that the values are in Descending order.
        """
        expected_value='[All]'
        value_list=['[All]', '$1,139.00', '$1,124.00', '$1,123.00', '$1,109.00', '$1,108.00', '$1,094.00', '$1,093.00', '$1,079.00', '$1,078.00', '$1,075.00']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_6", value_list=value_list, msg="Step 07:01:Verify the dropdown values are in descending order", expected_default_selected_value=expected_value, default_selection_msg="Step 07:02:Verify default selected value shows All in the first dropdown")
        """
            Now select value $1,075.00 from the list.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_6", "visible_text", '$1,075.00')
        time.sleep(1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 .arGrid [id^='TCOL']", 6, 65)
        """
            Expect to see a single row for PACKED7 - $1,075.00, as that column contains only unique values.
        """
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', 'Step 07:03: Verify the Report Heading shows 90of1000records')
        column_list=['Order Number', 'Store Code', 'ORDER_YYMD', 'DECIMAL', 'PACKED7', 'HYYMDSA']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07:04: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds07.xlsx","Step 07:05: Verify report data")
        time.sleep(2)
        """
            Reset the Drop Down Box to the ALL option for the next test.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_6", "visible_text", '[All]')
        time.sleep(5)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_6", expected_default_selected_value='[All]', default_selection_msg="Step 07:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 07:07: Verify the Report Heading shows 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 07:08: Verify report data",desired_no_of_rows=20)

if __name__ == "__main__":
    unittest.main()