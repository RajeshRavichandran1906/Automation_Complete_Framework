'''
Created on Oct 31, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053852
Verify that NOPRINT field do not export with WEBVIEWER=ON
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui

class C2053852_TestClass(BaseTestCase):

    def test_C2053852(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached 121993.fex 
        """
        utillobj.active_run_fex_api_login("121993.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY', 'CAR','MODEL', 'SEATS']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', '121993.xlsx','Step 01.3: Verify data set')
        #utillobj.create_data_set('ITableData0', 'I0r', '121993.xlsx')
        """
        Step 02: Click on Country drop down menu and select export to -> Excel (All records)
        """
        
        #verify that NOPRINT value should not display when export AHTML report to Excel
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','Excel','All records')
        
        time.sleep(25)
        utillobj.save_file_from_browser('C2053852_actual_1')
        utillobj.verify_xml_xls('C2053852_actual_1.xlsx', 'C2053852_base_1.xlsx', 'Step 2. Verify that NOPRINT value should not display')
        
        
        utillobj.switch_to_main_window()
        if browser == 'Chrome': 
            pyautogui.hotkey('ctrl','j')
            time.sleep(2)
            pyautogui.hotkey('ctrl','w')
            time.sleep(2)
            
        utillobj.infoassist_api_logout()
        time.sleep(3)
         

         

if __name__ == "__main__":
    unittest.main()