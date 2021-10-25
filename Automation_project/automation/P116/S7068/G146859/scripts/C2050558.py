'''
Created on Aug 2, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050522
Description : 

Numeric Decimal field tests.
These tests use Filter, then:

Greater than
Greater than or equal to
Less than
Less than or equal to
Between
Not Between

Contains and Omits are not applicable to Numeric fields, as they do not consist of a set of digits but a value.

'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages import active_pivot_comment  
from common.lib import utillity
import unittest
import time
import re

class C2050558_TestClass(BaseTestCase):

    def test_C2050558(self):
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2050558'
        
        """
            Step 01:Execute the attached AR-RP-141DE.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141DE.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
        
       
         
        #utillobj.verify_data_set('ITableData0','I0r','AR-RP-193_page1.xlsx',"Step 01: Verify Page 1 data loaded correctly ")
        
        #utillobj.create_data_set('ITableData0','I0r','AR-RP-193_page1.xlsx')
        
        """Step 02 : For the following DECIMAL fields, select Filter, then Greater than and use these values:

        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00%
      
      
        """
        #D10.2 Unit Price - 17.00
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than")
        
        filterselectionobj.create_filter(1, 'Greater than',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 02: Expect 817 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2LM Unit Price - $0,000,026.00
        
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than")
        
        filterselectionobj.create_filter(1, 'Greater than',value1='$0,000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '683of1000records,Page1of12', "Step 02: Expect 683 rows - value $0,000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #D10.2E Unit Price - 0.13D+02
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
         
        filterselectionobj.create_filter(1, 'Greater than',value1='0.13D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 02: Expect 916 rows - value 0.13D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #D10.2B Unit Price - (81.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than")
        
        filterselectionobj.create_filter(1, 'Greater than',value1='(81.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '582of1000records,Page1of11', "Step 02: Expect 582 rows - value (81.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2R Unit Price - 140.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than")
        
        filterselectionobj.create_filter(1, 'Greater than',value1='140.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '933of1000records,Page1of17', "Step 02: Expect 933 rows - value 140.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 28.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than")
        
        filterselectionobj.create_filter(1, 'Greater than',value1='28.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '535of1000records,Page1of10', "Step 02: Expect 933 rows - value 140.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        """Step 03:For the following DECIMAL fields, select Filter, then Greater than or equal to and use these values:

        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00 CR
        D10.2% Unit Price - 28.00%
        """
        
        #D10.2 Unit Price - 17.00
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 03: Expect 916 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2LM Unit Price - $0,000,026.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='$0,000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 03: Expect 817 rows - value $0,000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2E Unit Price - 0.13D+02
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='0.13D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02: Expect 1000 rows - value 0.13D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2B Unit Price - (81.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='(81.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '800of1000records,Page1of15', "Step 03: Expect 800 rows - value (81.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2R Unit Price - 140.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='140.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03: Expect 1000 rows - value 140.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 28.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Greater than or equal to")
        
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='28.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '683of1000records,Page1of12', "Step 03: Expect 683 rows - value 28.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()

        """Step 04: For the following DECIMAL fields, select Filter, then Less than and use these values:

        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00% """
        
        #D10.2 Unit Price - 17.00
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 04: Expect 84 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        time.sleep(3)
        #D10.2LM Unit Price - $0,000,026.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='$0,000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 04: EExpect 183 rows - value $0,000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2E Unit Price - 0.13D+02
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='0.13D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 04: Expect 0 rows - value 0.13D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2B Unit Price - (81.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='(81.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '200of1000records,Page1of4', "Step 04: Expect 800 rows - value (81.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2R Unit Price - 125.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='125.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        #ISSUE present
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 04: Expect 67 rows - value 125.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 28.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than")
        
        filterselectionobj.create_filter(1, 'Less than',value1='28.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 04: Expect 317 rows - value 28.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        """Step 05:  For the following DECIMAL fields, select Filter, then Less than or equal to the selected value:

        D10.2 Unit Price - 17.00
        D10.2LM Unit Price - $0,000,026.00
        D10.2E Unit Price - 0.13D+02
        D10.2B Unit Price - (81.00)
        D10.2R Unit Price - 140.00CR
        D10.2% Unit Price - 28.00%
        """
        
        #D10.2 Unit Price - 17.00
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 05: Expect 183 rows - value 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2LM Unit Price - $0,000,026.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='$0,000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '317of1000records,Page1of6', "Step 05: EExpect 317 rows - value $0,000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2E Unit Price - 0.13D+02
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='0.13D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 05: Expect 84 rows - value 0.13D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2B Unit Price - (81.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='(81.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '418of1000records,Page1of8', "Step 05: Expect 418 rows - value (81.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 67 rows - value 140.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='140.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 05: Expect 67 rows - value 140.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 28.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Less than or equal to")
        
        filterselectionobj.create_filter(1, 'Less than or equal to',value1='28.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '465of1000records,Page1of9', "Step 02: Expect 465 rows - value 28.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
 

        """Step 06: For the following DECIMAL fields, select Filter, then Between the selected pair of values:

        D10.2 Unit Price - 17.00 & 26.00
        D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        D10.2E Unit Price - 0.13D+02 & 0.17D+02
        D10.2B Unit Price - (81.00) & (58.00)
        D10.2R Unit Price - 140.00CR & 125.00 CR
        D10.2% Unit Price - 76.00% & 96.00%
        """
        
        #D10.2 Unit Price - 17.00 & 26.00
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '233of1000records,Page1of5', "Step 02: Expect 233 rows - values 17.00 & 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='$0,000,026.00', value2='$0,000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '282of1000records,Page1of5', "Step 02: Expect 282 rows - values $0,000,026.00 & $0,000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2E Unit Price - 0.13D+02 & 0.17D+02
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='0.13D+02', value2='0.17D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 02: Expect 183 rows - values 0.13D+02 & 0.17D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2B Unit Price - (81.00) & (58.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='(81.00)',value2='(58.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 02: Expect 335 rows - values (81.00) & (58.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2R Unit Price - 140.00CR & 125.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='140.00 CR', value2='125.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 02: Expect 133 rows - values 140.00CR & 125.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 76.00% & 96.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Between")
        
        filterselectionobj.create_filter(1, 'Between',value1='76.00%', value2='96.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '318of1000records,Page1of6', "Step 02: Expect 318 rows - values 76.00% & 96.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        """Step 07: For the following DECIMAL fields, select Filter, then Not Between the selected pair of values:

        D10.2 Unit Price - 17.00 & 26.00
        D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        D10.2E Unit Price - 0.13D+02 & 0.17D+02
        D10.2B Unit Price - (81.00) & (58.00)
        D10.2R Unit Price - 140.00CR & 125.00CR
        D10.2% Unit Price - 76.00% & 96.00%
        """
        
        #D10.2 Unit Price - 17.00 & 26.00
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '767of1000records,Page1of14', "Step 02: Expect 767 rows - values 17.00 & 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2LM Unit Price - $0,000,026.00 & $0,000,028.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='$0,000,026.00', value2='$0,000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '718of1000records,Page1of13', "Step 02: Expect 718 rows - values $0,000,026.00 & $0,000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2E Unit Price - 0.13D+02 & 0.17D+02
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='0.13D+02', value2='0.17D+02')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 02: Expect 817 rows - values 0.13D+02 & 0.17D+02")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2B Unit Price - (81.00) & (58.00)
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='(81.00)',value2='(58.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '665of1000records,Page1of12', "Step 02: Expect 665 rows - values (81.00) & (58.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2R Unit Price - 140.00CR & 125.00CR
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='140.00 CR', value2='125.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '867of1000records,Page1of16', "Step 02: Expect 867 rows - values 140.00CR & 125.00CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #D10.2% Unit Price - 76.00% & 96.00%
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not Between")
        
        filterselectionobj.create_filter(1, 'Not Between',value1='76.00%', value2='96.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        
        miscelanousobj.verify_page_summary(0, '682of1000records,Page1of12', "Step 02: Expect 682 rows - values 76.00% & 96.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        
 
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        