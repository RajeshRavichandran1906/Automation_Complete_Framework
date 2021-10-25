'''
Created on Oct 4, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053850
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest,time

class C2053850_TestClass(BaseTestCase):

    def test_C2053850_1(self):
        
        driver = self.driver #Driver reference object created'
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        
        """
        Step 01: Execute the AR-RP-001.fex.
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Verify Page Summary")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report AR-RP-001.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'AR-RP-001.xlsx','Step 01.2: Verify data set')
         
        """
        Step 02: Click dropdown next to any column and select Export > CSV > All Records
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','CSV (comma delim)','All records')
        time.sleep(12)
        utillobj.switch_to_window(1)
        time.sleep(9)
        driver.maximize_window()
        time.sleep(5)
        miscelanousobj.compare_active_csv(1,'C2053850_Ds01.csv',"Step 02: Verify csv file")
        time.sleep(5)
        self.driver.close()
        utillobj.switch_to_window(0)
     
         
        """
        Step 03: Now do filter on State column Select State > Filter > equals > IL and MA
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        filterselectionobj.create_filter(1, 'Equals', value1='IL',value2='MA')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.verify_page_summary(0, '19of107records,Page1of1', "Step 04.1: Verify Page Summary")
 
 
        """
        Step 04: Click dropdown next to any column and select Export > CSV >Filetered Only
        """
        miscelanousobj.move_active_popup('1', '500', '200')
        miscelanousobj.select_menu_items('ITableData0', 0, 'Export','CSV (comma delim)','Filtered only')
        time.sleep(12)
        utillobj.switch_to_window(1)
        time.sleep(9)
        driver.maximize_window()
        time.sleep(5)
         
        """
        Step 05: Verify that all the filtered records are displayed on a new browser page (19 of 107)
        """
         
        time.sleep(3)
        miscelanousobj.compare_active_csv(1,'C2053850_Ds02.csv',"Step 05: Verify filtered csv file")
        time.sleep(5)
        self.driver.close()
        utillobj.switch_to_window(0)
         
        
        


if __name__ == "__main__":
    unittest.main()