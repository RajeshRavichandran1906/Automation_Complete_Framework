'''
Created on Aug 10, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2066747
TestCase Name = AHTML: Visualization: Incorrectly rendered for DEFINEs with Decimals
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException

class C2066747_TestClass(BaseTestCase):

    def test_C2066747(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - act-327.fex
        """
        utillobj.active_run_fex_api_login("act-327.fex", "S7073", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.a: Verify the Report Heading')
        column_list=['COUNTRY', 'RETAIL_COST', 'DEALER_COST', 'SALES', 'DCOST minus RCOST', 'RCOST minus DCOST', 'Mixed pos neg']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2066747_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2066747_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1") 
        
        """
        Step 02: Click the drop down control for DCOST minus RCOST and click Visualize. 
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')  
        time.sleep(2)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'red', 'Step 02a: Verify visualization added for DCOST minus RCOST ')         
        time.sleep(5)
        
        """
        Step 03: Click the drop down control for RCOST minus DCOST and click Visualize..
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Visualize')  
        time.sleep(2)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'red', 'Step 03a: Verify visualization added for DCOST minus RCOST ') 
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 6, 'blue', 'Step 03b: Verify visualization added for RCOST minus DCOST')         
        time.sleep(5)       
        
        """
        Step 04: Click the drop down control for Mixed pos/neg and click Visualize..
        """
        miscelanousobj.select_menu_items('ITableData0', 6, 'Visualize')  
        time.sleep(2)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'red', 'Step 04a: Verify visualization added for DCOST minus RCOST ') 
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 6, 'blue', 'Step 04b: Verify visualization added for RCOST minus DCOST')
        #Expected_list = ['rgba(255, 0, 0, 1)', 'Null', 'rgba(0, 0, 255, 1)', 'rgba(255, 0, 0, 1)', 'rgba(0, 0, 255, 1)']
        
        Expected_list = [True, 'Null', False, True, False]
        
        actual_list = []
        driver.implicitly_wait(1)
        total_rows=driver.find_elements_by_css_selector("[id='ITableData0'] tr[id ^= 'I0r']")
        a = range(0, len(total_rows))
        for i in a:
            try:
                elem=driver.find_element_by_css_selector("[id='ITableData0']" + " tr[id ^= 'I0r" + str(i) +"'] > td:nth-child(10) > table table td")
                actual_color_code=elem.value_of_css_property('background-color')
                color = True if actual_color_code in ['rgba(255, 0, 0, 1)', 'rgb(255, 0, 0)'] else False
                actual_list.append(color)
            except NoSuchElementException:
                actual_list.append('Null')
        utillity.UtillityMethods.asequal(self,actual_list, Expected_list,'Step 04.c: Verify visualization added for Mixed pos/neg')
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
