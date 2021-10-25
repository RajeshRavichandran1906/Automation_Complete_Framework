'''
Created on Sep 22, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203689 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest
import time
from selenium.webdriver import ActionChains



class C2203689_TestClass(BaseTestCase):

    def test_C2203689(self):
        """
            TESTCASE VARIABLES
        """
        
        """
            Step 01: Execute the attached fex, 107491.fex.
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        utillobj.active_run_fex_api_login("107491.fex", "S7068", 'mrid', 'mrpass')
        header_css="table[id='IWindowBody0'] .arGridBar table>tbody"
        utillobj.synchronize_with_visble_text(header_css, "5of5records,Page1of1", 45, 1)
        miscelanousobj.verify_page_summary('0','5of5records,Page1of1', 'Step 01: Verify Page summary 5of5')
        column=['COUNTRY','CAR','DEALER_COST','RETAIL_COST','MODEL']
        miscelanousobj.verify_column_heading('ITableData0', column, "Step 01.a: Verify Column heading of 107491.fex")
        utillobj.verify_data_set('ITableData0','I0r','107491.xlsx',"Step 01.b: Verify 107491.fex dataset")      
        
        """
        Step 02: Click Dealer_Cost and select calculate ->Sum 
        """
        
        miscelanousobj.select_menu_items('ITableData0', 2, 'Calculate','Sum')
        miscelanousobj.verify_calculated_value(2, 3, "Total Sum 143,794",True, "Step 02: Verify Total Sum 143,794")
        
        """
        Step 03: Select option Filter Dealer_Cost equals "5,512" and click on filter\highlight.
        Verify value "5,512" is filtered\highlighted accordingly.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        filterselectionobj.create_filter(1, 'Equals', value1='5,512')
        filterselectionobj.filter_button_click('Highlight')
        miscelanousobj.move_active_popup("1", "600", "200")
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2203689_Ds01.xlsx',"Step 03.1: Verify Highlighted datset",color='navy')        
        
        filterselectionobj.filter_button_click('Filter')
        utillobj.synchronize_with_visble_text(header_css, "SUB/TOT1of5records,Page1of1", 45, 1)
        miscelanousobj.verify_page_summary('0','1of5records,Page1of1', 'Step 03.2: Verify Page summary 1of5')
        miscelanousobj.verify_calculated_value(2, 3, "Filtered Sum 5,512(3.83%)\nTotal Sum 143,794",True, "Step 03.3: Verify Filtered Sum 5,512(3.83%)\nTotal Sum 143,794")

        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        