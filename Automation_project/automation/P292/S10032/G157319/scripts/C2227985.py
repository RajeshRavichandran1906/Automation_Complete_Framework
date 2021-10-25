'''
Created on AUG 18, 2017

@author: Pavithra/updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227985
TestCase Name = AHTML: Extended Decimal Datatype - Floating Point/Packed Decimal field variations.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2227985_TestClass(BaseTestCase):

    def test_C2227985(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227985'
        
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name1="AR_RP_EXTENDED_FLOATING_Formats.fex"
        fex_name2="AR_RP_EXTENDED_PACKED_Formats.fex"
         
        """
           Step 01:Sign in to WebFOCUS using the below link. http://machine:port/ibi_apps as basic user
           Step 02:Execute the attached Fex - AR-RP-EXTENDED-FLOATING-Formats
        """
        active_reportobj.run_active_report_using_api(fex_name1, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02.1:  1000of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", "Step 02.2:AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=20)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 02.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 02.4: Verify column heading')
         
        """
        Step 03:For each of the columns, left click on the first row and select Filter Cell.
                After Filter Cell for each column, left-click and select
                Clear Remove Cell Filter to return to the initial 1000 rows.
                 
                Expect to see the following count of rows by column:
                D17.4 - 1
                D22.8 - 1
                D25.6 - 84
                D19.10 - 1
                D30.12 - 1
                D32.15 - 84
                D34.30 - 84
                D34.26 - 1
        """
         
        #D17.4 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.1: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx", "Step 03.2:Verify D17.4 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.4: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Remove Cell Filter")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.4.1: AAR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #D22.8 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.5: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx", "Step 03.6:Verify D22.8 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.7 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.8: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.8.1:AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # D25.6 - 84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.9: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds04.xlsx",desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds04.xlsx", "Step 03.10:Verify D25.6 - 84 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.11 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.12: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.12.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #D19.10 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.13: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds05.xlsx", "Step 03.14:Verify D19.10 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.15 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.16: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.16.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #D30.12 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.17: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds06.xlsx", "Step 03.18:Verify D30.12 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.19 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.20: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.20.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # D32.15 - 84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.21: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds07.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds07.xlsx", "Step 03.22:Verify D32.15 - 84 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.23 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.24: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.24.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #D34.30 - 84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.25: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds08.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds08.xlsx", "Step 03.26:Verify D34.30 - 84 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.27 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.28: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.28.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #D34.26 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.29: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds09.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds09.xlsx", "Step 03.30:Verify D34.26 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 03.31 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.32: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.32.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        """
            Step 04:Clear the previous Filter panel. For the D17.4 column drop down, select the Filter option.
                    Select Equals, then select values .1760, .5062, .7520 & 1.0172.
                    Click the Filter button.
                    
                    Expect to see a 4 row filtered report.
        """
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='.1760',value2='.5062',value3='.7520',value4='1.0172')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 04.1:verify 4of1000records,Page1of1 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds10.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds10.xlsx", "Step 04.2:Verify  4 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 04.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 04.4: Verify column heading')
         
        """
            Step 05:Clear the previous filter panel.For the D22.8 column drop down, select the Filter option.
                    Select Not equal, then select value 50.12345678.
                    Click the Filter button.
                    
                    Expect to see a 997 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 05.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Not equal")
        filterselectionobj.create_filter(1, 'Not equal','large',value1='50.12345678')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '997of1000records,Page1of18', "Step 05.1:verify 997of1000records,Page1of18 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds11.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds11.xlsx", "Step 05.2:Verify 997 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 05.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 05.4: Verify column heading') 
         
        """
            Step 06:Clear the previous filter panel. For the D25.6 column drop down, select the Filter option.
                    Select Greater than, then select value 7,600,000,000.123456.
                    Click the Filter button.
                    
                    Expect to see a 418 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 06:0  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 06.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Greater than")
        filterselectionobj.create_filter(1, 'Greater than',value1='7,600,000,000.123456')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '418of1000records,Page1of8', "Step 06.1:verify 418of1000records,Page1of8 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds12.xlsx",desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds12.xlsx", "Step 06.2:Verify  418 rows data verification",desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 06.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 06.4: Verify column heading') 
         
        """
            Step 07:Clear the previous filter panel.For the D19.10 column drop down, select the Filter option.
                    Select Greater than or equal to, then select value 1,000,050.5134567891.
                    Click the Filter button.
                    
                    Expect to see a 962 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 07.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 07.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to','large',value1='1,000,050.5134567891')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '962of1000records,Page1of17', "Step 07.1:verify 962of1000records,Page1of17 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds13.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds13.xlsx", "Step 07.2:Verify 962 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 07.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 07.4: Verify column heading') 
         
        """
        Step 08:Clear the previous filter panel.For the D30.12 column drop down, select the Filter option.
                Select Less than, then select value 45.123456789123.
                Click the Filter button.
                
                Expect to see a 38 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 08.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 08.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        filterselectionobj.create_filter(1, 'Less than','large',value1='45.123456789123')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '38of1000records,Page1of1', "Step 08.1:verify 962of1000records,Page1of1 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds14.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds14.xlsx", "Step 08.2:Verify 38 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 08.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 08.4: Verify column heading') 
         
        """
            Step 09:Clear the previous filter panel. For the D32.15 column drop down, select the Filter option.
                    Select Less than or equal to, then select value 2,600,000,000.123456954956055.
                    Click the Filter button.
                    
                    Expect to see a 317 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 09.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 09.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2,600,000,000.123456954956055')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 09.1:verify 317of1000records,Page1of6 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds15.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds15.xlsx", "Step 09.2:Verify 317 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 09.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 09.4: Verify column heading') 
         
        """
            Step 10:Clear the previous filter panel.For the D34.30 column drop down, select the Filter option.
            Select Between, then select .703456789123456771584130819974 for the first value and .883456789123456820433943903481
            for the second value.
            Click the Filter button.
            
            Expect to see a 117 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 10.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Between")
        filterselectionobj.create_filter(1, 'Between',value1='.703456789123456771584130819974',value2='.883456789123456820433943903481')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '117of1000records,Page1of3', "Step 10.1:verify 117of1000records,Page1of3 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds16.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds16.xlsx", "Step 10.2:Verify 117 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 10.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 10.4: Verify column heading') 
         
        """
            Step 11.Clear the previous filter panel.For the D34.26 column drop down, select the Filter option.
                Select Not Between, then select 10,025.21345678912257426418364048 for the first value and
                10,062.13345678912264702375978231 for the second value.
                Click the Filter button.
                
                Expect to see a 936 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 11.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Not Between")
        filterselectionobj.create_filter(1, 'Not Between','large',value1='10,025.21345678912257426418364048',value2='10,062.13345678912264702375978231')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '936of1000records,Page1of17', "Step 11.1:verify 117of1000records,Page1of3 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds17.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds17.xlsx", "Step 11.2:Verify 936 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedDecimal'], "Step 11.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'D17.4', 'D22.8', 'D25.6', 'D19.10', 'D30.12', 'D32.15', 'D34.30', 'D34.26']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 11.4: Verify column heading') 
         
        """
            Step 12:Execute the attached Fex - AR-RP-EXTENDED-PACKED-Formats
        """
        utillobj.infoassist_api_logout()
        resultobj.wait_for_property("#SignonbtnLogin", 1)
        active_reportobj.run_active_report_using_api(fex_name2, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 12.1:  1000of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds18.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds18.xlsx", "Step 12.2:AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=20)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 12.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 12.4: Verify column heading')
         
        """
        Step 13:For each of the columns, left click on the first row and select Filter Cell.
                Expect to see the following count of rows by column:
 
                P17.4 - 1
                P22.8 - 1
                P25.6 - 84
                P19.10 - 1
                P30.12 - 1
                P32.15 - 84
                P34.30 - 84
                P34.26 - 1
        """
         
        # P17.4 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 13.1: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds19.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds19.xlsx", "Step 13.2:Verify P17.4 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.4: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Remove Cell Filter")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.4.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        #P22.8 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 13.5: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds20.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds20.xlsx", "Step 13.6:Verify P22.8 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.7 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.8: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.8.1:AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # P25.6 - 84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 13.9: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds21.xlsx",desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds21.xlsx", "Step 13.10:Verify P25.6 - 84 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.11 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.12: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.12.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # P19.10 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 13.13: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds22.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds22.xlsx", "Step 13.14:Verify P19.10 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.15 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.16: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.16.1: AR-RP-EXTENDED-PACKED--Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # P30.12 - 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 13.17: 1of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds23.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds23.xlsx", "Step 13.18:Verify P30.12 - 11 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.19 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.20: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.20.1: AR-RP-EXTENDED-PACKED--Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
                
        # P32.15 - 84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 13.21: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds24.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds24.xlsx", "Step 13.22:Verify P32.15 - 84 row data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.23 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.24: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.24.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # P34.27-84
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 13.25: 84of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds25.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds25.xlsx", "Step 13.26:Verify P34.30 - 84 row data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.27 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.28: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.28.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        # P34.30- 1
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 9)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 13.29: 1of1000records,Page1of2 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds26.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds26.xlsx", "Step 13.30:Verify P34.26 - 1 row data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 13.31 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.32: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 13.32.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
         
        """
            Step 14:For the P17.4 column drop down, select the Filter option.Select Equals, then select values .1760, .5062, .7120 & 1.0172.
                    Click the Filter button.
                    
                    Expect to see a 4 row filtered report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='.1760',value2='.5062',value3='.7120',value4='1.0172')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 14.1:verify 4of1000records,Page1of1 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds27.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds27.xlsx", "Step 14.2:Verify  4 rows data verification")        
        utillobj.verify_run_time_title('ITableData0',  ['Datatype-ExtendedPackedDecimal'], "Step 14.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 14.4: Verify column heading')
         
        """
            Step 15:Clear the previous filter panel.For the P22.8 column drop down, select the Filter option.
                    Select Not equal, then select value 50.12345678.
                    Click the Filter button.
                    
                    Expect to see a 997 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 15.0.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Not equal")
        filterselectionobj.create_filter(1, 'Not equal','large',value1='50.12345678')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '997of1000records,Page1of18', "Step 15.1:verify 997of1000records,Page1of18 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds28.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds28.xlsx", "Step 15.2:Verify 997 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 15.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 15.4: Verify column heading') 
         
        """
            Step 16:Clear the previous filter panel.For the P25.6 column drop down, select the Filter option.
                    Select Greater than, then select value 7600000000.123456.
                    Click the Filter button.
                    
                    Expect to see a 418 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 16:0  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 16.0.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Greater than")
        filterselectionobj.create_filter(1, 'Greater than',value1='7600000000.123456')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '418of1000records,Page1of8', "Step 16.1:verify 418of1000records,Page1of8 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds29.xlsx",desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds29.xlsx", "Step 16.2:Verify  418 rows data verification",desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 16.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 06.4: Verify column heading') 
         
        """
            Step 17:Clear the previous filter panel.For the P19.10 column drop down, select the Filter option.
                    Select Greater than or equal to, then select value 1000050.5134567891.
                    Click the Filter button.
                     
                    Expect to see a 962 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 17.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 17.0.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to','large',value1='1000050.5134567891')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '962of1000records,Page1of17', "Step 17.1:verify 962of1000records,Page1of17 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds30.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds30.xlsx", "Step 17.2:Verify 962 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 17.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 17.4: Verify column heading') 
         
        """
            Step 18:Clear the previous filter panel.For the P30.12 column drop down, select the Filter option.
                    Select Less than, then select value 45.123456789123.
                    Click the Filter button.
                     
                    Expect to see a 38 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 18.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 18.0.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        filterselectionobj.create_filter(1, 'Less than','large',value1='45.123456789123')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '38of1000records,Page1of1', "Step 18.1:verify 962of1000records,Page1of1 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds31.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds31.xlsx", "Step 18.2:Verify 38 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 18.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 18.4: Verify column heading') 
        
        """
            Step 19:Clear the previous filter panel.For the P32.15 column drop down, select the Filter option.
                    Select Less than or equal to, then select value 2600000000.123456789123456.
                    Click the Filter button.
                    
                    Expect to see a 317 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 19.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 19.0.1: AR-RP-EXTENDED-PACKED-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='2600000000.123456789123456')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 19.1:verify 317of1000records,Page1of6 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds32.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds32.xlsx", "Step 19.2:Verify 317 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 19.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 19.4: Verify column heading') 
        
        """
            Step 20:Clear the previous filter panel.For the P34.27 column drop down, select the Filter option.
                    Select Between, then select .703456789123456789123456789123 for the first value and 
                    .883456789123456789123456789123 for the second value.
                    Click the Filter button.
                    
                    Expect to see a 117 row filtered report.
        """
        
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 20.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 20.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Between")
        filterselectionobj.create_filter(1, 'Between',value1='.703456789123456789123456789123',value2='.883456789123456789123456789123')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '117of1000records,Page1of3', "Step 20.1:verify 117of1000records,Page1of3 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds33.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds33.xlsx", "Step 20.2:Verify 117 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 20.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 10.4: Verify column heading') 
        
        """
            Step 21:Clear the previous filter panel.For the P34.30 column drop down, select the Filter option.
                    Select Not Between, then select 10025.21345678912345678912345600 for the first value and
                    10062.13345678912345678912345600 for the second value.
                    Click the Filter button.
                    
                    Expect to see a 936 row filtered report.
                    
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 21.0:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_2.xlsx", "Step 21.0.1: AR-RP-EXTENDED-FLOATING-Formats.fex data verification", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Not Between")
        filterselectionobj.create_filter(1, 'Not Between','large',value1='10025.21345678912345678912345600',value2='10062.13345678912345678912345600')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '936of1000records,Page1of17', "Step 21.1:verify 117of1000records,Page1of3 Active Report. - page summary verification.")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds34.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds34.xlsx", "Step 21.2:Verify 962 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-ExtendedPackedDecimal'], "Step 21.3 ",custom_css="[id^='THEAD']")
        expected_list=['Order Number INTEGER', 'P17.4', 'P22.8', 'P25.6', 'P19.10', 'P30.12', 'P32.15', 'P34.27', 'P34.30']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 21.4: Verify column heading') 
        time.sleep(3)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
         
if __name__ == '__main__':
    unittest.main()
               
        