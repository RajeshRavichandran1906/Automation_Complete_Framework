'''
Created on Jul 28, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7069&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050639
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050639_TestClass(BaseTestCase):

    def test_C2050639(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the AR-AHTML-001.fex
        """
        utillobj.active_run_fex_api_login("AR-AHTML-001.fex", "S7069", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01: Execute the AR-AHTML-001.fex and Verify the Report Heading')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.1: Execute the AR-AHTML-001.fex and Verify the column heading')
        """
        2. Select Dollar Sales > Calculate
        Verify Calculate menu shows all the filter options mentioned in the Test Description
        """
        calculate_menu = ['Clear','Clear All','Sum','Avg','Min','Max','Count','Distinct','% of Total']
        miscelanousobj.verify_menu_items('ITableData0', 5, 'Calculate', calculate_menu,'Step 02: Verify Calculate menu shows all the filter options mentioned')
        
        temp_obj=driver.find_elements_by_css_selector("#ITableData0 td table td b span")
        temp_obj[-1].click()
        time.sleep(5)
        """
        3. Select Calculate > Sum
        Verify Total Sum value is "46,156,290" displayed under column name.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Calculate','Sum')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Sum 46156290', True, 'Step 03: Expect to see Total Sum 46156290 under Dollar Sales.')
        """
        4. Select Calculate > Avg
        Expect to see the Total Sum replaced by a Total Avg of 431,367.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Calculate','Avg')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Avg 431367', True, 'Step 04: Expect to see the Total Sum replaced by a Total Avg of 431367 under Dollar Sales.')
        """
        5. Select Calculate > Min
        Expect to see the Total Avg replaced by a Total Min of 158,995.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Calculate','Min')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Min 158995', True, 'Step 05: Expect to see the Total Avg replaced by a Total Min of 158995 under Dollar Sales.')
        """
        6. Select Calculate > Max
        Expect to see the Total Min replaced by a Total Max of 1,745,509.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Calculate','Max')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', True, 'Step 06: Expect to see the Total Min replaced by a Total Max of 1745509 under Dollar Sales.')
        """
        7. For Calculate options of Cnt & Cnt Dst, change the column used.
        Select State > Calculate > Count
        Expect to see the Total Cnt of 107 under the State column.
        Total Max for Dollar Sales remains.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Calculate','Count')
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt 107', True, 'Step 07: Expect to see the Total Cnt of 107 under the State column.')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', True, 'Step 07.1: Expect to see the Total Max of 1745509 under Dollar Sales remains.')
        """
        8. Select State > Calculate > Cnt Dst
        Expect to see the Total Cnt replaced by a Total Cnt Dst of 11.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Calculate','Distinct')
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt Dist 11', True, 'Step 08: Expect to see the Total Cnt replaced by a Total Cnt Dst of 11 under the State column.')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', True, 'Step 08.1: Expect to see the Total Max of 1745509 under Dollar Sales remains.')
        """
        9. For Calculate option % of Total, change the column used.
        Select Unit Sales > Calculate > % of Total
        Expect to see a new column added to the right of Unit Sales. This represents the ratio of one Unit Sales row to the total for all Unit Sales.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Calculate','% of Total')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', '% of Total', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09: Expect to see a new column added to the right of Unit Sales in the column heading.')
        miscelanousobj.verify_field_color("IBIS0_1", "green", 57, "Step 09.1: Verify Total number items of '% of Total' field, which are Green Color")
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt Dist 11', True, 'Step 09.2: Expect to see Total Cnt Dst of 11 under the State column.')
        miscelanousobj.verify_calculated_value(2, 7, 'Total Max 1745509', True, 'Step 09.3: Expect to see the Total Max of 1745509 under Dollar Sales remains.')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050639_Ds01.xlsx', 'Step 09.4: Verify the entire data set after adding % of Total to Unit Sales Column.')
        """
        10. Remove the % of Total column by
        Select Unit Sales > Calculate > Clear
        Expect to see the % of Total column removed.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Calculate','Clear')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10: Expect to see the % of Total column removed in the column heading.')
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt Dist 11', True, 'Step 10.1: Expect to see Total Cnt Dst of 11 under the State column.')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', True, 'Step 10.2: Expect to see the Total Max of 1745509 under Dollar Sales remains.')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050639_Ds02.xlsx', 'Step 10.3: Verify the entire data set after removing % of Total to Unit Sales Column.')
        """
        11. Remove the remaining Calculations by
        Select State > Calculate > Clear All
        Expect to see all Calculations removed from under all fields.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Calculate','Clear All')
        miscelanousobj.verify_calculated_value(2, 4, 'Total Cnt Dst 11', False, 'Step 11: Expect to see Total Cnt Dst of 11 is removed under the State column.')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', False, 'Step 11.1: Expect to see the Total Max of 1745509 is removed under Dollar Sales remains.')
        
if __name__ == '__main__':
    unittest.main()