'''
Created on Aug 29, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053825
TestCase Name = Verify Freeze icon (when locked) does not apply filter on Pivot table
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2053825_TestClass(BaseTestCase):

    def test_C2053825(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """Test case variables"""
        unlock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'i3AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG1_-1']//img[contains(@src,'GNertexgnyiHAzoQJGG3')]"
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        
        """
        Step 02: Click dropdown menu for State column and mouse over Pivot(Cross Tab)
        """
        values=['Group By(COU)', 'Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)', values, 'Step 02: Verify Group By (Columns) list are displayed', all_items='yes')
        time.sleep(3)
        ele = driver.find_element_by_css_selector("#TCOL_0_C_3")
        ele.click()
        time.sleep(3)
        """
        Step 03: Click dropdown menu for State column and mouse over Pivot(Cross Tab) > any column (Category) > Product ID
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot (Cross Tab)','Category','Product ID')
        miscelanousobj.verify_popup_appears('wall1', 'State by Product ID, Category', 'Step 03: Verify Pivot table State By Product ID, Category is generated based on the columns selection')
        utillobj.verify_pivot_data_set('piv1', 'C2053818_Ds01.xlsx','Step 03: Verify pivot data')
        
        """
        Step 04: Ensure to click Freeze chart icon to unlink the chart to the report filters.
        """
        self.driver.find_element(By.XPATH, unlock).click()
        try: 
            lock_icon = self.driver.find_element(By.XPATH,lock).is_displayed()
            utillobj.asequal(True,lock_icon,'Step 04: Verify that freeze icon is locked')
        except NoSuchElementException:
            print('Step 04: Verify that freeze icon is locked - Failed')
            
        """
        Step 05: Now go to the original report and click dropdown menu next to Product ID. Select Filter > Equals
        """
        miscelanousobj.move_active_popup('1', '600', '200')
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        miscelanousobj.verify_popup_appears('wall2', 'Filter Selection for Report1', 'Step 05: Verify that Filter Selection for Report1 is opened')
        """
        Step 06: Select value = C142 from the dropdown and click Filter button.
        """
        filterobj.create_filter(1, 'Equals', value1='C142', popup_id='wall2')
        filterobj.filter_button_click('Filter', popup_id='wall2')
        utillobj.verify_pivot_data_set('piv1', 'C2053818_Ds01.xlsx','Step 06.1: Verify that report shows filter records without affecting records on pivot table')    
        utillobj.verify_data_set('ITableData0','I0r','C2053825_Ds01.xlsx','Step 06.2: Verify table data')
            
if __name__ == '__main__':
    unittest.main()      
        
        
        
        