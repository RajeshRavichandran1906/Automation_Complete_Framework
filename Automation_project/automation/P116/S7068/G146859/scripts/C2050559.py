'''
Created on Aug 18, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050559
TestCase Name = AHTML: Verify Filter operators against various DATE fields(Part 1).
'''
import unittest,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.lib import take_screenshot
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2050559_TestClass(BaseTestCase):

    def test_C2050559(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050559'
        """
        Step 01: Execute the attached AR-RP-141DA.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141DA.fex','S7068','mrid','mrpass')      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000records')
        column=['Order Number INTEGER', 'YYMD Order Date', 'MTRDYY Order Date', 'YYJUL Order Date', 'JULIAN Order Date', 'QYY Order Date', 'wrMtrYY Order Date', 'Mtr Order Date', 'Wtr Order Date']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for AR-RP-141DA")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141DA_page1.xlsx',"Step 01.3: Verify Data set of AR-RP-141DA page1")
          
        """
        Step 02: For the following DATE fields, select Filter, then Equals and use these values:
        """
        """YYMD Order Date - 19960201"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='19960201')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - value 19960201"""
        active_misobj.verify_page_summary('0','180of1000records,Page1of4', 'Step 02.3: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.4: Verify Page summary 1000of1000records after close dialog')
          
        """MTRDYY Order Date - MARCH 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='MARCH 1, 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - value MARCH 1, 1996"""
        active_misobj.verify_page_summary('0','180of1000records,Page1of4', 'Step 02.5: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.6: Verify Page summary 1000of1000records after close dialog')
          
        """YYJUL Order Date - 1996/001"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='1996/001')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - value 1996/001"""
        active_misobj.verify_page_summary('0','180of1000records,Page1of4', 'Step 02.7: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.8: Verify Page summary 1000of1000records after close dialog')
           
        """JULIAN Order Date - 96/092"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='96/092')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - value 96/092"""
        active_misobj.verify_page_summary('0','180of1000records,Page1of4', 'Step 02.9: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.10: Verify Page summary 1000of1000records after close dialog')
          
        """QYY Order Date - Q1 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Q1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 540 rows - value Q1 1996"""
        active_misobj.verify_page_summary('0','540of1000records,Page1of10', 'Step 02.11: Verify Page summary 540of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
          
        """wrMtrYY Order Date - Wednesday, May 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Wednesday, May 1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - value Wednesday, May 1 1996 """
        active_misobj.verify_page_summary('0','180of1000records,Page1of4', 'Step 02.13: Verify Page summary 180of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.14: Verify Page summary 1000of1000records after close dialog')
          
        """Mtr Order Date - June"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='June')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 100 rows - value June"""
        active_misobj.verify_page_summary('0','100of1000records,Page1of2', 'Step 02.15: Verify Page summary 100of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.16: Verify Page summary 1000of1000records after close dialog')
          
        """Wtr Order Date - Monday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Monday')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - value Monday"""
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 02.17: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.18: Verify Page summary 1000of1000records after close dialog')
          
        """
        Step 03: For the following DATE fields, select Filter, then Equals and use these values:
        """
        """YYMD Order Date - 19960201 & 19960601"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='19960201',value2='19960601')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 280 rows - values 19960201 & 19960601"""
        active_misobj.verify_page_summary('0','280of1000records,Page1of5', 'Step 03.1: Verify Page summary 280of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.2: Verify Page summary 1000of1000records after close dialog')
          
        """MTRDYY Order Date - MARCH 1, 1996 & APRIL 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='MARCH 1, 1996',value2='APRIL 1, 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values MARCH 1, 1996 & APRIL 1, 1996"""
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 03.3: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.4: Verify Page summary 1000of1000records after close dialog')
          
        """YYJUL Order Date - 1996/001 & 1996/061 & 1996/122"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='1996/001',value2='1996/061',value3='1996/122')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 540 rows - values 1996/001 & 1996/061 & 1996/122"""
        active_misobj.verify_page_summary('0','540of1000records,Page1of10', 'Step 03.5: Verify Page summary 540of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.6: Verify Page summary 1000of1000records after close dialog')
           
        """JULIAN Order Date - 96/032 & 96/061"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='96/032',value2='96/061')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values 96/032 & 96/061"""
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 03.7: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.8: Verify Page summary 1000of1000records after close dialog')
          
        """QYY Order Date - Q1 1996 & Q2 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Q1 1996',value2='Q2 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 1000 rows - values Q1 1996 & Q2 1996"""
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.9: Verify Page summary 540of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.10: Verify Page summary 1000of1000records after close dialog')
          
        """wrMtrYY Order Date - Thursday, February 1 1996 & Monday, April 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Thursday, February 1 1996',value2='Monday, April 1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values Thursday, February 1 1996 & Monday, April 1 1996 """
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 03.11: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.12: Verify Page summary 1000of1000records after close dialog')
          
        """Mtr Order Date - January & February"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='January',value2='February')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values January & February"""
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 03.13: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.14: Verify Page summary 1000of1000records after close dialog')
          
        """Wtr Order Date - Thursday & Friday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Thursday',value2='Friday')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values Thursday & Friday"""
        active_misobj.verify_page_summary('0','360of1000records,Page1of7', 'Step 03.15: Verify Page summary 360of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.16: Verify Page summary 1000of1000records after close dialog')
          
        """
        Step 04: For the following DATE fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
        """
        """YYMD Order Date - 19960201"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='19960201')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 19960201 to be Highlighted, page down to verify."""
        active_misobj.move_active_popup("1", "600", "200")
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds01_Page4.xlsx',"Step 04.1: Verify highlighted dataset 19960201")
        time.sleep(8)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page4of18', 'Step 04.2: Verify Page summary 1000of1000records after close dialog')
          
        """MTRDYY Order Date - MARCH 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='MARCH 1, 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value MARCH 1, 1996 to be Highlighted, page down to verify."""
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds02_Page7.xlsx',"Step 04.3: Verify highlighted dataset MARCH 1, 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page7of18', 'Step 04.4: Verify Page summary 1000of1000records after close dialog')
          
        """YYJUL Order Date - 1996/001"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='1996/001')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 1996/001 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds03_Page1.xlsx',"Step 04.5: Verify highlighted dataset 1996/001")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.6: Verify Page summary 1000of1000records after close dialog')
           
        """JULIAN Order Date - 96/092"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='96/092')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 96/092 to be Highlighted, page down to verify."""
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds04_Page10.xlsx',"Step 04.7: Verify highlighted dataset 96/092")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page10of18', 'Step 04.8: Verify Page summary 1000of1000records after close dialog')
          
        """QYY Order Date - Q1 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Q1 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Q1 1996 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds05_Page1.xlsx',"Step 04.9: Verify highlighted dataset Q1 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.10: Verify Page summary 1000of1000records after close dialog')
          
        """wrMtrYY Order Date - Wednesday, May 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Wednesday, May 1 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Wednesday, May 1 1996 to be Highlighted, page down to verify."""
        active_misobj.navigate_page('last_page')
        active_misobj.navigate_page('previous_page')
        active_misobj.navigate_page('previous_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds06_Page16.xlsx',"Step 04.11: Verify highlighted dataset Wednesday, May 1 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page16of18', 'Step 04.12: Verify Page summary 1000of1000records after close dialog')
          
        """Mtr Order Date - June"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='June')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value June to be Highlighted, page down to verify."""
        active_misobj.navigate_page('last_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds07_Page18.xlsx',"Step 04.13: Verify highlighted dataset June")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page18of18', 'Step 04.14: Verify Page summary 1000of1000records after close dialog')
          
        """Wtr Order Date - Monday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='Monday')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Monday to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds08_Page1.xlsx',"Step 04.15: Verify highlighted dataset Monday")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.16: Verify Page summary 1000of1000records after close dialog')
          
        """
        Step 05: For the following DATE fields, select Filter, then Not equal and use these values:
        """
        """YYMD Order Date - 19960201"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='19960201')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 820 rows - values not 19960201"""
        active_misobj.verify_page_summary('0','820of1000records,Page1of15', 'Step 05.1: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.2: Verify Page summary 1000of1000records after close dialog')
           
        """MTRDYY Order Date - MARCH 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='MARCH 1, 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 820 rows - values not MARCH 1, 1996"""
        active_misobj.verify_page_summary('0','820of1000records,Page1of15', 'Step 05.3: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.4: Verify Page summary 1000of1000records after close dialog')
           
        """YYJUL Order Date - 1996/001"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='1996/001')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 820 rows - values not 1996/001"""
        active_misobj.verify_page_summary('0','820of1000records,Page1of15', 'Step 05.5: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.6: Verify Page summary 1000of1000records after close dialog')
            
        """JULIAN Order Date - 96/092"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='96/092')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 820 rows - values not 96/092"""
        active_misobj.verify_page_summary('0','820of1000records,Page1of15', 'Step 05.7: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.8: Verify Page summary 1000of1000records after close dialog')
           
        """QYY Order Date - Q1 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Q1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 460 rows - values not Q1 1996"""
        active_misobj.verify_page_summary('0','460of1000records,Page1of9', 'Step 05.9: Verify Page summary 460of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.10: Verify Page summary 1000of1000records after close dialog')
           
        """wrMtrYY Order Date - Wednesday, May 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Wednesday, May 1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 180 rows - values not Wednesday, May 1 1996 """
        active_misobj.verify_page_summary('0','820of1000records,Page1of15', 'Step 05.11: Verify Page summary 820of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.12: Verify Page summary 1000of1000records after close dialog')
           
        """Mtr Order Date - June"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='June')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 100 rows - values not June"""
        active_misobj.verify_page_summary('0','900of1000records,Page1of16', 'Step 05.13: Verify Page summary 900of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.14: Verify Page summary 1000of1000records after close dialog')
           
        """Wtr Order Date - Monday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Monday')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 360 rows - values not Monday"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 05.15: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.16: Verify Page summary 1000of1000records after close dialog')
           
        """
        Step 06: For the following DATE fields, select Filter, then Not equal and use these multi-selected values:
        """
        """YYMD Order Date - 19960201 & 1996061"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='19960201',value2='19960601')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 720 rows - values not 19960201 or 19960601"""
        active_misobj.verify_page_summary('0','720of1000records,Page1of13', 'Step 06.1: Verify Page summary 720of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.2: Verify Page summary 1000of1000records after close dialog')
           
        """MTRDYY Order Date - MARCH 1, 1996 & APRIL 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='MARCH 1, 1996',value2='APRIL 1, 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 640 rows - values notMARCH 1, 1996 or APRIL 1, 1996"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 06.3: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.4: Verify Page summary 1000of1000records after close dialog')
           
        """YYJUL Order Date - 1996/001 & 1996/061 & 1996/122"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='1996/001',value2='1996/061',value3='1996/122')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 460 rows - values not 1996/001 or 1996/061 or 1996/122"""
        active_misobj.verify_page_summary('0','460of1000records,Page1of9', 'Step 06.5: Verify Page summary 460of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.6: Verify Page summary 1000of1000records after close dialog')
            
        """JULIAN Order Date - 96/032 & 96/061"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='96/032',value2='96/061')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 640 rows - values not96/032 or 96/061"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 06.7: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.8: Verify Page summary 1000of1000records after close dialog')
           
        """QYY Order Date - Q1 1996 & Q2 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Q1 1996',value2='Q2 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 0 rows - values not Q1 1996 or Q2 1996"""
        active_misobj.verify_page_summary('0','0of1000records,Page1of1', 'Step 06.9: Verify Page summary 0of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.10: Verify Page summary 1000of1000records after close dialog')
           
        """wrMtrYY Order Date - Thursday, February 1 1996 & Monday, April 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Thursday, February 1 1996',value2='Monday, April 1 1996')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 640 rows - values not Thursday, February 1 1996 or Monday, April 1 1996"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 06.11: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.12: Verify Page summary 1000of1000records after close dialog')
           
        """Mtr Order Date - January & February"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='January',value2='February')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 640 rows - values not January or February"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 06.13: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.14: Verify Page summary 1000of1000records after close dialog')
           
        """Wtr Order Date - Thursday & Friday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Thursday',value2='Friday')
        active_filter.filter_button_click('Filter')
        time.sleep(5)
        """Expect 640 rows - values Thursday & Friday"""
        active_misobj.verify_page_summary('0','640of1000records,Page1of12', 'Step 06.15: Verify Page summary 640of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.16: Verify Page summary 1000of1000records after close dialog')
          
         
        """
        Step 07: For the following DATE fields, select Filter, then Not equal and use these values:
        Click the Highlight button instead of the Filter button.
        """
        """YYMD Order Date - 19960201"""
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='19960201')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 19960201 to be Highlighted, page down to verify."""
        active_misobj.move_active_popup("1", "600", "200")
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds09_Page1.xlsx',"Step 07.1: Verify highlighted dataset not equal 19960201")
        time.sleep(8)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.2: Verify Page summary 1000of1000records after close dialog')
          
        """MTRDYY Order Date - MARCH 1, 1996"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='MARCH 1, 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value MARCH 1, 1996 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds10_Page1.xlsx',"Step 07.3: Verify highlighted dataset not equal MARCH 1, 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.4: Verify Page summary 1000of1000records after close dialog')
          
        """YYJUL Order Date - 1996/001"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='1996/001')
        active_filter.filter_button_click('Highlight')
        time.sleep(8)
        """Expect only rows with value 1996/001 to be Highlighted, page down to verify."""
        active_misobj.move_active_popup("1", "600", "200")
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds011_Page4.xlsx',"Step 07.5: Verify highlighted dataset not equal 1996/001")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page4of18', 'Step 07.6: Verify Page summary 1000of1000records after close dialog')
           
        """JULIAN Order Date - 96/092"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='96/092')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value 96/092 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds12_Page1.xlsx',"Step 07.7: Verify highlighted dataset not equal 96/092")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.8: Verify Page summary 1000of1000records after close dialog')
           
        """QYY Order Date - Q1 1996"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Q1 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Q1 1996 to be Highlighted, page down to verify."""
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds13_Page10.xlsx',"Step 07.9: Verify highlighted dataset not equal Q1 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page10of18', 'Step 07.10: Verify Page summary 1000of1000records after close dialog')
           
        """wrMtrYY Order Date - Wednesday, May 1 1996"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Wednesday, May 1 1996')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Wednesday, May 1 1996 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds14_Page1.xlsx',"Step 07.11: Verify highlighted dataset not equal Wednesday, May 1 1996")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.12: Verify Page summary 1000of1000records after close dialog')
           
        """Mtr Order Date - June"""
        active_misobj.select_menu_items('ITableData0', 7, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='June')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value June to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds15_Page1.xlsx',"Step 07.13: Verify highlighted dataset not equal June")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.14: Verify Page summary 1000of1000records after close dialog')
           
        """Wtr Order Date - Monday"""
        active_misobj.select_menu_items('ITableData0', 8, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='Monday')
        active_filter.filter_button_click('Highlight')
        time.sleep(5)
        """Expect only rows with value Monday to be Highlighted, page down to verify."""
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        active_misobj.navigate_page('next_page')
        utillobj.verify_data_set('ITableData0','rgb','C2050559_Ds16_Page4.xlsx',"Step 07.15: Verify highlighted dataset not equal Monday")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page4of18', 'Step 07.16: Verify Page summary 1000of1000records after close dialog')
           
if __name__ == '__main__':
    unittest.main()  
        
        
        