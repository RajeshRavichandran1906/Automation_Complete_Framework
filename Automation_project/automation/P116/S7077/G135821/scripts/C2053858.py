'''
Created on Oct 31, 2016

@author: Khan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053858
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time, pyautogui

class C2053858_TestClass(BaseTestCase):

    def test_C2053858(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached Fex - Currency_WV_ON
        """
        utillobj.active_run_fex_api_login("Currency_WV_ON.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'Format M $', 'Format !D $', 'Format !L Pounds', 'Format !Y Yen', 'Format !E Euro', 'Format !F trail Euro']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', 'Currency_WV_ON.xlsx','Step 01.3: Verify data set')

        """
        Step 02: Click the Active drop down arrow on any column, then Export, then Excel and finally All Records.
        """
        val = ['HTML', 'CSV (comma delim)', 'Excel', 'PDF']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val, 'Step 02.1: Expect to see the Export menu.')
        utillobj.synchronize_until_element_is_visible('#popid0_1', 30)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','Excel','All records')
        
        """
        Step 03: Click the All Records menu entry.
        Step 04: Click the Open button.
        Step 05: Click the Yes button.
        """
       
        time.sleep(19)
        utillobj.save_file_from_browser('C2053858_actual_1')
        utillobj.verify_xml_xls('C2053858_actual_1.xlsx', 'C2053858_base_1.xlsx', 'Step 05.1: Verify file contents')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        Step 06: Exit any spreadsheets and/or blank screens. Execute the attached Fex - Currency_WV_OFF        
        """
        utillobj.active_run_fex_api_login("Currency_WV_OFF.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 06.1: Verify Page Summary")
        column_list=['COUNTRY', 'Format M $', 'Format !D $', 'Format !L Pounds', 'Format !Y Yen', 'Format !E Euro', 'Format !F trail Euro']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', 'Currency_WV_OFF.xlsx','Step 06.3: Verify data set')

        """
        Step 07: Click the Active drop down arrow on any column, then Export, then Excel and finally All Records.
        """
        val1 = ['HTML', 'CSV (comma delim)', 'XML (Excel)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val1, 'Step 07.1: Expect to see the Export menu.')

        """
        Step 08: Click the All Records menu entry.
        Step 09: Click the Yes option on the ActiveX allow screen.
        Step 10: Click the highlighted Excel button at the bottom of the screen.
        Step 11: Expand columns B and C to see the full numbers and proper stacked column titles.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        time.sleep(19)
       
        utillobj.save_file_from_browser('C2053858_actual_2')
        utillobj.verify_xml_xls('C2053858_actual_2.xls', 'C2053858_base_2.xls', 'Step 11.1 Verify file contents')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.switch_to_main_window()
        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()