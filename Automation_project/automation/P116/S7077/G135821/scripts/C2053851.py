'''
Created on Oct 17, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053851
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest,time

class C2053851_TestClass(BaseTestCase):

    def test_C2053851(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        """
        Step 01: Execute the AR-RP-001.fex.
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7077", 'mrid', 'mrpass')
        
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20, pause_time=1)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Verify Page Summary")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report AR-RP-001.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.2: Verify data set')
           
        """
        Step 02: Click dropdown next to any column and select Export > XML (Excel) > All Records
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2053851_actual_1')
        utillobj.verify_xml_xls('C2053851_actual_1.xls', 'C2053851_base_1.xls', 'Step 2. Verify file contents')
        
        """
        Step 03: Now do filter on State column Select State > Filter > equals > IL and MA
        """
        time.sleep(10)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        utillobj.synchronize_with_number_of_element("#wall1", 1, 10, 1)
        time.sleep(5)
        miscelanousobj.move_active_popup("1", "600", "200")
        time.sleep(5)
        filterobj.create_filter(1, 'Equals', value1='IL',value2='MA')
        filterobj.filter_button_click('Filter')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053851_Ds01.xlsx', 'Step 03: Verify 19 records for states IL and MA are listed')
        time.sleep(5)
        """
        Step 04: Click dropdown next to any column and select Export > XML (Excel) >Filtered Only
        """
        
        time.sleep(10)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','Filtered only')
           
        """
        Step 05: Verify that all the filtered records are displayed on a new excel page (19 of 107)
        """
        time.sleep(19)
        utillobj.save_file_from_browser('C2053851_actual_2')
        utillobj.verify_xml_xls('C2053851_actual_2.xls', 'C2053851_base_2.xls', 'Step 2. Verify file contents')
        
        utillobj.switch_to_main_window()
        
        

if __name__ == "__main__":
    unittest.main()
