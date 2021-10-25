'''
Created on AUG 11, 2017

@author: Pavithra/updated by :Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227980
TestCase Name = AHTML: Datatype - DATETIME format variations.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_filter_selection
from common.lib import utillity
from common.wftools import active_report


class C2227980_TestClass(BaseTestCase):

    def test_C2227980(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227980'
        
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AR_RP_DATETIME_Formats.fex"
       
        """
           Step 01:Sign in to WebFOCUS using the below link. http://machine:port/ibi_apps
           
           Step 02:Execute the attached Fex - AR-RP-DATETIME-Formats using the below API URL:
                    http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9066&BIP_item=AR-RP-DATETIME-Formats.fex
                    Expect to see an 18 Page, 1000 line report with 12 columns.
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02.1: 1000of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01.xlsx", "Step 02.2: AR-RP-DATE-Formats.fex data verification", desired_no_of_rows=20)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 02.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 02.4: Verify column heading')
          
        """
            Step 03:For each of the columns, starting with HYYMDSA, left click on the first row and select Filter Cell.After Filter Cell for each column, left-click and select
                    Clear Remove Cell Filter to return to the initial 1000 rows.
                      
                    Expect to see the following count of rows by column:
                      
                    HMDYY - 5 
                    HDMtY - 5
                    HYYMtDS - 5
                    HYY - 5
                    HHISA Date Time - 5
                    HYYMDIA Datetime constant - 10
                    HYYMDIA HINPUT func - 5
                    HYYMDIA Datetime DT func - 10
                    HYYMDm Datetime - 10
                    HYYMDn Datetime - 10
        """
        #HMDYY - 5 
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.1:5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds02.xlsx", "Step 03.2:Verify HMDYY - 5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.4: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Remove Cell Filter")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.4.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
          
        #HDMtY - 5      
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.5: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds03.xlsx", "Step 03.6:Verify HDMtY - 5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.7 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.8: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.8.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
          
        #HYYMtDS - 5
          
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.9: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds04.xlsx", "Step 03.10:Verify-HYYMtDS 5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.11 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.12: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.12.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
          
        #HYY - 5
          
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.13: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds05.xlsx", "Step 03.14:Verify-HYY - 5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.15 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.16: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.16.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
          
        #HHISA Date Time - 5
          
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.17: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds06.xlsx", "Step 03.18:Verify-HHISA Date Time - 5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.19 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.20: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.20.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
          
        #HYYMDIA Datetime constant - 10
          
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 03.21: 10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds07.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds07.xlsx", "Step 03.22:Verify-HYYMDIA Datetime constant - 10 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.23 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.24: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.25.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
         
        #HYYMDIA HINPUT func - 5
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 03.26: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds08.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds08.xlsx", "Step 03.27:Verify-HYYMDIA HINPUT func-5 rows data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.28 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.29: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.29.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
         
        #HYYMDIA Datetime DT func - 10
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 03.30: 10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds09.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds09.xlsx", "Step 03.31:Verify-HYYMDIA Datetime DT func-10 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.32 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.33: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.33.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
         
        #HYYMDm Datetime - 10
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 03.34:10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds010.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds010.xlsx", "Step 03.35:Verify-HYYMDm Datetime - 10 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.36 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.37: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.37.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
         
        #HYYMDn Datetime - 10
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Filter Cell")
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 12)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 03.38:10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds11.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds11.xlsx", "Step 03.39:Verify-HYYMDIA Datetime DT func-10 rows data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 03.40 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.41: Verify column heading')
        time.sleep(1)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Remove Cell Filter")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 03.41.1: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5)         
        time.sleep(3)
         
        """
            Step 04:For the HYYMDSA column drop down, select the Filter option. Select Equal, then values 2002/12/31 11:59:59PM and 2007/08/08 12:13:14PM.
                    Click the Filter button.
                    Expect to see 10 rows on the filtered report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='2002/12/31 11:59:59PM',value2='2007/08/08 12:13:14PM' )
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 04.1: 10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds12.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds12.xlsx", "Step 04.2:Verify 10 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 04.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 04.4: Verify column heading')
         
        """
            Step 05:Clear the previous filter panel.For the HMDYY column drop down, select the Filter option.
                    Select Not equal, then value 10/04/2013.
                    Click the Filter button.
                    Expect to see 15 rows on the filtered report.
        """
         
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 05: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Not equal")
        filterselectionobj.create_filter(1, 'Not equal',value1='10/04/2013')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 05.1: 15of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds13.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds13.xlsx", "Step 05.2:Verify 15 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 05.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 05.4: Verify column heading')
         
        """
            Step 06:Clear the previous filter panel.For the HDMtY column drop down, select the Filter option.
                    Select Greater than, then value 30 Mar 2011
                    Click the Filter button.
                    Expect to see 985 rows on the filtered report.
        """
         
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 06: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
        filterselectionobj.create_filter(1, 'Greater than',value1='30 Mar 2011')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '985of1000records,Page1of18', "Step 06.1: 985of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds14.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds14.xlsx", "Step 06.2:Verify 985 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 06.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 06.4: Verify column heading')
         
        """
            Step 07:Clear the previous filter panel.For the HYYMtDS column drop down, select the Filter option.
                    Select Greater than or equal to, then value 2011 Mar 30 22:23:24.
                    Click the Filter button.
                    Expect to see 990 rows on the filtered report.
        """
         
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 07: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='2011 Mar 30 22:23:24')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '990of1000records,Page1of18', "Step 07.1: 990of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds15.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds15.xlsx", "Step 07.2:Verify 990 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 07.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 07.4: Verify column heading')
        
        """
            Step 08:Clear the previous filter panel.For the HYY column drop down, select the Filter option.
                    Select Less than, then value 2007.
                    Click the Filter button.
                    Expect to see 975 rows on the filtered report.                   
        """
        
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 08: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than")
        filterselectionobj.create_filter(1, 'Less than',value1='2007')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '975of1000records,Page1of18', "Step 08.1:975of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds16.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds16.xlsx", "Step 08.2:Verify 975 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 08.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 08.4: Verify column heading')
         
        """
            Step 09:Clear the previous filter panel.For the HHISA Datetime column drop down, select the Filter option.
                    Select Less than or equal to, then value 10:23:24PM.
                    Click the Filter button.
                    Expect to see 995 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 09: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='10:23:24PM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '995of1000records,Page1of18', "Step 09.1: 995of1000records,Page1of18 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds17.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds17.xlsx", "Step 09.2:Verify 995 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 09.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 09.4: Verify column heading')
         
        """
            Step 10:Clear the previous filter panel.For the HYYMDIA Datetime constant column drop down, select the Filter option.
                    Select Between, then select 2013/04/04 12:00AM for the first value and 2013/10/04 12:00AM for the second value.
                    Click the Filter button.
                    Expect to see 20 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 10: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Between")
        filterselectionobj.create_filter(1, 'Between',value1='2013/04/04 12:00AM',value2='2013/10/04 12:00AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '20of1000records,Page1of1', "Step 10.1:20of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds18.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds18.xlsx", "Step 10.2:Verify 20 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 10.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 10.4: Verify column heading')
         
        """
            Step 11:Clear the previous filter panel.For the HYYMDIA Datetime HINPUT func column drop down, select the Filter option.
                    Select Not Between, then select 2013/01/01 12:00AM for the first value and 2013/05/04 12:00AM for the second value.
                    Click the Filter button.
                    Expect to see 15 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 11: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not Between")
        filterselectionobj.create_filter(1, 'Not Between',value1='2013/01/01 12:00AM',value2='2013/05/04 12:00AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 11.1:15of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds19.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds19.xlsx", "Step 11.2:Verify 15 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 11.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 11.4: Verify column heading')
         
        """
            Step 12:Clear the previous filter panel.For the HYYMDIA Datetime DT func column drop down, select the Filter option.
                    Select Equals, then value 07/14/2013 12:00AM.
                    Click the Filter button.
                    Expect to see 5 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 12: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='07/14/2013 12:00AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 12.1: 5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds20.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds20.xlsx", "Step 12.2:Verify 5 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 12.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 12.4: Verify column heading')
         
        """
            Step 13:Clear the previous filter panel.For the HYYMDm Datetime column drop down, select the Filter option.
                    Select Not equal, then value 2016/01/01 01:01:01.010101
                    Click the Filter button.
                    Expect to see 30 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 13: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Not equal")
        filterselectionobj.create_filter(1, 'Not equal',value1='2016/01/01 01:01:01.010101')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '30of1000records,Page1of1', "Step 13.1:30of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds21.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds21.xlsx", "Step 13.2:Verify 30 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 13.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 13.4: Verify column heading')
         
        """
            Step 14: Clear the previous filter panel.For the HYYMDn Datetime column drop down, select the Filter option.
                    Select Greater than, then value 2013/07/14 22:23:24.111315170
                    Click the Filter button.
                    Expect to see 10 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 14: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "11", "Filter","Greater than")
        filterselectionobj.create_filter(1, 'Greater than',value1='2013/07/14 22:23:24.111315170')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '10of1000records,Page1of1', "Step 14.1: 10of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds22.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds22.xlsx", "Step 14.2:Verify 10 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 14.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 14.4: Verify column heading')
         
        """
            Step 15:Clear the previous filter panel.For the HDMtY Datetime column drop down, select the Filter option.
                    Select Contains and enter the string Mar.
                    Expect to see 5 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 15: AR-RP-DATE-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Contains")
        filterselectionobj.create_filter(1, 'Contains', value1='Mar')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '5of1000records,Page1of1', "Step 15.1:5of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds23.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds23.xlsx", "Step 15.2:Verify 5 rows on the filtered report data verification")        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 15.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 15.4: Verify column heading')
        
        """
            Step 16:Clear the previous filter panel.For the HHISA Datetime column drop down, select the Filter option.
                    Select Omits and enter the string AM.
                    Expect to see 15 rows on the filtered report.
        """
        filterselectionobj.close_filter_dialog()
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds01_1.xlsx", "Step 16: AR-RP-DATETIME-Formats.fex data verification", desired_no_of_rows=5) 
        time.sleep(3)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Omits")
        filterselectionobj.create_filter(1, 'Omits',value1='AM')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '15of1000records,Page1of1', "Step 16.1:  15of1000records,Page1of1 Active Report. - page summary verification")
#         utillobj.create_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds24.xlsx", desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r',Test_Case_ID+"_Ds24.xlsx", "Step 16.2:Verify 15 rows on the filtered report data verification", desired_no_of_rows=5)        
        utillobj.verify_run_time_title('ITableData0', ['Datatype-DATETIME'], "Step 16.3 ",custom_css="[id^='THEAD']")
        expected_list=['Or No I5', 'HYYMDSA', 'HMDYY', 'HDMtY', 'HYYMtDS', 'H Y Y', 'HHISA Date time', 'HYYMDIA Datetime constant', 'HYYMDIA Datetime HINPUT func', 'HYYMDIA Datetime DT func', 'HYYMDm Datetime', 'HYYMDn Datetime']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 16.4: Verify column heading')
        time.sleep(3)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()