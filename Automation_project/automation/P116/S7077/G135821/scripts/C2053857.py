'''
Created on Nov 01, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053857
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2053857_TestClass(BaseTestCase):

    def test_C2053857(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        """
        Step 01: Execute the attached fex - Negatives_WV_ON
        Expect to see the following Active Report with negative numbers.
        There will be a mixture of lead/trail minus signs, brackets and Credit Symbols
        """
        utillobj.active_run_fex_api_login("Negatives_WV_ON.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary 18of18records")
        column_list=['COUNTRY', 'Negative default format', 'Negative format M(Dol)', 'Negative no commas', 'Negative Brackets', 'Negative CR symbol', 'Negative trail minus', 'Negative P12.2C', 'Negative F9.2B', 'Negative I9R']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report Negatives_WV_ON.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'Negatives_WV_ON.xlsx','Step 01.2: Verify data set of Negatives_WV_ON')
        
        """
        Step 02: Click on any Active dropdown arrow, select Export, then Excel and finally All Records.
        """
        time.sleep(4)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        
        """
        Step 03: Click the All Records selection.
        Step 04: Click the Excel button at the bottom of the screen to open the spreadsheet.
        """
        
        time.sleep(19)
        utillobj.save_file_from_browser('C2053857_actual_1')
        utillobj.verify_xml_xls('C2053857_actual_1.xlsx', 'C2053857_base_1.xlsx', 'Step 3. Verify file contents')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.infoassist_api_logout()
        time.sleep(3)
               
        """
        Step 05: Execute the attached Fex - Negatives_WV_OFF
        """
        utillobj.active_run_fex_api_login("Negatives_WV_OFF.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 05.1: Verify Page Summary 18of18records")
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 05.2: Verify all columns listed on the report Negatives_WV_ON.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'Negatives_WV_ON.xlsx','Step 05.3: Verify data set of Negatives_WV_OFF')
        
        """
        Step 06: Click on any Active dropdown arrow, select Export, then Excel and finally All Records.
        Step 07: Click the All Records selection.
        Step 08: Click the Open button.
        Step 09: Click the Yes button.
        """
        time.sleep(4)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','XML (Excel)','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2053857_actual_2')
        utillobj.verify_xml_xls('C2053857_actual_2.xls', 'C2053857_base_2.xls', 'Step 3. Verify file contents')
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
        

if __name__ == "__main__":
    unittest.main()