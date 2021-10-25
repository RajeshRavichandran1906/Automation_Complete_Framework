'''
Created on Feb 5, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223215
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_mainpage
from common.lib import utillity
import unittest,time
from selenium.webdriver.common.by import By



class C2223215_TestClass(BaseTestCase):

    def test_C2223215(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscellaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute the attached repro - act-1049-default.fex.
        """
        utillobj.active_run_fex_api_login("act-1049-default.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '18of18records,Page1of2', 'Step 01.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-default.xlsx','Step 01.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step02: Execute the attached repro - act-1049-json1.fex.
        10/18 Records, Page 1 of 2
        """
        utillobj.active_run_fex_api_login("act-1049-json1.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '10/18Records,Page1of2', 'Step 02.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 02.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-json1.xlsx','Step 02.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step03: Execute the attached repro - act-1049-json2.fex.
        10 of 18 Records, Page 1 of 2
        """
        utillobj.active_run_fex_api_login("act-1049-json2.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '10of18Records,Page1of2', 'Step 03.a: Verify Page summary 10of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 03.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-json2.xlsx','Step 03.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step04: Execute the attached repro - act-1049-json4.fex.
        1 -10 Records, Page 1 of 2
        """
        utillobj.active_run_fex_api_login("act-1049-json4.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '1-10Records,Page1of2', 'Step 04.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 04.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-json4.xlsx','Step 04.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step05: Execute the attached repro - act-1049-json5.fex.
        1 10 of 18 Records, Page 1 of 2
        """
        utillobj.active_run_fex_api_login("act-1049-json5.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '1-10of18Records,Page1of2', 'Step 05.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 05.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-json5.xlsx','Step 05.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step06: Execute the attached repro - 
        act-1049-custom1.fex.
        1 of 10 Records out of a total of 18 Records, Page 1 of 2
        """
        utillobj.active_run_fex_api_login("act-1049-custom1.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, '1of10Recordsoutofatotalof18Records,Page1of2', 'Step 06.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 06.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-custom1.xlsx','Step 06.c: Verify data set of act-1049-default')
        time.sleep(5)        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step07: Execute the attached repro - 
        act-1049-custom2.fex.
        Page 1 of 2 showing 1 thru 10 Records out of a total of 18 Records
        """
        utillobj.active_run_fex_api_login("act-1049-custom2.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscellaneousobj.verify_page_summary(0, 'Page1of2showing1thru10Recordsoutofatotalof18Records', 'Step 07.a: Verify Page summary 18of18 records')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST', 'SALES']
        miscellaneousobj.verify_column_heading('ITableData0', column_list, 'Step 07.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-1049-custom2.xlsx','Step 07.c: Verify data set of act-1049-default')
        time.sleep(5) 
        
         
if __name__ == '__main__':
    unittest.main()  
                       
        