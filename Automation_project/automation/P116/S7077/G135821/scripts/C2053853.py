'''
Created on Nov 3, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053853
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2053853_TestClass(BaseTestCase):
    
    def test_C2053853(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        """
        Step 01: Run the fex attached or Execute a simple fex.
        """
        utillobj.active_run_fex_api_login("108282.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'RETAIL_COST', 'DEALER_COST', 'SALES', 'ABC']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', '108282.xlsx','Step 01.3: Verify data set')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '108282.xlsx')
        
        """
        Step 02: Select Country dropdown and click on filter and select France and England as values and click on filter button.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        time.sleep(7)
        miscelanousobj.move_active_popup(1, 350, 450)
        time.sleep(4)
        filterselectionobj.create_filter(1, 'Equals',value1='FRANCE', value2='ENGLAND')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(5)
        
        
        """
        Step 03: From any dropdown select export and click on HTML->Filtered only.
        Verify Filtered values are exported.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','HTML','Filtered only')
        utillobj.switch_to_window(1)
        time.sleep(7)
        
        column_list=['COUNTRY', 'RETAIL_COST', 'DEALER_COST', 'SALES', 'ABC']
         
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 03.1: Verify Filtered values columnn title.')
         
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2053853_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053853_Ds01.xlsx','Step 03.2: Verify data set')
        time.sleep(1)
        utillobj.switch_to_main_window() 
        time.sleep(7)
         
         
        """
        Step 04: From any dropdown select export and click on CSV->Filtered only.
        Verify Filtered values are exported.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','CSV (comma delim)','Filtered only')
        utillobj.switch_to_window(1)
        time.sleep(7)
        
        #miscelanousobj.create_active_csv(1, "C2053853_Ds02.csv")
         
        miscelanousobj.compare_active_csv(1, "C2053853_Ds02.csv", "Step 04:Verify Filtered values are exported.")
        time.sleep(1)
        utillobj.switch_to_main_window() 
        
        time.sleep(7)
         
        """
        Step 05: From any dropdown select export and click on Excel->Filtered only.
        Verify Filtered values are exported.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','XML (Excel)','Filtered only')
        time.sleep(15)
        utillobj.save_file_from_browser('C2053853_actual_1')
        utillobj.verify_xml_xls('C2053853_actual_1.xls', 'C2053853_base_1.xls', 'Step 2. Verify that NOPRINT value should not display')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        
        
        utillobj.switch_to_main_window()
         

if __name__ == "__main__":
    
    unittest.main()