'''
Created on Oct 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053849
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest,time, pyautogui


class C2053849_TestClass(BaseTestCase):

    def test_C2053849(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the AR-RP-001.fex.
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 60, 1)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Verify Page Summary")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report AR-RP-001.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.3: Verify data set')
         
        """
        Step 02: Click dropdown next to any column and select Export > HTML > All Records
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','HTML','All records')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(7)
        driver.maximize_window()
        time.sleep(5)
        utillobj.verify_data_set_old('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 02.1: Verify data set')
#         utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 02.1: Verify data set')
        ''' (Ctrl + S) is applicable for chrome  '''
        if browser in ['IE', 'Firefox']:
            utillobj.default_click(self.driver.find_element_by_css_selector('[id="I0r0.0"]'))
            time.sleep(2)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(5)
            utillobj.save_as_file_from_browser('C2053849_Ds01')
            #utillobj.verify_export_save_as('C2053849_Ds01')
            time.sleep(20)
            if browser=="IE":
                utillobj.check_htm_file_exist("C2053849_Ds01.htm","Step 02.2: Verify HTML file")
            else:
                utillobj.check_htm_file_exist("C2053849_Ds01.html","Step 02.2: Verify HTML file")
        self.driver.close()
        time.sleep(15)
        utillobj.switch_to_window(0)
        time.sleep(7)
        
        """
        Step 03: Now do filter on State column Select State > Filter > equals > IL and MA
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        filterselectionobj.create_filter(1, 'Equals', value1='IL',value2='MA')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '19of107records,Page1of1', "Step 03.1: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2053849_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053849_Ds02.xlsx', 'Step 03.2: Verify data set')
          
        """
        Step 04: Click dropdown next to any column and select Export > HTML >Filtered Only
        Step 05: Verify that all the filetred records are displayed on a new browser page (19 of 107)
        """
        miscelanousobj.move_active_popup('1', '600', '200')
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','HTML','Filtered only')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(7)
        driver.maximize_window()
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2053849_Ds02.xlsx', 'Step 05: Verify data set')
        if browser in ['IE', 'Firefox']:
            utillobj.default_click(self.driver.find_element_by_css_selector('[id="I0r0.0"]'))
            time.sleep(2)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(5)
            utillobj.save_as_file_from_browser('C2053849_Ds03')
#             utillobj.verify_export_save_as('C2053849_Ds03')
            time.sleep(5)
            if browser=="IE":
                utillobj.check_htm_file_exist("C2053849_Ds03.htm","Step 05.1: Verify filtered HTML file")
            else:
                utillobj.check_htm_file_exist("C2053849_Ds03.html","Step 05.1: Verify filtered HTML file")
           
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()