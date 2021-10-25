'''
Created on Aug 2, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050557
TestCase Name = AHTML: Verify Filter operators against various Decimal fields(Part 1).
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


class C2050557_TestClass(BaseTestCase):

    def test_C2050557(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050557'
        """
            Step 01: Execute AR-RP-141DE to produce the mixed field output report.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141DE.fex','S7068','mrid','mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        utillobj.synchronize_with_number_of_element("table .arGridBar table table > tbody", 1, 50, 1)      
                
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000records')
        column=['Order Number INTEGER', 'D10.2 Unit Price', 'D10.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'Store Code']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for AR-RP-141DE")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141DE_page1.xlsx',"Step 01.3: Verify Data set of AR-RP-141DE page1")
         
        """
        Step 02: For the following DECIMAL fields, select Filter, then Equals and use these values:
        D10.2 Unit Price - 17.00
        """        
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', value1='17.00')
        active_filter.filter_button_click('Filter')
        """Expect 99 rows - value 17.00"""
        active_misobj.verify_page_summary('0','99of1000records,Page1of2', 'Step 02.1: Verify Page summary 99of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,026.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='$0,000,026.00')
        active_filter.filter_button_click('Filter')
        """Expect 134 rows - value $0,000,026.00"""
        active_misobj.verify_page_summary('0','134of1000records,Page1of3', 'Step 02.3: Verify Page summary 134of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.13D+02"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='0.13D+02')
        active_filter.filter_button_click('Filter')
        """Expect 84 rows - value 0.13D+02"""
        active_misobj.verify_page_summary('0','84of1000records,Page1of2', 'Step 02.5: Verify Page summary 84of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (81.00)"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='(81.00)')
        active_filter.filter_button_click('Filter')
        """Expect 218 rows - value (81.00)"""
        active_misobj.verify_page_summary('0','218of1000records,Page1of4', 'Step 02.7: Verify Page summary 218of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='140.00 CR')
        active_filter.filter_button_click('Filter')
        """Expect 67 rows - value 140.00CR"""
        active_misobj.verify_page_summary('0','67of1000records,Page1of2', 'Step 02.9: Verify Page summary 67of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 28.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='28.00%')
        active_filter.filter_button_click('Filter')
        """Expect 148 rows - value 28.00%"""
        active_misobj.verify_page_summary('0','148of1000records,Page1of3', 'Step 02.11: Verify Page summary 148of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.12: Verify Page summary 1000of1000records after close dialog')
         
        """
        Step 03:For the following DECIMAL fields, select Filter, then Equals and use these multiple values:
        D10.2 Unit Price - 13.00 & 17.00
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', value1='13.00',value2='17.00')
        active_filter.filter_button_click('Filter')
        """Expect 183 rows - values 13.00 & 17.00"""
        active_misobj.verify_page_summary('0','183of1000records,Page1of4', 'Step 03.1: Verify Page summary 183of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='$0,000,125.00',value2='$0,000,140.00')
        active_filter.filter_button_click('Filter')
        """Expect 133 rows - values $0,000,125.00 & $0,000,140.00"""
        active_misobj.verify_page_summary('0','133of1000records,Page1of3', 'Step 03.3: Verify Page summary 133of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.26D+02 & 0.28D+02 """
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='0.26D+02',value2='0.28D+02')
        active_filter.filter_button_click('Filter')
        """Expect 282 rows - values 0.26D+02 & 0.28D+02"""
        active_misobj.verify_page_summary('0','282of1000records,Page1of5', 'Step 03.5: Verify Page summary 282of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (76.00) & (58.00) & (28.00))"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='(76.00)',value2='(58.00)',value3='(28.00)')
        active_filter.filter_button_click('Filter')
        """Expect 265 rows - values (76.00) & (58.00) & (28.00)"""
        active_misobj.verify_page_summary('0','265of1000records,Page1of5', 'Step 03.7: Verify Page summary 265of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR & 13.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='140.00 CR',value2='13.00 CR')
        active_filter.filter_button_click('Filter')
        """Expect 151 rows - values 140.00CR & 13.00CR"""
        active_misobj.verify_page_summary('0','151of1000records,Page1of3', 'Step 03.9: Verify Page summary 151of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 13.00% & 76.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='13.00%',value2='76.00%')
        active_filter.filter_button_click('Filter')
        """Expect 117 rows - values 13.00% & 76.00%"""
        active_misobj.verify_page_summary('0','117of1000records,Page1of3', 'Step 03.11: Verify Page summary 148of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03.12: Verify Page summary 1000of1000records after close dialog')
         
        """
        Step 04:For the following ALPHA fields, select Filter, then Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
        D10.2 Unit Price - 13.00
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', value1='13.00')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 13.00 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds01.xlsx',"Step 04.1: Verify highlighted dataset of D10.2 Unit Price - 13.00")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,125.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='$0,000,125.00')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value $0,000,125.00 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds02.xlsx',"Step 04.3: Verify highlighted dataset of D10.2LM Unit Price - $0,000,125.00")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.26D+02"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='0.26D+02')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 0.26D+_02 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds03.xlsx',"Step 04.5: Verify highlighted dataset of D10.2E Unit Price - 0.26D+02")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (76.00)"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='(76.00)')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value (76.00) to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds04.xlsx',"Step 04.7: Verify highlighted dataset of D10.2B Unit Price - (76.00)")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='140.00 CR')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 140.00CR to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds05.xlsx',"Step 04.9: Verify highlighted dataset of D10.2R Unit Price - 140.00CR")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 17.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals',value1='17.00%')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 17.00% to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds06.xlsx',"Step 04.11: Verify highlighted dataset of D10.2% Unit Price - 17.00%")
        time.sleep(5)
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 04.12: Verify Page summary 1000of1000records after close dialog')
         
        """
        Step 05: For the following DECIMAL fields, select Filter, then Equals and use these values:
        D10.2 Unit Price - 17.00
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal', value1='17.00')
        active_filter.filter_button_click('Filter')
        """Expect 901 rows - value 17.00"""
        active_misobj.verify_page_summary('0','901of1000records,Page1of16', 'Step 05.1: Verify Page summary 901of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.2: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2LM Unit Price - $0,000,026.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='$0,000,026.00')
        active_filter.filter_button_click('Filter')
        """Expect 866 rows - value $0,000,026.00"""
        active_misobj.verify_page_summary('0','866of1000records,Page1of16', 'Step 05.3: Verify Page summary 866of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.4: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2E Unit Price - 0.13D+02"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='0.13D+02')
        active_filter.filter_button_click('Filter')
        """Expect 916 rows - value 0.13D+02"""
        active_misobj.verify_page_summary('0','916of1000records,Page1of17', 'Step 05.5: Verify Page summary 916of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.6: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2B Unit Price - (81.00)"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Equals')
        active_filter.create_filter(1, 'Not equal',value1='(81.00)')
        active_filter.filter_button_click('Filter')
        """Expect 782 rows - value (81.00)"""
        active_misobj.verify_page_summary('0','782of1000records,Page1of14', 'Step 05.7: Verify Page summary 782of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.8: Verify Page summary 1000of1000records after close dialog')
                  
        """D10.2R Unit Price - 140.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')
        active_filter.create_filter(1, 'Not equal',value1='140.00 CR')
        active_filter.filter_button_click('Filter')
        """Expect 933 rows - value 140.00CR"""
        active_misobj.verify_page_summary('0','933of1000records,Page1of17', 'Step 05.9: Verify Page summary 933of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.10: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2% Unit Price - 28.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Equals')
        active_filter.create_filter(1, 'Not equal',value1='28.00%')
        active_filter.filter_button_click('Filter')
        """Expect 852 rows - value 28.00%"""
        active_misobj.verify_page_summary('0','852of1000records,Page1of15', 'Step 05.11: Verify Page summary 852of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 05.12: Verify Page summary 1000of1000records after close dialog')
          
        """
        Step 06:For the following DECIMAL fields, select Filter, then Equals and use these multiple values:
        D10.2 Unit Price - 13.00 & 17.00
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal', value1='13.00',value2='17.00')
        active_filter.filter_button_click('Filter')
        """Expect 817 rows - values not 13.00 or 17.00"""
        active_misobj.verify_page_summary('0','817of1000records,Page1of15', 'Step 06.1: Verify Page summary 817of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.2: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2LM Unit Price - $0,000,125.00 & $0,000,140.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='$0,000,125.00',value2='$0,000,140.00')
        active_filter.filter_button_click('Filter')
        """Expect 867 rows - values not $0,000,125.00 or $0,000,140.00"""
        active_misobj.verify_page_summary('0','867of1000records,Page1of16', 'Step 06.3: Verify Page summary 867of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.4: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2E Unit Price - 0.26D+02 & 0.28D+02 """
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='0.26D+02',value2='0.28D+02')
        active_filter.filter_button_click('Filter')
        """Expect 718 rows - values not 0.26D+02 or 0.28D+02 """
        active_misobj.verify_page_summary('0','718of1000records,Page1of13', 'Step 06.5: Verify Page summary 718of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.6: Verify Page summary 1000of1000records after close dialog')
           
        """D10.2B Unit Price - (76.00) & (58.00) & (28.00))"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='(76.00)',value2='(58.00)',value3='(28.00)')
        active_filter.filter_button_click('Filter')
        """Expect 735 rows - values not (76.00) or (58.00) or (28.00)"""
        active_misobj.verify_page_summary('0','735of1000records,Page1of13', 'Step 06.7: Verify Page summary 735of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.8: Verify Page summary 1000of1000records after close dialog')
                  
        """D10.2R Unit Price - 140.00CR & 13.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='140.00 CR',value2='13.00 CR')
        active_filter.filter_button_click('Filter')
        """Expect 849 rows - values not 140.00CR or 13.00CR"""
        active_misobj.verify_page_summary('0','849of1000records,Page1of15', 'Step 06.9: Verify Page summary 849of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.10: Verify Page summary 1000of1000records after close dialog')
          
        """D10.2% Unit Price - 13.00% & 76.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='13.00%',value2='76.00%')
        active_filter.filter_button_click('Filter')
        """Expect 883 rows - values not 13.00% or 76.00%"""
        active_misobj.verify_page_summary('0','883of1000records,Page1of16', 'Step 06.11: Verify Page summary 883of1000records')
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 06.12: Verify Page summary 1000of1000records after close dialog')
          
        """
        Step 07:For the following ALPHA fields, select Filter, then Not equal and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
        D10.2 Unit Price - 13.00
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal', value1='13.00')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 13.00 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds07.xlsx',"Step 07.1: Verify highlighted dataset of D10.2 Unit Price - 13.00")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.2: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2LM Unit Price - $0,000,125.00"""
        active_misobj.select_menu_items('ITableData0', 2, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='$0,000,125.00')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value $0,000,125.00 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds08.xlsx',"Step 07.3: Verify highlighted dataset of D10.2LM Unit Price - $0,000,125.00")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.4: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2E Unit Price - 0.26D+02"""
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='0.26D+02')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 0.26D+_02 to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds09.xlsx',"Step 07.5: Verify highlighted dataset of D10.2E Unit Price - 0.26D+02")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.6: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2B Unit Price - (76.00)"""
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='(76.00)')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value (76.00) to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds10.xlsx',"Step 07.7: Verify highlighted dataset of D10.2B Unit Price - (76.00)")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.8: Verify Page summary 1000of1000records after close dialog')
                 
        """D10.2R Unit Price - 140.00CR"""
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='140.00 CR')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 140.00CR to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds11.xlsx',"Step 07.9: Verify highlighted dataset of D10.2R Unit Price - 140.00CR")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.10: Verify Page summary 1000of1000records after close dialog')
         
        """D10.2% Unit Price - 17.00%"""
        active_misobj.select_menu_items('ITableData0', 6, 'Filter','Not equal')
        active_filter.create_filter(1, 'Not equal',value1='17.00%')
        active_filter.filter_button_click('Highlight')
        """Expect only rows with value 17.00% to be Highlighted, page down to verify."""
        utillobj.verify_data_set('ITableData0','rgb','C2050557_Ds12.xlsx',"Step 07.11: Verify highlighted dataset of D10.2% Unit Price - 17.00%")
        active_misobj.close_popup_dialog("1")
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 07.12: Verify Page summary 1000of1000records after close dialog')
 

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
