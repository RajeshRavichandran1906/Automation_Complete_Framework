'''
Created on Aug 9, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050433
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050433_TestClass(BaseTestCase):

    def test_C2050433(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute attached repro 117330.
    
        Expect to see the report sorted by CAR by COUNTRY, with eight numeric columns following.
        Expect to see four columns each for Dealer_Cost and Sales.
        The first column is the Original field format from the Master File.
        The second column is the Original field format with leading zeros added to show the true length of the field.
        The third column is for the reformatted field value.
        The last column for each field is the reformatted value with leading zeros to show the true length of the field.
        The first screen shot displays the Dealer_Cost columns.
        
        Step 2. Scroll the report to the right to completely display the Sales columns.
        Expect to see the four Sales columns and their reformatting.
        """
        utillobj.active_run_fex_api_login("117330.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the 117330.fex and Verify the Report Heading')
        l1=['CAR', 'COUNTRY']
        l2=['Original Dealer_Cost D7', 'Original Dealer_Cost D7L with leading zeros', 'Net Cases Shipped Reformatted Dealer_Cost P12C', 'Net Cases Shipped Reformatted Dealer_Cost P12CL with leading zeros']
        l3=['Original Sales I6', 'Original Sales I6 with leading zeros', 'Extended Sales Reformatted Sales P13CM', 'Extended Sales Reformatted Sales P13CML with leading zeros']
        column_list=l1+l2+l3
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 117330.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050433_Ds01.xlsx', 'Step 01.3: Verify Report data for correct reformatted numeric values for all required columns.')
        
if __name__ == '__main__':
    unittest.main()