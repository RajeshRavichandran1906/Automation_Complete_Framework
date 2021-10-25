'''
Created on April 11, 2017

@author: AAKhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227214
Description : AHTML:Highlight Row- wrong row after sorting performed (Act-437)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity,core_utility

class C2227214_TestClass(BaseTestCase):

    def test_C2227214(self):
        
        """ class object """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj= visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """ This function to move mouse on page summary    """
        def move_mouse():
            
            element=driver.find_element_by_css_selector('table[id="IWindowBody0"] .arGridBar')
            core_utils.move_to_element(element)
        
        """ Step 1: Execute the attached repro - Act-437.fex
                    Expect to see an 18 row report.
        """
        utillobj.active_run_fex_api_login("Act-437.fex", "S7070", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.01: Verify all columns listed on the report Act-437.fex')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.02: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227214_DS01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227214_DS01.xlsx','Step 01.03: Verify data set')
             
        """ Step 2: Select Sort descending from CAR column dropdown.
                    Expect to see the report in Descending CAR order.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Descending')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02.01: Verify all columns listed on the report Act-437.fex')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 02.02: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227214_DS02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227214_DS02.xlsx','Step 02.03: Verify data set')
               
        """ Step 3: Left click on 'TR7" from model column and select Highlight row option.
                    Expect to see the TR7 row and no others Highlighted.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 3, 2,'Highlight Row', original_rownum=0)
        time.sleep(1)
        move_mouse()
        miscelanousobj.verify_highlighted_rows('ITableData0', 1, 'Step 03.01: Verify row is highlighted as expected.')
        time.sleep(2)
         
        """ Step 4: Left click on TR7 and select Unhighlight Row and from any field drop down click restore original.
                    Click on the first Alfa Romeo row and select Highlight Value.
                    Expect to see the all 3 Alfa Romeo rows and no others Highlighted.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 3,'Unhighlight Row')
        time.sleep(3)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Restore Original')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227214_DS01.xlsx','Step 04.01: Verify data set')
        time.sleep(1)
        miscelanousobj.select_field_menu_items('ITableData0', 6, 1,'Highlight Value')
        time.sleep(3)
        move_mouse()
        miscelanousobj.verify_highlighted_rows('ITableData0', 3, 'Step 04.02: Verify all 3 Alfa Romeo rows and no others Highlighted.')
        time.sleep(2)
        
        """ Step 5: From the drop down for CAR, select Sort Descending.
                    Expect to see the report sorted in Descending CAR order.
                    Also expect to see that the Highlighted rows remain only for Alfa Romeo.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Descending')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 05.01: Verify all columns listed on the report Act-437.fex')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 05.02: Verify Page Summary")
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227214_DS02.xlsx','Step 05.03: Verify data set')
        time.sleep(3)
        move_mouse()
        miscelanousobj.verify_highlighted_rows('ITableData0', 3, 'Step 05.04: Verify all 3 Alfa Romeo rows and no others Highlighted.')
        time.sleep(2)
        
        """ Step 6: From the drop down for CAR, select Sort Ascending.
                    Expect to see the report sorted in Ascending CAR order.
                    Also expect to see that the Highlighted rows remain only for Alfa Romeo.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Ascending')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'SALES']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.01: Verify all columns listed on the report Act-437.fex')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 06.02: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227214_DS03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227214_DS03.xlsx','Step 06.03: Verify data set')
        time.sleep(3)
        move_mouse()
        miscelanousobj.verify_highlighted_rows('ITableData0', 3, 'Step 06.04: Verify all 3 Alfa Romeo rows and no others Highlighted.')
                
if __name__ == "__main__":
    unittest.main()