'''
Created on Sep 01, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055541
'''
from common.lib.global_variables import Global_variables
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest, time

class C2055541_TestClass(BaseTestCase):

    def test_C2055541(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        if Global_variables.browser_name in ['firefox']:
            expected_text_color=utillity.UtillityMethods.color_picker(self, 'white', 'rgb')
            expected_bg_color=utillity.UtillityMethods.color_picker(self, 'red', 'rgb')
        else:
            expected_text_color=utillity.UtillityMethods.color_picker(self, 'white', 'rgba')
            expected_bg_color=utillity.UtillityMethods.color_picker(self, 'red', 'rgba')
        cell_css="#ITableData0 .arGridColumnHeading > td > table"

        """
        Step 01: Execute the attached repro - 132748.fex.
        """
        utillobj.active_run_fex_api_login('132748.fex','S7078','mrid','mrpass')     
        column_list=['COUNTRY', 'CAR', 'MODEL', 'RETAIL_COST', 'DEALER_COST']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 01.01: Verify the column heading')
        actual_text_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('color')
        utillity.UtillityMethods.asequal(self, expected_text_color, actual_text_color, "Step 01.02: Verify Title Country's text color is White.")
        actual_bg_color=self.driver.find_element_by_css_selector(cell_css).value_of_css_property('background-color')
        utillity.UtillityMethods.asequal(self, expected_bg_color, actual_bg_color, "Step 01.03: Verify Title Country's background color is Red.")
        utillobj.verify_data_set('ITableData0','I0r','132748.xlsx', 'Step 01.04: Verify the data set for 132748.fex Report')
        """
        Step 02: From report any field dropdown click pivot cross table eg: Country->GROUP BY(CAR)->ACROSS(COUNTRY).
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','CAR','COUNTRY')
        time.sleep(1)
        utillobj.verify_pivot_data_set('piv1','C2055541_Ds01.xlsx',"Step 02.01: Verify data set to see the Pivot Table.")
        """
        Step 03: Verify color red is reflected in column titles.
        """
        elements=self.driver.find_elements_by_css_selector("#piv1 .arPivotColumnHeading")
        country_elem=elements[0]
        car_elem=elements[1]
        country_text=country_elem.text.strip()
        utillity.UtillityMethods.asequal(self, 'COUNTRY', country_text, "Step 03.01: Verify Title COUNTRY's text.")
        country_text_color=country_elem.value_of_css_property('color')
        utillity.UtillityMethods.asequal(self, expected_text_color, country_text_color, "Step 03.02: Verify Title COUNTRY's text color is White.")
        country_bg_color=country_elem.value_of_css_property('background-color')
        utillity.UtillityMethods.asequal(self, expected_bg_color, country_bg_color, "Step 03.03: Verify Title COUNTRY's background color is Red.")
        
        car_text=car_elem.text.strip()
        utillity.UtillityMethods.asequal(self, 'CAR', car_text, "Step 03.04: Verify Title CAR's text.")
        car_text_color=car_elem.value_of_css_property('color')
        utillity.UtillityMethods.asequal(self, expected_text_color, car_text_color, "Step 03.05: Verify Title CAR's text color is White.")
        car_bg_color=car_elem.value_of_css_property('background-color')
        utillity.UtillityMethods.asequal(self, expected_bg_color, car_bg_color, "Step 03.06: Verify Title CAR's background color is Red.")
        
if __name__ == '__main__':
    unittest.main()