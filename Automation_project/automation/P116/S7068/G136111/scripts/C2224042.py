'''
Created on April 07, 2017

@author: AAKhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2224042
Description : AHTML:Cache Report Filtering using negative values(ACT-1067)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea, active_filter_selection
from common.lib import utillity
import unittest, time, re


class C2224042_TestClass(BaseTestCase):

    def test_C2224042(self):
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        
        """ Step 1: Execute the attached repro - act-1067.fex
                    Expect to see the following Active report with 4521 records.
        """
        utillobj.active_run_fex_api_login("act-1067.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report act-1067.fex')
        miscelanousobj.verify_page_summary(0, '5409of5409records,Page1of95', "Step 01.2: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS01.xlsx','Step 01.3: Verify data set')
        
        
        """ Step 2: Click the drop down for Gross Profit and select Sort Ascending.
                    Expect to see 9 negative values appear at the top of the report.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Sort Ascending')
        time.sleep(7)
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS02.xlsx','Step 02: Verify data set')
        
        
        """ Step 3: From the drop down for Gross Profit, select Equals, then select values -$430.80 and -$.03 from the value box.
                    Expect to see the Filter menu with 2 values secected(highlighted).
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        time.sleep(7)
        filterselectionobj.create_filter(1, 'Equals', 'large', value1='-$430.80', value2='-$.03')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        actual=filter_value[1].text
        status = False
        if actual in ['*-$430.80','*-$.03'] :
            status = True
        utillobj.asequal(status, True, 'Step 3: Expect to see the Active Report, the Filter menu and the selected values')
        
        
        """ Step 4: Click the Filter button.
                    Expect to see two rows, one for each of the values selected.
        """
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of5409records,Page1of1', "Step 04.1: Verify Page Summary")
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 04.2: Verify all columns listed on the report act-1067.fex')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS03.xlsx','Step 04.3: Verify data set')
        
        
        """ Step 5: Clear the filter and again select Filter Equals from the Gross Profit drop down control.
                    Use the Filter scroll bar to navigate to the bottom of the value box and select the last three values: 
                    $3,150,971.88, $3,179,848.57 and $3,480,231.39
                    Expect to see the three highest values selected(highlighted).
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        time.sleep(7)
        filterselectionobj.create_filter(1, 'Equals', 'large', value1='$3,145,370.78', value2='$3,150,971.88', value3='$3,476,595.04')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        actual=filter_value[1].text
        status = False
        if actual in ['*$3,145,370.78','*$3,150,971.88','*$3,476,595.04']:
            status = True
        utillobj.asequal(status, True, 'Step 5: Expect to see the Active Report, the Filter menu and the selected values')
        
        
        """ Step 6: Click the Filter button.
                    Expect to see three rows, one for each of the values selected.
        """
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '3of5409records,Page1of1', "Step 06.1: Verify Page Summary")
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 06.2: Verify all columns listed on the report act-1067.fex')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS04.xlsx','Step 06.3: Verify data set')
        
        
        """ Step 7: Clear the filter and again select Filter Equals from the Gross Profit drop down control.
                    Use the Filter scroll bar to navigate to the bottom of the value box and select the lowest value(first negative) and the highest value(bottom of the filter box).
                    Click Filter.
                    Expect to see two rows, one for the lowest value and one for the highest value.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        time.sleep(7)
        filterselectionobj.create_filter(1, 'Equals', 'large', value1='-$430.80', value2='$3,476,595.04')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        actual=filter_value[1].text
        status = False
        if actual in ['*-$430.80','*$3,476,595.04']:
            status = True
        utillobj.asequal(status, True, 'Step 7: Expect to see the Active Report, the Filter menu and the selected values')
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of5409records,Page1of1', "Step 07.1: Verify Page Summary")
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 07.2: Verify all columns listed on the report act-1067.fex')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS05.xlsx','Step 07.3: Verify data set')
        
        
        
        """ Step 8: Clear the filter and select Less than or Equal from the Gross Profit drop down control.
                    Select the first positive value, $4.99.
                    Click Filter.
                    Expect to see ten rows, one for the positive value and nine rows for the negative values.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Less than or equal to')
        time.sleep(7)
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='$4.99')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        actual=filter_value[1].text
        status = False
        if actual == '$4.99':
            status = True
        utillobj.asequal(status, True, 'Step 8: Expect to see the Active Report, the Filter menu and the selected values')
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '15of5409records,Page1of1', "Step 08.1: Verify Page Summary")
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 08.2: Verify all columns listed on the report act-1067.fex')
        utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS06.xlsx','Step 08.3: Verify data set')
         
         
         
        """ Step 9: Clear the filter and select Greater than or Equal from the Gross Profit drop down control.
                    Navigate to the bottom of the value box and select value $3,150,971.88
                    Click Filter.
                    Expect to see three rows, one for each of the three highest values.
        """
        miscelanousobj.close_popup_dialog('1')
        time.sleep(2)
        miscelanousobj.select_menu_items('ITableData0', 2, 'Filter','Greater than or equal to')
        time.sleep(7)
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large', value1='$3,145,370.78')
        filter_value = driver.find_elements_by_css_selector("#FiltTable1 .arFilterItemDrowpDown")
        actual=filter_value[1].text
        status = False
        if actual == '$3,145,370.78':
            status = True
        utillobj.asequal(status, True, 'Step 9: Expect to see the Active Report, the Filter menu and the selected values')
        time.sleep(1)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '3of5409records,Page1of1', "Step 09.1: Verify Page Summary")
        column_list=['Customer State Province', 'Product Category', 'Gross Profit']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 09.2: Verify all columns listed on the report act-1067.fex')
        utillobj.create_data_set('ITableData0', 'I0r', 'C2224042_DS07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2224042_DS07.xlsx','Step 09.3: Verify data set')
        


if __name__ == "__main__":
    unittest.main()