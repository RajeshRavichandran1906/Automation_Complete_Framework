'''
Created on Oct 31, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053859
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2053859_TestClass(BaseTestCase):

    def test_C2053859(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        """
        Step 01: Execute the attached Fex - Curr_Cty_WV_OFF
        """
        utillobj.active_run_fex_api_login("Curr_Cty_WV_OFF.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'DEALER_COST', 'Raw DCOST', 'RETAIL_COST', 'Raw RCOST', 'SALES', 'Raw SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'Curr_Cty_WV_OFF.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Click the Active dropdown arrow for the first SALES column, select Export, then Excel and lastly All Records.
        """
        val = ['HTML', 'CSV (comma delim)', 'XML (Excel)']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val, 'Step 02: Expect to see the Export menu.')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        
        """
        Step 03: Click the All Records option.
        Step 04: Click the Yes button on the allow ActiveX screen.
        Step 05: Click the highlighted Excel button at the bottom of the screen.
        """
        time.sleep(19)
        utillobj.save_file_from_browser('C2053859_actual_1')
        utillobj.verify_xml_xls('C2053859_actual_1.xls', 'C2053859_base_1.xls', 'Step 5. Verify file contents')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        STep 06: Close any spreadsheets and/or blank screens. Execute the attached Fex - Curr_Cty_WV_ON
        """
        

        utillobj.active_run_fex_api_login("Curr_Cty_WV_ON.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 06.1: Verify Page Summary")
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'Curr_Cty_WV_ON.xlsx','Step 06.3: Verify data set')
        
        """
        Step 07: Click the Active dropdown arrow for the Country column, select Export, then Excel and lastly All Records.
        """
        val = ['HTML', 'CSV (comma delim)', 'Excel', 'PDF']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val, 'Step 07: Expect to see the Export menu.')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','Excel','All records')
        time.sleep(19)
        """
        Step 08: Click the All Records button.    
        Step 09: Click the Open button.
        Step 10: Click the Yes button.
        """
        utillobj.save_file_from_browser('C2053859_actual_2')
        utillobj.verify_xml_xls('C2053859_actual_2.xlsx', 'C2053859_base_2.xlsx', 'Step 11 Verify file contents')
        
        
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