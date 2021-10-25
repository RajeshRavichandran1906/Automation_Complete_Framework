'''
Created on Jan 20, 2016

@author: AAKhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223381
Description : AHTML:Active Report Filter options not working consistently for decimal values(ACT-775). 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity

class C2223381_TestClass(BaseTestCase):

    def test_C2223381(self):
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        filter_selsection_box_css = "#wall1"
        
        """ Step 1: Execute the attached Fex - act-775 using the below API Url
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9043&BIP_item=Active_Technologies/Report/act-775.fex
        """
        utillobj.active_run_fex_api_login("act-775.fex", "S7068", 'mrid', 'mrpass')
        utillobj.wait_for_page_loads(10)
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, miscelanousobj.home_page_medium_timesleep, pause_time=1)
        miscelanousobj.verify_page_summary(0, '538of538records,Page1of10', "Step 01.01: Verify Page Summary")
        column_list=['Store State Province', 'Product Category', 'Gross Profit', 'Cost of Goods', 'Discount']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.02: Verify all columns listed on the report Act-461b.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2223381_DS01.xlsx','Step 01.03: Verify data set')
         
        """ Step 2: Select the drop down for Gross Profit and select Filter/Equals.
                    Move the Filter dialogue box off to the right-side.
                    Expect to see the Active report with the Filter menu.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        utillobj.synchronize_with_visble_text(filter_selsection_box_css, 'Filter', miscelanousobj.home_page_medium_timesleep)
        miscelanousobj.move_active_popup('1', '400', '100')
        expected = ['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        actual=[]
        filter_value = utillobj.validate_and_get_webdriver_objects("#FiltTable1 .arFilterButton", 'filter value')
        for val in filter_value:
            actual.append(val.text)
        utillobj.asequal(actual, expected, 'Step 02.01: Expect to see the Active report with the Filter menu.')
        
        
        """ Step 3: From the Filter Selection value box, click the down arrow.
                    Move the values box below the Filter Selection menu.
                    Click the first two values of: $226.97, $268.28.
                    Expect to see the Active Report, the Filter menu and the selected values.
        """
        #utillobj.synchronize_with_visble_text(filter_selsection_box_css, '*$226.97', miscelanousobj.home_page_medium_timesleep)
        filterselectionobj.create_filter(1, 'Equals', 'large', value1='$226.97', value2='$268.28')
        utillobj.wait_for_page_loads(5)
        #utillobj.synchronize_with_visble_text(filter_selsection_box_css, '*$226.97', miscelanousobj.home_page_medium_timesleep)
        filter_value = utillobj.validate_and_get_webdriver_object("#wall1 .arFilterItem #ftpv1_1_0", 'filter value')
        actual_value=filter_value.text.strip()
        expected_value = '*$226.97'
        msg='Step 03.01: Expect to see the *$226.97 value is displaying in the second value box against the actual captured value [' + actual_value + '].'
        utillobj.asequal(expected_value, actual_value, msg)
        
        
        """ Step 4: Click the Filter Button in the Filter Selection menu.
                    Expect to see the following filtered report with two rows for:
                    $22f6.97 and $268.28.
        """        
        filterselectionobj.filter_button_click('Filter')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Beijing", miscelanousobj.home_page_medium_timesleep)
        miscelanousobj.verify_page_summary(0, '2of538records,Page1of1', "Step 04.01: Verify Page Summary")
        column_list=['Store State Province', 'Product Category', 'Gross Profit', 'Cost of Goods', 'Discount']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 04.02: Verify all columns listed on the report AR-RP-001.fex')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2223381_DS02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2223381_DS02.xlsx', 'Step 04.03: Verify data set')
               
if __name__ == "__main__":
    unittest.main()