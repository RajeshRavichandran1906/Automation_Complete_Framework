'''
Created on Nov 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2157262
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2157262_TestClass(BaseTestCase):

    def test_C2157262(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached repro - ACT-711WVOFF.This repro will use Cache OFF
        """
        utillobj.active_run_fex_api_login("act-711WVOFF.fex", "S7077", 'mrid', 'mrpass')
        
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'SEATS', 'RETAIL_COST', 'DEALER_COST']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'act_711WVOFF.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Click the drop down for Country.Select the Export option, then Excel.Select All Records.
        """
        val = ['All records','Filtered only']
        miscelanousobj.verify_menu_items('ITableData0', 0, 'Export->XML (Excel)', val, 'Step 02: Expect to see the options menu.')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','XML (Excel)','All records')
        """
        Step 03: If an ActiveX screen appears, click Allow.
        Step 04: Click or open the Excel file just downloaded.
        Step 05: Click the Excel Save button in the upper left corner of the spreadsheet.
        """
        time.sleep(19)
        utillobj.save_file_from_browser('C2157262_actual_1')
        utillobj.verify_xml_xls('C2157262_actual_1.xls', 'C2157262_base_1.xls', 'Step 5. Verify that NOPRINT value should not display')
        
        
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
        Step 06: Cancel/Exit the Excel Save menu.Execute the attached repro - ACT-711WVOFFThis repro will use Cache ON
        """
        utillobj.active_run_fex_api_login("act-711WVON.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 06.1: Verify Page Summary")
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.2: Verify all columns listed on the report')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'act_711WVON.xlsx','Step 06.3: Verify data set')
       
        """
        Step 07: Click the drop down for Country. Select the Export option, then Excel.
        """
        val = ['HTML', 'CSV (comma delim)', 'Excel', 'PDF']
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export', val, 'Step 07: Expect to see the Export menu.')
        time.sleep(2)
        
        """
        Step 08: Select All Records.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2157262_actual_2')
        utillobj.verify_xml_xls('C2157262_actual_2.xlsX', 'C2157262_base_2.xlsx', 'Step 8. Verify that NOPRINT value should not display')
        
        
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