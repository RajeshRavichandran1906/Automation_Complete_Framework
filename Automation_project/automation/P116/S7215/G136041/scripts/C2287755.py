'''
Created on April 20, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7215
Test Case =  http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2287755
Description = AHTML: Report with custom stylesheet and filtering produces incorrect report when filter is Cleared. (ACT-1095)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, active_filter_selection, ia_run
from common.lib import utillity
import unittest, time
from selenium.webdriver.support.color import Color


class C2287755_TestClass(BaseTestCase):

    def test_C2287755(self):
        
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """ Step 1: Execute the attached repro - ACT-1095.fex
                    Expect to see the following Active Report.
                    Notice the changed Filter panel display.
        """
        utillobj.active_run_fex_api_login("act-1095.fex", "S7215", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, ia_runobj.home_page_long_timesleep)
        time.sleep(7)
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 01.1: Verify Page Summary")
#         ia_runobj.create_table_data_set('table#ITableData1', 'C2287755_DS01.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData1', 'C2287755_DS01.xlsx', 'Step 01.2: Data set verified')
        
        
        """ Step 2: From the Dealer_Cost drop down select 
                    Filter/Less than or equal to.
                    Select value 6,000
                    Expect to see the following Filter panel in a larger font and displaying a blue color.
        """
        miscelanousobj.select_menu_items('ITableData1', 3, 'Filter', 'Less than or equal to')
        time.sleep(7)
        miscelanousobj.move_active_popup(1, 755, 126)
        time.sleep(10)
        filterselectionobj.create_filter(1, 'Less than or equal to', table_id='ITableData1', value1='6,000')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        time.sleep(1)
        actual=filter_value[1].text
        status = False
        if actual == '6,000':
            status = True
        utillobj.asequal(status, True, 'Step 2: Expect to see the Active Report, the Filter menu and the selected values')
        actual_panel_color=Color.from_string(self.driver.find_element_by_css_selector("#wall1 #wtop1").value_of_css_property("background-color")).rgba
        expected_panel_color=utillobj.color_picker('blue_1', 'rgba')
        utillobj.asequal(expected_panel_color, actual_panel_color , "Step 2.1: Verify panel window blue color.")
        
        
        """ Step 3: Click the Filter button.
                    Expect to see the Filtered report.
        """
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(1, '10of18records,Page1of1', "Step 03.1: Verify Page Summary")
#         ia_runobj.create_table_data_set('table#ITableData1', 'C2287755_DS02.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData1', 'C2287755_DS02.xlsx', 'Step 03.2: Data set verified')
        time.sleep(3)
                
        
        """ Step 4: Click the Clear All option in the Filter panel.
                    Expect to see the original report redisplay and the Filter panel still present.
        """
        time.sleep(1)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(3)
        parent_css="#MAINTABLE_wbody1 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 04.1: Verify Page Summary")
        ia_runobj.verify_table_data_set('table#ITableData1', 'C2287755_DS01.xlsx', 'Step 04.2: Data set verified')
        
        
        
        """ Step 5: Close the Filter panel.
                    Expect to see the original report.
                    Verify that all columns contain the data appropriate to the column heading.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(1)
        parent_css="#MAINTABLE_wbody1 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(3)
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 05.1: Verify Page Summary")
        ia_runobj.verify_table_data_set('table#ITableData1', 'C2287755_DS01.xlsx', 'Step 05.2: Data set verified')
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()