'''
Created on Oct 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053854
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest,time

class C2053854_TestClass(BaseTestCase):

    def test_C2053854(self):
        
        driver = self.driver #Driver reference object created'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute the attached repro - 162940.fex.
        """
        utillobj.active_run_fex_api_login("162940.fex", "S7077", 'mrid', 'mrpass')
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30, pause_time=1)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.1: Verify Page Summary")
        column_list=['COUNTRY','CAR','DEALER_COST','RETAIL_COST','COMPUTE_1']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report AR-RP-001.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '162940.xlsx','Step 01.3: Verify data set')
         
        """
        Step 02: From any active control, select Export, then XML(Excel), and lastly All Records.
        Step 03: Expect to see the following Excel report appear.
        """
         
        miscelanousobj.verify_menu_items('ITableData0', 1, 'Export',['HTML', 'CSV (comma delim)', 'XML (Excel)'],  'Step 02: Expect to see an Excel export options appear')
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        time.sleep(19)
        utillobj.save_file_from_browser('C2053854_actual')
        utillobj.verify_xml_xls('C2053854_actual.xls', 'C2053854_base.xls', 'Step 3. Verify file contents')
        
        
        utillobj.switch_to_main_window()
        time.sleep(2)
         


if __name__ == "__main__":
    unittest.main()