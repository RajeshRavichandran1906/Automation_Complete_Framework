'''
Created on Jul 25, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050494
'''
import unittest
from common.lib import utillity
from common.pages import active_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2050494_TestClass(BaseTestCase):

    def test_C2050494(self):
        
        """
        Class & Object
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.01: Execute the AR-RP-001.fex")
        columns1=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01.02: Verify all columns listed on the report')

        """
            Step 02: Select Unit Sales > Calculate > % of Total
            Verify % of Total option returns % of Total, which computes the percentage of a field, based on the total values for the field.
            Verify that the % of Total calculation appears in a new column to the right of the selected column.
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Calculate","% of Total")
        
        utillobj.verify_data_set('ITableData0','I0r', 'C2050494_Ds01.xlsx',"Step 02.01: Verify % of Total option returns % of Total, which computes the percentage of a field")
        
        column=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', '% of Total', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0',column,'Step 02.02: Verify that the % of Total calculation appears in a new column to the right of the selected column.')
        miscelanousobj.verify_field_color("IBIS0_1", "green", 57, "Step 02.03: Verify color of '% of Total' field")
 
if __name__ == '__main__':
    unittest.main()       