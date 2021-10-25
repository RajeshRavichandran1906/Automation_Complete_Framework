'''
Created on Sep 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203732

NFR:AHTML:allow customization of pagination bar(Project 97564)
Verify pagination bar in active report display display number of record and page number
and verify active report with hidden pagination bar

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time
from selenium.webdriver.common.by import By

class C2203732_TestClass(BaseTestCase):

    def test_C2203732(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Run 97564.fex from the repro
        """
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("97564.fex", "S7072", 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR,'#ITableData0')
        utillobj._validate_page(elem1)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-886-report.fex and Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act-886-report.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '97564.xlsx', 'Step 01.3: Execute the 97564.fex and Verify the entire data')
        #utillobj.create_data_set('ITableData0', 'I0r', '97564.xlsx')

        """
        Step 02:Select unit sales drop down option show record--> 5 record
        """
        #verify report get displayed with 5 record in first page
        miscelanousobj.select_menu_items("ITableData0", "3", "Show Records","5 Records")
        time.sleep(6)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of2', 'Step 02.1:Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203732_Ds01.xlsx', 'Step 02.2:verify report get displayed with 5 record in first page')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2203732_Ds01.xlsx')
        
        
        """Step 03: Select next page icon"""
        #verify respective next page get displayed
        miscelanousobj.navigate_page('next_page')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '10of10records,Page2of2', 'Step 03.1: Verify the Report Heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203732_Ds02.xlsx', 'Step 03.2: verify respective next page get displayed')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2203732_Ds02.xlsx')
        utillobj.infoassist_api_logout()
        

        """Step 04: Run 97564 hidden.fex from the repro"""
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        utillobj._validate_page(uname)
        time.sleep(2)
        utillobj.active_run_fex_api_login("97564_hidden.fex", "S7072", 'mrid', 'mrpass')
        elem=(By.CSS_SELECTOR,'#ITableData0')
        utillobj._validate_page(elem)
        msg="Step 04: Execute the act-886-report.fex and Verify the Report Heading is hidden"
        try:
            page_summary=True
            miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', msg)
        except:
            page_summary=False
        utillobj.asequal(False, page_summary, msg)
            
        
if __name__ == "__main__":
    unittest.main()