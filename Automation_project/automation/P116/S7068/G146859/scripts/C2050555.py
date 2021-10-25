'''
Created on Aug 2, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050555
Description : 

AHTML: Verify Filter operators against various Alphanumeric fields(Part 1).


Alphanumeric field tests.
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
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages import active_pivot_comment  
from common.lib import utillity
import unittest
import time


class C2050555_TestClass(BaseTestCase):

    def test_C2050555(self):
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2050555'
        
        """
            Step 01:Execute AR-RP-141AL to produce the alphanumeric output..
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141AL.fex", "S7068", 'mrid', 'mrpass')
        #time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01:  Expect to see the following Active Report. - page summary verification")
          
        """Step 02 : For the following ALPHA fields, select Filter, then Equals and use these values:
        ALPHA ORDER - 000001
        ALPHA ANV - 000005
        ALPHA TEXT - 000010
        ALPHA A80 - 000015
        ALPHA Edit - G-104
        ALPHA Store Code - R1020
        ALPHA Vendor Code - V102
        ALPHA Vendor Name - Thermo Tech, Inc
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast
        """
          
        #Expect 1 row - value 000001
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 02: Expect 1 row - value 000001")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 1 row - value 000005
          
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 02: Expect 1 row - value 000005")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 1 row - value 000010
          
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
           
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
           
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 02: Expect 1 row - value 000010")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog() 
          
        # Expect 1 row - value 000015
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large', value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 02: Expect 1 row - value 000015")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 67 row - value G-104 
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 02: Expect 67 row - value G-104 ")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 90 rows - value R1020
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', "Step 02: Expect 90 rows - value R1020")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()

          
        #Expect 84 rows - value V102
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 02: Expect 84 rows - value V102")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
          
        # Expect 67 rows - value Thermo Tech, Inc
          
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 02: Expect 90 rows - value R1020")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
    
        # Expect 134 rows - value G100
          
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '134of1000records,Page1of3', "Step 02: Expect 134 rows - value G100")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
  
        # Expect 218 rows - value French Roast
          
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '218of1000records,Page1of4', "Step 02: Expect 218 rows - value French Roast")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        """Step 03:For the following ALPHA fields, select Filter, then Equals and use these multiple values:
  
        ALPHA ORDER - 000001 & 000005
        ALPHA ANV - 000010 & 000015
        ALPHA TEXT - 000020 & 000025
        ALPHA A80 - 000030 & 000035
        ALPHA Edit - B-141, B-142 & B-144
        ALPHA Store Code - R1100 & R1109
        ALPHA Vendor Code - V081, V100 & V303
        ALPHA Vendor Name - Coffee Connection & Thermo Tech, Inc
        ALPHA Product Code - B144, F101 & G121
        ALPHA Product Descr. - Coffee Grinder & Coffee Pot
  
        """
        # Expect 2 rows - value 000001 & 000005
          
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001', value2='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03: Expect 2 rows - value 000001 & 000005")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 2 rows - value 000010 & 000015
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010',value2='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03: Expect 2 rows - value 000010 & 000015")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 2 rows - value 000020 & 000025
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000020', value2='000025')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 02: Expect 2 rows - value 000020 & 000025")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 2 rows - value 000030 & 000035
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000030', value2='000035')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03: Expect 2 rows - value 000030 & 000035")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 335 rows - value B-141, B-142 & B-144
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='B-141', value2='B-142', value3='B-144')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 03: Expect 335 rows - value B-141, B-142 & B-144")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
  
          
        #Expect 161 rows - value R1100 & R1109
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='R1100', value2='R1109')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '161of1000records,Page1of3', "Step 03:Expect 161 rows - value R1100 & R1109")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 198 rows - value V081, V100 & V303
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='V081', value2='V100', value3='V303')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '198of1000records,Page1of4', "Step 03: Expect 198 rows - value V081, V100 & V303")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
          
        # Expect 151 rows - value Coffee Connection & Thermo Tech, Inc
          
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='Coffee Connection',value2='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '151of1000records,Page1of3', "Step 03: Expect 151 rows - value Coffee Connection & Thermo Tech, Inc")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        # Expect 184 rows - value B144, F101 & G121
          
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='B144',value2='F101',value3='G121')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '184of1000records,Page1of4', "Step 03: Expect 134 rows - value G100")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
  
        # Expect 133 rows - value Coffee Grinder & Coffee Po
          
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='Coffee Grinder',value2='Coffee Pot')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 03: Expect 133 rows - value Coffee Grinder & Coffee Po")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        

        """Step 04: For the following ALPHA fields, select Filter, then Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
         
         
        ALPHA ANV - 000005
        ALPHA TEXT - 000010
        ALPHA A80 - 000015
        ALPHA Edit - G-104
        ALPHA Store Code - R1020
        ALPHA Vendor Code - V102
        ALPHA Vendor Name - Thermo Tech, Inc
         
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast
        """
         
        #Expect 1 row highlighted - value 000001
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds01_Page1.xlsx',"Step 04: Expect 1 row highlighted - value 000001")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds01_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #time.sleep(3)
        #Expect 1 row highlighted - value 000005
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large', value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
 
        #time.sleep(5)
         
         
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds02_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000005")
         
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds02_Page1.xlsx')
         
        filterselectionobj.close_filter_dialog()
        #Expect 1 row highlighted - value 000010
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight') 
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds03_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000010")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds03_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 1 row highlighted - value 000015
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals','large',value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
 
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds04_Page1.xlsx',"Step 04 Expect 1 row highlighted - value 000015")
         
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds04_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        # Expect only G-104 rows highlighted, page down to verify
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds05_Page1.xlsx',"Step 04 Expect only G-104 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds05_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
        #Expect only R1020 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds06_Page1.xlsx',"Step 04 Expect only R1020 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds06_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect only V102 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
         
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds07_Page1.xlsx',"Step 04.1: Expect only V102 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds07_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
         
         
         
        # Expect only Thermo Tech, Inc rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
         
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds08_Page1.xlsx',"Step 04 Expect only Thermo Tech, Inc rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds08_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
         
        # Expect only G100 rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
  
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds09_Page1.xlsx',"Step 04:Expect only G100 rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds09_Page1.xlsx')
        #time.sleep(5)
         
        filterselectionobj.close_filter_dialog()
 
        # Expect only French Roast rows highlighted, page down to verify
         
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
         
        filterselectionobj.create_filter(1, 'Equals',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(5)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds10_Page1.xlsx',"Step 04 Expect only French Roast rows highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds10_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        """Step 05:  For the following ALPHA fields, select Filter, then Not equal and use these values:
 
        ALPHA ORDER - 000001
        ALPHA ANV - 000005
        ALPHA TEXT - 000010
        ALPHA A80 - 000015
        ALPHA Edit - G-104
        ALPHA Store Code - R1020
        ALPHA Vendor Code - V102
        ALPHA Vendor Name - Thermo Tech, Inc
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast
 
        """
         
        #Expect 999 rows - not value 000001
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 05: Expect 999 rows - not value 000001")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 999 rows - not value 000005
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 05: Expect 999 rows - not value 000005")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 999 rows - not value 000010
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 05: Expect 999 rows - not value 0000102")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 999 rows - not value 000015
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 05: Expect 418 rows - value (81.00)")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 933 rows - not value G-104
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '933of1000records,Page1of17', "Step 05: Expect 933 rows - not value G-104")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 910 rows - not value R1020
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '910of1000records,Page1of16', "Step 05: Expect 910 rows - not value R1020")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
         
 
         
        #Expect 916 rows - not value V102
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 05: Expect 916 rows - not value V102")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
         
        # Expect 933 rows - not value Thermo Tech, Inc
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '933of1000records,Page1of17', "Step 05: Expect 933 rows - not value Thermo Tech, Inc")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 866 rows - not value G100
         
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '866of1000records,Page1of16', "Step 05: Expect 866 rows - not value G100")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #  Expect 782 rows - not value French Roast
         
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '782of1000records,Page1of14', "Step 05: Expect 782 rows - not value French Roast")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        """Step 06: For the following ALPHA fields, select Filter, then Not equal and use these multiple values:
 
        ALPHA ORDER - 000001 & 000005
        ALPHA ANV - 000010 & 000015
        ALPHA TEXT - 000020 & 000025
        ALPHA A80 - 000030 & 000035
        ALPHA Edit - B-141, B-142 & B-144
        ALPHA Store Code - R1100 & R1109
        ALPHA Vendor Code - V081, V100 & V303
        ALPHA Vendor Name - Coffee Connection & Thermo Tech, Inc
        ALPHA Product Code - B144, F101 & G121
        ALPHA Product Descr. - Coffee Grinder & Coffee Pot
 
        """

        
        #Expect 998 rows - not values 000001 & 000005
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000001', value2='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '998of1000records,Page1of18', "Step 06: Expect 998 rows - not values 000001 & 000005")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 998 rows - not values 000010 & 000015
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000010', value2='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '998of1000records,Page1of18', "Step 06: Expect 998 rows - not values 000010 & 000015")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 998 rows - not values 000020 & 000025
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000020', value2='000025')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '998of1000records,Page1of18', "Step 06: Expect 998 rows - not values 000020 & 000025")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 998 rows - not values 000030 & 000035
         
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000030',value2='000035')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '998of1000records,Page1of18', "Step 06:Expect 998 rows - not values 000030 & 000035")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()    
         
        #Expect 665 rows - not values B-141, B-142 & B-144
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='B-141', value2='B-142', value3='B-144')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '665of1000records,Page1of12', "Step 06:Expect 665 rows - not values B-141, B-142 & B-144")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
       
         
        #Expect 839 rows - not values R1100 & R1109
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='R1100', value2='R1109')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '839of1000records,Page1of15', "Step 06: Expect 939 rows - not values R1100 & R1109")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 802 rows - not values V081, V100 & V303
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='V081', value2='V100', value3='V303' )
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '802of1000records,Page1of15', "Step 06:Expect 802 rows - not values V081, V100 & V303")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
         
        # Expect 849 rows - not values Coffee Connection & Thermo Tech, Inc
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='Coffee Connection',value2='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(5)
         
        miscelanousobj.verify_page_summary(0, '849of1000records,Page1of15', "Step 06: Expect 933 rows - not value Thermo Tech, Inc")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        # Expect 816 rows - not values B144, F101 & G121
         
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='B144', value2='F101',value3='G121')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '816of1000records,Page1of15', "Step 06:  Expect 816 rows - not values B144, F101 & G121")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
 
        #  Expect 867 rows - not values Coffee Grinder & Coffee Pot
         
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='Coffee Grinder',value2='Coffee Pot')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '867of1000records,Page1of16', "Step 06:  Expect 867 rows - not values Coffee Grinder & Coffee Pot")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        
        """Step 07: For the following ALPHA fields, select Filter, then Not Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
        
        ALPHA ORDER - 000001
        ALPHA ANV - 000005
        ALPHA TEXT - 000010
        ALPHA A80 - 000015
        ALPHA Edit - G-104
        ALPHA Store Code - R1020
        
        ALPHA Vendor Code - V102
        
        ALPHA Vendor Name - Thermo Tech, Inc
        
        ALPHA Product Code - G100
        ALPHA Product Descr. - French Roast

        """

        
        #Expect 999 rows highlighted - only value 000001 is not
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal', 'large', value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds11_Page1.xlsx',"Step 07: Expect 1 row highlighted - value 000001")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds11_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 999 rows highlighted - only value 000005 is not
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" , "Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds12_Page1.xlsx',"Step 07: Expect 999 rows highlighted - only value 000005 is not")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds12_Page1.xlsx')
         
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 999 rows highlighted - only value 000010 is not
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds13_Page1.xlsx',"Step 07: Expect 999 rows highlighted - only value 000010 is not")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds13_Page1.xlsx')
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 999 rows highlighted - only value 000015 is not
        
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds14_Page1.xlsx',"Step 07: Expect 999 rows highlighted - only value 000015 is not")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds14_Page1.xlsx')
        
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect only G-104 rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds15_Page1.xlsx',"Step 07: Expect only G-104 rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds15_Page1.xlsx')
         
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect only R1020 rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds16_Page1.xlsx',"Step 07: Expect only R1020 rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds16_Page1.xlsx')
        
         
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        # Expect only V102 rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds17_Page1.xlsx',"Step 07: Expect only V102 rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds17_Page1.xlsx')
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        # Expect only Thermo Tech, Inc rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds18_Page1.xlsx',"Step 07: Expect only Thermo Tech, Inc rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds18_Page1.xlsx')
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        # Expect only G100 rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds19_Page1.xlsx',"Step 07: Expect only G100 rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds19_Page1.xlsx')
         
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()

        # Expect only French Roast rows Not highlighted, page down to verify
        
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Highlight')
        #time.sleep(4)
        utillobj.verify_data_set('ITableData0','rgb','C2050555_Ds20_Page1.xlsx',"Step 07: Expect only French Roast rows Not highlighted, page down to verify")
        #utillobj.create_data_set('ITableData0','rgb','C2050555_Ds20_Page1.xlsx')
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        
        
 
         
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        