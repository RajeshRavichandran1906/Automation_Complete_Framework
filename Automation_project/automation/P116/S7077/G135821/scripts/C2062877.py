'''
Created on Nov 2, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2062877
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest,time

class C2062877_TestClass(BaseTestCase):

    def test_C2062877(self):
        
        driver = self.driver #Driver reference object created'
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Execute the attached repro - 92542005.fex
        """
        utillobj.active_run_fex_api_login("92542005.fex", "S7077", 'mrid', 'mrpass')
        time.sleep(9)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary 18of18records")
        column_list=['COUNTRY', 'CAR', '% SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report 92542005.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '92542005.xlsx','Step 01.2: Verify data set')
        
        """
        Step 02: Click on the down arrow in the '% SALES' column. Highlight Filter > Equals but don't select it yet.
        The filter selection pulldown should appear normally with no errors reported.
        """
        option=['Equals','Not equal','Greater than','Greater than or equal to','Less than','Less than or equal to','Between','Not Between','Contains','Contains (match case)','Omits','Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',2,'Filter',option,'Step 02: Verify Filter menu')
        time.sleep(2)
        
        """
        Step 03: Click on Filter > Equals; select a value of 0.
        Click on Filter.
        Move the filter box so the resulting report is visible.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        time.sleep(19)
        filterobj.create_filter(1, 'Equals', value1='0')
        time.sleep(2)
        filterobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.move_active_popup("1", "600", "200")
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2062877_Ds01.xlsx', 'Step 03: Verify 5 records are listed')
       

if __name__ == "__main__":
    unittest.main()