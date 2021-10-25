'''
Created on Sep 01, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053848
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.support.color import Color

class C2053848_TestClass(BaseTestCase):

    def test_C2053848(self):
        driver = self.driver 
#         driver.implicitly_wait(35) 
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        expected_text_color=utillity.UtillityMethods.color_picker(self, 'white', 'rgba')
        expected_bg_color=utillity.UtillityMethods.color_picker(self, 'red', 'rgba')
        cell_css="#ITableData0 .arGridColumnHeading > td > table"
        
        """
        Step 01: Execute the attached repro - 147775.fex.
        """
        utillobj.active_run_fex_api_login('147775.fex','S7078','mrid','mrpass')     
        column_list=['COUNTRY', 'CAR', 'MODEL', 'RETAIL_COST', 'DEALER_COST']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 01.1: Verify the column heading')
        actual_text_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('color')
        actual_text_color = Color.from_string(actual_text_color).rgba
        
        utillity.UtillityMethods.asequal(self, expected_text_color, actual_text_color, "Step 01.2: Verify Title Country's text color is White.")
        
        actual_bg_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('background-color')
        actual_bg_color = Color.from_string(actual_bg_color).rgba
        
        utillity.UtillityMethods.asequal(self, expected_bg_color, actual_bg_color, "Step 01.3: Verify Title Country's background color is Red.")
        utillobj.verify_data_set('ITableData0','I0r','147775.xlsx', 'Step 01.4: Verify the data set for 132748.fex Report')
        
        
        
        """
        Step 02: In report from country dropdown select pivot(cross table) eg:->GROUP BY(CAR)->ACCROSS(COUNTRY).
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','CAR','COUNTRY')
        time.sleep(1)
        utillobj.verify_pivot_data_set('piv1','C2053848_Ds01.xlsx',"Step 02.1: Verify data set to see the Pivot Table.")
        """
        Step 03: Check that column title color reflected in pivot total title.
        """
        elements=self.driver.find_elements_by_css_selector("#piv1 .arPivotColumnHeading")
        row_total_elem=elements[2]
        col_total_elem=elements[3]
        row_total_text=row_total_elem.text.strip()
        utillity.UtillityMethods.asequal(self, 'Total', row_total_text, "Step 03.1: Verify Title Row Total's text.")
        
        row_total_text_color=row_total_elem.value_of_css_property('color')
        row_total_text_color = Color.from_string(row_total_text_color).rgba
        
        utillity.UtillityMethods.asequal(self, expected_text_color, row_total_text_color, "Step 03.2: Verify Title Row Total's text color is White.")
        
        row_total_bg_color=row_total_elem.value_of_css_property('background-color')
        row_total_bg_color = Color.from_string(row_total_bg_color).rgba
        
        
        utillity.UtillityMethods.asequal(self, expected_bg_color, row_total_bg_color, "Step 03.3: Verify Title Row Total's background color is Red.")
        
        
        col_total_text=col_total_elem.text.strip()
        
        
        utillity.UtillityMethods.asequal(self, 'Total', col_total_text, "Step 03.4: Verify Title Total's text.")
        
        col_total_text_color=col_total_elem.value_of_css_property('color')
        col_total_text_color = Color.from_string(col_total_text_color).rgba
        
        
        utillity.UtillityMethods.asequal(self, expected_text_color, col_total_text_color, "Step 03.5: Verify Title Column Total's text color is White.")
        
        col_total_bg_color=col_total_elem.value_of_css_property('background-color')
        col_total_bg_color = Color.from_string(col_total_bg_color).rgba
        
        utillity.UtillityMethods.asequal(self, expected_bg_color, col_total_bg_color, "Step 03.6: Verify Title Column Total's background color is Red.")


if __name__ == '__main__':
    unittest.main()