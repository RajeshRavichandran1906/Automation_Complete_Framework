'''
Created on AUG 10, 2017

@author: Pavithra/Updated by:Bhagavathi
Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227979&group_by=cases:section_id&group_order=asc&group_id=157319
TestCase Name = AHTML: Datatype - DATE format variations.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report

class C2227979_TestClass(BaseTestCase):

    def test_C2227979(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227979'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        
        fex_name="AR_RP_DATE_Formats.fex"
        parent_table_css='ITableData0'
        filter_dialog_css="#wall1 .arWindowBar td[class='arWindowBarTitle']"
        parent_table_column_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        page_summary_css="table[id='IWindowBody0'] .arGridBar table>tbody td>table>tbody>tr>td:nth-child(2)"
        runtime_report_title=['DatatypeFormat=DATE']
        exp_column_heading_list=['Order Number INTEGER', 'Order Date YYMD', 'Order Date DMYY', 'Order Date MDYY', 'Order Date YYBMBD', 'Order Date YY-M-D', 'Order Date I8M|D|YY', 'Order Date I8MtDYY', 'MTRDYY Order Date', 'YYJUL Order Date', 'JULIAN Order Date', 'QYY Order Date', 'wrMtrYY Order Date', 'Mtr Order Date', 'Wtr Order Date']
        expire_time=60
        exp_number=15
        filterdlg_exp_number=1
        row_num=0
        page_num=0
        
        def verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, step_num):
            miscelanousobj.verify_page_summary(page_num, exp_report_title, 'Step' + str(step_num) + ':01:'+' Verify report shows ' +exp_report_title+' page summary')
#             utillobj.create_data_set(parent_table_css, tr_id, Test_Case_ID+"_Ds"+ds_no+".xlsx")
            utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds"+ds_no+".xlsx")
            utillobj.verify_run_time_title(parent_table_css, runtime_report_title, "Step "+ str(step_num) +':02:',custom_css="[id^='THEAD']") 
            miscelanousobj.verify_column_heading(parent_table_css, exp_column_heading_list,'Step:'+ str(step_num)+':03:'+'Verify column heading')
       
        """
           Step 01:Sign in to WebFOCUS as a basic user using following link
           http://machine:port/ibi_apps
           
           Step 02:Execute the attached Fex - AR_RP_DATE_Formats using the below API URL:
                        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157319%252FDatatypes&BIP_item=AR_RP_DATE_Formats.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        
        """    Expect to see an 18 Page, 1000 line report with 15 columns.    """
        exp_report_title='1000of1000records,Page1of18'
        ds_no='01'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '02')
                
        """
            Step 03:For each of the columns, starting with Order Date YYMD, left click on the first row and select Filter Cell.
                    After Filter Cell for each column, left-click and select
                    Clear Remove Cell Filter to return to the initial 1000 rows.
                    This test does NOT use the Active drop down option menu.    """
        column_num=11
        menu_item_name='Filter Cell'
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, menu_item_name)
        
        """               
                    Expect to see 1 row returned for each column, except for rows:
                    QYY Order Date - 10 rows
                    Mtr Order Date - 169 rows.
                    Wtr Order Date - 354 rows.
        """
        
        exp_report_title='10of1000records,Page1of1'
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        """    QYY Order Date - 10 rows    """
        
        ds_no='02'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '03:01:')
        
        """    Clear Remove Cell Filter to return to the initial 1000 rows.    """
        column_num=11
        menu_item_name='Remove Cell Filter'
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, menu_item_name)
        utillobj.synchronize_with_number_of_element(parent_table_column_css, exp_number, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        time.sleep(3)
        
        """    Mtr Order Date - 169 rows.    """
        column_num=13
        menu_item_name='Filter Cell'
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, menu_item_name)
        exp_report_title='169of1000records,Page1of3'
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        time.sleep(3)
        
        ds_no='03'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '03:02:')
        
        """    Clear Remove Cell Filter to return to the initial 1000 rows.    """
        menu_item_name='Remove Cell Filter'
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, menu_item_name)
        visible_text="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        time.sleep(3)
       
        """    Wtr Order Date - 354 rows.    """
        column_num=14
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, 'Filter Cell')
        exp_report_title="354of1000records,Page1of7"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        time.sleep(3)
        
        ds_no='04'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '03')
        
        miscelanousobj.select_field_menu_items(parent_table_css, row_num, column_num, 'Remove Cell Filter')
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        time.sleep(3)
        
        """
            Step 04:For the Order Date YYMD column drop down, select the Filter option.
                    Select Equals, then value 1996/02/01.
                    Click the Filter button
                    Expect to see 180 rows on the report.
        """
        column_num=1
        miscelanousobj.select_menu_items(parent_table_css, column_num, 'Filter', 'Equals')
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        
        
        filter_row_num=1
        value1="1996/02/01"
        filterselectionobj.create_filter(filter_row_num, 'Equals', value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="180of1000records,Page1of4"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        """    Expect to see 180 rows on the report.    """
        
        ds_no='05'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '04')
         
        """
            Step 05:Close the Filter box. For the Order Date DMYY column drop down, select the Filter option.
                    Select Not equal, then value 26/12/1996.
                    Click the Filter button.
                    Expect to see 999 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no=2
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Not equal")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        filter_row_num=1
        value1='26/12/1996'
        filterselectionobj.create_filter(filter_row_num, 'Not equal',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="999of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='06'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '05')
           
        """
            Step 06:Close the Filter box. For the Order Date MDYY column drop down, select the Filter option.
                    Select Not equal, then value 01/01/1997, 02/01/1996 and 01/10/1997. 
                    Click the Filter button.
                    Expect to see 828 rows on the report.
        """
           
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='3'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Not equal")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        filter_row_num=1
        value1="01/01/1997"
        value2="02/01/1996"
        value3="01/10/1997"
        filterselectionobj.create_filter(filter_row_num, 'Not equal',value1=value1,value2=value2, value3=value3)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="828of1000records,Page1of15"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='07'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '06')
           
        """
            Step 07:Close the Filter box. For the Order Date YYBMBD column drop down, select the Filter option.
                    Select Greater Than, then value 1996 12 25
                    Click the Filter button.
                    Expect to see 7 rows on the report.
        """
           
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='4'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Greater than")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        
        filter_row_num=1
        value1="1996 12 25"
        filterselectionobj.create_filter(filter_row_num, 'Greater than',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="7of1000records,Page1of1"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='08'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '07')
           
        """
            Step 08:Close the Filter box. For the Order Date YY-M-D column drop down, select the Filter option.
                    Select Greater Than or equal to, then value 1996-06-19
                    Click the Filter button.
                    Expect to see 110 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of1"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time*3)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        utillobj.infoassist_api_logout()
        utillobj.synchronize_with_number_of_element("input[id=SignonUserName]", 1, 85)
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
               
        col_no='5'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Greater than or equal to")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        
        value1="1996-06-19"
        filterselectionobj.create_filter(filter_row_num, 'Greater than or equal to',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="110of1000records,Page1of2"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time*2)
        
        ds_no='09'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '08')

        """
            Step 09:Close the Filter box.For the Order Date I8YY|M|D column drop down, select the Filter option.
                    Select Less Than, then value 03011996
                    Click the Filter button.
                    Expect to see 350 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time*2)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='6'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Less than")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='03011996'
        filterselectionobj.create_filter(filter_row_num, 'Less than',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="350of1000records,Page1of7"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='10'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '09')
           
        """
            Step 10:Close the Filter box.For the Order Date I8MtDYY column drop down, select the Filter option.
                    Select Less than or equal to, then value APR 01 1996
                    Click the Filter button.
                    Expect to see 710 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='7'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Less than or equal to")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1="APR 01 1996"
        filterselectionobj.create_filter(filter_row_num, 'Less than or equal to',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="710of1000records,Page1of13"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='11'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '10')

   
        """
            Step 11: Close the Filter box.For the Order Date MTRDYY column drop down, select the Filter option.
            Select Between,then APRIL 1, 1996 for the first valueand MAY 1, 1996 for the second value.
            Click the Filter button.           
            Expect to see 360 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='8'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Between")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1="APRIL 1, 1996"
        value2="MAY 1, 1996"
        filterselectionobj.create_filter(filter_row_num, 'Between',value1=value1, value2=value2)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="360of1000records,Page1of7"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        
        ds_no='12'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '11')
           
        """
            Step 12:Close the Filter box.For the YYJUL Order Date column drop down, select the Filter option.
                    Select Not Between, then 1996/032 for the first value and 1996/344 for the second value. 
                    Click the Filter button.
                    Expect to see 171 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='9'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Not Between")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        
        value1="1996/032"
        value2="1996/344"
        filterselectionobj.create_filter(filter_row_num, 'Not Between',value1=value1, value2=value2)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="171of1000records,Page1of3"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        
        ds_no='13'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '12')
           
        """
            Step 13:Close the Filter box. For the JULIAN Order Date column drop down, select the Filter option.
                    Select Contains, then enter the string - 153 in the value box.
                    Click the Filter button.
                    Expect to see 100 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        visible_text="1000of1000 records, Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='10'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Contains")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='153'
        filterselectionobj.create_filter(filter_row_num, 'Contains',value1=value1)
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        
        exp_report_title="100of1000records,Page1of2"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='14'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '13')
        
        """
            Step 14: Close the Filter box.For the QYY Order Date column drop down, select the Filter option.
                    Select Contains(match case), then enter the string - q4 in the value box.
                    Click the Filter button. Change the string to Q4 and click the Filter button again.
                    Expect to see 0 records, since q4 contains lower case 'q'.
                    Expect to see 10 records on the report, using the upper case 'Q4'.
        """
        filterselectionobj.close_filter_dialog()
        visible_text="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='11'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Contains (match case)")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='q4'
        filterselectionobj.create_filter(filter_row_num, 'Contains (match case)',value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="0of1000records,Page1of1"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no="15_1"
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '14')
        
        value1='Q4'
        filterselectionobj.create_filter(filter_row_num, 'Contains (match case)', value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="10of1000records,Page1of1"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no="15_2"
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '14')
          
        """
            Step 15:Close the Filter box.For the wrMtrYY Order Date column drop down, select the Filter option.
            Select Omits, then enter the string - JANUARY in the value box.
            Click the Filter Button.
            Expect to see 830 rows on the report, even though the month entered is in upper case. Case does not matter.
        """
        filterselectionobj.close_filter_dialog()
        exp_report_title="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='12'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Omits")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='JANUARY'
        filterselectionobj.create_filter(filter_row_num, 'Omits',value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="830of1000records,Page1of15"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='16'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '15')
           
        """
            Step 16:Close the Filter box.For the Mtr Order Date column drop down, select the Filter option.
                    Select Omits(match case), then enter the string - Ma in the value box.
                    Click the Filter button.Change the value from Ma to May.
                    Click the Filter button again.
                    Expect to see 638 rows on the report.This Omits all March & May values because Ma is in both values.    
                    Expect to see 819 rows on the report.This Omits only May values. 
        """
        filterselectionobj.close_filter_dialog()
        visible_text="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='13'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Omits (match case)")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='Ma'
        filterselectionobj.create_filter(filter_row_num, 'Omits (match case)',value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="638of1000records,Page1of12"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no="17_1"
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '16')
          
        """    Expect to see 819 rows on the report.This Omits only May values.    """
        
        value1='May'
        filterselectionobj.create_filter(filter_row_num, 'Omits (match case)',value1=value1)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="819of1000records,Page1of15"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no="17_2"
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '16')
           
        """
            Step 17:Close the Filter box.For the Wtr Order Date column drop down, select the Filter option.
                    Select Equals, then select Tuesday and Sunday.
                    Click the Filter button.
                    Expect to see 2 rows on the report.
        """
        filterselectionobj.close_filter_dialog()
        visible_text="1000of1000records,Page1of18"
        utillobj.synchronize_with_visble_text(page_summary_css, visible_text, expire_time)
        utillobj.verify_table_data(parent_table_css, Test_Case_ID+"_Ds01.xlsx")
        
        col_no='14'
        miscelanousobj.select_menu_items(parent_table_css, col_no, "Filter","Equals")
        utillobj.synchronize_with_number_of_element(filter_dialog_css, filterdlg_exp_number, expire_time)
        value1='Tuesday'
        value2='Sunday'
        
        filterselectionobj.create_filter(filter_row_num, 'Equals', value1=value1, value2=value2)
        time.sleep(4)
        
        filterselectionobj.filter_button_click('Filter')
        exp_report_title="2of1000records,Page1of1"
        utillobj.synchronize_with_visble_text(page_summary_css, exp_report_title, expire_time)
        
        ds_no='18'
        verify_active_table_verification(page_num, exp_report_title, ds_no, runtime_report_title, exp_column_heading_list, '17')
        
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()
        