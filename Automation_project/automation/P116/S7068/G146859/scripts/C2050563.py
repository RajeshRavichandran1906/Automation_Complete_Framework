'''
Created on Aug 2, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050563
Description : 

AHTML: Verify Filter operators against various Alphanumeric fields(Part 1).


PACKED data field tests.
These tests use Filter, then:

Equals
Equals(multi-select)
Equals(Highlight)
Not equal
Not equal(multi-select)
Not equal Highlight.


'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest, time

class C2050563_TestClass(BaseTestCase):

    def test_C2050563(self):
                
        """
            Step 01:Execute AR-RP-141PA to produce the alphanumeric output..
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        
       
        
        
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
        
        column=['Order Number INTEGER', 'Packed Order', 'P9.2M Unit Price', 'P9.2C Unit Price', 'P9.2Lc Unit Price', 'P9.2B Unit Price', 'P9.2R Unit Price', 'P9.2% Unit Price']
        miscelanousobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see column headings for AR-RP-141PA")
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141PA_Page1.xlsx',"Step 01: Verify Page data loaded correctly ")
        
        #utillobj.create_data_set('ITableData0','I0r','AR-RP-141PA_Page1.xlsx')
        
         
        """Step 02 : For the following PACKED data fields, select Filter, then Equals and use these values:
 
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
 
        """
 
          
        #Expect 1 row - only one Equal to 5
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 02: Expect 1 row - only one Equal to 5")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 84 rows - all Equal to $13.00
          
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 02: Expect 84 rows - all Equal to $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 99 rows - all Equal to 17.00
          
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
           
        filterselectionobj.create_filter(1, 'Equals',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
           
        miscelanousobj.verify_page_summary(0, '99of1000records,Page1of2', "Step 02: Expect 99 rows - all Equal to 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        # Expect 134 rows - all Equal to $000,026.00
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',  value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '134of1000records,Page1of3', "Step 02: Expect 134 rows - all Equal to $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 148 rows - all Equal to (28.00)
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '148of1000records,Page1of3', "Step 02: Expect 148 rows - all Equal to (28.00) ")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 84 rows - all Equal to 58.00 CR
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 02: Expect 84 rows - all Equal to 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
      
        #Expect 33 rows - all Equal to 76.00% 
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '33of1000records,Page1of1', "Step 02:Expect 33 rows - all Equal to 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        """Step 03:For the following PACKED data fields, select Filter, then Equals and use the pairs of values:
 
        Packed Order - 5 & 10 & 15
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00
        P9.2Lc Unit Price - $000,026.00 & $000.028.00
        P9.2B Unit Price - (28.00) & (58.00)
        P9.2R Unit Price - 58.00 CR & 76.00 CR
        P9.2% Unit Price - 76.00% & 81.00%
  
        """
 
 
         
         
        # Expect 3 rows - only one Equal to 5 or 10 or 15
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass') 
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='5', value2='10', value3='15')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '3of1000records,Page1of1', "Step 03: Expect 3 rows - only one Equal to 5 or 10 or 15")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
     
        #Expect 183 rows - all Equal to $13.00 or $17.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='$13.00',value2='$17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 03: Expect 183 rows - all Equal to $13.00 or $17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 233 rows - all Equal to 17.00 or 26.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '233of1000records,Page1of5', "Step 02: Expect 233 rows - all Equal to 17.00 or 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 282 rows - all Equal to $000,026.00 or $000,028.00
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='$000,026.00', value2='$000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '282of1000records,Page1of5', "Step 03:Expect 282 rows - all Equal to $000,026.00 or $000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 232 rows - all Equal to (28.00) or (58.00)
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='(28.00)', value2='(58.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '232of1000records,Page1of5', "Step 03: Expect 282 rows - all Equal to $000,026.00 or $000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 117 rows - all Equal to 58.00 CR or 76.00 CR
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='58.00 CR', value2='76.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '117of1000records,Page1of3', "Step 03:Expect 117 rows - all Equal to 58.00 CR or 76.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 251 rows - all Equal to 76.00% or 81.00%
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='76.00%', value2='81.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '251of1000records,Page1of5', "Step 03: Expect 251 rows - all Equal to 76.00% or 81.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        """Step 04: For the following PACKED data fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
         
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
         
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
 
        """
          
        #Expect to see only 1 row with value 5 Highlighted.
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)  
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds01_Page1.xlsx',"Step 04: Expect to see only 1 row with value 5 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds01_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        time.sleep(3)
         
        #Expect to see only rows with value $13.00 Highlighted.
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Equals")
          
        filterselectionobj.create_filter(1, 'Equals', value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(5)
          
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds02_Page1.xlsx',"Step 04 Expect to see only rows with value $13.00 Highlighted.")
          
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds02_Page1.xlsx')
          
        filterselectionobj.close_filter_dialog()
         
        #Expect to see only rows with value 17.00 Highlighted.
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight') 
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds03_Page1.xlsx',"Step 04 Expect to see only rows with value 17.00 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds03_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect to see only rows with value $000,026.00 Highlighted.
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
  
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds04_Page1.xlsx',"Step 04 Expect to see only rows with value $000,026.00 Highlighted.")
          
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds04_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        # Expect to see only rows with value (28.00) Highlighted.
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds05_Page1.xlsx',"Step 04 Expect to see only rows with value (28.00) Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds05_Page1.xlsx')
        time.sleep(5)
          
        filterselectionobj.close_filter_dialog()
        #Expect to see only rows with value 58.00 CR Highlighted.
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds06_Page1.xlsx',"Step 04 Expect to see only rows with value 58.00 CR Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds06_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #  Expect to see only rows with value 76.00% Highlighted.
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
         
        time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds07_Page1.xlsx',"Step 04.1:  Expect to see only rows with value 76.00% Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds07_Page1.xlsx')
        time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
         
         
        """Step 05:  For the following PACKED data fields, select Filter, then Not equal and use these values:

        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
        """

         
        #Expect 999 rows - all Not equal to 5
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass') 
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 05: Expect 999 rows - all Not equal to 5")
        
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 916 rows - all Not equal to $13.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 05: Expect 916 rows - all Not equal to $13.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 901 rows - all Not equal to 17.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal', value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '901of1000records,Page1of16', "Step 05: Expect 901 rows - all Not equal to 17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 866 rows - all Not equal to $000,026.00
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal', value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '866of1000records,Page1of16', "Step 05: Expect 866 rows - all Not equal to $000,026.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 852 rows - all Not equal to (28.00)
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '852of1000records,Page1of15', "Step 05:Expect 852 rows - all Not equal to (28.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 916 rows - all Not equal to 58.00 CR
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 05: Expect 916 rows - all Not equal to 58.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
         
         
        #Expect 967 rows - all Not equal to 76.00%
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '967of1000records,Page1of17', "Step 05: Expect 967 rows - all Not equal to 76.00% CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
 
        """Step 06: For the following PACKED data fields, select Filter, then Not equal and use the pairs of values:

        Packed Order - 5 & 10 & 15
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00
        P9.2Lc Unit Price - $000,026.00 & $000.028.00
        P9.2B Unit Price - (28.00) & (58.00)
        P9.2R Unit Price - 58.00 CR & 76.00 CR
        P9.2% Unit Price - 76.00% & 81.00%

        """        

        #Expect 997 rows - only one Equal to 5 or 10 or 15
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login("AR-RP-141PA.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(4) td:nth-child(1)", "1", 60)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='5', value2='10',value3='15')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '997of1000records,Page1of18', "Step 06: Expect 997 rows - only one Equal to 5 or 10 or 15")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 817 rows - all Equal to $13.00 or $17.00
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='$13.00', value2='$17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '817of1000records,Page1of15', "Step 06: Expect 817 rows - all Equal to $13.00 or $17.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 767 rows - all Equal to 17.00 or 26.00
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
        filterselectionobj.create_filter(1, 'Not equal',value1='17.00', value2='26.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '767of1000records,Page1of14', "Step 06: Expect 767 rows - all Equal to 17.00 or 26.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 718 rows - all Equal to $000,026.00 or $000,028.00
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='$000,026.00',value2='$000,028.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '718of1000records,Page1of13', "Step 06:Expect 718 rows - all Equal to $000,026.00 or $000,028.00")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()    
         
        #Expect 768 rows - all Equal to (28.00) or (58.00)
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='(28.00)', value2='(58.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '768of1000records,Page1of14', "Step 06:Expect 768 rows - all Equal to (28.00) or (58.00)")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
       
         
        #Expect 883 rows - all Equal to 58.00 CR or 76.00 CR
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='58.00 CR', value2='76.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '883of1000records,Page1of16', "Step 06: Expect 883 rows - all Equal to 58.00 CR or 76.00 CR")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 749 rows - all Equal to 76.00% or 81.00%
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='76.00%', value2='81.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '749of1000records,Page1of14', "Step 06:Expect 749 rows - all Equal to 76.00% or 81.00%")
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        
        """Step 07: For the following DATE fields, select Filter, then Not equal and use these values:
        Click the Highlight button instead of the Filter button.
        
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%

        """
        
        #Expect to see all rows except 5 Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal', 'large', value1='5')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds08_Page1.xlsx',"Step 07: Expect to see all rows except 5 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds08_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect to see all rows except $13.00 Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='$13.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds09_Page1.xlsx',"Step 07: Expect to see all rows except $13.00 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds09_Page1.xlsx')
         
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect to see all rows except 17.00 Highlighted.
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='17.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds10_Page1.xlsx',"Step 07:  Expect to see all rows except 17.00 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds10_Page1.xlsx')
        
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect to see all rows except $000,026.00 Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='$000,026.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds11_Page1.xlsx',"Step 07: Expect to see all rows except $000,026.00 Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds11_Page1.xlsx')
        
        
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect to see all rows except (28.00) Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='(28.00)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds12_Page1.xlsx',"Step 07: Expect to see all rows except (28.00) Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds12_Page1.xlsx')
         
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect to see all rows except 58.00 CR Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='58.00 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds13_Page1.xlsx',"Step 07: Expect to see all rows except 58.00 CR Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds13_Page1.xlsx')
        
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        # Expect to see all rows except 76.00% Highlighted.
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='76.00%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050563_Ds14_Page1.xlsx',"Step 07: Expect to see all rows except 76.00% Highlighted.")
        #utillobj.create_data_set('ITableData0','rgb','C2050563_Ds14_Page1.xlsx')
        time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
 
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        