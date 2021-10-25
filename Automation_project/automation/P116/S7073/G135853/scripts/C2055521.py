'''
Created on Aug 09, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055521
TestCase Name = AHTML:Apply visualize, across field heading disappears (146606)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException

class C2055521_TestClass(BaseTestCase):

    def test_C2055521(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - 90502.fex
        """
        utillobj.active_run_fex_api_login("146606.fex", "S7073", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.a: Verify the Report Heading')
        #Step VP: Verifying the Across field labels on Report'
        expected_list=['COUNTRY', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        actual_list=[]
        columns = driver.find_elements_by_css_selector("#ITableData0 > tbody > tr:nth-child(1) > td")
        for c in range(0, len(columns)):
            actual_list.append(columns[c].text)
        utillity.UtillityMethods.asequal(self,actual_list, expected_list,'Step 01.b: Verifying the Across field labels on Report')
        #Step VP: Verifying the Across Values are Center_justified on Report'
        expected_list=['CENTER', '2', 'CENTER', '2', 'CENTER', '2', 'CENTER', '2', 'CENTER', '2']
        actual_list=[]
        columns = driver.find_elements_by_css_selector("#ITableData0 > tbody > tr:nth-child(1) > td")
        for c in range(1, len(columns)):
            oalign=columns[c].get_attribute("align")
            actual_list.append(oalign.upper())
            actual_list.append(columns[c].get_attribute("colspan"))
        utillity.UtillityMethods.asequal(self,actual_list, expected_list,'Step 01.c: Verifying the Across Values are Center_justified on Report and colspan as 2')
        '''
        #Step VP: Verifying the Across Values are having colspan as 2 [each across field values contains two columns]'
        expected_list=['2', '2', '2', '2', '2']
        actual_list=[]
        columns = driver.find_elements_by_css_selector("#ITableData0 > tbody > tr:nth-child(1) > td")
        for c in range(1, len(columns)):
            actual_list.append(columns[c].get_attribute("colspan"))
        utillity.UtillityMethods.asequal(self,actual_list, expected_list,'Step 01.d: Verifying the Across Values are colspan as 2')
        '''
        column_list=['CAR', 'SALES', 'SEATS', 'SALES', 'SEATS', 'SALES', 'SEATS', 'SALES', 'SEATS', 'SALES', 'SEATS']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.d: Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2055521_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2055521_Ds_01.xlsx',"Step 01.e: Verify entire Data set in Page 1") 
        
        
        """
        Step 02a: Select the ABC field drop down select visualize.
        """
        driver.implicitly_wait(1)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Visualize')  
        time.sleep(2)
        actual_list = []
        total_rows=driver.find_elements_by_css_selector("[id='ITableData0'] tr[id ^= 'I0r']")
        for i in range(0, len(total_rows)):
            try:
                actual_color_code=driver.find_element_by_css_selector("[id='ITableData0']" + " tr[id ^= 'I0r" + str(i) +"'] > td:nth-child(4) > table table td").value_of_css_property('background-color')
                color = True if actual_color_code in ['rgba(192, 192, 192, 1)', 'rgb(192, 192, 192)'] else False
                actual_list.append(color)        
            except NoSuchElementException:
                actual_list.append('Null')
        Expected_list = ['Null', 'Null', 'Null', 'Null', True, True, 'Null', 'Null', 'Null', True]
        utillity.UtillityMethods.asequal(self,actual_list, Expected_list,'Step 04.c: Verify visualization added for Mixed pos/neg')
        time.sleep(5)        
        
       

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
