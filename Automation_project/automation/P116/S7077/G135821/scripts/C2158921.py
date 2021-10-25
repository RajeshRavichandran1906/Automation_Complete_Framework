'''
Created on Nov 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2158921
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2158921_TestClass(BaseTestCase):

    def test_C2158921(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached repro - act-138-off
        """
        utillobj.active_run_fex_api_login("act-138-off.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'CAR', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', 'act_138_off.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act_138_off.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Click the drop down for Country.Select the Export option, then Excel.Select All Records.
        Step 03: If an ActiveX screen appears, click Allow.
        Step 04: Click or open the Excel file just downloaded.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2158921_actual_1')
        utillobj.verify_xml_xls('C2158921_actual_1.xlsx', 'C2158921_base_1.xlsx', 'Step 5. Notice that all cells for Country now have values.')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        
        utillobj.switch_to_main_window()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(3)

        
        """
        Step 05: Execute the attached repro - act-138-on
        """
        utillobj.active_run_fex_api_login("act-138-on.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 05.1: Verify Page Summary")
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 05.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'act_138_on.xlsx','Step 05.3: Verify data set')
        
        """
        Step 06: Click the drop down for Country. Select the Export option, then Excel.Select All Records.
        Step 07: If an ActiveX screen appears, click Allow.
        Step 08: Click or open the Excel file just downloaded.
        """
        val = ['All records','Filtered only']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Export->Excel', val, 'Step 06: Expect to see the Export menu.')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2158921_actual_2')
        utillobj.verify_xml_xls('C2158921_actual_2.xlsx', 'C2158921_base_2.xlsx', 'Step 8. Expect to see only valid values for Country. No blanks.')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
        
        utillobj.switch_to_main_window()
        time.sleep(2)
    
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()