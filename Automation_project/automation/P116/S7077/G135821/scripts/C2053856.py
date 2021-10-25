'''
Created on Oct 31, 2016

@author: Khan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053856
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time, pyautogui

class C2053856_TestClass(BaseTestCase):
    
    def test_C2053856(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached Fex - C506773_WV_ON
        """
        utillobj.active_run_fex_api_login("C560773_WV_ON.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'Neg. $ format M', 'Neg. $ format !D', 'Neg. Pounds', 'Neg. Yen', 'Neg. Euro', 'Neg. trail Euro']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C560773_WV_ON.xlsx','Step 01.3: Verify data set')
 
        """
        Step 02: Click any drop down arrow, select Export, then Excel, then All Records.
        """
        
        utillobj.synchronize_until_element_is_visible('#popid0_1', 30)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','Excel','All records')
         
        """
        Step 03: If an Open message box appears, click OPEN. For older Excel(.xls) click the Yes button, if an invalid format message appears.
        """
        time.sleep(19)
         
        utillobj.save_file_from_browser('C2053856_actual_1')
        utillobj.verify_xml_xls('C2053856_actual_1.xlsx', 'C2053856_base_1.xlsx', 'Step 03.1. Verify file contents')
        utillobj.switch_to_main_window()
        time.sleep(2) 
        
        'Opening downloads window and closing it to remove th downloaded xlsx icon which is not allowing to click the menu items correctly.'
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        
        """
        Step 04: Execute the attached Fex - C506773_WV_OFF
        """
        utillobj.active_run_fex_api_login("C560773_WV_OFF.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 04.1: Verify Page Summary")
        column_list=['COUNTRY', 'Neg. $ format M', 'Neg. $ format !D', 'Neg. Pounds', 'Neg. Yen', 'Neg. Euro', 'Neg. trail Euro']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 04.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C560773_WV_OFF.xlsx','Step 04.3: Verify data set')
 
 
        """
        Step 05: Click any drop down arrow, select Export, then Excel, then All Records.
        """
        val = ['HTML', 'CSV (comma delim)', 'XML (Excel)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val, 'Step 05.1: Expect to see the Export menu.')
         
        """
        Step 06: Click YES to the ActiveX Open message dialogue box.
        Step 07: Open the Excel spreadsheet by clicking the highlighted Excel button at the bottom of the screen.
        """
        
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2053856_actual_2')
        utillobj.verify_xml_xls('C2053856_actual_2.xls', 'C2053856_base_2.xls', 'Step 07.1. Verify file contents')
        utillobj.switch_to_main_window()
        time.sleep(2)
        
        

if __name__ == "__main__":
    unittest.main()