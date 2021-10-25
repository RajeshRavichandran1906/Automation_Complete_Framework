'''
Created on Aug 08, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7073&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055520
TestCase Name = AHTML negative values not working Visualize & %of Total (90502)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2055520_TestClass(BaseTestCase):

    def test_C2055520(self):
        
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the attached repro - 90502.fex
        """
        utillobj.active_run_fex_api_login("90502.fex", "S7073", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element('#ITableData0 .arGridColumnHeading > td', 5, 40)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.01: Verify the Report Heading')
        column_list=['COUNTRY', 'RETAIL_COST', 'DEALER_COST', 'SALES', 'ABC']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2055520_Ds_01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2055520_Ds_01.xlsx',"Step 01.03: Verify entire Data set in Page 1") 
        """
        Step 02a: Select the ABC field drop down select visualize.
        """
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')  
        utillobj.synchronize_with_number_of_element('#ITableData0 .arGridColumnHeading > td', 6, 40)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'red', 'Step 02.01: Verify visualization added')         
        time.sleep(5)        
        
        """
        Step 03: Select the ABC field drop down select calculate-->% of Total
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Calculate","% of Total")
        utillobj.synchronize_with_number_of_element('#ITableData0 .arGridColumnHeading > td', 7, 40)
        utillobj.synchronize_with_visble_text('#ITableData0 .arGridColumnHeading', '% of Total', 40)
        column=['COUNTRY', 'RETAIL_COST', 'DEALER_COST', 'SALES', 'ABC', '% of Total', '']
        miscelanousobj.verify_column_heading('ITableData0',column,'Step 03.01: Verify that the % of Total is inserted between the ABC column and the Visualization bars column.')
        Expected_list = ['-25.39%', '-3.33%', '-33.42%', '-3.28%', '-34.58%']
        actual_list = []
        per_of_total = driver.find_elements_by_css_selector("[class^='IBIS0_']")
        for i in range(len(per_of_total)):
            actual_list.append(per_of_total[i].text)
        utillity.UtillityMethods.asequal(self,actual_list ,Expected_list, "Step 03.02: Verify that the % of Total is inserted ")
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 5, 'red', 'Step 03.03: Verify % of Total column added')  
        miscelanousobj.verify_field_color("IBIS0_1", "red", 5, "Step 03.04: Also verify that the figures displayed for % of Total are also shown in Red")
        
if __name__ == '__main__':
    unittest.main()