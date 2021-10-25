'''
Created on Aug 09, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055522
TestCase Name = AHTML:apply visualize, column-total value does not move (139120)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2055522_TestClass(BaseTestCase):

    def test_C2055522(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - 139120.fex
        """
        utillobj.active_run_fex_api_login("139120.fex", "S7073", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.a: Verify the Report Heading')
        column_list=['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2055522_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2055522_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1") 
        
        #Step VP: Verifying the Across Values are having colspan as 2 [each across field values contains two columns]'
        expected_list=['TOTAL', '2', '143,794', '1', '173,204', '1']
        actual_list=[]
        columns = driver.find_elements_by_css_selector("#ITableData0 > tbody > tr:nth-child(12)>td")
        for c in range(0, len(columns)):
            actual_list.append(columns[c].text)
            actual_list.append(columns[c].get_attribute("colspan"))
        utillity.UtillityMethods.asequal(self,actual_list, expected_list,'Step 01.d: Verifying the Total Values and its colspan')
        
        """
        Step 02a: Select the ABC field drop down select visualize.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Visualize')  
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Visualize')  
        time.sleep(2)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 2, 'light_gray', 'Step 02a: Verify visualization added for Dealer_Cost')         
        time.sleep(5) 
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'light_gray', 'Step 02b: Verify visualization added for Retail_Cost')         
        time.sleep(5)       
        
        expected_list = ['TOTAL', '2', '143,794', '1', ' ', '1', '173,204', '1', ' ', '1']
        actual_list=[]
        columns = driver.find_elements_by_css_selector("#ITableData0 > tbody > tr:nth-child(12)>td")
        for c in range(0, len(columns)):
            actual_list.append(columns[c].text)
            actual_list.append(columns[c].get_attribute("colspan"))
        utillity.UtillityMethods.asequal(self,actual_list, expected_list,'Step 02.c: Verifying the Total Values remains to its column and doesnot gets moved')
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
